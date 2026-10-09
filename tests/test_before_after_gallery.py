import json
import unittest

from helpers import TempRoot, load_script, run_main

mod = load_script("before_after_gallery")
RULE = "Chosen as the task with the largest judged difference."
README = "# Demo\n\n" + mod.START + "\nstale\n" + mod.END + "\n\nTail.\n"


def meta(skill, kind="design", **over):
    base = {"skill": skill, "kind": kind, "suite": "heldout", "task_id": "t1", "prompt": "Make a *thing* | now.",
            "loaded_only": "5 / 2 / 3", "marginal": False, "judge_gap": 1.3, "pick_rule": RULE,
            "without_file": "without.md", "with_file": "with.md"}
    base.update(over)
    return json.dumps(base)


class GalleryTest(unittest.TestCase):
    def setUp(self):
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        self.t.write("README.md", README)
        self.add("alpha", "design", without="Plain `code` | pipe\n\n- item\n[...]", with_="With <b>tags</b> & @user")
        self.add("beta", "copy", marginal=True, judge_gap="0.5")

    def add(self, skill, kind, without="without text", with_="with text", **over):
        d = f"docs/before-after/{skill}"
        self.t.write(f"{d}/meta.json", meta(skill, kind, **over))
        self.t.write(f"{d}/without.md", without)
        self.t.write(f"{d}/with.md", with_)
        self.t.write(f"evals/{skill}/heldout/runs/t1/with.md", "x")

    def text(self):
        return "\n".join(mod.render(self.t.root))

    def test_one_panel_per_skill_under_its_kind(self):
        text = self.text()
        self.assertLess(text.index("### Design skills"), text.index("<b>alpha</b>"))
        self.assertLess(text.index("<b>alpha</b>"), text.index("### Copywriting skills"))
        self.assertLess(text.index("### Copywriting skills"), text.index("<b>beta</b>"))
        self.assertEqual(text.count("<details>"), 2)

    def test_summary_shows_tally_and_marginal_only_when_marked(self):
        text = self.text()
        self.assertIn("<summary><b>alpha</b> &middot; 5 / 2 / 3 loaded only</summary>", text)
        self.assertIn("<summary><b>beta</b> &middot; 5 / 2 / 3 loaded only &middot; marginal</summary>", text)

    def test_footer_line_numbers_and_link(self):
        text = self.text()
        self.assertIn("Judged difference on this task: +1.30 rubric points. Overall for this skill: "
                      "5 wins / 2 losses / 3 ties (loaded-only) over 10 tasks.", text)
        self.assertIn("Judged difference on this task: +0.50 rubric points.", text)
        self.assertIn("[Full run files](evals/alpha/heldout/runs/t1/)", text)
        self.assertIn("the largest judged difference", text)

    def test_excerpts_render_as_plain_text_in_one_table_row(self):
        row = next(ln for ln in self.text().splitlines() if "pipe" in ln)
        self.assertEqual(row, "| Plain \\`code\\` &#124; pipe<br><br>- item<br>\\[...\\] | "
                              "With &lt;b&gt;tags&lt;/b&gt; &amp; &#64;user |")
        self.assertIn("> Make a \\*thing\\* &#124; now.", self.text())

    def test_screenshots_go_in_a_second_row_with_alt_text(self):
        self.add("alpha", "design", images=[{"file": "without.png", "alt": "Before [x]", "side": "without"},
                                            {"file": "with.png", "alt": "After", "side": "with"}])
        self.assertIn("| ![Before \\[x\\]](docs/before-after/alpha/without.png) | "
                      "![After](docs/before-after/alpha/with.png) |", self.text())

    def test_missing_run_folder_is_an_error(self):
        (self.t.root / "evals/alpha/heldout/runs/t1/with.md").unlink()
        (self.t.root / "evals/alpha/heldout/runs/t1").rmdir()
        with self.assertRaises(ValueError):
            mod.render(self.t.root)

    def test_bad_tally_and_mixed_rules_are_errors(self):
        self.add("beta", "copy", loaded_only="5-2-3")
        with self.assertRaises(ValueError):
            mod.render(self.t.root)
        self.add("beta", "copy", pick_rule="Another rule.")
        with self.assertRaises(ValueError):
            mod.render(self.t.root)

    def test_main_writes_then_check_passes_and_detects_drift(self):
        self.assertEqual(run_main(mod, self.t.root)[0], 0)
        self.assertIn("<b>alpha</b>", (self.t.root / "README.md").read_text())
        self.assertIn("Tail.", (self.t.root / "README.md").read_text())
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 0)
        self.t.write("docs/before-after/alpha/with.md", "changed")
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 1)

    def test_missing_markers_are_an_error(self):
        self.t.write("README.md", "# Demo\n")
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 2)


if __name__ == "__main__":
    unittest.main()
