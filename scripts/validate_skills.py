#!/usr/bin/env python3
"""Validate <root>/<name>/SKILL.md structure for every skill folder (skills/, copy-skills/, withdrawn/)."""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mdlinks import broken_links, relative_links, resolve  # noqa: E402
from roots import SKILL_ROOTS, skill_dirs  # noqa: E402

KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_NAME, MAX_DESCRIPTION, MAX_BODY_LINES = 64, 1024, 500
KEY = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*)$")
HEADING = re.compile(r"^#{1,6}\s+(.*)$")


def parse_frontmatter(text):
    """Return (fields, body_lines) or (None, error). Supports plain and folded/literal scalars."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing YAML frontmatter (file must start with '---')"
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None, "frontmatter is not closed with '---'"
    fields, key = {}, None
    for raw in lines[1:end]:
        m = KEY.match(raw)
        if m and not raw.startswith((" ", "\t")):
            key, value = m.group(1), m.group(2).strip()
            if value in (">", ">-", ">+", "|", "|-", "|+"):
                value = ""
            fields[key] = value
        elif key and raw.strip():
            fields[key] = (fields[key] + " " + raw.strip()).strip()
    return fields, lines[end + 1:]


def unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def validate_skill(skill_dir):
    errors = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return ["SKILL.md is missing"]
    fields, rest = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    if fields is None:
        return [rest]

    name = unquote(fields.get("name", ""))
    if not name:
        errors.append("frontmatter 'name' is missing or empty")
    else:
        if not KEBAB.match(name):
            errors.append(f"name '{name}' is not kebab-case")
        if len(name) > MAX_NAME:
            errors.append(f"name is {len(name)} chars (max {MAX_NAME})")
        if name != skill_dir.name:
            errors.append(f"name '{name}' does not match directory '{skill_dir.name}'")

    description = unquote(fields.get("description", ""))
    if not description:
        errors.append("frontmatter 'description' is missing or empty")
    elif len(description) > MAX_DESCRIPTION:
        errors.append(f"description is {len(description)} chars (max {MAX_DESCRIPTION})")

    if len(rest) > MAX_BODY_LINES:
        errors.append(f"body is {len(rest)} lines (max {MAX_BODY_LINES})")
    if not any((m := HEADING.match(l)) and "when not to use" in m.group(1).lower() for l in rest):
        errors.append("no heading containing 'When not to use'")

    for line, target in broken_links(skill_md):
        errors.append(f"SKILL.md:{line}: broken link: {target}")
    refs = skill_dir / "references"
    linked = set()
    for _, target in relative_links(skill_md.read_text(encoding="utf-8")):
        linked.add(resolve(skill_md, target))
    if refs.is_dir():
        for ref in sorted(p for p in refs.rglob("*") if p.is_file()):
            rel = ref.relative_to(skill_dir)
            if ref.resolve() not in linked:
                errors.append(f"{rel} is not linked from SKILL.md")
            if ref.suffix == ".md":
                for line, target in broken_links(ref):
                    errors.append(f"{rel}:{line}: broken link: {target}")
    return errors


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    args = p.parse_args(argv)
    failed = 0
    counts = {sub: 0 for sub in SKILL_ROOTS}
    owners = {}
    for sub, d in skill_dirs(args.root):
        counts[sub] += 1
        for err in validate_skill(d):
            print(f"{sub}/{d.name}: {err}")
            failed += 1
        # validate_skill checks name == directory; here the same name must not appear in two folders.
        if d.name in owners:
            print(f"{sub}/{d.name}: skill name '{d.name}' is already used by {owners[d.name]}/{d.name}")
            failed += 1
        else:
            owners[d.name] = sub
    copy = f" and {counts['copy-skills']} copy" if counts["copy-skills"] else ""
    extra = f" and {counts['withdrawn']} withdrawn" if counts["withdrawn"] else ""
    print(f"validated {counts['skills']} skills{copy}{extra}, {failed} problems")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
