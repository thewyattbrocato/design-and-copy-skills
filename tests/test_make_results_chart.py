import contextlib
import io
import json
import re
import unittest
import xml.etree.ElementTree as ET

from helpers import TempRoot, load_script, skill_md

mod = load_script("make_results_chart")
SVG = "docs/img/results.svg"


def protocol1(mean_with, mean_without, loaded=(("with", True), ("with", True), ("without", True), ("tie", False))):
    verdicts = [{"task_id": f"t{i}", "winner": w, "judge_notes": "n", "rubric_scores": {"with": 4, "without": 4},
                 "with_skill_invoked": inv} for i, (w, inv) in enumerate(loaded)]
    summary = {"with_wins": 2, "without_wins": 1, "ties": 1, "model": "sonnet", "judge": "claude:opus",
               "gate": {"passed": True, "mean_rubric_with": mean_with, "mean_rubric_without": mean_without}}
    return json.dumps({"verdicts": verdicts, "summary": summary})


def protocol2(wins, losses, ties, mean_with, mean_without, tasks=8, decision="pass"):
    verdicts = [{"task_id": f"t{i}", "winner": "tie", "judge_notes": "n", "rubric_scores": {"with": 4, "without": 4}}
                for i in range(tasks)]
    loaded = {"with_wins": wins, "without_wins": losses, "ties": ties, "tasks_with_loaded_sample": tasks,
              "loaded_samples": tasks * 3, "total_samples": tasks * 3, "mean_rubric_with": mean_with,
              "mean_rubric_without": mean_without}
    summary = {"protocol": 2, "samples": 3, "with_wins": wins, "without_wins": losses, "ties": ties, "model": "sonnet",
               "judge": "claude:opus", "gate": {"decision": decision}, "loaded": loaded}
    return json.dumps({"verdicts": verdicts, "summary": summary})


def main(*argv):
    with contextlib.redirect_stdout(io.StringIO()):
        return mod.main(list(argv))


class ResultsChartTest(unittest.TestCase):
    def setUp(self):
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        for name in ("alpha", "beta", "gamma", "delta"):
            self.t.write(f"skills/{name}/SKILL.md", skill_md(name, f"Use when making {name}. Not for others."))
        self.t.write("evals/alpha/heldout/results.json", protocol2(6, 1, 1, 4.8, 4.2))      # +0.60, solid
        self.t.write("evals/beta/heldout/results.json", protocol2(4, 3, 1, 4.3, 4.2))       # +0.10, marginal
        self.t.write("evals/gamma/heldout/results.json", protocol1(4.5, 4.2))               # +0.30, protocol 1
        # delta has no held-out result

    def stats(self):
        return mod.stats(self.t.root)

    def svg(self):
        rows, pending = self.stats()
        return mod.draw(rows, pending)

    def test_rows_are_ordered_by_rubric_difference_and_carry_loaded_only_counts(self):
        rows, pending = self.stats()
        self.assertEqual([r["name"] for r in rows], ["alpha", "gamma", "beta"])
        self.assertEqual(pending, ["delta"])
        alpha, gamma, beta = rows
        self.assertAlmostEqual(alpha["diff"], 0.6)
        self.assertEqual((alpha["wins"], alpha["losses"], alpha["ties"], alpha["tasks"]), (6, 1, 1, 8))
        # protocol 1: the tally is recomputed from the samples where the skill loaded (3 of 4 here)
        self.assertEqual((gamma["wins"], gamma["losses"], gamma["ties"], gamma["tasks"]), (2, 1, 0, 3))
        self.assertTrue(gamma["all_pairs"] and not alpha["all_pairs"])

    def test_marginal_flag_comes_from_the_results_table_rule(self):
        marginal = {r["name"]: r["marginal"] for r in self.stats()[0]}
        self.assertEqual(marginal, {"alpha": False, "gamma": True, "beta": True})  # gamma: three loaded tasks

    def test_the_svg_is_well_formed_and_every_skill_has_a_row_and_a_value(self):
        text = self.svg()
        root = ET.fromstring(text)
        ns = {"s": "http://www.w3.org/2000/svg"}
        self.assertEqual(root.find("s:title", ns).text, "Held-out results for every listed skill, loaded runs only")
        labels = [e.text for e in root.iterfind(".//s:text[@class='name']", ns)]
        self.assertEqual(labels, ["alpha", "gamma", "beta"])
        values = [e.text for e in root.iterfind(".//s:text[@class='val']", ns)]
        self.assertEqual(values, ["+0.60", "+0.30\u2020", "+0.10"])

    def test_bars_start_at_the_zero_line_and_scale_with_the_difference(self):
        root = ET.fromstring(self.svg())
        ns = {"s": "http://www.w3.org/2000/svg"}
        zero = float(root.find(".//s:line[@class='zero']", ns).get("x1"))
        bars = [e for e in root.iterfind(".//s:rect", ns) if e.get("class", "").startswith(("bar-", "hollow-"))]
        self.assertEqual(len(bars), 3)
        for bar in bars:
            self.assertAlmostEqual(float(bar.get("x")), zero, delta=0.1)
        widths = [float(b.get("width")) for b in bars]
        self.assertAlmostEqual(widths[0] / widths[1], 2.0, places=1)   # +0.60 against +0.30
        self.assertAlmostEqual(widths[1] / widths[2], 3.0, places=1)   # +0.30 against +0.10

    def test_a_negative_difference_is_drawn_to_the_left_of_zero(self):
        self.t.write("evals/delta/heldout/results.json", protocol2(4, 3, 1, 4.1, 4.3))
        rows, pending = self.stats()
        root = ET.fromstring(mod.draw(rows, pending))
        ns = {"s": "http://www.w3.org/2000/svg"}
        zero = float(root.find(".//s:line[@class='zero']", ns).get("x1"))
        last = [e for e in root.iterfind(".//s:rect", ns) if e.get("class", "").startswith(("bar-", "hollow-"))][-1]
        self.assertEqual(rows[-1]["name"], "delta")
        self.assertLess(float(last.get("x")) + float(last.get("width")), zero + 0.1)
        self.assertIn("loss", last.get("class"))
        self.assertIn("−0.20", self.svg_text(rows, pending))

    def svg_text(self, rows, pending):
        return mod.draw(rows, pending)

    def test_marginal_bars_are_hollow_and_tagged_in_words(self):
        text = self.svg()
        self.assertEqual(len(re.findall(r'class="hollow-gain"', text)), 2)
        self.assertEqual(len(re.findall(r'class="bar-gain"', text)), 1)
        self.assertEqual(text.count(">marginal<"), 2)

    def test_notes_state_the_loaded_only_basis_and_the_protocol_one_caveat(self):
        text = self.svg()
        self.assertIn("Loaded-only: counts only runs where the skill actually loaded; "
                      "task counts vary by skill; judge Opus, generator Sonnet.", text)
        self.assertIn("† One answer per side", text)
        self.assertIn("No held-out result yet: delta.", text)
        self.assertIn("gamma</text>", text)

    def test_ten_tasks_per_skill_is_written_out_when_every_suite_has_ten(self):
        for name in ("alpha", "beta"):
            self.t.write(f"evals/{name}/heldout/results.json", protocol2(5, 2, 3, 4.5, 4.0, tasks=10))
        self.t.write("evals/gamma/heldout/results.json", protocol2(5, 2, 3, 4.5, 4.0, tasks=10))
        self.assertIn("ten tasks per skill", self.svg())

    def test_dark_scheme_block_is_present_and_light_only_removes_it(self):
        text = self.svg()
        self.assertIn("@media (prefers-color-scheme:dark)", text)
        self.assertNotIn("prefers-color-scheme", mod.light_only(text))
        ET.fromstring(mod.light_only(text))

    def test_output_is_deterministic(self):
        self.assertEqual(self.svg(), self.svg())

    def test_check_mode_follows_the_committed_file(self):
        out = self.t.root / SVG
        self.assertEqual(main("--root", str(self.t.root), "--check"), 1)      # nothing committed yet
        self.assertEqual(main("--root", str(self.t.root)), 0)
        self.assertTrue(out.is_file())
        self.assertEqual(main("--root", str(self.t.root), "--check"), 0)
        self.t.write("evals/alpha/heldout/results.json", protocol2(6, 1, 1, 4.9, 4.2))  # a result changes
        self.assertEqual(main("--root", str(self.t.root), "--check"), 1)
        out.write_text("hand edited", encoding="utf-8")
        self.assertEqual(main("--root", str(self.t.root), "--check"), 1)
        main("--root", str(self.t.root))
        self.assertEqual(main("--root", str(self.t.root), "--check"), 0)

    def test_check_mode_does_not_write(self):
        main("--root", str(self.t.root), "--check")
        self.assertFalse((self.t.root / SVG).exists())


if __name__ == "__main__":
    unittest.main()
