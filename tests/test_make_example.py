import contextlib
import io
import json
import os
import unittest

from helpers import TempRoot, load_script, skill_md
from test_run_eval import EnvCase

make_example = load_script("make_example")
RUBRIC = ["First criterion.", "Second criterion."]


class MakeExampleTest(EnvCase):
    def setUp(self):
        super().setUp()
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        self.t.write("skills/demo/SKILL.md", skill_md())
        os.environ.pop("EVAL_MOCK_RUN_SCORES", None)
        self.addCleanup(os.environ.pop, "EVAL_MOCK_RUN_SCORES", None)

    def config(self, **extra):
        example = {"id": "hero", "skill": "demo", "prompt": "Build a hero.", "rubric": RUBRIC}
        return self.t.write("config.json", json.dumps({"model": "sonnet", "examples": [example], **extra}))

    def run_cfg(self, *argv, **extra):
        with contextlib.redirect_stdout(io.StringIO()):
            return make_example.main([str(self.config(**extra)), "--root", str(self.t.root), *argv])

    def out(self, model="sonnet"):
        return self.t.root / "docs/examples/hero" / model

    def meta(self, model="sonnet"):
        return json.loads((self.out(model) / "meta.json").read_text())

    def test_writes_example_folder_with_meta(self):
        self.assertEqual(self.run_cfg(), 0)
        out = self.out()
        for name in ("without.png", "with.png", "compare.png", "contact-sheet.png", "without.html", "with.html", "meta.json"):
            self.assertTrue((out / name).is_file(), name)
        meta = self.meta()
        self.assertEqual(meta["prompt"], "Build a hero.")
        self.assertEqual((meta["model"], meta["mode"], meta["runs_per_arm"]), ("sonnet", "installed", 3))
        self.assertIn("median", meta["featuring_rule"])
        self.assertEqual(len(meta["spread"]["with"]), 3)
        self.assertEqual(len(meta["pairs"]), 3)
        self.assertEqual(meta["rubric"], RUBRIC)
        self.assertIn("single self-contained HTML file", meta["prompt_suffix"])
        self.assertEqual(meta["skill_invoked_in_with_runs"], [False, False, False])  # the mock never calls the skill
        self.assertRegex(meta["date"], r"^\d{4}-\d{2}-\d{2}$")
        self.assertIn("SKILLED", (out / "with.html").read_text())
        self.assertIn("PLAIN", (out / "without.html").read_text())
        self.assertEqual(sorted(p.name for p in (out / "runs").glob("*.html")),
                         [f"{a}-{i}.html" for a in ("with", "without") for i in (1, 2, 3)])

    def test_every_run_is_generated_with_the_same_prompt(self):
        log = self.t.root / "calls.log"
        os.environ["EVAL_MOCK_LOG"] = str(log)
        self.run_cfg("--runs", "2")
        calls = [c for c in log.read_text().split() if not c.startswith("probe")]
        self.assertEqual(sorted(calls), ["hero/with/0/with", "hero/with/1/with", "hero/without/0/without", "hero/without/1/without"])

    def test_median_run_is_featured_not_the_best(self):
        os.environ["EVAL_MOCK_RUN_SCORES"] = json.dumps({"with": [3, 5, 4], "without": [2, 1, 3]})
        self.assertEqual(self.run_cfg(), 0)
        meta = self.meta()
        self.assertEqual(meta["spread"], {"with": [3.0, 5.0, 4.0], "without": [2.0, 1.0, 3.0]})
        self.assertEqual(meta["featured_run"], {"with": 3, "without": 1})
        self.assertIn("with/2", (self.out() / "with.html").read_text())
        self.assertIn("without/0", (self.out() / "without.html").read_text())

    def test_even_count_takes_the_lower_median(self):
        self.assertEqual(make_example.median_index([4.0, 2.0, 3.0, 1.0]), 1)
        self.assertEqual(make_example.median_index([3.0, 3.0, 3.0]), 1)
        self.assertEqual(make_example.median_index([5.0]), 0)

    def test_model_flag_overrides_config_and_gets_its_own_folder(self):
        self.assertEqual(self.run_cfg("--model", "haiku", "--runs", "1"), 0)
        self.assertEqual(self.meta("haiku")["model"], "haiku")
        self.assertFalse(self.out("sonnet").exists())

    def test_rerun_reuses_finished_runs(self):
        self.run_cfg("--runs", "1")
        log = self.t.root / "calls.log"
        os.environ["EVAL_MOCK_LOG"] = str(log)
        self.run_cfg("--runs", "1")
        self.assertEqual([c for c in log.read_text().split() if not c.startswith("probe")], [])

    def test_judgments_are_cached_beside_the_runs(self):
        self.run_cfg("--runs", "1")
        cache = self.out() / "runs/judgment-1.json"
        self.assertTrue(cache.is_file())
        cache.write_text(cache.read_text().replace('"winner": "with"', '"winner": "tie"'))
        os.environ["EVAL_JUDGE_CMD"] = "false"  # a second judge call would fail the run
        self.assertEqual(self.run_cfg("--runs", "1"), 0)

    def test_contact_sheet_stays_small(self):
        self.run_cfg()
        sheet = next(self.out().glob("contact-sheet.*"))
        self.assertLess(sheet.stat().st_size, 400 * 1024)

    def test_bad_config_is_rejected(self):
        self.t.write("bad.json", json.dumps({"examples": [{"id": "Bad Id", "skill": "demo", "prompt": "p", "rubric": RUBRIC}]}))
        self.assertEqual(make_example.main([str(self.t.root / "bad.json"), "--root", str(self.t.root)]), 2)

    def test_rubric_is_required(self):
        self.t.write("c.json", json.dumps({"examples": [{"id": "x", "skill": "demo", "prompt": "p"}]}))
        self.assertEqual(make_example.main([str(self.t.root / "c.json"), "--root", str(self.t.root)]), 2)

    def test_featuring_the_best_is_not_allowed(self):
        self.assertEqual(self.run_cfg(featuring={"pick": "best", "text": "best of three"}), 2)

    def test_judge_must_differ_from_the_generator(self):
        self.assertEqual(self.run_cfg(judge="claude:sonnet"), 2)
        self.assertEqual(self.run_cfg("--model", "haiku", "--runs", "1", judge="claude:sonnet"), 0)

    def test_missing_skill_is_reported(self):
        example = {"id": "x", "skill": "nope", "prompt": "p", "rubric": RUBRIC}
        cfg = self.t.write("c.json", json.dumps({"examples": [example]}))
        self.assertEqual(make_example.main([str(cfg), "--root", str(self.t.root)]), 2)


if __name__ == "__main__":
    unittest.main()
