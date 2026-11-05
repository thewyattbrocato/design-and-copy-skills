import json
import unittest

from helpers import TempRoot, load_script, run_main

mod = load_script("before_after_gallery")
RULE = "Chosen as the task with the largest judged difference."
README = ("# Demo\n\n" + mod.FEATURED_START + "\nstale\n" + mod.FEATURED_END + "\n\n" + mod.START + "\nstale\n" + mod.END
          + "\n\nTail.\n")
ALT = "# Alt\n\n" + mod.ALT_START + "\nstale\n" + mod.ALT_END + "\n\nAfter.\n"
PROMPT = "Make a *thing* | now."
WITHOUT = "Plain `code` | pipe\n\n- item\n\nA later line."
WITH = "With <b>tags</b> & @user"


def sample(winner="with", loaded=True):
    return {"winner": winner, "loaded": loaded}


def verdict(task_id, gap, samples=None, loaded=True):
    samples = samples or [sample(), sample(), sample("tie")]
    return {"task_id": task_id, "winner": "with", "samples": samples,
            "loaded_winner": "with" if loaded else None,
            "loaded_rubric_scores": {"with": 3.0 + gap, "without": 3.0} if loaded else None,
            "rubric_scores": {"with": 3.0 + gap, "without": 3.0}}


def results(verdicts, wins=5, losses=2, ties=3, mean_with=4.4, mean_without=4.0, tasks=10):
    loaded = {"with_wins": wins, "without_wins": losses, "ties": ties, "tasks_with_loaded_sample": tasks,
              "loaded_samples": 28, "total_samples": 30, "mean_rubric_with": mean_with,
              "mean_rubric_without": mean_without, "mean_advantage": round(mean_with - mean_without, 3)}
    return json.dumps({"summary": {"protocol": 2, "judge": "claude:opus", "same_model_judge": False, "samples": 3,
                                   "with_wins": wins, "without_wins": losses, "ties": ties, "loaded": loaded,
                                   "gate": {"decision": "pass", "passed": True}},
                       "verdicts": verdicts})


class GalleryTest(unittest.TestCase):
    def setUp(self):
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        self.t.write("README.md", README)
        self.t.write("docs/img/ALT.md", ALT)
        self.add("alpha", "design", without="Plain `code` | pipe\n\n- item\n[...]", with_=WITH, featured=True)
        self.add("beta", "copy", res=results([verdict("t1", 0.5), verdict("t2", 0.2)], wins=4, losses=3, ties=0,
                                              mean_with=4.1, mean_without=4.05, tasks=7))

    def add(self, skill, kind, without="A later line.", with_="With <b>tags</b>", res=None, stored=None, **over):
        d = f"docs/before-after/{skill}"
        meta = {"skill": skill, "kind": kind, "suite": "heldout", "task_id": "t1", "prompt": PROMPT,
                "pick_rule": RULE, "without_file": "without.md", "with_file": "with.md"}
        meta.update(over)
        self.t.write(f"{d}/meta.json", json.dumps(meta))
        self.t.write(f"{d}/without.md", without)
        self.t.write(f"{d}/with.md", with_)
        self.t.write(f"evals/{skill}/heldout/tasks.json", json.dumps([{"id": "t1", "prompt": PROMPT},
                                                                       {"id": "t2", "prompt": "Other."}]))
        self.t.write(f"evals/{skill}/heldout/results.json", res or results([verdict("t1", 1.3), verdict("t2", 0.4)]))
        stored = stored or {"without.md": WITHOUT, "with.md": WITH + "\n\nMore of the answer."}
        for name, text in stored.items():
            self.t.write(f"evals/{skill}/heldout/runs/t1/{name}", text)

    def text(self):
        return "\n".join(mod.render(self.t.root))

    def test_one_panel_per_skill_under_its_kind(self):
        text = self.text()
        self.assertLess(text.index("### Design skills"), text.index("<b>alpha</b>"))
        self.assertLess(text.index("<b>alpha</b>"), text.index("### Copywriting skills"))
        self.assertLess(text.index("### Copywriting skills"), text.index("<b>beta</b>"))
        self.assertEqual(text.count("<details>"), 2)

    def test_tally_and_marginal_mark_come_from_the_results_file(self):
        text = self.text()
        self.assertIn("<summary><b>alpha</b> &middot; 5 / 2 / 3 loaded only</summary>", text)
        self.assertIn("<summary><b>beta</b> &middot; 4 / 3 / 0 loaded only &middot; marginal</summary>", text)

    def test_footer_line_numbers_and_link(self):
        text = self.text()
        self.assertIn("Judged difference on this task: +1.30 rubric points. Overall for this skill: "
                      "5 wins / 2 losses / 3 ties (loaded-only) over 10 tasks.", text)
        self.assertIn("Judged difference on this task: +0.50 rubric points.", text)
        self.assertIn("The excerpts are from sample 1 of each side. [Full run files](evals/alpha/heldout/runs/t1/)", text)
        self.assertIn("the largest judged difference", text)

    def test_excerpts_render_as_plain_text_in_one_table_row(self):
        row = next(ln for ln in self.text().splitlines() if "pipe" in ln)
        self.assertEqual(row, "| Plain \\`code\\` &#124; pipe<br><br>- item<br>\\[...\\] | "
                              "With &lt;b&gt;tags&lt;/b&gt; &amp; &#64;user |")
        self.assertIn("> Make a \\*thing\\* &#124; now.", self.text())

    def test_an_excerpt_that_is_not_in_the_stored_answer_is_an_error(self):
        self.add("alpha", "design", with_="With <b>tags</b> and a rewritten ending")
        with self.assertRaisesRegex(ValueError, "not in"):
            mod.render(self.t.root)

    def test_a_cut_must_be_marked(self):
        self.add("alpha", "design", without="Plain `code` | pipe\nA later line.")
        with self.assertRaises(ValueError):
            mod.render(self.t.root)
        self.add("alpha", "design", without="Plain `code` | pipe\n[...]\nA later line.")
        self.assertIn("A later line.", self.text())

    def test_the_prompt_must_be_the_task_prompt(self):
        self.add("alpha", "design", prompt="A paraphrase.")
        with self.assertRaisesRegex(ValueError, "prompt differs"):
            mod.render(self.t.root)

    def test_a_task_with_a_larger_difference_must_be_picked_or_passed_over_with_a_reason(self):
        self.add("alpha", "design", res=results([verdict("t1", 0.4), verdict("t2", 1.3)]))
        with self.assertRaisesRegex(ValueError, "larger judged difference"):
            mod.render(self.t.root)
        self.add("alpha", "design", res=results([verdict("t1", 0.4), verdict("t2", 1.3)]),
                 passed_over=[{"task_id": "t2", "reason": "the answers quote a third party at length"}])
        self.assertIn("+0.40 rubric points", self.text())

    def test_a_task_where_the_skill_did_not_load_cannot_be_shown(self):
        self.add("alpha", "design", res=results([verdict("t1", 1.3, loaded=False), verdict("t2", 0.4)]))
        with self.assertRaisesRegex(ValueError, "did not load"):
            mod.render(self.t.root)

    def test_the_first_loaded_sample_is_the_one_shown(self):
        res = results([verdict("t1", 1.3, samples=[sample(loaded=False), sample(), sample()]), verdict("t2", 0.4)])
        self.add("alpha", "design", res=res, stored={"without.s1.md": WITHOUT, "with.s1.md": WITH})
        self.assertIn("The excerpts are from sample 2 of each side.", self.text())

    def test_build_answers_need_byte_identical_screenshots(self):
        for name in ("with.md", "without.md"):
            (self.t.root / f"evals/alpha/heldout/runs/t1/{name}").unlink()
        images = [{"file": "without.png", "alt": "Before [x]", "side": "without"},
                  {"file": "with.png", "alt": "After", "side": "with"}]
        self.add("alpha", "design", stored={"without.html": "<p>a</p>", "with.html": "<p>b</p>",
                                            "without.png": "PNG-A", "with.png": "PNG-B"}, images=images)
        self.t.write("docs/before-after/alpha/without.png", "PNG-A")
        self.t.write("docs/before-after/alpha/with.png", "PNG-B")
        text = self.text()
        self.assertIn("| ![Before \\[x\\]](docs/before-after/alpha/without.png) | "
                      "![After](docs/before-after/alpha/with.png) |", text)
        self.assertIn("Both answers are web pages; the screenshots are the stored renders of sample 1", text)
        self.t.write("docs/before-after/alpha/with.png", "PNG-other")
        with self.assertRaisesRegex(ValueError, "not a copy"):
            mod.render(self.t.root)

    def test_featured_block_shows_prompt_answers_and_the_judge_result(self):
        text = "\n".join(mod.featured_lines(self.t.root))
        self.assertIn("with and without the `alpha` skill installed:", text)
        self.assertIn("> Make a \\*thing\\* &#124; now.", text)
        self.assertIn("The answer with the skill won this task, 2 of 3 samples, by +1.30 rubric points", text)
        self.assertIn("`claude:opus`, a different model from the one that wrote the answers", text)
        self.assertIn("the skill won 5, lost 2 and tied 3", text)
        self.assertIn("This is one example, not a typical one", text)
        self.assertIn("Examples for 1 other skills", text)

    def test_featured_block_says_so_when_the_skill_lost_the_task(self):
        v = verdict("t1", 1.3, samples=[sample("without")])
        v["winner"] = "without"
        self.add("alpha", "design", without="Plain `code` | pipe\n\n- item\n[...]", with_=WITH, featured=True,
                 res=results([v, verdict("t2", 0.4)]))
        self.assertIn("The answer without the skill won this task, 1 of 1 samples",
                      "\n".join(mod.featured_lines(self.t.root)))

    def test_exactly_one_skill_must_be_featured(self):
        self.add("beta", "copy", featured=True)
        with self.assertRaises(ValueError):
            mod.featured_lines(self.t.root)
        self.add("alpha", "design")
        self.add("beta", "copy")
        with self.assertRaises(ValueError):
            mod.featured_lines(self.t.root)

    def test_missing_run_folder_is_an_error(self):
        for name in ("with.md", "without.md"):
            (self.t.root / f"evals/alpha/heldout/runs/t1/{name}").unlink()
        (self.t.root / "evals/alpha/heldout/runs/t1").rmdir()
        with self.assertRaises(ValueError):
            mod.render(self.t.root)

    def test_bad_kind_and_mixed_rules_are_errors(self):
        self.add("beta", "other")
        with self.assertRaises(ValueError):
            mod.render(self.t.root)
        self.add("beta", "copy", pick_rule="Another rule.")
        with self.assertRaises(ValueError):
            mod.render(self.t.root)

    def test_main_writes_then_check_passes_and_detects_drift(self):
        self.assertEqual(run_main(mod, self.t.root)[0], 0)
        self.assertIn("<b>alpha</b>", (self.t.root / "README.md").read_text())
        self.assertIn("**Judge result.**", (self.t.root / "README.md").read_text())
        self.assertIn("Tail.", (self.t.root / "README.md").read_text())
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 0)
        self.t.write("docs/before-after/alpha/with.md", "With <b>tags</b>")
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 1)

    def test_missing_markers_are_an_error(self):
        self.t.write("README.md", "# Demo\n")
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 2)

    def test_alt_md_lists_each_screenshot_with_the_readme_alt_text(self):
        self.add("alpha", "design", stored={"without.md": WITHOUT, "with.md": WITH, "without.png": "a", "with.png": "b"},
                 images=[{"side": "with", "file": "with.png", "alt": "A | calm page."},
                         {"side": "without", "file": "without.png", "alt": "A  busy page."}], featured=True)
        self.t.write("docs/before-after/alpha/without.png", "a")
        self.t.write("docs/before-after/alpha/with.png", "b")
        rows = mod.alt_lines(self.t.root)
        self.assertEqual(rows[2:], ["| `docs/before-after/alpha/without.png` (without the skill) | A busy page. |",
                                    "| `docs/before-after/alpha/with.png` (with the skill) | A \\| calm page. |"])
        self.assertEqual(run_main(mod, self.t.root)[0], 0)
        alt = (self.t.root / "docs/img/ALT.md").read_text()
        self.assertIn(rows[2], alt)
        self.assertIn("After.", alt)
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 0)
        self.t.write("docs/img/ALT.md", ALT)
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 1)


if __name__ == "__main__":
    unittest.main()
