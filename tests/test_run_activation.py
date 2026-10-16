import contextlib
import io
import json
import os
import shlex
import sys
import unittest
from pathlib import Path

from helpers import TempRoot, load_script, run_main, skill_md

import activation as act  # noqa: E402  (helpers puts scripts/ on sys.path)

run_activation = load_script("run_activation")
validate_evals = load_script("validate_evals")
activation_summary = load_script("activation_summary")

MOCK = Path(__file__).resolve().parent / "mock_eval_cmd.py"
ROUTES = {"miss-me": "beta", "topic-a": "alpha", "topic-b": "beta"}


def stub():
    return " ".join(shlex.quote(p) for p in (sys.executable, str(MOCK), "generate"))


def requests(own, other, extra_load=None):
    """Six should_load requests that route to `own` and four should_not_load ones: three for `other`, one for no skill."""
    load = [f"topic-{own} {own} ask {i}" for i in range(6)]
    if extra_load:
        load[0] = extra_load
    return {"should_load": load, "should_not_load": [f"topic-{other} {own} side {i}" for i in range(3)] + [f"topic-z {own} off"]}


class Base(unittest.TestCase):
    def setUp(self):
        self._saved = {k: os.environ.get(k) for k in ("EVAL_GENERATOR_CMD", "EVAL_MOCK_ROUTES", "EVAL_MOCK_LOG")}
        os.environ["EVAL_GENERATOR_CMD"] = stub()
        os.environ["EVAL_MOCK_ROUTES"] = json.dumps(ROUTES)
        os.environ.pop("EVAL_MOCK_LOG", None)
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        self.addCleanup(self.restore)
        self.t.write("skills/alpha/SKILL.md", skill_md("alpha", "Use for topic a things. Not for topic b (beta)."))
        self.t.write("copy-skills/beta/SKILL.md", skill_md("beta", "Use for topic b things. Not for topic a (alpha)."))
        self.t.write("evals/alpha/activation.json", json.dumps(requests("a", "b")))
        self.t.write("evals/beta/activation.json", json.dumps(requests("b", "a")))

    def restore(self):
        for k, v in self._saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v

    def run_all(self, *extra):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return run_activation.main(["--root", str(self.t.root), *extra])

    def results(self, skill):
        return json.loads((self.t.root / "evals" / skill / "activation-results.json").read_text())


class RunTest(Base):
    def test_writes_a_results_file_per_skill_with_counts(self):
        self.assertEqual(self.run_all(), 0)
        a = self.results("alpha")
        self.assertEqual((a["skill"], a["model"], a["catalog_size"]), ("alpha", "haiku", 2))
        self.assertEqual(a["should_load"]["picked"], 6)
        self.assertEqual(a["should_load"]["recall"], 1.0)
        self.assertEqual(a["should_not_load"]["false_picks"], 0)
        self.assertEqual([r["picked"] for r in a["should_not_load"]["results"]], ["beta", "beta", "beta", None])

    def test_a_missed_request_and_a_false_pick_are_counted_and_attributed(self):
        data = requests("a", "b", extra_load="miss-me topic-a")
        data["should_not_load"][0] = "topic-a wrongly claimed"
        self.t.write("evals/alpha/activation.json", json.dumps(data))
        self.assertEqual(self.run_all(), 0)
        a = self.results("alpha")
        self.assertEqual(a["should_load"]["picked"], 5)
        self.assertEqual(a["should_load"]["results"][0], {"prompt": "miss-me topic-a", "picked": "beta", "correct": False})
        self.assertEqual(a["should_not_load"]["false_picks"], 1)
        self.assertEqual(a["should_not_load"]["false_pick_rate"], 0.25)
        self.assertTrue(a["should_not_load"]["results"][0]["false_pick"])

    def test_every_request_is_one_call_and_shows_all_skills_but_no_body(self):
        log = self.t.root / "calls.log"
        os.environ["EVAL_MOCK_LOG"] = str(log)
        self.assertEqual(self.run_all(), 0)
        self.assertEqual(len(log.read_text().splitlines()), 20)
        rows = act.catalog(self.t.root)
        prompt = act.router_prompt(rows, "some request")
        self.assertIn("- alpha: Use for topic a things.", prompt)
        self.assertIn("- beta: Use for topic b things.", prompt)
        self.assertNotIn("When not to use", prompt)

    def test_a_reply_naming_no_skill_after_three_asks_counts_as_no_pick(self):
        os.environ["EVAL_MOCK_ROUTES"] = json.dumps({"topic-a a ask 0": "interaction-thing", **ROUTES})
        log = self.t.root / "calls.log"
        os.environ["EVAL_MOCK_LOG"] = str(log)
        self.assertEqual(self.run_all("--skills", "alpha"), 0)
        self.assertIsNone(self.results("alpha")["should_load"]["results"][0]["picked"])
        self.assertEqual(len(log.read_text().splitlines()), 10 + 2)  # two extra asks for the unusable reply

    def test_skills_filter_runs_only_those(self):
        self.assertEqual(self.run_all("--skills", "beta"), 0)
        self.assertTrue((self.t.root / "evals/beta/activation-results.json").is_file())
        self.assertFalse((self.t.root / "evals/alpha/activation-results.json").exists())

    def test_unknown_skill_and_bad_activation_file_are_errors(self):
        self.assertEqual(self.run_all("--skills", "nope"), 2)
        self.t.write("evals/alpha/activation.json", json.dumps({"should_load": ["x"], "should_not_load": []}))
        self.assertEqual(self.run_all(), 2)

    def test_dry_run_asks_nothing(self):
        os.environ["EVAL_GENERATOR_CMD"] = "false"
        self.assertEqual(self.run_all("--dry-run"), 0)
        self.assertFalse((self.t.root / "evals/alpha/activation-results.json").exists())

    def test_a_failing_call_reports_the_skill_and_still_writes_the_others(self):
        bad = requests("a", "b")
        bad["should_load"][1] = "topic-a boom"
        self.t.write("evals/alpha/activation.json", json.dumps(bad))
        orig = run_activation.ask

        def flaky(rows, request, *a, **k):
            if "boom" in request:
                raise run_activation.ek.EvalError("model unreachable")
            return orig(rows, request, *a, **k)
        run_activation.ask = flaky
        self.addCleanup(setattr, run_activation, "ask", orig)
        self.assertEqual(self.run_all(), 2)
        self.assertFalse((self.t.root / "evals/alpha/activation-results.json").exists())
        self.assertTrue((self.t.root / "evals/beta/activation-results.json").is_file())


class ParseTest(unittest.TestCase):
    NAMES = ["chart-design", "color-palette"]

    def test_plain_and_decorated_names_and_none(self):
        self.assertEqual(act.parse_pick("chart-design", self.NAMES), "chart-design")
        self.assertEqual(act.parse_pick("`color-palette`.\n", self.NAMES), "color-palette")
        self.assertEqual(act.parse_pick("I'd load chart-design here.", self.NAMES), "chart-design")
        self.assertIsNone(act.parse_pick("NONE", self.NAMES))
        self.assertIsNone(act.parse_pick("None - nothing fits", self.NAMES))

    def test_unknown_or_two_names_raise(self):
        for reply in ("chart", "chart-design and color-palette", "", "design"):
            with self.assertRaises(ValueError):
                act.parse_pick(reply, self.NAMES)

    def test_a_name_inside_a_longer_hyphenated_word_is_not_a_match(self):
        with self.assertRaises(ValueError):
            act.parse_pick("chart-design-extra", self.NAMES)


class ValidatorTest(Base):
    def validate(self, skill="alpha"):
        warnings = []
        context = validate_evals.activation_context(self.t.root)
        errors = validate_evals.validate_activation_files(self.t.root / "evals" / skill, context, warnings)
        return errors, warnings

    def test_valid_files_pass_and_a_missing_results_file_warns(self):
        errors, warnings = self.validate()
        self.assertEqual(errors, [])
        self.assertTrue(any("activation-results.json is missing" in w for w in warnings))
        self.run_all()
        self.assertEqual(self.validate(), ([], []))

    def coverage(self):
        return validate_evals.activation_coverage(self.t.root / "evals", validate_evals.activation_context(self.t.root))

    def test_every_live_skill_needs_an_activation_json(self):
        self.assertEqual(self.coverage(), [])
        (self.t.root / "evals/beta/activation.json").unlink()
        self.assertEqual(self.coverage(), ["evals/beta: activation.json is missing (6 should_load and 4 should_not_load requests)"])

    def test_a_request_used_by_two_skills_is_an_error(self):
        self.t.write("evals/beta/activation.json", json.dumps(requests("a", "b")))
        self.assertTrue(any("is also in evals/alpha/activation.json" in e for e in self.coverage()))

    def test_the_summary_check_fails_on_either_problem(self):
        self.run_all()
        root = ["--root", str(self.t.root)]
        activation_summary.main(root)
        self.assertEqual(activation_summary.main([*root, "--check"]), 0)
        (self.t.root / "evals/beta/activation.json").unlink()
        with contextlib.redirect_stderr(io.StringIO()) as err:
            self.assertEqual(activation_summary.main([*root, "--check"]), 1)
        self.assertIn("evals/beta: activation.json is missing", err.getvalue())

    def test_shape_errors(self):
        def check(data, skill="alpha", fragment=""):
            errs = validate_evals.validate_activation(data, skill, "Use for topic a. Not for b.")
            self.assertTrue(any(fragment in e for e in errs), (fragment, errs))
        good = requests("a", "b")
        check([], fragment="top level must be an object")
        check({"should_load": good["should_load"]}, fragment="keys must be exactly")
        check({**good, "should_load": good["should_load"][:5]}, fragment="must list 6")
        check({**good, "should_not_load": good["should_not_load"] + ["x"]}, fragment="must list 4")
        check({**good, "should_load": good["should_load"][:5] + [""]}, fragment="non-empty string")
        check({**good, "should_load": good["should_load"][:5] + [good["should_load"][0]]}, fragment="repeats another")
        check({**good, "should_load": good["should_load"][:5] + ["x" * 401]}, fragment="max 400")
        check({**good, "should_load": good["should_load"][:5] + ["please do alpha things"]}, fragment="names the skill")

    def test_a_should_load_request_may_not_repeat_the_description(self):
        desc = 'Use for charts - "make it clearer", "does this graph mislead". Not for tables.'
        good = requests("a", "b")
        for text in ("Make it clearer!", "hey, does this graph mislead people?"):
            data = {**good, "should_load": good["should_load"][:5] + [text]}
            errs = validate_evals.validate_activation(data, "alpha", desc)
            self.assertTrue(any("repeats the description's phrase" in e for e in errs), (text, errs))
        data = {**good, "should_load": good["should_load"][:5] + ["clearer please"]}  # a two-word quote fragment is fine
        self.assertEqual(validate_evals.validate_activation(data, "alpha", desc), [])

    def test_results_must_follow_from_their_records(self):
        self.run_all()
        path = self.t.root / "evals/alpha/activation-results.json"
        base = json.loads(path.read_text())

        def broken(edit):
            data = json.loads(json.dumps(base))
            edit(data)
            path.write_text(json.dumps(data))
            return "\n".join(self.validate()[0])

        self.assertIn("'picked' is 5 but the records give 6", broken(lambda d: d["should_load"].update(picked=5)))
        self.assertIn("'recall' does not match", broken(lambda d: d["should_load"].update(recall=0.5)))
        self.assertIn("'false_picks' is 2", broken(lambda d: d["should_not_load"].update(false_picks=2)))
        self.assertIn("is not a skill", broken(lambda d: d["should_load"]["results"][0].update(picked="zeta")))
        self.assertIn("'correct' does not match picked", broken(lambda d: d["should_load"]["results"][0].update(correct=False)))
        self.assertIn("prompt is not the request", broken(lambda d: d["should_load"]["results"][0].update(prompt="other")))
        self.assertIn("'skill' must be 'alpha'", broken(lambda d: d.update(skill="beta")))
        self.assertIn("'date' must be YYYY-MM-DD", broken(lambda d: d.update(date="today")))
        self.assertIn("'catalog_size' must be a positive integer", broken(lambda d: d.update(catalog_size=0)))
        self.assertIn("one record per request", broken(lambda d: d["should_load"].update(results=[])))
        self.assertIn("keys must be", broken(lambda d: d.pop("model")))

    def test_changed_descriptions_warn_but_do_not_fail(self):
        self.run_all()
        self.t.write("skills/alpha/SKILL.md", skill_md("alpha", "A new description for topic a."))
        errors, warnings = self.validate()
        self.assertEqual(errors, [])
        self.assertTrue(any("descriptions have changed" in w for w in warnings))

    def test_results_for_stale_requests_are_an_error(self):
        self.run_all()
        data = requests("a", "b")
        data["should_load"][2] = "topic-a a rewritten ask"
        self.t.write("evals/alpha/activation.json", json.dumps(data))
        self.assertIn("prompt is not the request", "\n".join(self.validate()[0]))

    def test_withdrawn_or_unknown_skill_folders_are_not_checked(self):
        self.t.write("evals/gone/activation.json", "not json")
        context = validate_evals.activation_context(self.t.root)
        self.assertEqual(validate_evals.validate_activation_files(self.t.root / "evals/gone", context, []), [])


class SummaryTest(Base):
    def test_summary_lists_each_skill_and_flags_low_recall_and_false_picks(self):
        data = requests("a", "b")
        data["should_load"] = ["miss-me topic-a one", "miss-me topic-a two", "miss-me topic-a three"] + data["should_load"][3:]
        data["should_not_load"][0] = "topic-a wrongly claimed"
        self.t.write("evals/alpha/activation.json", json.dumps(data))
        self.run_all()
        text = "\n".join(activation_summary.render(self.t.root))
        self.assertIn("recall 9 of 12 (75%)", text)
        self.assertIn("false-pick rate 1 of 8 (12%)", text)
        flagged = text.split("## Flagged")[1].split("## All skills")[0]
        self.assertIn("| alpha | 3 of 6 | 1 of 4 | recall 3 of 6; 1 false pick | beta 3 |", flagged)
        self.assertNotIn("| beta |", flagged)
        self.assertIn("| beta | 6 of 6 | 0 of 4 | - |", text)

    def test_no_flag_when_all_skills_do_well_and_a_skill_without_results_is_shown_as_not_run(self):
        self.run_all("--skills", "alpha")
        text = "\n".join(activation_summary.render(self.t.root))
        self.assertIn("No skill is flagged.", text)
        self.assertIn("| beta | not run | not run | - | - |", text)

    def test_check_flags_a_stale_file_and_write_fixes_it(self):
        self.run_all()
        root = ["--root", str(self.t.root)]
        self.assertEqual(activation_summary.main([*root, "--check"]), 1)
        self.assertEqual(activation_summary.main(root), 0)
        self.assertEqual(activation_summary.main([*root, "--check"]), 0)
        path = self.t.root / "evals/activation-summary.md"
        path.write_text(path.read_text() + "edited\n")
        self.assertEqual(activation_summary.main([*root, "--check"]), 1)

    def test_no_results_at_all(self):
        text = "\n".join(activation_summary.render(self.t.root))
        self.assertIn("No activation results yet.", text)

    def test_output_is_stable(self):
        self.run_all()
        self.assertEqual(activation_summary.render(self.t.root), activation_summary.render(self.t.root))


if __name__ == "__main__":
    unittest.main()
