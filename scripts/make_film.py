#!/usr/bin/env python3
"""Build the short silent film in docs/launch/ from the repo's own saved test runs.

  python3 scripts/make_film.py            # rebuild the MP4, the poster, the still version and the transcript
  python3 scripts/make_film.py --check    # exit 1 if the transcript, film, poster or still is out of date

The film shows eight moves of the library: a request arriving, a skill loading, then a form, a chart, a table, a
deck, a pricing page and an accessibility pass. Everything on screen is real saved material: screenshots and answers
from evals/*/heldout/runs/, request text word for word from the task and activation files, and counts read from the
results files through scripts/results_table.py (the same code that writes the README tables). The only drawn parts are
the title, the skill-list picture in move 2 (labelled illustrative in its caption) and the layout around the evidence.
No audio and no generated imagery: frames are HTML pages captured with headless Chrome (scripts/render.py), joined
with ffmpeg.

Needs Chrome (set CHROME_BIN if it is not at the default path), ffmpeg and, optionally, pngquant for smaller stills.
Outputs, in docs/launch/: skills-at-work.mp4, skills-at-work-poster.png, skills-at-work-still.png and
skills-at-work.md (the transcript, written without Chrome or ffmpeg).

The MP4, the poster and the still each carry a `source-sha256` digest of everything they are drawn from: every frame
page and how long it is held, the two still pages, and the bytes of each saved screenshot those pages load (paths taken
relative to the repo, so the digest is the same in any checkout). It is written into the MP4's comment metadata and
into a text chunk of each PNG (scripts/pngstamp.py). --check recomputes it without Chrome or ffmpeg and fails when the
transcript differs or any of the three files carries another digest, so a film left behind after new results, new
picks or a layout change fails CI. Standard library only.
"""
import argparse
import concurrent.futures
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pngstamp  # noqa: E402
import render  # noqa: E402
import results_table as rt  # noqa: E402

NAME = "skills-at-work"
OUT = Path("docs") / "launch"
W, H, FPS = 1280, 720, 30
MEDIA_W, MEDIA_H = 820, 548
HEAD_H = 36  # the label strip above a saved screenshot or a column
# The latest round of skill updates: how many were tried and shelved for missing the held-out bar. This is a
# maintainer-supplied figure that cannot be derived from this repository, and nothing checks it. When it changes, update
# it by hand here and also in the film's transcript, the still image, the README paragraph on the film and the
# docs/img/ALT.md row for the still.
SHELVED_LATEST_ROUND = 12
MOVE_SECONDS = 10.0

# One entry per move. `crop` is (x, y, width) in the 1280x800 saved screenshot, shown scaled to the media box.
MOVES = [
    {"id": "form", "label": "A form", "skill": "form-design", "task": "fd-h08", "kind": "twoup-answers",
     "why": "its biggest gap in this skill's set",
     "caption_a": "Move 3, a form: “make it more professional”",
     "caption_b": "Without the skill: a new card, colors and shadow",
     "caption_c": "With the skill: the answer says “already in good shape”, five small fixes",
     "left": "Without the skill", "right": "With the skill"},
    {"id": "chart", "label": "A chart", "skill": "chart-design", "task": "cd3-h08-donations-toward-goal",
     "kind": "wipe", "crop": (140, 15, 1000),
     "why": "its biggest gap among the tasks that produced a page",
     "caption_a": "Move 4, a chart: donations against a goal",
     "caption_b": "Without the skill: a stacked area chart",
     "caption_c": "With the skill: one bar to the goal, a pace marker, a table"},
    {"id": "table", "label": "A table", "skill": "data-tables", "task": "dt2-01-invoice-list", "kind": "wipe",
     "crop": (140, 20, 990), "why": "its biggest gap among the tasks that produced a page",
     "caption_a": "Move 5, a table: unpaid invoices",
     "caption_b": "Without the skill: a stack of cards",
     "caption_c": "With the skill: a table, a balance column, a total row"},
    {"id": "deck", "label": "A presentation", "skill": "presentation-design", "task": "pd2-05-search-vendor-proposal",
     "kind": "twoup-titles", "why": "a request for slide titles, so the titles can be shown",
     "caption_a": "Move 6, a deck: slide titles for a 15-minute pitch",
     "caption_b": "Without the skill: topic labels as titles",
     "caption_c": "With the skill: each title states its point",
     "left": "Without the skill: slide titles", "right": "With the skill: slide titles"},
    {"id": "pricing", "label": "A pricing page", "skill": "visual-hierarchy", "task": "vh-h02-podcast-pricing",
     "kind": "wipe", "crop": (60, 50, 1160), "why": "it is the pricing-page task in this skill's set",
     "caption_a": "Move 7, a pricing page: three plans",
     "caption_b": "Without the skill: a dark page, a glowing middle card",
     "caption_c": "With the skill: key numbers in bold, the middle plan boxed"},
    {"id": "access", "label": "An accessibility pass", "skill": "ui-polish-pass", "task": "polish2-polish-bakery-orders",
     "kind": "twoup-code", "request_limit": 242,
     "why": "a polish task where the accessibility fixes can be read in both saved answers",
     "caption_a": "Move 8: “Can you finish it?” and its accessibility checks",
     "caption_b": "Without the skill: buttons named just “Edit” and “Delete”",
     "caption_c": "With the skill: each button names its order; focus moves",
     "left": "Without the skill: a row's buttons", "right": "With the skill: the same buttons",
     "extra": "Both saved answers also added labels to the search box and filter, a visible keyboard focus ring and a status "
              "message, so the difference is in the row buttons and where focus goes after a delete. The answer with the skill "
              "says it did not try the page with a screen reader."},
]


# ---------------------------------------------------------------------------------------------------------- data

def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def tally_text(wins, losses, ties):
    def n(k, one, many):
        return f"{k} {one if k == 1 else many}"
    return f"{n(wins, 'win', 'wins')}, {n(losses, 'loss', 'losses')}, {n(ties, 'tie', 'ties')}"


def record(root):
    """The library's headline record, summed by the same code that writes the README line."""
    wins = losses = ties = marginal = skills = 0
    for _, results in rt.heldout_results(root):
        outcome = rt.loaded_outcome(results)
        if outcome is None:
            continue
        t = outcome[0]
        skills += 1
        wins, losses, ties = wins + t["with_wins"], losses + t["without_wins"], ties + t["ties"]
        marginal += bool(rt.marginal_reasons(results))
    return {"skills": skills, "wins": wins, "losses": losses, "ties": ties, "tasks": wins + losses + ties,
            "marginal": marginal, "listed": len(rt.live_rows(root))}


def skill_names(root):
    return [name for name, _, _ in rt.live_rows(root)]


def first_clause(root, skill):
    """The skill's own description up to its first ` - ` (the part before the example phrases)."""
    text = (rt.find_skill(root, skill)[1] / "SKILL.md").read_text(encoding="utf-8")
    desc = re.search(r"^description:\s*(.+)$", text, re.M).group(1).strip()
    return desc.split(" - ")[0].strip().rstrip(".")


def shorten(text, limit):
    """The start of a saved request, cut at a word and marked with [...] when it is shortened."""
    text = " ".join(text.split("```")[0].split())
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].rstrip(",;:")
    return cut + " […]"


def first_code_block(markdown):
    m = re.search(r"```html\n(.*?)```", markdown, re.S)
    return m.group(1) if m else ""


def slide_titles(markdown):
    """Numbered slide titles from a saved answer, whichever of the two bold patterns the answer used."""
    titles = []
    for line in markdown.splitlines():
        m = re.match(r"^\s*(\d+)\.\s+\*\*(.+?)\*\*", line) or re.match(r"^\*\*(\d+)\.\s+(.+?)\*\*\s*$", line)
        if m:
            titles.append((int(m.group(1)), m.group(2).strip()))
    return titles


def row_buttons(markdown):
    """The first table cell of row buttons in a saved answer's page."""
    m = re.search(r'<td class="actions">.*?</td>', markdown, re.S)
    return m.group(0) if m else ""


def focus_excerpt(markdown):
    """The saved answer's lines that name each row button and move focus, and its two bullets about them."""
    lines = [x.strip() for x in markdown.splitlines()]
    code = [x for x in lines if "'Edit '+l" in x or "'Delete '+l" in x or x.startswith("(next?")]
    bullets = [x[2:] for x in lines if x.startswith(("- Each button names its order", "- After deleting"))]
    return code, bullets


def move_data(root, move):
    root = Path(root)
    skill, task = move["skill"], move["task"]
    folder = root / "evals" / skill / "heldout"
    run = folder / "runs" / task
    results = load_json(folder / "results.json")
    summary = results["summary"]
    t = rt.loaded_outcome(results)[0]
    verdict = next(v for v in results["verdicts"] if v["task_id"] == task)
    prompt = next(x for x in load_json(folder / "tasks.json") if x["id"] == task)["prompt"]
    winners = [s["winner"] for s in verdict["samples"]]
    return {
        **move, "run": run, "prompt": prompt, "request": shorten(prompt, move.get("request_limit", 175)),
        "tally": tally_text(t["with_wins"], t["without_wins"], t["ties"]),
        "tasks": t["tasks_with_loaded_sample"], "marginal": bool(rt.marginal_reasons(results)),
        "scores": verdict["rubric_scores"], "winners": winners, "judge": summary.get("judge"),
    }


def sample_text(winners):
    n = len(winners)
    parts = [f"the answer with the skill won {winners.count('with')} of {n} samples"]
    if winners.count("without"):
        parts.append(f"without won {winners.count('without')}")
    if winners.count("tie"):
        parts.append(f"{winners.count('tie')} tied")
    return ", ".join(parts)


def gather(root):
    root = Path(root)
    rec = record(root)
    moves = [move_data(root, m) for m in MOVES]
    return {"root": root, "record": rec, "names": skill_names(root), "moves": moves}


# ---------------------------------------------------------------------------------------------------- timeline

def captions_for_move(m):
    d = m
    last = f"{m['skill']}: {m['tally']}." if not m["marginal"] else f"{m['skill']}: {m['tally']}. A marginal pass."
    return [(0.0, d["caption_a"]), (2.6, d["caption_b"]), (5.0, d["caption_c"]), (8.0, last)]


def build_scenes(data):
    rec, names = data["record"], data["names"]
    pick = data["moves"][4]["skill"]  # the request and load scenes use the same skill as the pricing page
    request = load_json(Path(data["root"]) / "evals" / pick / "activation.json")["should_load"][rt.TRY_IT[0][1]]
    scenes = [
        {"id": "title", "dur": 3.0, "captions": [(0.0, f"{rec['listed']} skills for AI coding agents, shown at work in eight moves")]},
        {"id": "request", "dur": 5.0, "request": request,
         "captions": [(0.0, "Move 1: a request arrives"), (2.6, "Word for word from the repo's activation check")]},
        {"id": "load", "dur": 6.0, "pick": pick, "names": names, "clause": first_clause(data["root"], pick),
         "refs": sorted(p.name for p in (rt.find_skill(data["root"], pick)[1] / "references").glob("*.md")),
         "captions": [(0.0, "Move 2: the agent matches it to a skill"), (2.4, "Then it loads that skill's short instructions"),
                      (4.4, "Illustrative drawing. Names and text are the repo's own")]},
    ]
    for m in data["moves"]:
        scenes.append({"id": m["id"], "dur": MOVE_SECONDS, "move": m, "captions": captions_for_move(m)})
    shelved = f"Latest round: {SHELVED_LATEST_ROUND} updates tried and shelved, not merged"
    scenes.append({"id": "record", "dur": 11.0, "rec": rec, "captions": [
        (0.0, f"{rec['skills']} skills, {rec['tasks']} held-out tasks where the skill loaded"),
        (3.6, f"{rec['marginal']} of the {rec['skills']} passes are marginal"),
        (6.4, shelved), (8.8, "Two merged updates show weaker evidence")]})
    scenes.append({"id": "end", "dur": 3.0, "captions": [(0.0, "Saved output from the repo's test runs. Source: scripts/make_film.py")]})
    return scenes


def caption_at(scene, t):
    text = scene["captions"][0][1]
    for start, cap in scene["captions"]:
        if t >= start:
            text = cap
    return text


def total_seconds(scenes):
    return sum(s["dur"] for s in scenes)


def stamp(seconds):
    return f"{int(seconds // 60)}:{int(seconds % 60):02d}"


def rle(frames):
    """[(key, count)] for consecutive equal keys, so a held still becomes one frame with a duration."""
    out = []
    for k in frames:
        if out and out[-1][0] == k:
            out[-1][1] += 1
        else:
            out.append([k, 1])
    return [(k, n) for k, n in out]


# --------------------------------------------------------------------------------------------------------- html

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1280px;height:720px;background:#0d0f13;overflow:hidden;color:#f4f5f7;
 font-family:system-ui,-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}
.stage{position:absolute;inset:0}
.top{position:absolute;left:24px;right:24px;top:12px;height:52px;display:flex;align-items:center;gap:16px}
.move{color:#f5a524;font-weight:800;letter-spacing:.06em;text-transform:uppercase;font-size:20px}
.chip{border:2px solid #f5a524;color:#f5a524;padding:3px 12px;border-radius:999px;font-weight:700;font-size:20px;
 font-family:ui-monospace,Menlo,Consolas,monospace}
.chip.on{background:#f5a524;color:#0d0f13}
.media{position:absolute;left:24px;top:76px;width:820px;height:548px;background:#1a1d24;overflow:hidden;
 border-radius:10px;border:1px solid #3a4150}
.panel{position:absolute;left:868px;top:76px;width:388px;height:548px;background:#161920;border:1px solid #3a4150;
 border-radius:10px;padding:18px 20px;font-size:20px;line-height:1.35;overflow:hidden}
.lab{color:#b8bdc7;font-size:15px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin:0 0 6px}
.req{color:#f4f5f7;font-size:20px;line-height:1.38;margin-bottom:16px}
.caret{display:inline-block;width:3px;height:1.05em;background:#f5a524;vertical-align:-.15em;margin-left:2px}
.big{font-size:28px;font-weight:800;line-height:1.2}
.muted{color:#b8bdc7}
.cap{position:absolute;left:0;right:0;bottom:0;height:84px;background:#000;display:flex;align-items:center;
 padding:0 28px;font-size:30px;line-height:1.2;font-weight:600;color:#fff}
.tag{position:absolute;left:12px;top:12px;background:#000;color:#fff;font-weight:700;font-size:18px;
 padding:5px 12px;border-radius:6px;border:1px solid #6b7384;z-index:5}
.shot{position:absolute;transform-origin:0 0}
.div{position:absolute;top:0;bottom:0;width:4px;background:#f5a524;z-index:4}
.col{position:absolute;top:0;width:400px;height:548px}
.col .hd{height:36px;background:#000;color:#fff;font-weight:700;font-size:18px;padding:7px 12px;border-bottom:1px solid #6b7384}
.col .bd{position:absolute;top:36px;left:0;right:0;bottom:0;background:#fff;overflow:hidden}
.col iframe{border:0;width:500px;height:640px;background:#fff;display:block;transform:scale(.8);transform-origin:0 0}
.titles{padding:14px 16px;color:#16181d;font-size:18px;line-height:1.3;background:#fff;height:100%}
.titles li{margin:0 0 9px 26px}
.titles .note{color:#4b5260;font-size:15px;margin-top:10px}
.excerpt{padding:14px 16px;color:#16181d;font-size:18px;line-height:1.35;background:#fff;height:100%}
.excerpt h4{font-size:15px;letter-spacing:.06em;text-transform:uppercase;color:#4b5260;margin:0 0 8px}
.excerpt li{margin:0 0 7px 22px}
.code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;line-height:1.4;white-space:pre-wrap;
 overflow-wrap:anywhere;background:#f1f2f5;border:1px solid #d5d8de;border-radius:6px;padding:8px 10px}
.chips{display:flex;flex-wrap:wrap;gap:7px;padding:14px}
.sk{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:14.5px;border:1px solid #4a5160;color:#c9ced8;
 padding:3px 8px;border-radius:5px}
.sk.pick{background:#f5a524;color:#0d0f13;border-color:#f5a524;font-weight:800}
.bar{display:flex;height:64px;border:2px solid #f4f5f7;margin:10px 0 8px}
.bar div{display:flex;align-items:center;justify-content:center;font-weight:800;font-size:24px;color:#0d0f13}
.win{background:#f5a524}
.loss{background:repeating-linear-gradient(45deg,#f4f5f7 0 6px,#8c93a1 6px 12px)}
.tie{background:#8c93a1;color:#0d0f13}
"""


def page(body, extra_css=""):
    return f"<!doctype html><html lang='en'><meta charset='utf-8'><style>{CSS}{extra_css}</style><body>{body}</body></html>"


def esc(text):
    return html.escape(text, quote=True)


def stage(top, media, panel, caption, fade=1.0):
    return page(f"<div class='stage' style='opacity:{fade:.2f}'><div class='top'>{top}</div>{media}{panel}"
                f"<div class='cap'>{esc(caption)}</div></div>")


def shot_html(path, crop, cls="", style=""):
    x, y, w = crop
    s = MEDIA_W / w
    return (f"<img class='shot {cls}' src='{Path(path).resolve().as_uri()}' alt='' "
            f"style='width:{1280 * s:.2f}px;left:{-x * s:.2f}px;top:{-y * s:.2f}px;{style}'>")


def wipe_media(m, p):
    """The saved screenshots under a header strip that names the side, so the label never sits on the picture."""
    crop = m["crop"]
    run = Path(m["run"])
    right = round((1 - p) * 100, 2)
    label = "With the skill" if p >= 0.5 else "Without the skill"
    return ("<div class='media'>" + f"<div class='hd' style='position:absolute;left:0;right:0;top:0;height:{HEAD_H}px;background:#000;color:#fff;"
            f"font-weight:700;font-size:18px;padding:7px 12px;border-bottom:1px solid #6b7384;z-index:6'>{label}</div>"
            f"<div style='position:absolute;left:0;right:0;top:{HEAD_H}px;bottom:0;overflow:hidden;background:#fff'>" +
            shot_html(run / "without.png", crop) +
            f"<div style='position:absolute;inset:0;clip-path:inset(0 {right}% 0 0)'>{shot_html(run / 'with.png', crop)}</div>" +
            (f"<div class='div' style='left:{p * MEDIA_W - 2:.1f}px'></div>" if 0 < p < 1 else "") +
            "</div></div>")


def iframe(doc):
    if "<html" not in doc:
        doc = f"<!doctype html><meta charset='utf-8'><body style='margin:16px'>{doc}</body>"
    # Render in the light scheme so a rebuild looks the same on a machine set to dark mode.
    doc = doc.replace("prefers-color-scheme:dark", "prefers-color-scheme:none").replace("prefers-color-scheme: dark", "prefers-color-scheme: none")
    return f"<iframe srcdoc=\"{esc(doc)}\" scrolling='no'></iframe>"


def titles_html(titles, note):
    items = "".join(f"<li>{esc(t)}</li>" for _, t in titles)
    return f"<div class='titles'><ol style='list-style:decimal'>{items}</ol><p class='note'>{esc(note)}</p></div>"


def twoup_media(m, p, show_left=True):
    run, kind = Path(m["run"]), m["kind"]
    if kind == "twoup-answers":
        left = iframe(first_code_block((run / "without.md").read_text(encoding="utf-8")))
        right = iframe(first_code_block((run / "with.md").read_text(encoding="utf-8")))
    elif kind == "twoup-titles":
        wo = slide_titles((run / "without.md").read_text(encoding="utf-8"))
        wi = slide_titles((run / "with.md").read_text(encoding="utf-8"))
        left = titles_html(wo[:7], "Titles copied from the saved answer.")
        right = titles_html(wi[:6], "Titles copied from the saved answer.")
    else:  # twoup-code: the row buttons as the answer without the skill wrote them, and the answer with it
        wo = row_buttons((run / "without.md").read_text(encoding="utf-8"))
        code, bullets = focus_excerpt((run / "with.md").read_text(encoding="utf-8"))
        left = (f"<div class='excerpt'><h4>Markup in the saved answer</h4><pre class='code'>{esc(wo)}</pre>"
                "<p style='margin-top:14px'>Every row reads the same: “Edit”, “Delete”.</p></div>")
        items = "".join(f"<li>{esc(x)}</li>" for x in bullets)
        right = (f"<div class='excerpt'><h4>Code in the saved answer</h4><pre class='code'>{esc(chr(10).join(code))}</pre>"
                 f"<h4 style='margin-top:12px'>Its change list</h4><ul style='list-style:disc;font-size:16px'>{items}</ul></div>")
    body_left = f"<div class='col' style='left:0'><div class='hd'>{esc(m['left'])}</div><div class='bd'>{left}</div></div>"
    right_clip = round((1 - p) * 100, 2)
    body_right = (f"<div class='col' style='left:420px;clip-path:inset(0 {right_clip}% 0 0)'>"
                  f"<div class='hd'>{esc(m['right'])}</div><div class='bd'>{right}</div></div>")
    return f"<div class='media' style='background:#0d0f13'>{body_left if show_left else ''}{body_right}</div>"


def panel_move(m, typed, chip_on, tally_on):
    caret = "<span class='caret'></span>" if len(typed) < len(m["request"]) else ""
    size = "font-size:17px;margin-bottom:12px" if len(m["request"]) > 200 else ""
    out = f"<div class='lab'>Request, from the saved task</div><div class='req' style='{size}'>{esc(typed)}{caret}</div>"
    if chip_on:
        out += f"<div class='lab'>Skill loaded</div><div class='chip on' style='display:inline-block;margin-bottom:18px'>{esc(m['skill'])}</div>"
    if tally_on:
        s = m["scores"]
        out += (f"<div class='lab'>Saved test result</div><div style='font-size:18px;line-height:1.32'>"
                f"<b>{esc(m['skill'])}</b>, on its tasks where it loaded: <b>{esc(m['tally'])}</b>."
                f"{' A marginal pass.' if m['marginal'] else ''}<br>"
                f"This task: {s['with']:.2f} with, {s['without']:.2f} without, on a 5-point rubric; "
                f"{esc(sample_text(m['winners']))}.<br>"
                f"<span class='muted'>Picked as {esc(m['why'])}. A favorable example, not a typical one.</span></div>")
    return f"<div class='panel'>{out}</div>"


def move_frame(scene, t, fade):
    m = scene["move"]
    typed_n = min(len(m["request"]), max(0, int((t - 0.2) / 2.2 * len(m["request"]) // 3 * 3)))
    typed = m["request"][:typed_n] if t < 2.5 else m["request"]
    shown = t >= 2.6
    p = 0.0 if t < 5.0 else min(1.0, (t - 5.0) / 0.6)
    top = f"<span class='move'>{esc(m['label'])}</span><span class='chip{' on' if t >= 2.5 else ''}'>{esc(m['skill'])}</span>"
    if not shown:
        media = "<div class='media'></div>"
    elif m["kind"] == "wipe":
        media = wipe_media(m, p)
    else:
        media = twoup_media(m, p)
    return stage(top, media, panel_move(m, typed, t >= 2.5, t >= 8.0), caption_at(scene, t), fade)


def title_frame(scene, t, fade, data):
    body = (f"<div class='stage' style='opacity:{fade:.2f}'><div style='position:absolute;left:80px;top:150px;right:80px'>"
            f"<div class='move' style='font-size:24px'>design-and-copy-skills</div>"
            f"<div style='font-size:96px;font-weight:900;line-height:1.02;margin:14px 0 22px'>Skills at work</div>"
            f"<div style='font-size:34px;line-height:1.3;max-width:900px'>A silent film built from saved test runs. "
            f"Real requests, real answers, real counts.</div></div>"
            f"<div class='cap'>{esc(caption_at(scene, t))}</div></div>")
    return page(body)


def request_frame(scene, t, fade, data):
    text = scene["request"]
    n = min(len(text), max(0, int((t - 0.3) / 2.0 * len(text) // 2 * 2)))
    typed = text if t >= 2.4 else text[:n]
    caret = "<span class='caret'></span>" if len(typed) < len(text) or int(t * 2) % 2 == 0 else ""
    body = (f"<div class='stage' style='opacity:{fade:.2f}'><div style='position:absolute;left:100px;top:130px;width:1080px'>"
            f"<div class='lab'>A request, typed to a coding agent</div>"
            f"<div style='border:2px solid #6b7384;border-radius:14px;background:#161920;padding:34px 38px;font-size:46px;"
            f"line-height:1.3;min-height:220px'>{esc(typed)}{caret}</div></div>"
            f"<div class='cap'>{esc(caption_at(scene, t))}</div></div>")
    return page(body)


def load_frame(scene, t, fade, data):
    pick = scene["pick"]
    chips = "".join(f"<span class='sk{' pick' if (n == pick and t >= 1.2) else ''}'>{esc(n)}</span>" for n in scene["names"])
    media = f"<div class='media'><div class='chips'>{chips}</div></div>"
    panel = "<div class='panel'><div class='lab'>In the agent's context</div><div class='muted' style='margin-bottom:16px'>Only each skill's name and one-line description.</div>"
    if t >= 2.4:
        refs = "".join(f"<div class='muted' style='font-family:ui-monospace,Menlo,monospace;font-size:15px'>references/{esc(r)}</div>" for r in scene["refs"])
        panel += (f"<div class='lab'>Loaded now</div><div class='chip on' style='display:inline-block;margin-bottom:10px'>{esc(pick)}</div>"
                  f"<div style='font-size:18px;line-height:1.35;margin-bottom:12px'>“{esc(scene['clause'])}”</div>")
        if t >= 4.4:
            panel += f"<div class='lab'>Opened only when a step needs one</div>{refs}"
    panel += "</div>"
    top = "<span class='move'>The skill list</span><span class='muted' style='font-size:18px'>Illustrative: drawn, not recorded</span>"
    return stage(top, media, panel, caption_at(scene, t), fade)


def record_frame(scene, t, fade, data):
    r = scene["rec"]
    total = r["wins"] + r["losses"] + r["ties"]
    bar = (f"<div class='bar' style='height:84px'><div class='win' style='width:{r['wins'] / total * 100:.2f}%;font-size:32px'>{r['wins']} wins</div>"
           f"<div class='loss' style='width:{r['losses'] / total * 100:.2f}%;font-size:32px'><span style='background:#f4f5f7;padding:2px 8px'>{r['losses']}</span></div>"
           f"<div class='tie' style='width:{r['ties'] / total * 100:.2f}%;font-size:32px'>{r['ties']}</div></div>")
    key = ("<div style='display:flex;gap:34px;font-size:28px;font-weight:700;margin-bottom:34px'>"
           f"<span>{r['wins']} wins with the skill</span><span>{r['losses']} losses</span><span>{r['ties']} ties</span></div>")
    blocks = ["<div class='big' style='font-size:46px'>Against the same model without it</div>", bar, key]
    if t >= 3.6:
        blocks.append(f"<div class='big' style='font-size:34px;margin-bottom:22px'>{r['marginal']} of the {r['skills']} passes are marginal: weaker evidence, labeled as such.</div>")
    if t >= 6.4:
        blocks.append(f"<div class='big' style='font-size:34px;margin-bottom:22px'>Latest round: {SHELVED_LATEST_ROUND} proposed updates were tried and shelved for missing the bar.</div>")
    if t >= 8.8:
        blocks.append("<div style='font-size:28px;line-height:1.35' class='muted'>Two merged updates show weaker evidence: the user-research-basics usability "
                      "references, and the fresh second held-out set for that skill, which shows no measurable gain.</div>")
    body = (f"<div class='stage' style='opacity:{fade:.2f}'><div style='position:absolute;left:80px;top:50px;right:80px'>"
            f"<div class='lab' style='font-size:18px'>{r['skills']} skills · {r['tasks']} held-out tasks where the skill loaded</div>{''.join(blocks)}</div>"
            f"<div class='cap'>{esc(caption_at(scene, t))}</div></div>")
    return page(body)


def end_frame(scene, t, fade, data):
    body = (f"<div class='stage' style='opacity:{fade:.2f}'><div style='position:absolute;left:80px;top:170px;right:80px'>"
            "<div class='move' style='font-size:24px'>design-and-copy-skills</div>"
            "<div style='font-size:56px;font-weight:900;line-height:1.1;margin:16px 0 22px'>Each skill tested against the same agent without it</div>"
            "<div style='font-size:30px;line-height:1.35' class='muted'>A transcript and a still-image version sit beside this film in docs/launch.</div></div>"
            f"<div class='cap'>{esc(caption_at(scene, t))}</div></div>")
    return page(body)


def frame_html(scene, t, data):
    fade = min(1.0, t / 0.2)
    kind = scene["id"]
    if "move" in scene:
        return move_frame(scene, t, fade)
    return {"title": title_frame, "request": request_frame, "load": load_frame, "record": record_frame,
            "end": end_frame}[kind](scene, t, fade, data)


def frame_plan(scenes, data):
    """[(html, count)] for the whole film at FPS, with each held still collapsed to one entry."""
    keys = []
    for scene in scenes:
        for i in range(int(round(scene["dur"] * FPS))):
            keys.append(frame_html(scene, i / FPS, data))
    return rle(keys)


# --------------------------------------------------------------------------------------------- stills and text

def poster_html(data):
    cells = []
    for m in data["moves"]:
        if m["kind"] != "wipe":
            continue
        s = 380 / m["crop"][2]
        cells.append("<div style='width:380px;border:2px solid #f4f5f7;border-radius:8px;overflow:hidden;background:#000'>"
                     "<div style='position:relative;height:214px;overflow:hidden;background:#fff'>"
                     f"<img src='{(Path(m['run']) / 'with.png').resolve().as_uri()}' alt='' style='position:absolute;"
                     f"width:{1280 * s:.1f}px;left:{-m['crop'][0] * s:.1f}px;top:{-m['crop'][1] * s:.1f}px'></div>"
                     f"<div style='color:#fff;font-size:18px;font-weight:700;padding:6px 10px'>{esc(m['label'])}, with the skill</div></div>")
    body = ("<div class='stage'><div style='position:absolute;left:60px;top:44px;right:60px'>"
            "<div class='move' style='font-size:24px'>design-and-copy-skills</div>"
            "<div style='font-size:92px;font-weight:900;line-height:1.02;margin:10px 0 14px'>Skills at work</div>"
            "<div style='font-size:32px;line-height:1.3;max-width:1000px' class='muted'>A silent film with captions: a request, a skill loading, then a form, a chart, a table, a deck, a pricing page and an accessibility pass.</div></div>"
            f"<div style='position:absolute;left:60px;top:370px;display:flex;gap:20px'>{''.join(cells)}</div>"
            "<div class='cap' style='height:76px;font-size:26px'>Play docs/launch/skills-at-work.mp4. Pictures are saved outputs from the repo's test runs.</div></div>")
    return page(body)


def still_html(data):
    cards = []
    for m in data["moves"]:
        run = Path(m["run"])
        if m["kind"] == "wipe":
            s = 0.32
            def thumb(side):
                return (f"<div style='position:relative;width:{MEDIA_W * s:.0f}px;height:{MEDIA_H * s:.0f}px;overflow:hidden;border:1px solid #6b7384;background:#fff'>"
                        f"<img src='{(run / (side + '.png')).resolve().as_uri()}' alt='' style='position:absolute;width:{1280 * MEDIA_W / m['crop'][2] * s:.1f}px;"
                        f"left:{-m['crop'][0] * MEDIA_W / m['crop'][2] * s:.1f}px;top:{-m['crop'][1] * MEDIA_W / m['crop'][2] * s:.1f}px'></div>")
            media = (f"<div style='display:flex;gap:12px'><div><div class='lab'>Without the skill</div>{thumb('without')}</div>"
                     f"<div><div class='lab'>With the skill</div>{thumb('with')}</div></div>")
        else:
            s = 0.66
            media = f"<div style='width:{MEDIA_W * s:.0f}px;height:{MEDIA_H * s:.0f}px;overflow:hidden'><div style='transform:scale({s});transform-origin:0 0;width:{MEDIA_W}px;position:relative;height:{MEDIA_H}px'>{twoup_media(m, 1.0)}</div></div>"
        cards.append("<div style='width:580px;background:#161920;border:1px solid #3a4150;border-radius:10px;padding:16px 18px'>"
                     f"<div style='display:flex;gap:12px;align-items:center;margin-bottom:8px'><span class='move' style='font-size:18px'>{esc(m['label'])}</span>"
                     f"<span class='chip' style='font-size:16px'>{esc(m['skill'])}</span></div>{media}"
                     f"<div style='font-size:17px;line-height:1.35;margin-top:10px'><span class='muted'>Request: </span>{esc(shorten(m['prompt'], 150))}<br>"
                     f"<b>{esc(m['skill'])}</b>, tasks where it loaded: {esc(m['tally'])}{'; a marginal pass' if m['marginal'] else ''}.</div></div>")
    r = data["record"]
    body = ("<div style='width:1240px;padding:30px 30px 34px'>"
            "<div class='move' style='font-size:20px'>design-and-copy-skills</div>"
            "<div style='font-size:48px;font-weight:900;margin:6px 0 8px'>Skills at work: eight moves, as stills</div>"
            f"<div style='font-size:21px;line-height:1.4;margin-bottom:18px' class='muted'>A still version of the film, for anyone who prefers no motion. Moves 1 and 2 (a request arriving and a skill loading) are the film's illustrative drawing and are described in the transcript. The six pictures below are saved outputs from the repo's test runs; each one was picked to show the move, so they are favorable examples, not typical ones.</div>"
            f"<div style='display:grid;grid-template-columns:580px 580px;gap:18px'>{''.join(cards)}</div>"
            f"<div style='font-size:24px;line-height:1.4;margin-top:20px'><b>The record:</b> {r['skills']} skills, {r['tasks']} held-out tasks where the skill loaded: "
            f"{r['wins']} wins, {r['losses']} losses, {r['ties']} ties against the same model without it; {r['marginal']} of the {r['skills']} passes are marginal. "
            f"In the latest round {SHELVED_LATEST_ROUND} proposed updates were tried and shelved for missing the bar. Two merged updates show weaker evidence: the user-research-basics usability references, and the fresh second held-out set for that skill, which shows no measurable gain.</div></div>")
    return page(body, "html,body{width:1300px;height:2110px;overflow:visible}.media{position:relative;left:0;top:0}")


def transcript(data, scenes):
    rec = data["record"]
    lines = [
        "# Skills at work: transcript",
        "",
        f"Text version of [skills-at-work.mp4](skills-at-work.mp4), a silent film of about {int(round(total_seconds(scenes)))} seconds with captions burned in. "
        "There is no audio. A [still-image version](skills-at-work-still.png) is beside it for anyone who prefers no motion.",
        "",
        "Everything shown is saved material from this repository's test runs: screenshots, answers and request text from `evals/<skill>/heldout/`, "
        "and counts read from the results files by `scripts/results_table.py`. Each of the six examples was picked to show the move, so they are "
        "favorable examples and not typical ones. Nothing in the film is generated by an image or video model. The title and the skill-list "
        "picture in move 2 are drawn, and move 2's caption says so.",
        "",
        "## Captions, in order",
        "",
    ]
    t = 0.0
    for s in scenes:
        for start, cap in s["captions"]:
            lines.append(f"- {stamp(t + start)} {cap}")
        t += s["dur"]
    lines += ["", "## What each move shows", ""]
    lines.append(f"1. **A request arrives.** The request typed is word for word from `evals/{data['moves'][4]['skill']}/activation.json`; the repo's activation check routed it to that skill.")
    lines.append(f"2. **The skill loads.** An illustrative drawing of the {rec['listed']} skill names, the one chosen, and its own description text and reference file names.")
    for i, m in enumerate(data["moves"], start=3):
        lines.append(f"{i}. **{m['label']}.** Skill `{m['skill']}`, task `{m['task']}` ([run files](../../evals/{m['skill']}/heldout/runs/{m['task']}/)). "
                     f"Request, shortened: “{m['request']}” On its tasks where it loaded, {m['skill']} has {m['tally']}"
                     f"{' (a marginal pass)' if m['marginal'] else ''}. On this task the judge scored {m['scores']['with']:.2f} with the skill and "
                     f"{m['scores']['without']:.2f} without, on a 5-point rubric, and {sample_text(m['winners'])}. Picked as {m['why']}."
                     f"{' ' + m['extra'] if m.get('extra') else ''}")
    lines += [
        "",
        "## The record",
        "",
        f"Across {rec['skills']} skills, counting only the held-out tasks where the skill loaded ({rec['tasks']} in all): {rec['wins']} wins, "
        f"{rec['losses']} losses and {rec['ties']} ties against the same model without it. {rec['marginal']} of the {rec['skills']} passes are marginal.",
        "",
        f"In the latest round of updates, {SHELVED_LATEST_ROUND} proposed updates were tried and shelved because they missed the bar. They are not in the library.",
        "",
        "Two merged updates show weaker evidence: the usability references added to user-research-basics, and the fresh second held-out set for that skill, "
        "which shows no measurable gain on the new set.",
        "",
        "## Rebuild",
        "",
        "```sh",
        "python3 scripts/make_film.py",
        "```",
        "",
        "Needs Chrome (set `CHROME_BIN` if it is not at the default path) and ffmpeg. The script reads the counts, request text, screenshots and answers "
        "from this repository, so a rebuild after new test results shows the new numbers. `python3 scripts/make_film.py --check` fails if this transcript is out of date.",
        "",
    ]
    return "\n".join(lines)


# ------------------------------------------------------------------------------------------------- build steps

def render_many(docs, workdir, width, height, jobs=6):
    """Render each distinct html string once; returns {html: png path}."""
    paths = {}
    todo = []
    for doc in docs:
        if doc not in paths:
            name = hashlib.sha1(doc.encode("utf-8")).hexdigest()[:16]
            paths[doc] = Path(workdir) / f"{name}.png"
            todo.append((doc, name))

    def one(item):
        doc, name = item
        src = Path(workdir) / f"{name}.html"
        src.write_text(doc, encoding="utf-8")
        for attempt in range(3):
            try:
                render.render(src, paths[doc], width, height, timeout=90)
                return
            except render.RenderError:
                if attempt == 2:
                    raise

    with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
        list(pool.map(one, todo))
    return paths


def quantize(path):
    if shutil.which("pngquant"):
        subprocess.run(["pngquant", "--quality=60-90", "--speed", "1", "--force", "--output", str(path), str(path)],
                       check=False)


FILE_URI = re.compile(r"file://[^'\"\s)]+")
STAMP = re.compile(rb"source-sha256:([0-9a-f]{64})")


def film_digest(root, data, scenes):
    """SHA-256 of every frame page with its hold, the poster and still pages, and the screenshots they load."""
    root = Path(root).resolve()
    prefix = root.as_uri() + "/"
    pages = [f"{n}\0{doc}" for doc, n in frame_plan(scenes, data)] + [poster_html(data), still_html(data)]
    h = hashlib.sha256()
    refs = set()
    for page in pages:
        refs.update(FILE_URI.findall(page))
        h.update(page.replace(prefix, "").encode("utf-8") + b"\0")
    for rel in sorted(Path(unquote(urlparse(u).path)).relative_to(root).as_posix() for u in refs):
        h.update(rel.encode("utf-8") + b"\0" + (root / rel).read_bytes())
    return h.hexdigest()


def media_paths(root):
    base = Path(root) / OUT
    return base / f"{NAME}.mp4", base / f"{NAME}-poster.png", base / f"{NAME}-still.png"


def stale_media(root, digest):
    """[file names] of the film, poster and still that are missing or were not built from this digest."""
    mp4, *pngs = media_paths(root)
    found = STAMP.search(mp4.read_bytes()) if mp4.is_file() else None
    stale = [] if found and found.group(1).decode("ascii") == digest else [mp4.name]
    return stale + [png.name for png in pngs if pngstamp.read_stamp(png) != digest]


def build_video(root, data, scenes, workdir, digest):
    plan = frame_plan(scenes, data)
    paths = render_many([h for h, _ in plan], workdir, W, H)
    listing = Path(workdir) / "frames.txt"
    lines = []
    for doc, n in plan:
        lines += [f"file '{paths[doc]}'", f"duration {n / FPS:.5f}"]
    # The concat demuxer ignores the last entry's duration, so repeat it and cut the output at the planned length.
    lines += [f"file '{paths[plan[-1][0]]}'", f"duration {1 / FPS:.5f}"]
    length = sum(n for _, n in plan) / FPS
    listing.write_text("\n".join(lines) + "\n", encoding="utf-8")
    out = Path(root) / OUT / f"{NAME}.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(listing),
                    "-t", f"{length:.3f}", "-vf", f"fps={FPS},scale={W}:{H},format=yuv420p", "-c:v", "libx264", "-preset", "slow", "-crf", "26",
                    "-an", "-map_metadata", "-1", "-metadata", f"comment=source-sha256:{digest}",
                    "-movflags", "+faststart", str(out)], check=True)
    return out


def build_stills(root, data, workdir, digest):
    outs = []
    for kind, doc, size in (("poster", poster_html(data), (W, H)), ("still", still_html(data), (1300, 2110))):
        src = Path(workdir) / f"{kind}.html"
        src.write_text(doc, encoding="utf-8")
        dest = Path(root) / OUT / f"{NAME}-{kind}.png"
        render.render(src, dest, size[0], size[1], timeout=120)
        quantize(dest)
        pngstamp.stamp(dest, digest)
        outs.append(dest)
    return outs


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    p.add_argument("--check", action="store_true",
                   help="exit 1 if the transcript, or the film, poster or still, differs from what the repo's files produce")
    p.add_argument("--transcript-only", action="store_true", help="write only the transcript (needs neither Chrome nor ffmpeg)")
    args = p.parse_args(argv)
    root = Path(args.root).resolve()
    data = gather(root)
    scenes = build_scenes(data)
    text = transcript(data, scenes)
    dest = root / OUT / f"{NAME}.md"
    if args.check:
        if not dest.is_file() or dest.read_text(encoding="utf-8") != text:
            print(f"{dest.relative_to(root)} is out of date; run python3 scripts/make_film.py")
            return 1
        stale = stale_media(root, film_digest(root, data, scenes))
        if stale:
            print(f"{', '.join(stale)} not built from the current repo files; run python3 scripts/make_film.py "
                  "(needs Chrome and ffmpeg)")
            return 1
        print("transcript, film, poster and still are current")
        return 0
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    print(dest.relative_to(root))
    if args.transcript_only:
        return 0
    if not shutil.which("ffmpeg"):
        print("ffmpeg not found", file=sys.stderr)
        return 1
    digest = film_digest(root, data, scenes)
    with tempfile.TemporaryDirectory(prefix="film-") as tmp:
        for out in (build_video(root, data, scenes, tmp, digest), *build_stills(root, data, tmp, digest)):
            print(out.relative_to(root), out.stat().st_size, "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
