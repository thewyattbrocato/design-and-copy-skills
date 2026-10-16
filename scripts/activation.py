"""Shared pieces of the activation check: the skill catalog an agent sees, reply parsing and scoring.

The check asks a model which single skill, if any, it would load for one user request, showing it only each skill's
name and description (what an agent sees before it loads anything). The helpers here are used by run_activation.py
(which asks), activation_summary.py (which reports) and validate_evals.py (which checks the files). Standard library only.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_skills  # noqa: E402
from roots import LIVE_ROOTS, skill_dirs  # noqa: E402

SHOULD_LOAD, SHOULD_NOT_LOAD = 6, 4      # requests per skill in activation.json
MAX_REQUEST_CHARS = 400
NONE = "NONE"
LOW_RECALL = 4                           # a skill picked on fewer than this many of its should_load requests is flagged


def catalog(root):
    """[(name, description)] for every live skill, sorted by name. This is the list a model is shown."""
    rows = []
    for _, d in skill_dirs(root, LIVE_ROOTS):
        md = d / "SKILL.md"
        if not md.is_file():
            continue
        fields, _ = validate_skills.parse_frontmatter(md.read_text(encoding="utf-8"))
        desc = validate_skills.unquote((fields or {}).get("description", "")).strip()
        rows.append((d.name, " ".join(desc.split())))
    return rows


def catalog_hash(rows):
    """Hash of the names and descriptions shown to the model; results record it so a later description edit shows."""
    text = json.dumps([[n, d] for n, d in rows], separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def router_prompt(rows, request):
    listing = "\n".join(f"- {name}: {desc}" for name, desc in rows)
    return (
        "You are an assistant with access to the skills below. Each skill is a folder of expert instructions that you "
        "can load before answering. All you can see about a skill before loading it is its name and description.\n\n"
        f"Skills:\n{listing}\n\n"
        f"A user sends this request:\n\n\"\"\"\n{request}\n\"\"\"\n\n"
        "Which single skill, if any, would you load before answering? Reply with only the exact skill name, "
        f"or {NONE} when no skill is a good fit."
    )


def parse_pick(reply, names):
    """The skill name in a reply, None for NONE. Raises ValueError for a reply that names no skill, or two."""
    text = (reply or "").strip()
    found = sorted({n for n in names if re.search(rf"(?<![\w-]){re.escape(n)}(?![\w-])", text)})
    says_none = bool(re.search(rf"(?<![\w-]){NONE}(?![\w-])", text, re.IGNORECASE)) and not found
    if len(found) == 1:
        return found[0]
    if says_none:
        return None
    raise ValueError(f"reply names {'several skills' if found else 'no known skill'}: {text[:120]!r}")


def load_section(skill, prompts, picks):
    results = [{"prompt": p, "picked": k, "correct": k == skill} for p, k in zip(prompts, picks)]
    n = sum(r["correct"] for r in results)
    return {"total": len(results), "picked": n, "recall": round(n / len(results), 3) if results else 0.0, "results": results}


def not_load_section(skill, prompts, picks):
    results = [{"prompt": p, "picked": k, "false_pick": k == skill} for p, k in zip(prompts, picks)]
    n = sum(r["false_pick"] for r in results)
    return {"total": len(results), "false_picks": n,
            "false_pick_rate": round(n / len(results), 3) if results else 0.0, "results": results}


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def flagged(results):
    """Why a skill is flagged in the summary: low recall and/or any false pick. [] when it is not."""
    why = []
    sl, sn = results["should_load"], results["should_not_load"]
    if sl["picked"] < LOW_RECALL:
        why.append(f"recall {sl['picked']} of {sl['total']}")
    if sn["false_picks"]:
        why.append(f"{sn['false_picks']} false {'pick' if sn['false_picks'] == 1 else 'picks'}")
    return why
