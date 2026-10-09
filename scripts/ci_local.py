#!/usr/bin/env python3
"""Run the CI checks locally, in the order CI runs them, and stop at the first failure.

The steps are read from .github/workflows/checks.yml (every step with a `run:`), so this script cannot drift from
the workflow without a test failing. Before them it checks that the branch is rebased on origin/main and that the
README tables, results chart and before-and-after gallery are current. Run it before every push; a pull request that fails CI on a check this script runs was
pushed without it. Standard library only.
"""
import argparse
import shlex
import subprocess
import sys
from pathlib import Path

WORKFLOW = Path(".github") / "workflows" / "checks.yml"
STEP_KEYS = {"name", "uses", "with", "run"}
DONE = "all CI checks pass locally"


class WorkflowError(RuntimeError):
    pass


def indent_of(line):
    return len(line) - len(line.lstrip(" "))


def parse_workflow(text):
    """[(step name, [command lines])] for every step of the single job that has a `run:`.

    A small reader for the workflow's shape rather than a YAML parser (standard library only). It fails on
    anything it would have to guess at, so a workflow change this script cannot mirror is an error, not a
    silently skipped step."""
    lines = [ln.rstrip() for ln in text.splitlines()]
    jobs = [i for i, ln in enumerate(lines) if ln == "jobs:"]
    if len(jobs) != 1:
        raise WorkflowError("expected one top-level `jobs:` block")
    job_names = [ln for ln in lines[jobs[0] + 1:] if ln.strip() and indent_of(ln) == 2 and ln.strip().endswith(":")]
    if len(job_names) != 1:
        raise WorkflowError(f"expected exactly one job, found {len(job_names)}; teach ci_local.py about the new ones")
    start = next((i for i, ln in enumerate(lines) if ln.strip() == "steps:"), None)
    if start is None:
        raise WorkflowError("no `steps:` block")
    steps, current, i = [], None, start + 1
    base = None
    while i < len(lines):
        ln = lines[i]
        if not ln.strip() or ln.strip().startswith("#"):
            i += 1
            continue
        if base is None:
            base = indent_of(ln)
        if indent_of(ln) < base:
            break
        body = ln.strip()
        if indent_of(ln) == base and body.startswith("- "):
            current = {}
            steps.append(current)
            body = body[2:].strip()
            key_indent = base + 2
        else:
            key_indent = indent_of(ln)
        if current is None or key_indent != base + 2:
            i += 1  # nested content of `with:`; checked below by its parent key
            continue
        key, _, value = body.partition(":")
        if key not in STEP_KEYS:
            raise WorkflowError(f"unsupported step key `{key}` in {WORKFLOW}; teach ci_local.py how to mirror it")
        value = value.strip()
        if key == "run" and value in ("|", "|-", "|+"):
            block = []
            i += 1
            while i < len(lines) and (not lines[i].strip() or indent_of(lines[i]) > key_indent):
                if lines[i].strip():
                    block.append(lines[i].strip())
                i += 1
            current["run"] = block
            continue
        if key == "run" and value in (">", ">-", ">+"):
            raise WorkflowError("`run: >` folded blocks are not supported; use a single line or `run: |`")
        if key == "run":
            current["run"] = [value]
        else:
            current[key] = value
        i += 1
    return [(s.get("name") or s["run"][0], s["run"]) for s in steps if "run" in s]


def shell_command(command):
    """The workflow's `python` is the interpreter set up by CI; locally use the one running this script."""
    if command == "python" or command.startswith("python "):
        return shlex.quote(sys.executable) + command[len("python"):]
    return command


def run_shell(command, cwd):
    return subprocess.run(command, shell=True, cwd=cwd).returncode


def git(root, *args):
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)


def freshness(root, fetch=True, runner=run_shell):
    """None when the branch contains origin/main and the README tables and results chart are current, else what to do about it."""
    if fetch:
        got = git(root, "fetch", "--quiet", "origin", "main")
        if got.returncode != 0:
            return (f"could not fetch origin/main ({got.stderr.strip() or 'git fetch failed'}). Check the network and "
                    "the `origin` remote, or pass --no-fetch to compare against the origin/main you already have")
    if git(root, "rev-parse", "--verify", "--quiet", "origin/main").returncode != 0:
        return "there is no origin/main to compare with; fetch it with `git fetch origin main`"
    if git(root, "merge-base", "--is-ancestor", "origin/main", "HEAD").returncode != 0:
        return "this branch is not rebased on origin/main; run `git fetch origin main && git rebase origin/main`, then rerun"
    if runner(shell_command("python scripts/results_table.py --check"), root) != 0:
        return "the README tables are out of date; run `python3 scripts/results_table.py` and commit the result"
    if runner(shell_command("python scripts/make_results_chart.py --check"), root) != 0:
        return "the results chart is out of date; run `python3 scripts/make_results_chart.py` and commit the result"
    if runner(shell_command("python scripts/before_after_gallery.py --check"), root) != 0:
        return "the before-and-after gallery is out of date; run `python3 scripts/before_after_gallery.py` and commit the result"
    return None


def run_steps(steps, root, runner=run_shell, out=print):
    """Run each command of each step in order. Returns None, or (step name, command) of the first failure."""
    for name, commands in steps:
        out(f"\n== {name}")
        for command in commands:
            out(f"$ {command}")
            if runner(shell_command(command), root) != 0:
                return name, command
    return None


def main(argv=None, runner=run_shell):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    p.add_argument("--no-fetch", action="store_true", help="skip `git fetch origin main` and use the origin/main you have")
    args = p.parse_args(argv)
    root = Path(args.root)
    try:
        steps = parse_workflow((root / WORKFLOW).read_text(encoding="utf-8"))
    except (OSError, WorkflowError) as e:
        print(f"ci_local: cannot read the workflow: {e}", file=sys.stderr)
        return 2
    print("== freshness: rebased on origin/main, README tables, results chart and gallery current")
    problem = freshness(root, fetch=not args.no_fetch, runner=runner)
    if problem:
        print(f"\nFAILED freshness: {problem}", file=sys.stderr)
        return 1
    failed = run_steps(steps, root, runner)
    if failed:
        name, command = failed
        print(f"\nFAILED step '{name}': {command}\nFix it and rerun `python3 scripts/ci_local.py`; CI runs the same "
              "commands and will fail the same way.", file=sys.stderr)
        return 1
    print(f"\n{DONE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
