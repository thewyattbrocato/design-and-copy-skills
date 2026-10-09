#!/usr/bin/env python3
"""Fail when distinctive strings from eval tasks appear in the skills.

An eval is only evidence if the skill under test has not been shown the answer. This script extracts
distinctive strings from every evals/*/tasks.json and evals/*/heldout/tasks.json (prompts and rubrics) and looks
for them in every file under skills/, copy-skills/ and withdrawn/. A hit means a skill text repeats a scenario, product name or number from a
task, so a win on that task may be recall rather than design judgment.

What counts as distinctive:
  - quoted strings (four or more words, or 20+ characters, that read as text and not as code),
  - names: runs of capitalized words (Kettle & Co) and single capitalized words introduced as a name ("called
    Tidewell"; a bare "for Keyhollow" is not caught); words that also appear in lowercase in the same line, and a
    small list of common products and calendar words, are skipped,
  - specific numbers: currency, thousands separators on five-digit or decimal amounts, decimal percentages, percentages
    of 10 or more that are not round, clock times, runs of three or more listed values, counts of things (13 or more, 25 rows, 420 people)
    and long pixel values that are not standard viewport widths,
  - URL-style paths such as /v1/refunds.
Short values such as 14px, 16px, 1.5, 12 columns, 2024 or 1,240 are common example numbers and are deliberately not flagged,
so the guard under-reports on a task whose only fixtures are values like those. Read the rubric, not only the guard.

Held-out hits always fail (exit 1). Dev-suite hits are printed as warnings and exit 0 unless --strict is given:
the dev tasks were seen by the skill writers, and the skills are being cleaned of them. Use --strict to see
whether the fixtures the guard can detect are gone; it cannot see a scenario that is reworded without
sharing a name or number. --list prints what was extracted so a reviewer can judge the heuristic.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from roots import SKILL_ROOTS  # noqa: E402

TEXT_SUFFIXES = {".md", ".txt", ".json", ".html", ".css", ".js", ".yml", ".yaml", ".py", ".svg"}

COMMON_COUNTS = set(range(0, 13)) | {16, 20, 24, 32, 48, 50, 64, 100}
COMMON_WIDTHS = {320, 360, 375, 390, 414, 480, 600, 640, 720, 768, 800, 900, 960, 1024, 1080, 1100, 1200, 1280,
                 1366, 1440, 1536, 1600, 1920, 2560}
COUNT_NOUNS = ("rows|row|columns|weeks|days|months|years|hours|minutes|people|users|customers|orders|items|fields|"
               "steps|tasks|tickets|products|employees|patients|members|records|points|seats|nodes|stocks|"
               "invoices|sections|pages|screens|cards|tiles|charts|lines|bars|pieces|"
               "tabs|options|answers|respondents|events|messages|emails|files|projects|accounts")
ALLOWED_NAMES = {
    "Google", "Sheets", "Excel", "Slack", "Chrome", "Safari", "Firefox", "Figma", "React", "Tailwind", "Bootstrap",
    "Apple", "Android", "Windows", "Mac", "Notion", "Stripe", "GitHub", "Material", "Helvetica", "Arial", "Georgia",
    "Times", "Courier", "Verdana", "Inter", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
    "Sunday", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
    "November", "December", "Q1", "Q2", "Q3", "Q4", "English", "French", "German", "Spanish", "Japanese", "Chinese",
    "UK", "US", "EU", "HTML", "CSS", "SVG", "JSON", "API", "URL", "SQL", "CSV", "PDF", "PNG", "WCAG", "Mobile",
    "Desktop", "Tablet", "Dark", "Light", "Bold", "Regular", "Medium",
}
# Words that begin a sentence in a prompt or rubric and say nothing about the scenario.
SENTENCE_STOP = set("""
a an the this that these those our my your their its his her we i you it they he she there here what which who
how why when where if then else also and or but so because while after before for from with without on in at to
of by as is are was were be been do does did can could should would will may might must not no yes each every
all any some one two three four five six seven eight nine ten first second third next last new old good bad
design build make show write create draw give list pick choose use keep put add set return reply answer name
critique review fix change rewrite explain describe compare check find plan sketch lay place order sort group
include includes it's don't doesn't isn't aren't note notes example examples please let try tell say need
want ask answer answers most more less many few other another such both either neither once only just even
still yet already again never always often sometimes usually people person team user users customer customers
page pages screen screens section sections form forms table tables chart charts card cards button buttons
""".split())

QUOTE_PATTERNS = (
    re.compile(r"\"([^\"\n]{4,120})\""),
    re.compile(r"[“]([^”\n]{4,120})[”]"),
    re.compile(r"(?<![\w])'([^'\n]{4,120}?)'(?![\w])"),
)
WORD = r"[A-Z][a-z]{2,}(?:[A-Z][a-z]+)*"
NAME_RUN = re.compile(rf"\b{WORD}(?:(?:\s+&\s+|\s+)(?:{WORD}|Co\b|Inc\b|Ltd\b))*")
PATH = re.compile(r"(?<![\w/])/[a-z0-9_{}.-]+(?:/[a-z0-9_{}.-]+)+")
NUMBER_PATTERNS = (
    re.compile(r"\$\s?(?:\d{3,}|\d{1,3}(?:,\d{3})+|\d+\.\d+)(?:\.\d+)?(?:,\d{3})*(?:[kKmMbB]\b)?"),
    re.compile(r"(?<![\d,.])\d{2,3}(?:,\d{3})+(?:\.\d+)?(?![\d,])|(?<![\d,.])\d(?:,\d{3})+\.\d+(?![\d,])"),
    re.compile(r"(?<![\d.])\d+\.\d+\s?%"),
    re.compile(r"(?<![\d:])\d{1,2}:\d{2}(?::\d{2})?(?![\d:])(?:\s?[ap]m\b)?", re.I),
)
PERCENT = re.compile(r"(?<![\d.])(\d+)\s?%")
COUNT = re.compile(rf"(?<![\d,.$])(\d[\d,]*)\s+(?:{COUNT_NOUNS})\b", re.I)
PIXELS = re.compile(r"(?<![\d.])(\d{3,5})\s?px\b")
SERIES = re.compile(r"(?<![\d.])\d+(?:\.\d+)?(?:\s*,\s*\d+(?:\.\d+)?){2,}")


CODE_CHARS = set("<>=(){}[];\\")
CUES = {"called", "named", "titled", "dubbed"}


def clean(s):
    return re.sub(r"\s+", " ", s).strip()


def extract(text):
    """Return a sorted list of distinctive strings found in one prompt or rubric line."""
    found = set()
    for pat in QUOTE_PATTERNS:
        for m in pat.finditer(text):
            q = clean(m.group(1)).strip(".,;:!?")
            letters = sum(c.isalpha() for c in q)
            if (len(q.split()) >= 4 or len(q) >= 20) and letters >= 0.6 * len(q) and not CODE_CHARS & set(q):
                found.add(q)
    lowered = text.lower()
    for m in NAME_RUN.finditer(text):
        words = m.group(0).split()
        while words and (words[0].lower() in SENTENCE_STOP or words[0] in ALLOWED_NAMES):
            words = words[1:]
        words = [w for w in words if w not in ALLOWED_NAMES]
        if not words:
            continue
        if len(words) == 1:
            w = words[0]
            prev = re.search(r"(\w+)\W*$", text[:m.start()])
            elsewhere = re.search(rf"\b{w.lower()}s?\b", lowered[:m.start()] + " " + lowered[m.end():])
            if len(w) < 4 or not prev or prev.group(1).lower() not in CUES or elsewhere:
                continue
        found.add(" ".join(words))
    for m in PATH.finditer(text):
        found.add(m.group(0).rstrip(".,"))
    for pat in NUMBER_PATTERNS:
        for m in pat.finditer(text):
            found.add(clean(m.group(0)))
    for m in PERCENT.finditer(text):
        if int(m.group(1)) >= 10 and int(m.group(1)) % 5:
            found.add(clean(m.group(0)))
    for m in COUNT.finditer(text):
        n = int(m.group(1).replace(",", ""))
        if n not in COMMON_COUNTS:
            found.add(clean(m.group(0)))
    for m in PIXELS.finditer(text):
        if int(m.group(1)) not in COMMON_WIDTHS:
            found.add(clean(m.group(0)))
    for m in SERIES.finditer(text):
        nums = re.findall(r"\d+(?:\.\d+)?", m.group(0))
        for i in range(len(nums) - 2):
            if len(set(nums[i:i + 3])) > 1:
                found.add(", ".join(nums[i:i + 3]))
    return sorted(found)


def task_files(root):
    evals = Path(root) / "evals"
    if not evals.is_dir():
        return []
    out = []
    for skill in sorted(p for p in evals.iterdir() if p.is_dir()):
        for suite, path in (("dev", skill / "tasks.json"), ("heldout", skill / "heldout" / "tasks.json")):
            if path.is_file():
                out.append((suite, path))
    return out


def fixtures(root):
    """Map fixture string -> list of (suite, relative task file, task id, where)."""
    table = {}
    for suite, path in task_files(root):
        rel = path.relative_to(root).as_posix()
        try:
            tasks = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if not isinstance(tasks, list):
            continue
        for t in tasks:
            if not isinstance(t, dict):
                continue
            parts = [("prompt", t.get("prompt"))] + [("rubric", r) for r in (t.get("rubric") or [])]
            for where, text in parts:
                if isinstance(text, str):
                    for s in extract(text):
                        table.setdefault(s, []).append((suite, rel, t.get("id", "?"), where))
    return table


def skill_lines(root):
    for sub in SKILL_ROOTS:
        skills = Path(root) / sub
        if not skills.is_dir():
            continue
        # evidence-only folders in withdrawn/ (no SKILL.md) are archived answers, not skill text
        skip = [d for d in skills.iterdir() if sub == "withdrawn" and d.is_dir() and not (d / "SKILL.md").is_file()]
        for path in sorted(p for p in skills.rglob("*") if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES
                           and not any(d in p.parents for d in skip)):
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            for n, line in enumerate(text.splitlines(), 1):
                yield path.relative_to(root).as_posix(), n, line


def pattern_for(fixture):
    body = r"\s+".join(re.escape(tok) for tok in fixture.split())
    return re.compile(rf"(?<![\w$]){body}(?![\w])", re.I if re.search(r"[\"'“ ]", fixture) and fixture == fixture.lower() else 0)


def find_hits(root, table=None):
    """Return a list of (file, line, fixture, origins) for every fixture found in the skill folders."""
    table = fixtures(root) if table is None else table
    compiled = {f: pattern_for(f) for f in table}
    hits = []
    for rel, n, line in skill_lines(root):
        for f, pat in compiled.items():
            if pat.search(line):
                hits.append((rel, n, f, table[f]))
    return hits


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    p.add_argument("--strict", action="store_true", help="dev-suite hits fail too (default: warn)")
    p.add_argument("--list", action="store_true", help="print the extracted fixtures and exit")
    args = p.parse_args(argv)
    root = Path(args.root)
    table = fixtures(root)
    if args.list:
        for f in sorted(table):
            o = table[f][0]
            print(f"{f!r}\t{o[0]}\t{o[2]}\t{o[3]}")
        print(f"{len(table)} fixtures from {len(task_files(root))} task files")
        return 0
    hits = find_hits(root, table)
    failing = warned = 0
    for rel, n, f, origins in hits:
        suites = {o[0] for o in origins}
        fatal = "heldout" in suites or args.strict
        o = next((o for o in origins if o[0] == "heldout"), origins[0])
        print(f"{'error' if fatal else 'warning'}: {rel}:{n}: '{f}' is a fixture from {o[1]} task {o[2]} ({o[3]}; {o[0]} suite)")
        failing += fatal
        warned += not fatal
    print(f"checked {len(table)} fixtures from {len(task_files(root))} task files against the skill folders: "
          f"{failing} errors, {warned} warnings")
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())
