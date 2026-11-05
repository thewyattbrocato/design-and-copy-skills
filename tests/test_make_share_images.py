import json
import unittest

from helpers import TempRoot, load_script, run_main, tiny_png

mod = load_script("make_share_images")
pngstamp = load_script("pngstamp")
RULE = "Chosen as the task with the largest judged difference."
README = "\n\n".join(f"<!-- share-images:{b}:start -->\nstale\n<!-- share-images:{b}:end -->"
                     for b in ("banner", "families", "cards")) + "\n"
ALT = "# Alt\n\n<!-- share-images:alt:start -->\n<!-- share-images:alt:end -->\n"


def skill_md(name):
    return f"---\nname: {name}\ndescription: Use when testing {name}. Not for anything else.\n---\n\nBody.\n"


def results(wins, losses, ties, mean_with, mean_without, tasks=10, gap=1.0):
    loaded = {"with_wins": wins, "without_wins": losses, "ties": ties, "tasks_with_loaded_sample": tasks,
              "loaded_samples": 3 * tasks, "total_samples": 30, "mean_rubric_with": mean_with,
              "mean_rubric_without": mean_without, "mean_advantage": round(mean_with - mean_without, 3)}
    verdict = {"task_id": "t1", "winner": "with", "samples": [{"winner": "with", "loaded": True}],
               "loaded_winner": "with", "loaded_rubric_scores": {"with": 3 + gap, "without": 3}}
    return json.dumps({"summary": {"protocol": 2, "judge": "claude:opus", "samples": 3, "with_wins": wins,
                                   "without_wins": losses, "ties": ties, "loaded": loaded,
                                   "gate": {"decision": "pass", "passed": True}}, "verdicts": [verdict]})


class ShareImagesTest(unittest.TestCase):
    def setUp(self):
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        self.t.write("README.md", README)
        self.t.write("docs/img/ALT.md", ALT)
        self.skill("skills", "alpha", results(6, 1, 3, 4.5, 4.0))
        self.skill("skills", "beta", results(4, 3, 0, 4.1, 4.05, tasks=7))
        self.skill("copy-skills", "gamma", results(5, 0, 1, 4.6, 4.0, tasks=7))
        self.t.write("withdrawn/delta-pulled-evidence/heldout/tasks.json", "[]")
        self.t.write("withdrawn/alpha-pulled-evidence/heldout/tasks.json", "[]")
        self.gallery("alpha", "design", "Without answer line.", "With answer line.")
        self.gallery("gamma", "copy", "Old **bold** line here.", "New line here.")
        self.families([
            {"slug": "one", "name": "One", "kind": "design", "changes": "Changes one.", "skills": ["alpha", "beta"],
             "example": "alpha", "lines": {"without": ["Without answer line."], "with": ["With answer line."]}},
            {"slug": "two", "name": "Two", "kind": "copy", "changes": "Changes two.", "skills": ["gamma"],
             "example": "gamma", "lines": {"without": ["Old bold line"], "with": ["New line here."]}}])

    def skill(self, folder, name, res):
        self.t.write(f"{folder}/{name}/SKILL.md", skill_md(name))
        self.t.write(f"evals/{name}/heldout/results.json", res)
        self.t.write(f"evals/{name}/heldout/tasks.json", json.dumps([{"id": "t1", "prompt": "Do it."}]))

    def gallery(self, name, kind, without, with_):
        d = f"docs/before-after/{name}"
        self.t.write(f"{d}/meta.json", json.dumps({
            "skill": name, "kind": kind, "suite": "heldout", "task_id": "t1", "prompt": "Do it.",
            "pick_rule": RULE, "without_file": "without.md", "with_file": "with.md"}))
        self.t.write(f"{d}/without.md", without)
        self.t.write(f"{d}/with.md", with_)
        self.t.write(f"evals/{name}/heldout/runs/t1/without.md", without)
        self.t.write(f"evals/{name}/heldout/runs/t1/with.md", with_)

    def families(self, fams):
        self.t.write("docs/launch/families.json", json.dumps({"families": fams}))

    def outputs(self):
        return mod.outputs(self.t.root)

    def stamp_pngs(self):
        """Stand-in PNG copies stamped as --png would stamp them, without rendering."""
        files, _ = self.outputs()
        for rel, png, _ in mod.png_copies(files):
            path = self.t.root / png
            path.write_bytes(tiny_png())
            pngstamp.stamp(path, pngstamp.source_digest(files[rel], (self.t.root / rel).parent))

    def test_counts_come_from_the_skill_folders_and_results(self):
        files, blocks = self.outputs()
        self.assertIn("3 skills for AI coding agents.", files["docs/launch/hero.svg"])
        self.assertIn("2 design", files["docs/launch/hero.svg"])
        self.assertIn("1 copywriting", files["docs/launch/hero.svg"])
        gate = files["docs/launch/test-gate.svg"]
        self.assertIn("15 wins, 4 losses, 4 ties", gate)
        self.assertIn("23 held-out tasks where the skill loaded.", gate)
        self.assertIn("2 plain passes", gate)
        self.assertIn("1 marginal pass, labelled", gate)

    def test_only_pulled_skills_that_never_shipped_are_counted_as_not_in_the_library(self):
        gate = self.outputs()[0]["docs/launch/test-gate.svg"]
        self.assertIn("One more skill did not pass and is not in the library.", gate)
        self.assertNotIn("alpha", gate)

    def test_map_marks_marginal_passes_in_words_for_the_alt_text(self):
        files, blocks = self.outputs()
        self.assertIn("One (design, 2): alpha, beta (marginal).", files["docs/launch/skill-families.svg"])
        self.assertIn("3 skills in 2 families", files["docs/launch/skill-families.svg"])
        self.assertTrue(any("docs/launch/skill-families.svg" in ln for ln in blocks["families"]))

    def test_every_listed_skill_needs_exactly_one_family(self):
        self.families([{"slug": "one", "name": "One", "kind": "design", "changes": "x", "skills": ["alpha"],
                        "example": "alpha", "lines": {"without": ["Without answer line."], "with": ["With answer line."]}},
                       {"slug": "two", "name": "Two", "kind": "copy", "changes": "x", "skills": ["gamma"],
                        "example": "gamma", "lines": {"without": ["Old bold line"], "with": ["New line here."]}}])
        with self.assertRaisesRegex(ValueError, "no family for beta"):
            self.outputs()

    def test_a_family_mixing_design_and_copy_skills_is_an_error(self):
        self.families([{"slug": "one", "name": "One", "kind": "design", "changes": "x",
                        "skills": ["alpha", "beta", "gamma"], "example": "alpha",
                        "lines": {"without": ["Without answer line."], "with": ["With answer line."]}}])
        with self.assertRaisesRegex(ValueError, "copy skill"):
            self.outputs()

    def test_quoted_lines_must_be_in_the_stored_answer(self):
        data = json.loads((self.t.root / "docs/launch/families.json").read_text())
        data["families"][1]["lines"]["with"] = ["A line the model never wrote."]
        self.families(data["families"])
        with self.assertRaisesRegex(ValueError, "not in"):
            self.outputs()

    def test_cards_carry_the_example_numbers_and_escape_text(self):
        files, blocks = self.outputs()
        card = files["docs/launch/families/two.html"]
        self.assertIn("Example: gamma, held-out task t1, sample 1.", card)
        self.assertIn("Judged difference +1.00", card)
        self.assertIn("won 5, lost 0 and tied 1", card)
        self.assertIn("<p>New line here.</p>", card)
        self.assertTrue(blocks["alt"][0].startswith("| File | Alt text |"))

    def test_main_writes_then_check_passes_and_detects_drift(self):
        self.assertEqual(run_main(mod, self.t.root)[0], 0)
        readme = (self.t.root / "README.md").read_text()
        self.assertIn('<img src="docs/img/banner.svg" alt="', readme)
        self.assertIn("docs/launch/families/one.png", readme)
        self.assertIn("docs/launch/families/one.png", (self.t.root / "docs/img/ALT.md").read_text())
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 1)  # no PNG copies yet
        self.stamp_pngs()
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 0)
        self.skill("copy-skills", "epsilon", results(5, 0, 1, 4.6, 4.0))
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 2)

    def test_every_svg_and_card_but_the_banner_has_a_png_copy(self):
        files, _ = self.outputs()
        pngs = [png for _, png, _ in mod.png_copies(files)]
        self.assertIn("docs/launch/hero.png", pngs)
        self.assertIn("docs/launch/families/one.png", pngs)
        self.assertNotIn("docs/img/banner.png", pngs)
        self.assertEqual(dict((png, size) for _, png, size in mod.png_copies(files))["docs/launch/hero.png"], (1600, 900))

    def test_check_fails_on_a_png_left_behind_by_a_source_change(self):
        run_main(mod, self.t.root)
        self.stamp_pngs()
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 0)
        pngstamp.stamp(self.t.root / "docs/launch/hero.png", "0" * 64)
        self.assertEqual(mod.stale_pngs(self.t.root, self.outputs()[0]),
                         ["docs/launch/hero.png was rendered from a different source"])
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 1)

    def test_a_card_png_goes_stale_when_its_screenshot_changes(self):
        run_main(mod, self.t.root)
        files, _ = self.outputs()
        self.t.write("docs/launch/families/shot.png", "old")
        files["docs/launch/families/one.html"] += '<img src="shot.png">'
        rel = "docs/launch/families/one.html"
        path = self.t.root / "docs/launch/families/one.png"
        path.write_bytes(tiny_png())
        pngstamp.stamp(path, pngstamp.source_digest(files[rel], path.parent))
        self.assertIsNone(pngstamp.stale(path, files[rel], path.parent))
        self.t.write("docs/launch/families/shot.png", "new")
        self.assertEqual(pngstamp.stale(path, files[rel], path.parent), "was rendered from a different source")

    def test_missing_markers_are_an_error(self):
        self.t.write("README.md", "# Demo\n")
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 2)


if __name__ == "__main__":
    unittest.main()
