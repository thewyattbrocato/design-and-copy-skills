"""Eval protocol 2: samples, majority verdicts, loaded-only gating, re-sampling, the new task fields and rules."""
import contextlib
import io
import json
import os
import unittest

from helpers import TempRoot, load_script, run_main, skill_md
from test_run_eval import EnvCase, make_tasks

import evalkit as ek  # noqa: E402

run_eval = load_script("run_eval")
validate_evals = load_script("validate_evals")


def loaded_block(with_wins, without_wins, ties, tasks, mean_with, mean_without):
    return {"with_wins": with_wins, "without_wins": without_wins, "ties": ties, "tasks_with_loaded_sample": tasks,
            "loaded_samples": tasks, "total_samples": tasks, "mean_rubric_with": mean_with,
            "mean_rubric_without": mean_without, "mean_advantage": round(mean_with - mean_without, 3)}


class MajorityAndGateTest(unittest.TestCase):
    def test_majority_needs_more_than_half(self):
        self.assertEqual(ek.majority(["with", "with", "without"]), "with")
        self.assertEqual(ek.majority(["with", "with", "tie"]), "with")
        self.assertEqual(ek.majority(["with", "without", "tie"]), "tie")
        self.assertEqual(ek.majority(["with", "tie", "tie"]), "tie")
        self.assertEqual(ek.majority(["with", "without"]), "tie")
        self.assertEqual(ek.majority(["without"]), "without")

    def sample(self, k, winner, loaded=True, with_score=4, without_score=3):
        return {"sample": k, "winner": winner, "rubric_scores": {"with": with_score, "without": without_score},
                "judge_notes": "n", "loaded": loaded, "not_loaded": not loaded, "attempts": 1 if loaded else 3}

    def test_verdict_has_an_all_samples_and_a_loaded_only_winner(self):
        v = ek.build_verdict("t", [self.sample(0, "with"), self.sample(1, "without", loaded=False, with_score=1),
                                   self.sample(2, "without", loaded=False, with_score=1)])
        self.assertEqual(v["winner"], "without")
        self.assertEqual(v["loaded_winner"], "with")
        self.assertEqual(v["loaded_samples"], 1)
        self.assertEqual(v["loaded_rubric_scores"], {"with": 4, "without": 3})
        self.assertEqual(v["rubric_scores"]["with"], 2.0)

    def test_task_with_no_loaded_sample_has_no_loaded_winner(self):
        v = ek.build_verdict("t", [self.sample(0, "with", loaded=False)])
        self.assertIsNone(v["loaded_winner"])
        self.assertIsNone(v["loaded_rubric_scores"])
        agg = ek.aggregate_v2([v])
        self.assertEqual(agg["loaded"]["tasks_with_loaded_sample"], 0)
        self.assertEqual(agg["with_wins"], 1)

    def test_gate_needs_a_win_margin_or_a_rubric_advantage(self):
        gate = ek.ship_gate_v2
        self.assertEqual(gate(loaded_block(5, 3, 1, 9, 4.0, 3.9))["decision"], "pass")
        self.assertEqual(gate(loaded_block(4, 4, 1, 9, 4.0, 3.9))["decision"], "fail")  # a tie is not a pass
        self.assertEqual(gate(loaded_block(0, 0, 9, 9, 4.0, 4.0))["decision"], "fail")
        tie_with_advantage = gate(loaded_block(4, 4, 1, 9, 4.15, 4.0))
        self.assertEqual(tie_with_advantage["decision"], "pass")
        self.assertEqual(gate(loaded_block(4, 4, 1, 9, 4.14, 4.0))["decision"], "fail")
        self.assertEqual(gate(loaded_block(3, 4, 2, 9, 4.5, 3.5))["decision"], "fail")  # more losses than wins

    def test_gate_is_never_worse_than_the_tolerance_on_the_rubric(self):
        worse = loaded_block(6, 2, 1, 9, 3.8, 4.0)
        self.assertEqual(ek.ship_gate_v2(worse, 0.1)["decision"], "fail")
        self.assertEqual(ek.ship_gate_v2(worse, 0.25)["decision"], "pass")

    def test_too_few_loaded_tasks_is_inconclusive_and_not_a_pass(self):
        result = ek.ship_gate_v2(loaded_block(5, 0, 0, 5, 4.5, 3.0))
        self.assertEqual((result["decision"], result["passed"]), ("inconclusive", False))
        self.assertEqual(ek.ship_gate_v2(loaded_block(6, 0, 0, 6, 4.5, 3.0))["decision"], "pass")

    def test_noise_floor_for_a_skill_with_no_effect(self):
        nf = ek.noise_floor(10, 8)
        self.assertEqual((nf["wins_low"], nf["wins_high"], nf["expected_wins"]), (2, 8, 5))
        self.assertEqual(nf["p_at_least"], 0.055)
        self.assertEqual(ek.noise_floor(0, 0)["wins_low"], None)
        line = ek.noise_line({"with_wins": 6, "without_wins": 3})
        self.assertIn("2 to 7", line)
        self.assertIn("not evidence", line)

    def test_stub_output_may_report_skills(self):
        answer, meta = ek.parse_stub_output(json.dumps({"answer": "hi", "skills_invoked": ["demo"]}), "m")
        self.assertEqual((answer, meta["skills_invoked"]), ("hi", ["demo"]))
        self.assertEqual(ek.parse_stub_output("{not json", "m")[0], "{not json")
        self.assertEqual(ek.parse_stub_output("plain", "m")[1]["skills_invoked"], [])


class ProtocolRunCase(EnvCase):
    def setUp(self):
        super().setUp()
        for k in ("EVAL_MOCK_NOT_LOADED", "EVAL_MOCK_SAMPLE_VERDICTS"):
            self._saved.setdefault(k, os.environ.get(k))
            os.environ.pop(k, None)
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        self.t.write("skills/demo/SKILL.md", skill_md())
        self.log = self.t.root / "calls.log"
        os.environ["EVAL_MOCK_LOG"] = str(self.log)
        self.tasks = make_tasks()

    def write_tasks(self, tasks=None):
        self.t.write("evals/demo/tasks.json", json.dumps(tasks or self.tasks))

    def run_main(self, *extra, root=None):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = run_eval.main(["demo", "--root", str(root or self.t.root), "--seed", "5", *extra])
        return code, out.getvalue() + err.getvalue()

    def results(self):
        return json.loads((self.t.root / "evals/demo/results.json").read_text())

    def calls(self, suffix=""):
        lines = self.log.read_text().split() if self.log.exists() else []
        return [c for c in lines if not c.startswith("probe") and c.endswith(suffix)]

    def validate(self):
        return run_main(validate_evals, self.t.root)


class SamplingTest(ProtocolRunCase):
    def test_three_samples_per_arm_is_the_default(self):
        self.write_tasks()
        code, out = self.run_main()
        self.assertEqual(code, 0, out)
        self.assertEqual(len(self.calls()), 8 * 2 * 3)
        data = self.results()
        self.assertEqual((data["summary"]["protocol"], data["summary"]["samples"]), (2, 3))
        self.assertTrue(all(len(v["samples"]) == 3 for v in data["verdicts"]))
        runs = self.t.root / "evals/demo/runs/t0"
        for name in ("with.md", "with.s1.md", "with.s2.md", "without.s2.md", "judgment.s1.json", "with.s2.meta.json"):
            self.assertTrue((runs / name).is_file(), name)
        code, vout = self.validate()
        self.assertEqual(code, 0, vout)
        self.assertIn("noise floor", out)
        self.assertIn("all samples", out)

    def test_task_verdict_is_the_majority_of_its_samples(self):
        self.write_tasks()
        os.environ["EVAL_MOCK_SAMPLE_VERDICTS"] = json.dumps({
            "t0": ["with", "with", "without"], "t1": ["without", "without", "with"], "t2": ["with", "without", "tie"]})
        code, out = self.run_main()
        by_task = {v["task_id"]: v for v in self.results()["verdicts"]}
        self.assertEqual(by_task["t0"]["winner"], "with")
        self.assertEqual(by_task["t1"]["winner"], "without")
        self.assertEqual(by_task["t2"]["winner"], "tie")
        self.assertEqual([s["winner"] for s in by_task["t0"]["samples"]], ["with", "with", "without"])
        summary = self.results()["summary"]
        self.assertEqual((summary["with_wins"], summary["without_wins"], summary["ties"]), (6, 1, 1))
        self.assertEqual(self.validate()[0], 0)

    def test_sample_i_of_one_arm_is_judged_against_sample_i_of_the_other(self):
        self.write_tasks()
        seen = []
        original = ek.call_judge

        def spy(spec, prompt, files, timeout=600):
            seen.append(prompt)
            return original(spec, prompt, files, timeout)

        ek.call_judge = spy
        self.addCleanup(setattr, ek, "call_judge", original)
        self.run_main("--tasks", "t0")
        self.assertEqual(len(seen), 3 * 2)  # three samples, two swapped passes each
        for prompt in seen:
            samples = {m for m in ("[s0]", "[s1]", "[s2]") if m in prompt}
            self.assertEqual(len(samples), 1, "a judgment must compare one sample index on both sides")
            self.assertEqual(prompt.count("answer for t0 " + next(iter(samples))), 2)

    def test_swap_control_still_applies_per_sample(self):
        self.write_tasks()
        os.environ["EVAL_MOCK_JUDGE"] = "always_a"
        self.run_main()
        for v in self.results()["verdicts"]:
            self.assertTrue(all(s["winner"] == "tie" and not s["position_consistent"] for s in v["samples"]))

    def test_rerun_reuses_everything_and_a_larger_n_adds_only_new_samples(self):
        self.write_tasks()
        self.run_main("--samples", "2")
        first = len(self.calls())
        self.assertEqual(first, 8 * 2 * 2)
        (self.t.root / "evals/demo/results.json").unlink()
        self.run_main("--samples", "2")
        self.assertEqual(len(self.calls()), first)
        self.run_main("--samples", "3")
        self.assertEqual(len(self.calls()), first + 8 * 2)

    def test_build_tasks_render_a_screenshot_per_sample(self):
        self.write_tasks(make_tasks(build=(2,)))
        os.environ["EVAL_MOCK_JUDGE"] = "tie"
        self.run_main("--samples", "2")
        runs = self.t.root / "evals/demo/runs/t2"
        for name in ("with.html", "with.png", "with.s1.html", "with.s1.png", "without.s1.png"):
            self.assertTrue((runs / name).is_file(), name)

    def test_samples_must_be_positive(self):
        self.write_tasks()
        code, out = self.run_main("--samples", "0")
        self.assertEqual(code, 2)
        self.assertIn("--samples", out)


class LoadedOnlyTest(ProtocolRunCase):
    def test_a_sample_that_did_not_load_is_regenerated_until_it_loads(self):
        self.write_tasks()
        os.environ["EVAL_MOCK_NOT_LOADED"] = json.dumps({"t0": 2})
        code, out = self.run_main("--samples", "1")
        self.assertEqual(code, 0, out)
        self.assertEqual(self.calls("t0/with"), ["t0/with"] * 3)
        self.assertEqual(self.calls("t0/without"), ["t0/without"])
        sample = next(v for v in self.results()["verdicts"] if v["task_id"] == "t0")["samples"][0]
        self.assertEqual((sample["loaded"], sample["not_loaded"], sample["attempts"]), (True, False, 3))
        self.assertEqual(self.validate()[0], 0)

    def test_a_sample_that_never_loads_is_flagged_after_two_regenerations(self):
        self.write_tasks()
        os.environ["EVAL_MOCK_NOT_LOADED"] = json.dumps({"t0": 99})
        self.run_main("--samples", "1")
        self.assertEqual(len(self.calls("t0/with")), 3)
        data = self.results()
        sample = next(v for v in data["verdicts"] if v["task_id"] == "t0")["samples"][0]
        self.assertEqual((sample["loaded"], sample["not_loaded"], sample["attempts"]), (False, True, 3))
        self.assertEqual(data["summary"]["loaded"]["tasks_with_loaded_sample"], 7)
        self.assertEqual(data["summary"]["loaded"]["loaded_samples"], 7)
        self.assertEqual(data["summary"]["loaded"]["total_samples"], 8)
        self.assertEqual(self.validate()[0], 0)

    def test_regeneration_is_per_sample(self):
        self.write_tasks()
        os.environ["EVAL_MOCK_NOT_LOADED"] = json.dumps({"t0#1": 1})
        self.run_main("--samples", "3")
        self.assertEqual(len(self.calls("t0/with")), 4)
        samples = next(v for v in self.results()["verdicts"] if v["task_id"] == "t0")["samples"]
        self.assertEqual([s["attempts"] for s in samples], [1, 2, 1])

    def test_a_rerun_does_not_retry_a_sample_that_used_all_its_attempts(self):
        self.write_tasks()
        os.environ["EVAL_MOCK_NOT_LOADED"] = json.dumps({"t0": 99})
        self.run_main("--samples", "1")
        before = len(self.calls())
        self.run_main("--samples", "1")
        self.assertEqual(len(self.calls()), before)

    def test_gate_is_decided_on_loaded_only_samples(self):
        self.write_tasks()
        # t0-t2 never load and the judge prefers the baseline there; of the loaded tasks the skill wins 3, loses 2.
        os.environ["EVAL_MOCK_NOT_LOADED"] = json.dumps({"t0": 99, "t1": 99, "t2": 99})
        os.environ["EVAL_MOCK_SAMPLE_VERDICTS"] = json.dumps({
            "t0": ["without"], "t1": ["without"], "t2": ["without"], "t3": ["without"], "t4": ["without"]})
        code, out = self.run_main("--samples", "1")
        summary = self.results()["summary"]
        self.assertEqual((summary["with_wins"], summary["without_wins"]), (3, 5))
        loaded = summary["loaded"]
        self.assertEqual((loaded["with_wins"], loaded["without_wins"], loaded["tasks_with_loaded_sample"]), (3, 2, 5))
        self.assertEqual(summary["gate"]["decision"], "inconclusive")  # only five tasks have a loaded sample
        self.assertEqual(code, 1)
        self.assertIn("INCONCLUSIVE demo", out)
        self.assertEqual(self.validate()[0], 0)

    def test_loaded_only_tally_decides_pass_when_all_samples_would_fail(self):
        tasks = make_tasks()
        self.write_tasks(tasks)
        os.environ["EVAL_MOCK_NOT_LOADED"] = json.dumps({"t0": 99, "t1": 99})
        os.environ["EVAL_MOCK_SAMPLE_VERDICTS"] = json.dumps({"t0": ["without"], "t1": ["without"], "t7": ["without"]})
        code, out = self.run_main("--samples", "1")
        summary = self.results()["summary"]
        self.assertEqual((summary["with_wins"], summary["without_wins"]), (5, 3))
        self.assertEqual((summary["loaded"]["with_wins"], summary["loaded"]["without_wins"]), (5, 1))
        self.assertEqual((code, summary["gate"]["decision"]), (0, "pass"))
        self.assertIn("PASS demo", out)

    def test_fewer_than_six_tasks_with_a_loaded_sample_is_inconclusive(self):
        self.write_tasks()
        os.environ["EVAL_MOCK_NOT_LOADED"] = json.dumps({"t0": 99, "t1": 99, "t2": 99})
        code, out = self.run_main("--samples", "1")
        gate = self.results()["summary"]["gate"]
        self.assertEqual((gate["decision"], gate["passed"], code), ("inconclusive", False, 1))
        self.assertIn("INCONCLUSIVE", out)
        self.assertIn("only 5 tasks", out)
        self.assertEqual(self.validate()[0], 0)

    def test_injected_mode_counts_every_sample_as_loaded(self):
        self.write_tasks()
        os.environ["EVAL_MOCK_NOT_LOADED"] = json.dumps({"t0": 99})
        code, out = self.run_main("--samples", "1", "--mode", "injected")
        self.assertEqual(code, 0, out)
        self.assertEqual(self.results()["summary"]["loaded"]["tasks_with_loaded_sample"], 8)
        self.assertEqual(len(self.calls("t0/with")), 1)


class SecondaryRowTest(ProtocolRunCase):
    def test_secondary_model_is_reported_and_never_gated(self):
        self.write_tasks()
        os.environ["EVAL_MOCK_JUDGE"] = "prefer_with"
        code, out = self.run_main("--samples", "2", "--secondary-model", "haiku")
        self.assertEqual(code, 0, out)
        data = self.results()
        sec = data["secondary"]
        self.assertEqual(sec["summary"]["model"], "haiku")
        self.assertEqual(sec["summary"]["samples"], 2)
        self.assertNotIn("gate", sec["summary"])
        self.assertEqual(len(sec["verdicts"]), 8)
        runs = self.t.root / "evals/demo/runs/t0/secondary"
        self.assertTrue((runs / "with.md").is_file() and (runs / "without.s1.md").is_file())
        self.assertIn("secondary (not gated) haiku", out)
        self.assertEqual(self.validate()[0], 0)

    def test_a_losing_secondary_row_does_not_change_the_gate(self):
        self.write_tasks()
        self.run_main("--samples", "1")
        primary = self.results()["summary"]["gate"]
        os.environ["EVAL_MOCK_JUDGE"] = "prefer_with"
        os.environ["EVAL_MOCK_SAMPLE_VERDICTS"] = json.dumps({f"t{i}": ["without"] for i in range(8)})
        code, out = self.run_main("--samples", "1", "--secondary-model", "haiku")
        data = self.results()
        self.assertEqual(data["secondary"]["summary"]["without_wins"], 8)
        self.assertEqual(data["summary"]["gate"]["decision"], primary["decision"])

    def test_secondary_judge_must_not_be_the_secondary_generator(self):
        self.write_tasks()
        code, out = self.run_main("--secondary-model", "haiku", "--judge", "claude:haiku")
        self.assertEqual(code, 2)
        self.assertIn("same model as the secondary generator", out)
        self.assertEqual(self.calls(), [])

    def test_dropping_the_secondary_flag_says_so(self):
        self.write_tasks()
        self.run_main("--samples", "1", "--secondary-model", "haiku")
        code, out = self.run_main("--samples", "1")
        self.assertIn("pass --secondary-model again", out)
        self.assertNotIn("secondary", self.results())


class TaskFieldTest(unittest.TestCase):
    def tasks(self, **write):
        data = make_tasks()
        data[0].update(kind="write", **write)
        return data

    def test_write_tasks_may_declare_the_new_fields(self):
        errors, _ = validate_evals.validate_tasks(self.tasks(fact_sheet=False, pressure=True))
        self.assertEqual(errors, [])

    def test_fields_must_be_booleans_and_only_on_write_tasks(self):
        errors, _ = validate_evals.validate_tasks(self.tasks(fact_sheet="yes"))
        self.assertTrue(any("'fact_sheet' must be true or false" in e for e in errors))
        data = make_tasks()
        data[1]["pressure"] = True
        errors, _ = validate_evals.validate_tasks(data)
        self.assertTrue(any("only allowed on write tasks" in e for e in errors))

    def test_protocol_two_requires_fact_sheet_on_write_tasks(self):
        self.assertEqual(validate_evals.validate_tasks(self.tasks())[0], [])  # protocol 1 keeps validating
        errors, _ = validate_evals.validate_tasks(self.tasks(), protocol=2)
        self.assertTrue(any("must declare 'fact_sheet'" in e for e in errors))
        self.assertEqual(validate_evals.validate_tasks(self.tasks(fact_sheet=True), protocol=2)[0], [])

    def copy_suite(self, no_sheet, pressure):
        data = make_tasks()
        for i in range(6):
            data[i].update(kind="write", fact_sheet=i >= no_sheet, **({"pressure": True} if i < pressure else {}))
        return data

    def test_copy_heldout_needs_four_without_a_fact_sheet_and_two_under_pressure(self):
        check = lambda data: validate_evals.validate_tasks(data, protocol=2, copy_heldout=True)[0]  # noqa: E731
        self.assertEqual(check(self.copy_suite(4, 2)), [])
        short_sheets = check(self.copy_suite(3, 2))
        self.assertTrue(any("at least 4" in e and "fact_sheet false (has 3)" in e for e in short_sheets))
        short_pressure = check(self.copy_suite(4, 1))
        self.assertTrue(any("at least 2" in e and "pressure true (has 1)" in e for e in short_pressure))

    def test_the_copy_counts_do_not_apply_to_design_suites_or_protocol_one(self):
        data = make_tasks()
        self.assertEqual(validate_evals.validate_tasks(data, protocol=2, copy_heldout=False)[0], [])
        self.assertEqual(validate_evals.validate_tasks(self.copy_suite(0, 0), protocol=1, copy_heldout=True)[0], [])


class CopyRunTest(ProtocolRunCase):
    def setUp(self):
        super().setUp()
        (self.t.root / "skills/demo/SKILL.md").rename(self.t.root / "skills/demo/GONE.md")
        self.t.write("copy-skills/demo/SKILL.md", skill_md())

    def copy_tasks(self, no_sheet=4, pressure=2):
        data = make_tasks()
        for i in range(6):
            data[i].update(kind="write", fact_sheet=i >= no_sheet, **({"pressure": True} if i < pressure else {}))
        return data

    def test_run_refuses_a_heldout_copy_suite_that_breaks_the_counts(self):
        self.t.write("evals/demo/heldout/tasks.json", json.dumps(self.copy_tasks(no_sheet=2)))
        code, out = self.run_main()
        self.assertEqual(code, 2)
        self.assertIn("at least 4", out)
        self.assertEqual(self.calls(), [])

    def test_a_valid_heldout_copy_suite_runs_and_validates(self):
        self.t.write("evals/demo/heldout/tasks.json", json.dumps(self.copy_tasks()))
        code, out = self.run_main("--samples", "1")
        self.assertEqual(code, 0, out)
        self.assertEqual(self.validate()[0], 0)

    def test_dev_suite_of_a_copy_skill_only_needs_the_field(self):
        self.write_tasks(self.copy_tasks(no_sheet=0, pressure=0))
        code, out = self.run_main("--samples", "1")
        self.assertEqual(code, 0, out)

    def test_validator_enforces_the_counts_on_protocol_two_results(self):
        self.t.write("evals/demo/heldout/tasks.json", json.dumps(self.copy_tasks()))
        self.run_main("--samples", "1")
        path = self.t.root / "evals/demo/heldout/tasks.json"
        weak = self.copy_tasks(no_sheet=1)
        path.write_text(json.dumps(weak))
        code, out = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("at least 4", out)


class ValidatorProtocolTwoTest(ProtocolRunCase):
    def setUp(self):
        super().setUp()
        self.write_tasks()
        self.run_main("--samples", "2")
        self.path = self.t.root / "evals/demo/results.json"
        self.data = json.loads(self.path.read_text())

    def save(self, mutate):
        data = json.loads(json.dumps(self.data))
        mutate(data)
        self.path.write_text(json.dumps(data))
        return self.validate()

    def test_a_run_validates(self):
        self.assertEqual(self.validate()[0], 0)

    def test_a_hand_edited_sample_is_caught(self):
        code, out = self.save(lambda d: d["verdicts"][0]["samples"][0].update(winner="without"))
        self.assertEqual(code, 1)
        self.assertIn("'winner' is 'with' but the samples give", out)

    def test_a_hand_edited_gate_is_caught(self):
        code, out = self.save(lambda d: d["summary"]["gate"].update(decision="fail", passed=False))
        self.assertEqual(code, 1)
        self.assertIn("gate is fail", out)

    def test_loosened_gate_constants_are_caught(self):
        code, out = self.save(lambda d: d["summary"]["gate"].update(min_loaded_tasks=1))
        self.assertEqual(code, 1)
        self.assertIn("min_loaded_tasks", out)

    def test_a_hand_edited_loaded_tally_is_caught(self):
        code, out = self.save(lambda d: d["summary"]["loaded"].update(with_wins=0))
        self.assertEqual(code, 1)
        self.assertIn("loaded.with_wins", out)

    def test_a_not_loaded_flag_needs_all_attempts(self):
        def mutate(d):
            s = d["verdicts"][0]["samples"][0]
            s.update(loaded=False, not_loaded=True, attempts=1)
        code, out = self.save(mutate)
        self.assertEqual(code, 1)
        self.assertIn("flagged not_loaded only after 3 attempts", out)

    def test_wrong_sample_count_is_caught(self):
        code, out = self.save(lambda d: d["verdicts"][0]["samples"].pop())
        self.assertEqual(code, 1)
        self.assertIn("'samples' must list 2 samples", out)

    def test_every_sample_answer_must_be_committed(self):
        (self.t.root / "evals/demo/runs/t1/without.s1.md").unlink()
        code, out = self.validate()
        self.assertEqual(code, 1)
        self.assertIn("runs/t1: no without.s1.md or without.s1.html answer file", out)

    def test_secondary_answers_must_be_committed_too(self):
        self.run_main("--samples", "2", "--secondary-model", "haiku")
        self.assertEqual(self.validate()[0], 0)
        (self.t.root / "evals/demo/runs/t1/secondary/with.md").unlink()
        code, out = self.validate()
        self.assertIn("runs/t1/secondary: no with.md or with.html answer file", out)

    def test_protocol_two_results_record_the_suite_hash(self):
        self.assertEqual(self.data["summary"]["suite_hash"], validate_evals.suite_hash(self.tasks))
        code, out = self.save(lambda d: d["summary"].pop("suite_hash"))
        self.assertEqual(code, 1)
        self.assertIn("suite_hash", out)

    def test_changed_tasks_warn_but_do_not_fail(self):
        changed = json.loads(json.dumps(self.tasks))
        changed[0]["rubric"].append("A criterion added after the run.")
        self.write_tasks(changed)
        code, out = self.validate()
        self.assertEqual(code, 0, out)
        self.assertIn("warning: tasks.json has changed since this results file was written", out)
        self.assertIn("fresh held-out set", out)

    def test_whitespace_in_tasks_json_does_not_change_the_hash(self):
        self.t.write("evals/demo/tasks.json", json.dumps(self.tasks, indent=4) + "\n")
        code, out = self.validate()
        self.assertEqual(code, 0, out)
        self.assertIn("0 warnings", out)

    def test_protocol_one_results_still_validate_without_the_new_fields(self):
        v1 = {"verdicts": [{"task_id": f"t{i}", "winner": "with", "judge_notes": "n",
                            "rubric_scores": {"with": 4, "without": 3}} for i in range(8)],
              "summary": {"with_wins": 8, "without_wins": 0, "ties": 0, "model": "m", "date": "2026-01-31",
                          "protocol": 1}}
        self.path.write_text(json.dumps(v1))
        code, out = self.validate()
        self.assertEqual(code, 0, out)
        v1["summary"].pop("protocol")
        self.path.write_text(json.dumps(v1))
        self.assertEqual(self.validate()[0], 0)

    def test_protocol_must_be_known(self):
        code, out = self.save(lambda d: d["summary"].update(protocol=3))
        self.assertEqual(code, 1)
        self.assertIn("'protocol' must be one of", out)


if __name__ == "__main__":
    unittest.main()
