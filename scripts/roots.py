"""The folders that hold skills, shared by every script so they cannot drift apart.

withdrawn/ may also hold evidence-only folders (no SKILL.md, e.g. withdrawn/<name>-v1-evidence/) from an earlier
attempt; they are archived as-is, never validated as skills and never counted as a skill's results."""
from pathlib import Path

SKILL_ROOTS = ("skills", "copy-skills", "withdrawn")
# Folders whose skills are listed and installable; withdrawn/ is kept only as evidence.
LIVE_ROOTS = ("skills", "copy-skills")


def skill_dirs(root, folders=SKILL_ROOTS):
    """[(folder, dir)] for every skill directory under the given folders. An absent folder holds none."""
    found = []
    for sub in folders:
        base = Path(root) / sub
        if base.is_dir():
            found += [(sub, d) for d in sorted(base.iterdir())
                      if d.is_dir() and (sub != "withdrawn" or (d / "SKILL.md").is_file())]
    return found


def find_skill(root, name):
    """(folder, dir) of the live skill called `name`, or None when no live folder holds it."""
    for sub in LIVE_ROOTS:
        d = Path(root) / sub / name
        if (d / "SKILL.md").is_file():
            return sub, d
    return None
