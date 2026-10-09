import os
import shlex
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from helpers import TempRoot, load_script

ci_local = load_script("ci_local")
REPO = Path(__file__).resolve().parent.parent

# The commands CI runs, written out so that editing the workflow fails this test until ci_local.py (and this list)
# have been looked at. ci_local.py reads the workflow itself; this list is what makes a change deliberate.
EXPECTED_STEPS = [
    ("Unit tests", ["python -m unittest discover -s tests"]),
    ("Eval tooling smoke", [
        "python scripts/run_eval.py --help > /dev/null",
        "python scripts/make_example.py --help > /dev/null",
        "python scripts/render.py --help > /dev/null",
        "python scripts/check_skill_fixtures.py --help > /dev/null",
        "python scripts/results_table.py --help > /dev/null",
        "python scripts/make_results_chart.py --help > /dev/null",
        "python scripts/before_after_gallery.py --help > /dev/null",
        "python scripts/ci_local.py --help > /dev/null"]),
    ("Validate skills", ["python scripts/validate_skills.py"]),
    ("Check links", ["python scripts/check_links.py"]),
    ("Validate evals", ["python scripts/validate_evals.py"]),
    ("Check skills for eval fixtures", [
        "python scripts/check_skill_fixtures.py",
        'python scripts/check_skill_fixtures.py --strict || echo "::warning::dev-suite fixtures still appear under '
        'skills/ (not blocking; held-out hits fail the step above)"']),
    ("Check README tables", ["python scripts/results_table.py --check"]),
    ("Check results chart", ["python scripts/make_results_chart.py --check"]),
    ("Check before-and-after gallery", ["python scripts/before_after_gallery.py --check"]),
]

WORKFLOW_TEXT = """name: checks
on:
  pull_request:
jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@abc # v4
      - uses: actions/setup-python@abc # v5
        with:
          python-version: "3.12"
      - name: One
        run: python -m unittest discover -s tests
      - name: Two
        run: |
          python scripts/a.py
          python scripts/b.py --flag || echo done
      - run: echo unnamed
"""


class WorkflowDriftTest(unittest.TestCase):
    def workflow(self):
        return (REPO / ".github/workflows/checks.yml").read_text(encoding="utf-8")

    def test_the_real_workflow_is_mirrored_step_for_step_in_order(self):
        self.assertEqual(ci_local.parse_workflow(self.workflow()), EXPECTED_STEPS)

    def test_no_run_line_in_the_workflow_is_skipped(self):
        text = self.workflow()
        run_keys = [ln for ln in text.splitlines() if ln.strip().startswith(("run:", "- run:"))]
        self.assertEqual(len(run_keys), len(ci_local.parse_workflow(text)))

    def test_ci_runs_what_the_documentation_tells_writers_to_run(self):
        contributing = (REPO / "CONTRIBUTING.md").read_text(encoding="utf-8")
        self.assertIn("python3 scripts/ci_local.py", contributing)

    def test_every_command_script_exists(self):
        for _, commands in ci_local.parse_workflow(self.workflow()):
            for command in commands:
                for token in command.split():
                    if token.startswith("scripts/"):
                        self.assertTrue((REPO / token).is_file(), token)

    def test_parser_reads_blocks_single_lines_and_unnamed_steps(self):
        self.assertEqual(ci_local.parse_workflow(WORKFLOW_TEXT), [
            ("One", ["python -m unittest discover -s tests"]),
            ("Two", ["python scripts/a.py", "python scripts/b.py --flag || echo done"]),
            ("echo unnamed", ["echo unnamed"])])

    def test_parser_refuses_what_it_cannot_mirror(self):
        cases = {
            "if": WORKFLOW_TEXT.replace("      - name: One\n", "      - name: One\n        if: always()\n"),
            "env": WORKFLOW_TEXT.replace("      - name: One\n", "      - name: One\n        env:\n          A: b\n"),
            "working-directory": WORKFLOW_TEXT.replace("      - name: One\n",
                                                       "      - name: One\n        working-directory: x\n"),
            "second job": WORKFLOW_TEXT + "  other:\n    runs-on: x\n    steps:\n      - run: echo hi\n",
            "folded run": WORKFLOW_TEXT.replace("run: python -m unittest discover -s tests", "run: >\n          a\n          b"),
        }
        for label, text in cases.items():
            with self.assertRaises(ci_local.WorkflowError, msg=label):
                ci_local.parse_workflow(text)


class RunStepsTest(unittest.TestCase):
    def test_commands_run_in_order_with_the_running_interpreter(self):
        ran = []
        steps = [("A", ["python x.py", "echo one"]), ("B", ["python -m unittest"])]
        out = []
        self.assertIsNone(ci_local.run_steps(steps, "/root", runner=lambda c, cwd: ran.append((c, cwd)) or 0, out=out.append))
        self.assertEqual(shlex.split(ran[0][0]), [sys.executable, "x.py"])
        self.assertEqual(ran[1][0], "echo one")
        self.assertEqual(shlex.split(ran[2][0]), [sys.executable, "-m", "unittest"])
        self.assertEqual({cwd for _, cwd in ran}, {"/root"})

    def test_stops_at_the_first_failure(self):
        ran = []

        def runner(command, cwd):
            ran.append(command)
            return 1 if "bad" in command else 0

        steps = [("A", ["echo a"]), ("B", ["echo bad", "echo skipped"]), ("C", ["echo never"])]
        self.assertEqual(ci_local.run_steps(steps, ".", runner=runner, out=lambda _: None), ("B", "echo bad"))
        self.assertEqual(ran, ["echo a", "echo bad"])

    def test_real_shell_syntax_works(self):
        with tempfile.TemporaryDirectory() as tmp:
            steps = [("shell", ['false || echo fine > out.txt', "test -s out.txt"])]
            self.assertIsNone(ci_local.run_steps(steps, tmp, out=lambda _: None))


def sh(cwd, *args):
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@t", "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull}
    subprocess.run(["git", "-c", "commit.gpgsign=false", *args], cwd=cwd, check=True, capture_output=True, env=env)


class FreshnessTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        base = Path(tmp.name)
        self.origin, self.work, self.other = base / "origin.git", base / "work", base / "other"
        sh(base, "init", "--bare", "-b", "main", str(self.origin))
        sh(base, "clone", "-q", str(self.origin), str(self.work))
        (self.work / "a.txt").write_text("a")
        sh(self.work, "add", "."), sh(self.work, "commit", "-m", "first"), sh(self.work, "push", "-q", "origin", "HEAD:main")
        sh(self.work, "checkout", "-q", "-b", "feature")

    def advance_origin(self):
        sh(self.work.parent, "clone", "-q", str(self.origin), str(self.other))
        (self.other / "b.txt").write_text("b")
        sh(self.other, "add", "."), sh(self.other, "commit", "-m", "second"), sh(self.other, "push", "-q", "origin", "HEAD:main")

    def check(self, tables=0, fetch=True):
        return ci_local.freshness(self.work, fetch=fetch, runner=lambda command, cwd: tables)

    def test_a_branch_on_top_of_origin_main_is_fresh(self):
        self.assertIsNone(self.check())
        (self.work / "c.txt").write_text("c")
        sh(self.work, "add", "."), sh(self.work, "commit", "-m", "mine")
        self.assertIsNone(self.check())

    def test_a_branch_behind_origin_main_must_be_rebased(self):
        self.advance_origin()
        problem = self.check()
        self.assertIn("not rebased on origin/main", problem)
        self.assertIn("git rebase origin/main", problem)
        sh(self.work, "rebase", "-q", "origin/main")
        self.assertIsNone(self.check())

    def test_no_fetch_compares_with_the_origin_main_already_there(self):
        self.advance_origin()
        self.assertIsNone(self.check(fetch=False))  # origin/main was not updated, so the stale comparison passes
        self.assertIn("not rebased", self.check(fetch=True))

    def test_out_of_date_readme_tables_fail_freshness(self):
        self.assertIn("README tables are out of date", self.check(tables=1))

    def test_an_out_of_date_results_chart_fails_freshness(self):
        runner = lambda command, cwd: 1 if "make_results_chart" in command else 0
        problem = ci_local.freshness(self.work, fetch=True, runner=runner)
        self.assertIn("results chart is out of date", problem)
        self.assertIn("make_results_chart.py", problem)

    def test_an_out_of_date_gallery_fails_freshness(self):
        runner = lambda command, cwd: 1 if "before_after_gallery" in command else 0
        problem = ci_local.freshness(self.work, fetch=True, runner=runner)
        self.assertIn("gallery is out of date", problem)
        self.assertIn("before_after_gallery.py", problem)

    def test_a_missing_remote_is_explained(self):
        sh(self.work, "remote", "remove", "origin")
        self.assertIn("could not fetch origin/main", self.check())
        self.assertIn("no origin/main", self.check(fetch=False))


class MainTest(unittest.TestCase):
    def setUp(self):
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        self.t.write(".github/workflows/checks.yml", WORKFLOW_TEXT)
        self.original = ci_local.freshness
        self.addCleanup(setattr, ci_local, "freshness", self.original)

    def run_main(self, runner, fresh=None):
        ci_local.freshness = lambda root, fetch=True, runner=None: fresh
        import contextlib
        import io
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = ci_local.main(["--root", str(self.t.root), "--no-fetch"], runner=runner)
        return code, out.getvalue(), err.getvalue()

    def test_prints_the_final_line_when_everything_passes(self):
        ran = []
        code, out, _ = self.run_main(lambda c, cwd: ran.append(c) or 0)
        self.assertEqual(code, 0)
        self.assertTrue(out.rstrip().endswith("all CI checks pass locally"))
        self.assertEqual(len(ran), 4)

    def test_stops_with_a_clear_message_at_the_first_failing_step(self):
        ran = []

        def runner(command, cwd):
            ran.append(command)
            return 1 if "a.py" in command else 0

        code, out, err = self.run_main(runner)
        self.assertEqual(code, 1)
        self.assertNotIn("all CI checks pass locally", out)
        self.assertIn("FAILED step 'Two'", err)
        self.assertIn("a.py", err)
        self.assertFalse(any("b.py" in c or "unnamed" in c for c in ran))

    def test_a_stale_branch_stops_before_any_step_runs(self):
        ran = []
        code, out, err = self.run_main(lambda c, cwd: ran.append(c) or 0, fresh="this branch is not rebased on origin/main")
        self.assertEqual(code, 1)
        self.assertEqual(ran, [])
        self.assertIn("FAILED freshness: this branch is not rebased", err)

    def test_an_unreadable_workflow_is_reported(self):
        (self.t.root / ".github/workflows/checks.yml").write_text("name: x\n")
        code, _, err = self.run_main(lambda c, cwd: 0)
        self.assertEqual(code, 2)
        self.assertIn("cannot read the workflow", err)


if __name__ == "__main__":
    unittest.main()
