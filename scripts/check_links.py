#!/usr/bin/env python3
"""Check relative markdown links and images in top-level *.md, docs/, evals/*.md, and every skill folder (skills/, copy-skills/, withdrawn/)."""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mdlinks import broken_links  # noqa: E402
from roots import SKILL_ROOTS  # noqa: E402


def markdown_files(root):
    root = Path(root)
    yield from sorted(p for p in root.glob("*.md") if p.is_file())
    if (root / "evals").is_dir():
        yield from sorted(p for p in (root / "evals").glob("*.md") if p.is_file())
    for sub in ("docs", *SKILL_ROOTS):
        if (root / sub).is_dir():
            yield from sorted((root / sub).rglob("*.md"))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    args = p.parse_args(argv)
    root = Path(args.root).resolve()
    errors = 0
    count = 0
    for f in markdown_files(root):
        count += 1
        for line, target in broken_links(f):
            print(f"{f.relative_to(root)}:{line}: broken link: {target}")
            errors += 1
    print(f"checked {count} markdown files, {errors} broken links")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
