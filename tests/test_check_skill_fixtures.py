import json
import unittest

from helpers import TempRoot, load_script, run_main

mod = load_script("check_skill_fixtures")


def task(prompt, rubric=("Criterion.",), tid="t0"):
    return {"id": tid, "kind": "critique", "prompt": prompt, "rubric": list(rubric)}


class ExtractTest(unittest.TestCase):
    def test_names_numbers_and_quotes_are_extracted(self):
        found = mod.extract('Design a page for a scheduling tool called Tidewell. Kettle & Co sells 420 people '
                            'a "Welcome back to the whole studio" plan for $12,480 or 4.2% off, opening at 4:40.')
        for expected in ("Tidewell", "Kettle & Co", "420 people", "Welcome back to the whole studio", "$12,480", "4.2%", "4:40"):
            self.assertIn(expected, found)

    def test_generic_words_and_common_design_values_are_not_extracted(self):
        text = ("Design a settings page. Use 14px body text, 16px inputs, line height 1.5, 12 columns, 50% width, "
                "1280px wide, in 2024 we saw 1,240 hits and a 2% change, a Cancel and a Save button, and a Profile section. Show the Profile and profile.")
        self.assertEqual(mod.extract(text), [])

    def test_sentence_starts_are_not_names(self):
        self.assertEqual(mod.extract("Critique this. Our team agrees. Notifications are noisy."), [])

    def test_series_paths_and_pixels(self):
        found = mod.extract("Opened: 120, 135, 128, 150 on /v1/refunds in a 1337px frame.")
        for expected in ("120, 135, 128", "135, 128, 150", "/v1/refunds", "1337px"):
            self.assertIn(expected, found)

    def test_code_in_quotes_is_ignored(self):
        self.assertEqual(mod.extract("x = 'a rather long (quoted) code string'"), [])


class CheckTest(unittest.TestCase):
    def setUp(self):
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)

    def write_tasks(self, suite, tasks):
        rel = "evals/demo/tasks.json" if suite == "dev" else "evals/demo/heldout/tasks.json"
        self.t.write(rel, json.dumps(tasks))

    def check(self, *extra):
        import contextlib
        import io
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = mod.main(["--root", str(self.t.root), *extra])
        return code, out.getvalue()

    def test_empty_or_missing_skills_pass(self):
        self.write_tasks("heldout", [task("A tool called Tidewell.")])
        code, out = self.check()
        self.assertEqual(code, 0, out)
        self.assertIn("0 errors, 0 warnings", out)
        self.t.write("skills/.gitkeep", "")
        self.assertEqual(self.check()[0], 0)
        self.assertEqual(run_main(mod, self.t.root)[0], 0)

    def test_no_evals_passes(self):
        self.t.write("skills/demo/SKILL.md", "Anything at all.")
        self.assertEqual(self.check()[0], 0)

    def test_heldout_hit_fails_with_file_and_line(self):
        self.write_tasks("heldout", [task("Critique the page for a tool called Tidewell.", tid="held-1")])
        self.t.write("skills/demo/references/x.md", "# Notes\n\nFirst line.\nFor example Tidewell shows five sections.\n")
        code, out = self.check()
        self.assertEqual(code, 1)
        self.assertIn("error: skills/demo/references/x.md:4: 'Tidewell'", out)
        self.assertIn("evals/demo/heldout/tasks.json task held-1", out)

    def test_copy_skills_folder_is_scanned(self):
        self.write_tasks("heldout", [task("Write a launch note for a tool called Tidewell.", tid="held-1")])
        self.t.write("copy-skills/demo/SKILL.md", "For example Tidewell ships on Friday.\n")
        code, out = self.check()
        self.assertEqual(code, 1)
        self.assertIn("error: copy-skills/demo/SKILL.md:1: 'Tidewell'", out)

    def test_empty_copy_skills_folder_passes(self):
        self.write_tasks("heldout", [task("Write a launch note for a tool called Tidewell.")])
        self.t.write("copy-skills/README.md", "Nothing here yet.\n")
        self.assertEqual(self.check()[0], 0)

    def test_withdrawn_folder_is_scanned(self):
        self.write_tasks("heldout", [task("Critique the page for a tool called Tidewell.", tid="held-1")])
        self.t.write("withdrawn/demo/SKILL.md", "For example Tidewell shows five sections.\n")
        code, out = self.check()
        self.assertEqual(code, 1)
        self.assertIn("error: withdrawn/demo/SKILL.md:1: 'Tidewell'", out)

    def test_dev_hit_warns_and_strict_fails(self):
        self.write_tasks("dev", [task("A watchlist shows about 25 rows at once.", tid="dev-1")])
        self.t.write("skills/demo/SKILL.md", "Keep 25 rows visible.\n")
        code, out = self.check()
        self.assertEqual(code, 0)
        self.assertIn("warning: skills/demo/SKILL.md:1: '25 rows'", out)
        self.assertEqual(self.check("--strict")[0], 1)

    def test_rubric_text_is_checked_and_matching_is_whole_token(self):
        self.write_tasks("heldout", [task("Plain prompt.", rubric=['Says "week to week it never settles".'])])
        self.t.write("skills/demo/a.md", "Mentions the week to week it never settles pattern.\n")
        self.assertEqual(self.check()[0], 1)
        self.write_tasks("heldout", [task("Opened 9,420 items.")])
        self.t.write("skills/demo/a.md", "A total of 19,420 items and 9,4201 other.\n")
        self.assertEqual(self.check()[0], 0)

    def test_list_prints_fixtures(self):
        self.write_tasks("heldout", [task("A tool called Tidewell.")])
        code, out = self.check("--list")
        self.assertEqual(code, 0)
        self.assertIn("'Tidewell'", out)
        self.assertIn("1 fixtures from 1 task files", out)


if __name__ == "__main__":
    unittest.main()
