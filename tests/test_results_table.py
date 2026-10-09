import json
import unittest

from helpers import TempRoot, load_script, skill_md

mod = load_script("results_table")
START, END = "<!-- results-table:{}:start -->", "<!-- results-table:{}:end -->"
README = "# Demo\n\n" + "\n\n".join(f"{START.format(b)}\nstale\n{END.format(b)}" for b in mod.BLOCKS) + "\n\nTail.\n"


def results(judge, **summary):
    base = {"with_wins": 3, "without_wins": 1, "ties": 4, "model": "sonnet", "model_id": "claude-sonnet-5-5",
            "date": "2026-10-04", "judge": judge,
            "gate": {"passed": True, "tolerance": 0.1, "mean_rubric_with": 4.2, "mean_rubric_without": 3.9}}
    base.update(summary)
    verdicts = [{"task_id": f"t{i}", "winner": "tie", "judge_notes": "n", "rubric_scores": {"with": 4, "without": 4},
                 "with_skill_invoked": i < 2} for i in range(4)]
    return json.dumps({"verdicts": verdicts, "summary": base})


class ResultsTableTest(unittest.TestCase):
    def setUp(self):
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        self.t.write("README.md", README)
        self.t.write("skills/alpha/SKILL.md", skill_md("alpha", "Use when setting a thing: details here. Not for beta, or gamma."))
        self.t.write("skills/beta/SKILL.md", skill_md("beta", "Use whenever you make a beta - with extras. Not for alpha."))
        self.t.write("evals/alpha/tasks.json", "[]")
        self.t.write("evals/alpha/results.json", results("grok:grok-4.7"))
        self.t.write("evals/beta/tasks.json", "[]")
        self.t.write("evals/beta/results.json", results("claude:sonnet"))
        self.t.write("evals/beta/heldout/results.json", results("claude:opus", suite="heldout"))

    def blocks(self):
        return mod.render(self.t.root)

    def test_every_results_table_has_the_same_column_count_in_each_line(self):
        for name in ("heldout", "dev", "withdrawn"):
            counts = {ln.count("|") - ln.count("\\|") for ln in self.blocks()[name]}
            self.assertEqual(len(counts), 1, name)

    def test_skills_table_comes_from_frontmatter(self):
        rows = self.blocks()["skills"]
        self.assertIn("| [alpha](skills/alpha/SKILL.md) | setting a thing | beta, or gamma |", rows)
        self.assertIn("| [beta](skills/beta/SKILL.md) | you make a beta | alpha |", rows)

    def test_copy_block_says_none_yet_while_the_folder_is_empty(self):
        self.assertEqual(self.blocks()["copy"], ["none yet"])
        self.t.write("copy-skills/README.md", "# Copy\n")
        self.assertEqual(self.blocks()["copy"], ["none yet"])

    def test_copy_skill_has_its_own_block_and_joins_the_results_tables(self):
        self.t.write("copy-skills/omega/SKILL.md", skill_md("omega", "Use when drafting an omega. Not for alpha."))
        self.t.write("evals/omega/heldout/results.json", results("claude:opus", suite="heldout"))
        blocks = self.blocks()
        self.assertIn("| [omega](copy-skills/omega/SKILL.md) | drafting an omega | alpha |", blocks["copy"])
        self.assertFalse(any("omega" in r for r in blocks["skills"]))
        omega = next(r for r in blocks["heldout"] if r.startswith("| omega"))
        self.assertIn("3 / 1 / 4", omega)
        self.assertTrue(any(r.startswith("| omega | no development results") for r in blocks["dev"]))

    def test_withdrawn_skill_is_only_in_the_withdrawn_block(self):
        self.t.write("withdrawn/delta/SKILL.md", skill_md("delta", "Use when making delta. Not for alpha."))
        self.t.write("evals/delta/heldout/results.json", results("claude:opus", suite="heldout"))
        blocks = self.blocks()
        for name in ("skills", "copy", "heldout", "dev"):
            self.assertFalse(any("delta" in r for r in blocks[name]), name)
        row = next(r for r in blocks["withdrawn"] if "delta" in r)
        self.assertIn("(withdrawn/delta/SKILL.md)", row)
        self.assertIn("3 / 1 / 4", row)

    def test_heldout_table_shows_pending_without_results(self):
        rows = self.blocks()["heldout"]
        self.assertIn("| alpha | pending clean rerun |" + " |" * 8, rows)
        self.assertEqual(rows[0].count("|"), rows[2].count("|"))
        beta = next(r for r in rows if r.startswith("| beta"))
        self.assertIn("3 / 1 / 4", beta)
        self.assertIn("2 of 4 samples (2 of 4 tasks)", beta)
        self.assertIn("`claude:opus`, a different model from the generator", beta)

    def test_protocol_one_rows_recompute_the_loaded_only_tally_from_with_skill_invoked(self):
        beta = next(r for r in self.blocks()["heldout"] if r.startswith("| beta"))
        cells = [c.strip() for c in beta.strip("|").split("|")]
        self.assertEqual(cells[1:4], ["1", "1", "3 / 1 / 4"])
        self.assertEqual((cells[4], cells[-1]), ("0 / 0 / 2 (2 tasks)", "none"))

    def test_protocol_one_loaded_only_tally_counts_only_pairs_where_the_skill_loaded(self):
        data = json.loads(results("claude:opus", suite="heldout"))
        for v, (winner, invoked) in zip(data["verdicts"], [("with", False), ("with", True), ("without", True), ("with", False)]):
            v["winner"], v["with_skill_invoked"] = winner, invoked
        self.assertEqual(mod.loaded_tally(data), {"with_wins": 1, "without_wins": 1, "ties": 0, "tasks_with_loaded_sample": 2})
        for v in data["verdicts"]:
            del v["with_skill_invoked"]
        self.assertIsNone(mod.loaded_tally(data))
        self.assertEqual(mod.result_cells(data)[3], "n/a")

    def test_loaded_column_uses_one_wording_for_both_protocols(self):
        loaded = {"with_wins": 5, "without_wins": 1, "ties": 2, "tasks_with_loaded_sample": 8, "loaded_samples": 20,
                  "total_samples": 24, "mean_rubric_with": 4.4, "mean_rubric_without": 4.0, "mean_advantage": 0.4}
        data = json.loads(results("claude:opus", suite="heldout", protocol=2, samples=3, loaded=loaded,
                                  gate={"decision": "pass", "passed": True}))
        self.assertEqual(mod.loaded_text(data), "20 of 24 samples (8 of 4 tasks)")  # the fixture has 4 verdicts
        self.assertEqual(mod.loaded_text(json.loads(results("claude:opus"))), "2 of 4 samples (2 of 4 tasks)")

    def test_marginal_marker_follows_the_documented_rule(self):
        def p2(wins, losses, ties, tasks, mean_with, mean_without, decision="pass"):
            loaded = {"with_wins": wins, "without_wins": losses, "ties": ties, "tasks_with_loaded_sample": tasks,
                      "loaded_samples": tasks * 3, "total_samples": 30, "mean_rubric_with": mean_with,
                      "mean_rubric_without": mean_without}
            return json.loads(results("claude:opus", suite="heldout", protocol=2, samples=3, loaded=loaded,
                                      gate={"decision": decision, "passed": decision == "pass"}))
        self.assertEqual(mod.marginal_reasons(p2(5, 1, 2, 8, 4.4, 4.0)), [])
        self.assertEqual(mod.marginal_reasons(p2(5, 1, 2, 8, 4.4, 4.26)), ["rubric +0.14"])
        self.assertEqual(mod.marginal_reasons(p2(5, 1, 0, 6, 4.4, 4.0)), ["6 loaded tasks"])
        self.assertEqual(mod.marginal_reasons(p2(4, 3, 1, 8, 4.4, 4.0)), ["one-task win margin"])
        self.assertEqual(mod.marginal_reasons(p2(3, 3, 3, 9, 4.4, 4.0)), ["no win margin"])
        self.assertEqual(mod.marginal_reasons(p2(5, 1, 2, 8, 4.481, 4.485)), ["rubric level"])
        self.assertEqual(mod.marginal_reasons(p2(1, 0, 0, 3, 4.0, 4.4, decision="inconclusive")), [])
        row = mod.result_cells(p2(4, 3, 1, 8, 4.2, 4.1), mark_marginal=True)[6]
        self.assertEqual(row, "pass, marginal (rubric +0.10; one-task win margin)")
        self.assertEqual(mod.result_cells(p2(4, 3, 1, 8, 4.2, 4.1))[6], "pass")

    def test_marginal_marker_on_protocol_one_uses_the_loaded_only_tally(self):
        data = json.loads(results("claude:opus", suite="heldout"))
        for v, winner in zip(data["verdicts"], ["with", "without", "tie", "with"]):
            v["winner"], v["with_skill_invoked"] = winner, True
        data["summary"]["gate"].update(mean_rubric_with=4.5, mean_rubric_without=4.0)
        self.assertEqual(mod.marginal_reasons(data), ["4 loaded tasks", "one-task win margin"])
        self.assertEqual([r for r in mod.marginal_reasons(data) if "rubric" in r], [])

    def test_not_for_is_split_off_after_a_period_semicolon_or_colon_in_any_case(self):
        for desc in ("Use when making a gizmo. Not for beta, or gamma.",
                     "Use when making a gizmo; not for beta, or gamma.",
                     "Use when making a gizmo: not for beta, or gamma.",
                     "Use when making a gizmo.  NOT FOR beta, or gamma."):
            self.assertEqual(mod.split_description(desc)[1].rstrip("."), "beta, or gamma", desc)
        self.assertEqual(mod.split_description("Use when making a gizmo that is not for show."),
                         ("Use when making a gizmo that is not for show.", ""))

    def test_skills_table_handles_semicolon_and_colon_not_for_cells(self):
        self.t.write("skills/gamma/SKILL.md", skill_md("gamma", "Use when making a gamma, in any language; not for beta (beta-skill), or alpha."))
        self.t.write("skills/delta/SKILL.md", skill_md("delta", 'Use whenever a delta is judged: "is it good", "tear it apart"; findings with severity: not for building (alpha).'))
        rows = self.blocks()["skills"]
        self.assertIn("| [gamma](skills/gamma/SKILL.md) | making a gamma, in any language | beta (beta-skill), or alpha |", rows)
        self.assertIn("| [delta](skills/delta/SKILL.md) | a delta is judged | building (alpha) |", rows)

    def test_archived_evidence_includes_a_held_out_results_file_at_the_folder_root(self):
        self.t.write("withdrawn/old-v1-evidence/results.json", results("claude:opus", suite="heldout"))
        self.t.write("withdrawn/dev-v1-evidence/results.json", results("claude:opus", suite="dev"))
        self.t.write("withdrawn/both-v1-evidence/results.json", results("claude:opus", suite="dev", with_wins=9))
        self.t.write("withdrawn/both-v1-evidence/heldout/results.json", results("claude:opus", suite="heldout"))
        rows = self.blocks()["withdrawn"]
        self.assertTrue(any(r.startswith("| old-v1-evidence |") for r in rows))
        self.assertTrue(any(r.startswith("| both-v1-evidence |") and "3 / 1 / 4" in r for r in rows))
        self.assertFalse(any("dev-v1-evidence" in r for r in rows))

    def test_protocol_two_rows_show_samples_loaded_only_tally_gate_and_secondary(self):
        loaded = {"with_wins": 5, "without_wins": 1, "ties": 2, "tasks_with_loaded_sample": 8, "loaded_samples": 20,
                  "total_samples": 24, "mean_rubric_with": 4.4, "mean_rubric_without": 4.0, "mean_advantage": 0.4}
        secondary = {"summary": {"model": "haiku", "loaded": {**loaded, "with_wins": 4, "without_wins": 3, "ties": 1}},
                     "verdicts": []}
        data = json.loads(results("claude:opus", suite="heldout", protocol=2, samples=3, loaded=loaded,
                                  gate={"decision": "pass", "passed": True}))
        data["secondary"] = secondary
        self.t.write("evals/alpha/heldout/results.json", json.dumps(data))
        alpha = next(r for r in self.blocks()["heldout"] if r.startswith("| alpha"))
        cells = [c.strip() for c in alpha.strip("|").split("|")]
        self.assertEqual(cells[1:4], ["2", "3", "3 / 1 / 4"])
        self.assertEqual(cells[4], "5 / 1 / 2 (8 tasks)")
        self.assertEqual(cells[5], "4.4 / 4.0")
        self.assertEqual(cells[6], "20 of 24 samples (8 of 4 tasks)")
        self.assertEqual(cells[7], "pass")
        self.assertEqual(cells[-1], "`haiku`: 4 / 3 / 1 loaded only")

    def test_inconclusive_gate_is_shown_as_inconclusive(self):
        loaded = {"with_wins": 2, "without_wins": 0, "ties": 1, "tasks_with_loaded_sample": 3, "loaded_samples": 9,
                  "total_samples": 24, "mean_rubric_with": 4.4, "mean_rubric_without": 4.0, "mean_advantage": 0.4}
        self.t.write("evals/alpha/heldout/results.json", results(
            "claude:opus", suite="heldout", protocol=2, samples=3, loaded=loaded,
            gate={"decision": "inconclusive", "passed": False}))
        alpha = next(r for r in self.blocks()["heldout"] if r.startswith("| alpha"))
        self.assertIn("| inconclusive |", alpha)

    def test_dev_table_names_the_judge_and_marks_superseded(self):
        rows = self.blocks()["dev"]
        alpha = next(r for r in rows if r.startswith("| alpha"))
        beta = next(r for r in rows if r.startswith("| beta"))
        self.assertIn("`grok:grok-4.7`, a different model from the generator", alpha)
        self.assertIn("superseded, held-out rerun pending", alpha)
        self.assertIn("`claude:sonnet`, same model as the generator", beta)
        self.assertIn("superseded by the held-out run", beta)

    def test_update_check_and_idempotence(self):
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 1)
        self.assertEqual(mod.main(["--root", str(self.t.root)]), 0)
        text = (self.t.root / "README.md").read_text()
        self.assertNotIn("stale", text)
        self.assertTrue(text.endswith("Tail.\n"))
        self.assertEqual(mod.main(["--root", str(self.t.root), "--check"]), 0)

    def test_missing_markers_is_an_error(self):
        self.t.write("README.md", "# No markers\n")
        self.assertEqual(mod.main(["--root", str(self.t.root)]), 2)


if __name__ == "__main__":
    unittest.main()
