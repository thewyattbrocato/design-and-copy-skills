import json
import unittest

from helpers import TempRoot, load_script, run_main

mod = load_script("validate_evals")
KINDS = ["build", "critique", "choose", "layout", "polish", "explain", "write"]


def tasks(n=8):
    return [{"id": f"t{i}", "kind": KINDS[i % 7], "prompt": f"Prompt {i}", "rubric": ["Criterion."]}
            for i in range(n)]


def results(n=8, **summary):
    verdicts = [{"task_id": f"t{i}", "winner": "with" if i < 5 else "tie", "judge_notes": "Notes.",
                 "rubric_scores": {"with": 4, "without": 3}} for i in range(n)]
    base = {"with_wins": min(n, 5), "without_wins": 0, "ties": max(0, n - 5), "model": "m", "date": "2026-01-31"}
    base.update(summary)
    return {"verdicts": verdicts, "summary": base}


class ValidateEvalsTest(unittest.TestCase):
    def run_with(self, tasks_data=None, results_data=None):
        with TempRoot() as t:
            t.write("evals/.gitkeep", "")
            if tasks_data is not None:
                t.write("evals/demo/tasks.json", json.dumps(tasks_data))
            if results_data is not None:
                t.write("evals/demo/results.json", json.dumps(results_data))
            return run_main(mod, t.root)

    def test_no_skill_folders_passes(self):
        self.assertEqual(self.run_with()[0], 0)

    def test_valid_tasks_and_results_pass(self):
        code, out = self.run_with(tasks(), results())
        self.assertEqual(code, 0, out)

    def test_tasks_only_passes(self):
        self.assertEqual(self.run_with(tasks(10))[0], 0)

    def test_task_count_bounds(self):
        for n in (7, 11):
            code, out = self.run_with(tasks(n))
            self.assertEqual(code, 1)
            self.assertIn("need 8-10", out)

    def test_bad_task_fields_fail(self):
        data = tasks()
        data[0]["kind"] = "paint"
        data[1]["rubric"] = []
        data[2]["rubric"] = ["ok", " "]
        data[3]["prompt"] = ""
        data[4]["id"] = "t5"
        code, out = self.run_with(data)
        self.assertEqual(code, 1)
        for text in ("'kind' must be", "tasks.json[1]", "tasks.json[2]", "'prompt'", "duplicate id"):
            self.assertIn(text, out)

    def test_write_kind_is_valid_and_needs_a_text_answer_only(self):
        self.assertIn("write", mod.KINDS)
        data = tasks(8)
        data[0]["kind"] = "write"
        self.assertEqual(self.run_with(data)[0], 0)
        with TempRoot() as t:
            t.write("evals/demo/tasks.json", json.dumps(data))
            t.write("evals/demo/runs/t0/with.md", "Draft.\n")
            t.write("evals/demo/runs/t0/without.md", "Draft.\n")
            self.assertEqual(run_main(mod, t.root)[0], 0)
            (t.root / "evals/demo/runs/t0/without.md").unlink()
            code, out = run_main(mod, t.root)
            self.assertEqual(code, 1)
            self.assertIn("no without.md or without.html answer file", out)

    def test_missing_tasks_file_fails(self):
        with TempRoot() as t:
            t.write("evals/demo/results.json", "{}")
            code, out = run_main(mod, t.root)
            self.assertEqual(code, 1)
            self.assertIn("tasks.json is missing", out)

    def test_invalid_json_fails(self):
        with TempRoot() as t:
            t.write("evals/demo/tasks.json", "{nope")
            self.assertEqual(run_main(mod, t.root)[0], 1)

    def test_results_problems_fail(self):
        bad = results()
        bad["verdicts"][0]["winner"] = "both"
        bad["verdicts"][1]["task_id"] = "ghost"
        bad["verdicts"][2]["judge_notes"] = ""
        bad["verdicts"][3]["rubric_scores"] = {"with": 4}
        code, out = self.run_with(tasks(), bad)
        self.assertEqual(code, 1)
        for text in ("'winner' must be", "ghost", "'judge_notes'", "'rubric_scores'", "no verdict for tasks"):
            self.assertIn(text, out)

    def test_summary_mismatch_and_bad_date_fail(self):
        code, out = self.run_with(tasks(), results(with_wins=7, date="Jan 31"))
        self.assertEqual(code, 1)
        self.assertIn("'with_wins' is 7", out)
        self.assertIn("'date'", out)


def complete_runs(t, prefix, n=8):
    for i in range(n):
        t.write(f"{prefix}runs/t{i}/with.md", "answer")
        t.write(f"{prefix}runs/t{i}/without.html", "<p>answer</p>")


class RunFolderTest(unittest.TestCase):
    def setUp(self):
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        self.t.write("evals/demo/tasks.json", json.dumps(tasks()))

    def test_complete_run_folders_pass(self):
        complete_runs(self.t, "evals/demo/")
        self.t.write("evals/demo/results.json", json.dumps(results()))
        self.assertEqual(run_main(mod, self.t.root)[0], 0)

    def test_run_folder_without_an_answer_file_fails(self):
        complete_runs(self.t, "evals/demo/")
        (self.t.root / "evals/demo/runs/t3/without.html").unlink()
        code, out = run_main(mod, self.t.root)
        self.assertEqual(code, 1)
        self.assertIn("runs/t3: no without.md or without.html answer file", out)

    def test_judgment_or_meta_files_do_not_count_as_answers(self):
        self.t.write("evals/demo/runs/t0/with.meta.json", "{}")
        self.t.write("evals/demo/runs/t0/judgment.json", "{}")
        self.t.write("evals/demo/runs/t0/with.png", "x")
        code, out = run_main(mod, self.t.root)
        self.assertEqual(code, 1)
        self.assertIn("no with.md or with.html", out)
        self.assertIn("no without.md or without.html", out)

    def test_superseded_dev_results_turn_missing_answers_into_warnings(self):
        complete_runs(self.t, "evals/demo/")
        (self.t.root / "evals/demo/runs/t3/with.md").unlink()
        self.t.write("evals/demo/results.json", json.dumps(
            results(superseded=True, superseded_note="Seen by the skill writers.", suite="dev")))
        code, out = run_main(mod, self.t.root)
        self.assertEqual(code, 0, out)
        self.assertIn("warning: runs/t3: no with.md", out)
        self.assertIn("1 warnings", out)

    def test_superseded_must_be_a_boolean(self):
        self.t.write("evals/demo/results.json", json.dumps(results(superseded="yes")))
        self.assertIn("'superseded' must be true or false", run_main(mod, self.t.root)[1])


class HeldoutSuiteTest(unittest.TestCase):
    def setUp(self):
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        self.t.write("evals/demo/tasks.json", json.dumps(tasks()))
        self.t.write("evals/demo/heldout/tasks.json", json.dumps(tasks()))

    def heldout_results(self, **summary):
        base = {"judge": "claude:opus", "model_id": "claude-sonnet-5-5", "same_model_judge": False, "suite": "heldout"}
        base.update(summary)
        return json.dumps(results(**base))

    def test_heldout_folder_is_not_a_skill_and_is_validated(self):
        code, out = run_main(mod, self.t.root)
        self.assertEqual(code, 0, out)
        self.assertIn("validated 1 eval folders", out)
        self.t.write("evals/demo/heldout/tasks.json", json.dumps(tasks(3)))
        code, out = run_main(mod, self.t.root)
        self.assertEqual(code, 1)
        self.assertIn("evals/demo: heldout/tasks.json: 3 tasks", out)

    def test_heldout_only_skill_is_valid_but_dev_results_need_dev_tasks(self):
        with TempRoot() as t:
            t.write("evals/demo/heldout/tasks.json", json.dumps(tasks(8)))
            code, out = run_main(mod, t.root)
            self.assertEqual(code, 0, out)
            t.write("evals/demo/results.json", json.dumps(results()))
            code, out = run_main(mod, t.root)
            self.assertEqual(code, 1)
            self.assertIn("tasks.json is missing", out)

    def test_valid_heldout_results_pass(self):
        complete_runs(self.t, "evals/demo/heldout/")
        self.t.write("evals/demo/heldout/results.json", self.heldout_results())
        code, out = run_main(mod, self.t.root)
        self.assertEqual(code, 0, out)

    def test_heldout_results_need_a_run_folder_for_every_task(self):
        complete_runs(self.t, "evals/demo/heldout/", n=7)
        self.t.write("evals/demo/heldout/results.json", self.heldout_results())
        code, out = run_main(mod, self.t.root)
        self.assertEqual(code, 1)
        self.assertIn("heldout/runs/t7: no with.md", out)

    def test_same_model_judge_is_flagged_in_heldout_only(self):
        complete_runs(self.t, "evals/demo/heldout/")
        complete_runs(self.t, "evals/demo/")
        self.t.write("evals/demo/heldout/results.json", self.heldout_results(same_model_judge=True))
        code, out = run_main(mod, self.t.root)
        self.assertEqual(code, 1)
        self.assertIn("same_model_judge is true", out)
        self.t.write("evals/demo/heldout/results.json", self.heldout_results(judge="claude:sonnet"))
        code, out = run_main(mod, self.t.root)
        self.assertEqual(code, 1)
        self.assertIn("is the same model as the generator", out)
        self.t.write("evals/demo/heldout/results.json", self.heldout_results())
        self.t.write("evals/demo/results.json", json.dumps(
            results(judge="claude:sonnet", model_id="claude-sonnet-5-5", same_model_judge=True)))
        self.assertEqual(run_main(mod, self.t.root)[0], 0)

    def test_heldout_results_must_name_the_judge_and_cannot_be_superseded(self):
        complete_runs(self.t, "evals/demo/heldout/")
        data = json.loads(self.heldout_results())
        del data["summary"]["judge"]
        data["summary"]["superseded"] = True
        self.t.write("evals/demo/heldout/results.json", json.dumps(data))
        code, out = run_main(mod, self.t.root)
        self.assertEqual(code, 1)
        self.assertIn("must record 'judge'", out)
        self.assertIn("cannot be superseded", out)

    def test_suite_field_must_match_the_folder(self):
        complete_runs(self.t, "evals/demo/heldout/")
        self.t.write("evals/demo/heldout/results.json", self.heldout_results(suite="dev"))
        self.assertIn("suite is 'dev' but the file is in the heldout suite", run_main(mod, self.t.root)[1])


if __name__ == "__main__":
    unittest.main()
