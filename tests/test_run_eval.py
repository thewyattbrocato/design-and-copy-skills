import json
import os
import shlex
import sys
import unittest
from pathlib import Path

from helpers import TempRoot, load_script, run_main, skill_md

import evalkit as ek  # noqa: E402  (helpers puts scripts/ on sys.path; run_eval shares this module)

run_eval = load_script("run_eval")
validate_evals = load_script("validate_evals")

MOCK = Path(__file__).resolve().parent / "mock_eval_cmd.py"
KINDS = ["critique", "choose", "explain", "layout", "polish", "critique", "choose", "explain"]


def stub(role):
    return " ".join(shlex.quote(p) for p in (sys.executable, str(MOCK), role))


def make_tasks(n=8, build=()):
    return [{"id": f"t{i}", "kind": "build" if i in build else KINDS[i % 8], "prompt": f"Prompt {i}",
             "rubric": ["First criterion.", "Second criterion."]} for i in range(n)]


class EnvCase(unittest.TestCase):
    def setUp(self):
        self._saved = {k: os.environ.get(k) for k in
                       ("EVAL_GENERATOR_CMD", "EVAL_JUDGE_CMD", "EVAL_RENDER_CMD", "EVAL_MOCK_JUDGE", "EVAL_MOCK_LOG")}
        os.environ["EVAL_GENERATOR_CMD"] = stub("generate")
        os.environ["EVAL_JUDGE_CMD"] = stub("judge")
        os.environ["EVAL_RENDER_CMD"] = stub("render")
        os.environ.pop("EVAL_MOCK_JUDGE", None)
        os.environ.pop("EVAL_MOCK_LOG", None)

    def tearDown(self):
        for k, v in self._saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


class BlindingTest(unittest.TestCase):
    def test_assignment_is_seeded_and_second_pass_swaps(self):
        a = ek.assign_order(7, "t1")
        self.assertEqual(a, ek.assign_order(7, "t1"))
        self.assertEqual(a[1], a[0][::-1])
        self.assertEqual(sorted(a[0]), ["with", "without"])

    def test_assignment_varies_across_tasks(self):
        firsts = {ek.assign_order(3, f"t{i}")[0][0] for i in range(30)}
        self.assertEqual(firsts, {"with", "without"})

    def test_deblind_maps_sides_to_arms(self):
        j = {"verdict": "A", "notes": "n", "scores": {"A": [5, 5], "B": [1, 1]}}
        out = ek.deblind(j, ["without", "with"])
        self.assertEqual(out["winner"], "without")
        self.assertEqual(out["scores"], {"without": [5, 5], "with": [1, 1]})
        self.assertEqual(ek.deblind({**j, "verdict": "tie"}, ["with", "without"])["winner"], "tie")

    def test_judge_prompt_never_names_the_arms(self):
        task = make_tasks(1)[0]
        prompt = ek.judge_prompt(task, {"A": "first", "B": "second"}, {"A": None, "B": None})
        for word in ("with skill", "without", "baseline", "skill"):
            self.assertNotIn(word, prompt.lower())

    def test_parse_judgment_rejects_bad_scores(self):
        with self.assertRaises(ek.EvalError):
            ek.parse_judgment('{"verdict": "A", "scores": {"A": [9, 1], "B": [1, 1]}}', 2)
        with self.assertRaises(ek.EvalError):
            ek.parse_judgment('{"verdict": "C", "scores": {"A": [1, 1], "B": [1, 1]}}', 2)


class CombineTest(unittest.TestCase):
    def pass_(self, winner, order=("with", "without")):
        return {"order": list(order), "raw_verdict": "A", "winner": winner, "notes": "n",
                "scores": {"with": [4, 4], "without": [2, 2]}}

    def test_agreeing_passes_keep_the_winner(self):
        out = ek.combine_passes([self.pass_("with"), self.pass_("with", ("without", "with"))])
        self.assertEqual(out["winner"], "with")
        self.assertTrue(out["position_consistent"])

    def test_disagreeing_passes_are_a_tie(self):
        out = ek.combine_passes([self.pass_("with"), self.pass_("without", ("without", "with"))])
        self.assertEqual(out["winner"], "tie")
        self.assertFalse(out["position_consistent"])

    def test_tie_with_win_is_a_tie(self):
        self.assertEqual(ek.combine_passes([self.pass_("with"), self.pass_("tie")])["winner"], "tie")

    def test_rubric_scores_average_the_passes(self):
        a, b = self.pass_("with"), self.pass_("with")
        b["scores"] = {"with": [2, 4], "without": [4, 2]}
        out = ek.combine_passes([a, b])
        self.assertEqual(out["rubric_items"]["with"], [3.0, 4.0])
        self.assertEqual(out["rubric_scores"], {"with": 3.5, "without": 2.5})


class GateTest(unittest.TestCase):
    def verdicts(self, winners, with_score, without_score):
        return [{"winner": w, "rubric_scores": {"with": with_score, "without": without_score}} for w in winners]

    def test_passes_when_not_worse(self):
        self.assertTrue(ek.ship_gate(self.verdicts(["with", "tie", "without"], 4, 3))["passed"])
        self.assertTrue(ek.ship_gate(self.verdicts(["tie", "tie"], 3, 3))["passed"])

    def test_fails_on_more_losses_than_wins(self):
        self.assertFalse(ek.ship_gate(self.verdicts(["with", "without", "without"], 4, 3))["passed"])

    def test_fails_when_rubric_mean_is_lower_beyond_tolerance(self):
        self.assertFalse(ek.ship_gate(self.verdicts(["with", "tie"], 2.8, 3.0), tolerance=0.1)["passed"])
        self.assertTrue(ek.ship_gate(self.verdicts(["with", "tie"], 2.95, 3.0), tolerance=0.1)["passed"])

    def test_gate_records_tolerance_and_means(self):
        gate = ek.ship_gate(self.verdicts(["with"], 4, 2), tolerance=0.25)
        self.assertEqual((gate["tolerance"], gate["mean_rubric_with"], gate["mean_rubric_without"]), (0.25, 4, 2))


class RunEvalTest(EnvCase):
    def setUp(self):
        super().setUp()
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        self.t.write("skills/demo/SKILL.md", skill_md())
        self.log = self.t.root / "calls.log"
        os.environ["EVAL_MOCK_LOG"] = str(self.log)

    def write_tasks(self, tasks):
        self.t.write("evals/demo/tasks.json", json.dumps(tasks))

    def run_main(self, *extra):
        import contextlib
        import io
        out = io.StringIO()
        samples = [] if "--samples" in extra else ["--samples", "1"]
        with contextlib.redirect_stdout(out):
            code = run_eval.main(["demo", "--root", str(self.t.root), "--seed", "5", *samples, *extra])
        return code, out.getvalue()

    def results(self):
        return json.loads((self.t.root / "evals/demo/results.json").read_text())

    def calls(self):
        return self.log.read_text().split() if self.log.exists() else []

    def test_winning_skill_passes_and_writes_valid_results(self):
        self.write_tasks(make_tasks())
        code, out = self.run_main()
        self.assertEqual(code, 0, out)
        self.assertIn("PASS demo", out)
        data = self.results()
        self.assertEqual(data["summary"]["with_wins"], 8)
        self.assertEqual(data["summary"]["judge"], "claude:opus")
        self.assertEqual(data["summary"]["mode"], "installed")
        self.assertEqual(data["summary"]["seed"], 5)
        self.assertEqual(data["summary"]["model"], "sonnet")
        self.assertTrue(data["summary"]["gate"]["passed"])
        self.assertEqual(data["verdicts"][0]["rubric_scores"], {"with": 4.0, "without": 2.0})
        self.assertEqual(data["summary"]["protocol"], 2)
        self.assertEqual(data["summary"]["samples"], 1)
        self.assertEqual(len(data["verdicts"][0]["samples"]), 1)
        code, vout = run_main(validate_evals, self.t.root)
        self.assertEqual(code, 0, vout)

    def test_losing_skill_fails_the_gate(self):
        self.write_tasks(make_tasks())
        os.environ["EVAL_MOCK_JUDGE"] = "prefer_without"
        code, out = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("FAIL demo", out)
        self.assertFalse(self.results()["summary"]["gate"]["passed"])

    def test_position_biased_judge_yields_ties(self):
        self.write_tasks(make_tasks())
        os.environ["EVAL_MOCK_JUDGE"] = "always_a"
        code, out = self.run_main()
        data = self.results()
        self.assertEqual(data["summary"]["ties"], 8)
        self.assertTrue(all(not v["samples"][0]["position_consistent"] for v in data["verdicts"]))
        self.assertEqual(code, 1)  # a tie is not a pass for a skill that should clearly help
        self.assertIn("FAIL demo", out)

    def test_rerun_does_not_regenerate_or_rejudge(self):
        self.write_tasks(make_tasks())
        self.run_main()
        first = self.calls()
        self.assertEqual(len([c for c in first if not c.startswith("probe")]), 16)
        (self.t.root / "evals/demo/results.json").unlink()
        self.run_main()
        self.assertEqual(self.calls(), first)
        self.assertTrue((self.t.root / "evals/demo/results.json").is_file())

    def test_rerun_fills_only_missing_answers(self):
        self.write_tasks(make_tasks())
        self.run_main()
        (self.t.root / "evals/demo/runs/t3/with.md").unlink()
        before = len(self.calls())
        self.run_main()
        new = self.calls()[before:]
        self.assertIn("t3/with", new)
        self.assertEqual(len([c for c in new if not c.startswith("probe")]), 1)

    def test_changed_judge_rejudges_but_keeps_answers(self):
        self.write_tasks(make_tasks())
        self.run_main()
        before = self.calls()
        self.run_main("--judge", "grok:grok-test")
        self.assertEqual(self.calls(), before)
        self.assertEqual(self.results()["summary"]["judge"], "grok:grok-test")

    def test_summary_records_judge_separation(self):
        self.write_tasks(make_tasks())
        self.run_main()
        summary = self.results()["summary"]
        self.assertIs(summary["same_model_judge"], False)
        self.assertEqual(summary["suite"], "dev")

    def test_same_model_judge_is_refused_before_any_work(self):
        self.write_tasks(make_tasks())
        for judge in ("claude:sonnet", "claude:Sonnet", "claude:claude-sonnet-5-5"):
            import contextlib
            import io
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                code, _ = self.run_main("--judge", judge)
            self.assertEqual(code, 2, judge)
            self.assertIn("same model as the generator", err.getvalue())
        self.assertEqual(self.calls(), [])
        self.assertFalse((self.t.root / "evals/demo/results.json").exists())

    def test_same_model_judge_can_be_allowed_and_is_recorded(self):
        self.write_tasks(make_tasks())
        code, out = self.run_main("--judge", "claude:sonnet", "--allow-same-model-judge")
        self.assertEqual(code, 0, out)
        self.assertIs(self.results()["summary"]["same_model_judge"], True)
        self.assertIn("same model as the generator", out)

    def test_default_judge_is_not_the_generator(self):
        self.assertEqual(ek.default_judge("sonnet"), "claude:opus")
        self.assertEqual(ek.default_judge("claude-opus-5-5"), "claude:sonnet")
        self.write_tasks(make_tasks())
        code, out = self.run_main("--model", "opus")
        self.assertEqual(code, 0, out)
        self.assertEqual(self.results()["summary"]["judge"], "claude:sonnet")

    def test_heldout_suite_is_default_and_isolated_from_dev(self):
        self.write_tasks(make_tasks())
        self.t.write("evals/demo/heldout/tasks.json", json.dumps(make_tasks()))
        code, out = self.run_main()
        self.assertEqual(code, 0, out)
        held = self.t.root / "evals/demo/heldout"
        self.assertTrue((held / "results.json").is_file())
        self.assertTrue((held / "runs/t0/with.md").is_file())
        self.assertFalse((self.t.root / "evals/demo/results.json").exists())
        self.assertFalse((self.t.root / "evals/demo/runs").exists())
        self.assertEqual(json.loads((held / "results.json").read_text())["summary"]["suite"], "heldout")
        code, vout = run_main(validate_evals, self.t.root)
        self.assertEqual(code, 0, vout)
        code, out = self.run_main("--suite", "dev")
        self.assertEqual(code, 0, out)
        self.assertTrue((self.t.root / "evals/demo/results.json").is_file())

    def test_dev_is_the_default_without_a_heldout_suite(self):
        self.write_tasks(make_tasks())
        self.assertEqual(ek.resolve_suite(self.t.root / "evals/demo"), "dev")
        self.assertEqual(ek.resolve_suite(self.t.root / "evals/demo", "heldout"), "heldout")

    def test_missing_heldout_tasks_is_an_error(self):
        self.write_tasks(make_tasks())
        import contextlib
        import io
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            code, _ = self.run_main("--suite", "heldout")
        self.assertEqual(code, 2)
        self.assertIn("heldout/tasks.json not found", err.getvalue())

    def test_build_tasks_save_html_and_png_and_judge_sees_neutral_names(self):
        self.write_tasks(make_tasks(build=(2,)))
        os.environ["EVAL_MOCK_JUDGE"] = "tie"
        code, out = self.run_main()
        runs = self.t.root / "evals/demo/runs/t2"
        for name in ("with.html", "without.html", "with.png", "without.png"):
            self.assertTrue((runs / name).is_file(), name)
        self.assertIn("SKILLED", (runs / "with.html").read_text())
        self.assertNotIn("```", (runs / "with.html").read_text())

    def test_judge_images_are_copied_under_neutral_names(self):
        seen = {}

        def fake(spec, prompt, files, timeout=600):
            seen.update(files=sorted(files), prompt=prompt)
            return '{"verdict": "tie", "notes": "n", "scores": {"A": [3, 3], "B": [3, 3]}}'

        original = ek.call_judge
        ek.call_judge = fake
        self.addCleanup(setattr, ek, "call_judge", original)
        task = make_tasks(1, build=(0,))[0]
        png = self.t.write("x/with.png", "png").parent / "with.png"
        other = self.t.write("x/without.png", "png")
        ek.judge_pass("claude:opus", task, ["with", "without"], None, None, png, other)
        self.assertEqual(seen["files"], ["a.png", "b.png"])
        for leak in ("with.png", "without.png", "skill"):
            self.assertNotIn(leak, seen["prompt"].lower())

    def test_dry_run_calls_nothing(self):
        self.write_tasks(make_tasks())
        code, out = self.run_main("--dry-run")
        self.assertEqual(code, 0)
        self.assertIn("dry run", out)
        self.assertEqual(self.calls(), [])
        self.assertFalse((self.t.root / "evals/demo/runs").exists())

    def test_task_subset_does_not_write_results(self):
        self.write_tasks(make_tasks())
        code, out = self.run_main("--tasks", "t0,t1")
        self.assertIn("subset run", out)
        self.assertFalse((self.t.root / "evals/demo/results.json").exists())
        self.assertEqual(len([c for c in self.calls() if not c.startswith("probe")]), 4)

    def test_probe_failure_aborts_before_generation(self):
        self.write_tasks(make_tasks())
        original = ek.probe_skill

        def bad(*a, **k):
            raise ek.EvalError("probe: skill 'demo' is not visible in the WITH run")

        run_eval.ek.probe_skill = bad
        self.addCleanup(setattr, run_eval.ek, "probe_skill", original)
        code, out = self.run_main()
        self.assertEqual(code, 2)
        self.assertEqual([c for c in self.calls() if not c.startswith("probe")], [])

    def test_too_few_tasks_rejected_unless_allowed(self):
        self.write_tasks(make_tasks(2))
        self.assertEqual(self.run_main()[0], 2)
        code, out = self.run_main("--allow-small")
        self.assertEqual(code, 1)
        self.assertIn("INCONCLUSIVE demo", out)

    def test_skill_in_copy_skills_runs_and_write_tasks_are_text(self):
        (self.t.root / "skills/demo/SKILL.md").rename(self.t.root / "skills/demo/GONE.md")
        self.t.write("copy-skills/demo/SKILL.md", skill_md())
        tasks = make_tasks()
        tasks[0].update(kind="write", fact_sheet=True)
        self.write_tasks(tasks)
        code, out = self.run_main()
        self.assertEqual(code, 0, out)
        runs = self.t.root / "evals/demo/runs/t0"
        self.assertTrue((runs / "with.md").is_file())
        self.assertFalse((runs / "with.html").exists())
        self.assertFalse((runs / "with.png").exists())
        self.assertEqual(run_main(validate_evals, self.t.root)[0], 0)

    def test_skill_in_no_live_root_is_an_error(self):
        self.t.write("withdrawn/gone/SKILL.md", skill_md("gone"))
        self.write_tasks(make_tasks())
        import contextlib
        import io
        err = io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            code = run_eval.main(["gone", "--root", str(self.t.root)])
        self.assertEqual(code, 2)
        self.assertIn("gone/SKILL.md not found in skills/ or copy-skills/", err.getvalue())

    def test_installed_mode_copies_the_skill_from_whichever_root_holds_it(self):
        self.t.write("copy-skills/drafty/SKILL.md", skill_md("drafty"))
        self.t.write("copy-skills/drafty/references/a.md", "# A\n")
        seen = {}

        def fake(cmd, stdin_text=None, cwd=None, timeout=600, env=None):
            seen["files"] = sorted(p.relative_to(cwd).as_posix() for p in Path(cwd, ".claude").rglob("*") if p.is_file())

            class P:
                returncode, stderr = 0, ""
                stdout = '{"type": "result", "result": "answer", "total_cost_usd": 0}\n'
            return P()

        original = ek.run_cmd
        ek.run_cmd = fake
        self.addCleanup(setattr, ek, "run_cmd", original)
        from roots import find_skill
        folder, skill_dir = find_skill(self.t.root, "drafty")
        self.assertEqual(folder, "copy-skills")
        ek.claude_generate("Prompt", "drafty", skill_dir, "installed", "sonnet", None, 60)
        self.assertEqual(seen["files"], [".claude/skills/drafty/SKILL.md", ".claude/skills/drafty/references/a.md"])

    def test_probe_checks_skill_visibility(self):
        skill_dir = self.t.root / "skills/demo"
        info = ek.probe_skill("demo", skill_dir, "installed", "sonnet")
        self.assertTrue(info["reproducible"])
        self.assertIn("demo", info["with"])
        self.assertNotIn("demo", info["without"])


class ExtractHtmlTest(unittest.TestCase):
    def test_fenced_and_bare(self):
        self.assertEqual(ek.extract_html("note\n```html\n<p>x</p>\n```\nbye"), "<p>x</p>\n")
        self.assertEqual(ek.extract_html("<!doctype html><p>y</p>"), "<!doctype html><p>y</p>\n")

    def test_skill_body_strips_frontmatter(self):
        with TempRoot() as t:
            t.write("s/SKILL.md", skill_md(body="# Hi\n"))
            self.assertEqual(ek.skill_body(t.root / "s"), "# Hi")

    def test_parse_stream_collects_skill_use(self):
        lines = [json.dumps({"type": "assistant", "message": {"content": [
                    {"type": "tool_use", "name": "Skill", "input": {"skill": "demo"}}]}}),
                 json.dumps({"type": "result", "result": "done", "total_cost_usd": 0.01,
                             "modelUsage": {"claude-x": {}}})]
        answer, meta = ek.parse_stream("\n".join(lines))
        self.assertEqual((answer, meta["skills_invoked"], meta["model_id"]), ("done", ["demo"], "claude-x"))


class JudgeSeparationTest(unittest.TestCase):
    def test_same_model_normalisation(self):
        same = ek.same_model_judge
        self.assertTrue(same("claude:sonnet", "sonnet"))
        self.assertTrue(same("claude:sonnet", "claude-sonnet-5-5"))
        self.assertTrue(same("claude:claude-sonnet-5-5", "sonnet"))
        self.assertTrue(same("CLAUDE:Sonnet", "SONNET"))
        self.assertTrue(same("claude:", "opus"))
        self.assertFalse(same("claude:opus", "sonnet"))
        self.assertFalse(same("claude:opus", "claude-sonnet-5-5"))
        self.assertFalse(same("grok:grok-4.7", "sonnet"))
        self.assertFalse(same("claude:opus", ""))


class PrimaryModelTest(unittest.TestCase):
    def test_largest_token_count_wins_not_the_first_key(self):
        usage = {"claude-haiku": {"inputTokens": 20, "outputTokens": 5},
                 "claude-sonnet": {"inputTokens": 900, "outputTokens": 300, "costUSD": 99}}
        self.assertEqual(ek.primary_model(usage), "claude-sonnet")

    def test_first_key_on_a_tie_and_none_when_empty(self):
        self.assertEqual(ek.primary_model({"a": {}, "b": {}}), "a")
        self.assertIsNone(ek.primary_model({}))
        self.assertIsNone(ek.primary_model(None))

    def test_parse_stream_uses_it(self):
        line = json.dumps({"type": "result", "result": "ok", "modelUsage": {
            "small": {"inputTokens": 1}, "big": {"inputTokens": 50, "outputTokens": 9}}})
        self.assertEqual(ek.parse_stream(line)[1]["model_id"], "big")


class ValidatorExtensionTest(unittest.TestCase):
    def check(self, mutate):
        tasks = make_tasks()
        verdicts = [{"task_id": t["id"], "winner": "with", "judge_notes": "n",
                     "rubric_scores": {"with": 4, "without": 2}, "rubric_items": {"with": [4], "without": [2]},
                     "position_consistent": True, "passes": [{"winner": "with"}]} for t in tasks]
        summary = {"with_wins": 8, "without_wins": 0, "ties": 0, "model": "m", "date": "2026-01-31",
                   "judge": "claude:opus", "mode": "installed", "seed": 1,
                   "gate": {"passed": True, "tolerance": 0.1, "mean_rubric_with": 4, "mean_rubric_without": 2}}
        results = {"verdicts": verdicts, "summary": summary}
        mutate(results)
        return validate_evals.validate_results(results, [t["id"] for t in tasks])

    def test_extended_results_are_valid(self):
        self.assertEqual(self.check(lambda r: None), [])

    def test_inconsistent_gate_is_caught(self):
        errors = self.check(lambda r: r["summary"]["gate"].update(passed=False))
        self.assertTrue(any("gate.passed" in e for e in errors))

    def test_bad_extras_are_caught(self):
        def mutate(r):
            r["summary"]["mode"] = "magic"
            r["verdicts"][0]["rubric_items"] = {"with": []}
        errors = self.check(mutate)
        self.assertTrue(any("'mode'" in e for e in errors))
        self.assertTrue(any("rubric_items" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
