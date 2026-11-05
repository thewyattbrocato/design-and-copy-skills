#!/usr/bin/env python3
"""Draw the README banner, the share cards, the library map and the family cards from the repository.

Every number and name on these images is read from the files they describe, so they cannot fall behind the library:

- docs/img/banner.svg and docs/launch/hero.svg: the count of listed skills in skills/ (design) and copy-skills/
  (copywriting);
- docs/launch/test-gate.svg: the loaded-only wins, losses and ties summed over the held-out results and the plain
  and marginal passes, through the functions of scripts/results_table.py that write the README headline, and the
  skills that were built, tested and pulled (withdrawn/<name>-pulled-evidence/ with no live skill of that name);
- docs/launch/skill-families.svg: the library map, every listed skill in the family docs/launch/families.json puts
  it in, with a solid mark for a plain pass and an outlined mark for a marginal one;
- docs/launch/families/<slug>.html: one card per family, showing one example from the before-and-after gallery
  (docs/before-after/), checked by scripts/before_after_gallery.py. A build example shows the two stored
  screenshots; a text example shows the `lines` of families.json, each of which must appear word for word in the
  stored answer (markdown emphasis and heading marks aside).

It also rewrites three README blocks and one ALT.md block, so the alt text and captions carry the same numbers:

  README.md   <!-- share-images:banner:start --> ... <!-- share-images:banner:end -->
  README.md   <!-- share-images:families:start --> ... <!-- share-images:families:end -->
  README.md   <!-- share-images:cards:start --> ... <!-- share-images:cards:end -->
  ALT.md      <!-- share-images:alt:start --> ... <!-- share-images:alt:end -->

families.json must put every listed skill in exactly one family, so a new skill fails --check until it has a place
on the map. Output is deterministic. With --check nothing is written and the exit code is 1 when a committed file
differs from what the repository produces (CI uses this). With --png every SVG and card (the banner aside, which the
README shows as SVG) is also rendered to a PNG next to it with scripts/render.py (needs Chrome), and each PNG is stamped
with the digest of the source it was drawn from (scripts/pngstamp.py). --check also fails when a PNG copy is missing or
carries the digest of another source, so a PNG left behind after its SVG or card changed fails CI without Chrome.
Standard library only.
"""
import argparse
import html
import json
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import before_after_gallery as gallery  # noqa: E402
import pngstamp  # noqa: E402
import render  # noqa: E402
import results_table  # noqa: E402
from roots import LIVE_ROOTS  # noqa: E402

FAMILIES = Path("docs") / "launch" / "families.json"
CARD_DIR = Path("docs") / "launch" / "families"
ALT = Path("docs") / "img" / "ALT.md"
BLOCKS = {"banner": ("README.md", "share-images:banner"), "families": ("README.md", "share-images:families"),
          "cards": ("README.md", "share-images:cards"), "alt": (ALT.as_posix(), "share-images:alt")}
NAME = "design-and-copy-skills"

INK, PAPER, AMBER, MUTED, BAR_TIE = "#101114", "#f5f3ee", "#ffb224", "#c4c0b6", "#8a877f"
SANS = '-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif'
SERIF = 'Georgia,"Iowan Old Style","Times New Roman",serif'
STYLE = (f"<style>text{{font-family:{SANS}}}\n.w{{font-weight:800;fill:{PAPER}}}.a{{fill:{AMBER}}}.f{{fill:{PAPER}}}"
         f".m{{fill:{MUTED}}}\n.n{{font-family:{SERIF};font-style:italic;fill:{PAPER}}}</style>")
WORD = 'design<tspan class="a">-</tspan>and<tspan class="a">-</tspan>copy<tspan class="a">-</tspan>skills'


def esc(text):
    return html.escape(str(text), quote=True)


def plural(n, one, many):
    return f"{n} {one if n == 1 else many}"


NUMBERS = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}


def number_word(n):
    return NUMBERS.get(n, str(n))


# ---------- facts read from the repository ----------

def live_skills(root):
    """{'design': [names], 'copy': [names]} for every listed skill."""
    kinds = dict(zip(LIVE_ROOTS, ("design", "copy")))
    found = {"design": [], "copy": []}
    for folder in LIVE_ROOTS:
        found[kinds[folder]] = [name for name, _, _ in results_table.skill_rows(root, folder)]
    return found


def totals(root):
    """Loaded-only wins, losses, ties over the listed skills, the skills counted, and which passes are marginal."""
    wins = losses = ties = 0
    counted, marginal = [], set()
    for name, results in results_table.heldout_results(root):
        outcome = results_table.loaded_outcome(results)
        if outcome is None:
            continue
        t = outcome[0]
        wins, losses, ties = wins + t["with_wins"], losses + t["without_wins"], ties + t["ties"]
        counted.append(name)
        if results_table.marginal_reasons(results):
            marginal.add(name)
    return {"wins": wins, "losses": losses, "ties": ties, "tasks": wins + losses + ties, "skills": counted,
            "marginal": marginal}


def pulled(root, live):
    """Skills built and tested but not shipped: withdrawn/<name>-pulled-evidence/ with no live skill of that name."""
    base = Path(root) / "withdrawn"
    names = sorted(d.name.removesuffix("-pulled-evidence") for d in base.glob("*-pulled-evidence") if d.is_dir()) \
        if base.is_dir() else []
    everyone = set(live["design"]) | set(live["copy"])
    return [n for n in names if n not in everyone]


PLAIN_MD = re.compile(r"\*\*|__|`|^#+\s*", re.MULTILINE)


def plain(text):
    return " ".join(PLAIN_MD.sub("", text).split())


def load_families(root, live):
    data = json.loads((Path(root) / FAMILIES).read_text(encoding="utf-8"))
    families = data["families"]
    kinds = {n: k for k, names in live.items() for n in names}
    seen = {}
    for fam in families:
        for s in fam["skills"]:
            if s not in kinds:
                raise ValueError(f"{FAMILIES}: {s} in {fam['name']} is not a listed skill")
            if kinds[s] != fam["kind"]:
                raise ValueError(f"{FAMILIES}: {s} is a {kinds[s]} skill but {fam['name']} is {fam['kind']}")
            if s in seen:
                raise ValueError(f"{FAMILIES}: {s} is in both {seen[s]} and {fam['name']}")
            seen[s] = fam["name"]
        if fam["example"] not in fam["skills"]:
            raise ValueError(f"{FAMILIES}: the example {fam['example']} is not in {fam['name']}")
    missing = sorted(set(kinds) - set(seen))
    if missing:
        raise ValueError(f"{FAMILIES}: no family for {', '.join(missing)}; add each listed skill to one family")
    entries = {e.skill: e for e in gallery.load(root)}
    for fam in families:
        entry = entries.get(fam["example"])
        if entry is None:
            raise ValueError(f"{FAMILIES}: {fam['name']} uses {fam['example']}, which has no gallery entry")
        fam["entry"] = entry
        if entry.answer_kind == "text":
            lines = fam.get("lines") or {}
            for side in gallery.SIDES:
                if not lines.get(side):
                    raise ValueError(f"{FAMILIES}: {fam['name']} needs {side} lines for a text example")
                path, _ = gallery.stored_answer(Path(root) / entry.run, side, entry.sample)
                stored = path.read_text(encoding="utf-8")
                for line in lines[side]:
                    if plain(line) not in plain(stored):
                        raise ValueError(f"{FAMILIES}: {fam['name']} {side} line is not in {path}: {line[:60]!r}")
    return families


# ---------- SVG drawing ----------

def svg(width, height, title, desc, body):
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
        'role="img" aria-labelledby="t d">',
        f'<title id="t">{esc(title)}</title>', f'<desc id="d">{esc(desc)}</desc>', STYLE,
        f'<rect width="{width}" height="{height}" rx="{28 if width > 1300 else 16}" fill="{INK}"/>', *body, "</svg>", ""])


def strip(x0, x1, y, n_square, n_dash, square, dash_w, dash_h, gap_between):
    """A row of amber squares then amber dashes from x0 to x1; returns (svg marks, x where the dashes start)."""
    n = n_square + n_dash
    step = (x1 - x0 - gap_between - dash_w) / max(n - 1, 1)
    marks, x = [], x0
    for i in range(n_square):
        marks.append(f'<rect x="{x:.1f}" y="{y}" width="{square}" height="{square}" class="a"/>')
        x += step
    x += gap_between - (step - square) if n_square else 0
    dash_x = x
    for i in range(n_dash):
        marks.append(f'<rect x="{x:.1f}" y="{y + (square - dash_h) / 2:.1f}" width="{dash_w}" height="{dash_h}" class="a"/>')
        x += step
    return '<g aria-hidden="true">' + "".join(marks) + "</g>", dash_x


def banner(f):
    d, c = len(f["design"]), len(f["copy"])
    n = d + c
    marks, dash_x = strip(56, 1234, 240, d, c, 12, 18, 3, 40)
    desc = (f"The name {NAME} set very large on two lines in heavy sans-serif with amber hyphens, beside an italic "
            f"serif line: {n} skills for AI coding agents. Along the bottom, a strip of {n} small amber marks: {d} "
            f"squares labelled design, then {c} dashes labelled copywriting.")
    body = [
        f'<text class="w" x="52" y="104" font-size="106" letter-spacing="-4">design<tspan class="a">-</tspan>and<tspan class="a">-</tspan></text>',
        f'<text class="w" x="52" y="198" font-size="106" letter-spacing="-4">copy<tspan class="a">-</tspan>skills</text>',
        f'<rect x="858" y="106" width="6" height="88" fill="{AMBER}"/>',
        f'<text class="n" x="884" y="132" font-size="30">{n} skills for</text>',
        '<text class="n" x="884" y="170" font-size="30">AI coding agents</text>', marks,
        f'<text class="m" x="56" y="292" font-size="22">{d} design</text>'
        f'<text class="m" x="{dash_x:.1f}" y="292" font-size="22">{c} copywriting</text>']
    return svg(1280, 320, NAME, desc, body)


def hero(f):
    d, c = len(f["design"]), len(f["copy"])
    n = d + c
    marks, dash_x = strip(80, 1500, 738, d, c, 18, 28, 4, 64)
    desc = (f"The name {NAME} set very large on two lines in heavy white sans-serif on near-black, with amber hyphens. "
            f"Beneath it, an amber rule and an italic serif note: {n} skills for AI coding agents. Each tested against "
            f"the same agent without it. Along the bottom, a strip of {n} small amber marks: {d} squares labelled "
            f"{d} design, then {c} dashes labelled {c} copywriting.")
    body = [
        '<text class="w" x="80" y="262" font-size="230" letter-spacing="-9">design<tspan class="a">-</tspan>and<tspan class="a">-</tspan></text>',
        '<text class="w" x="80" y="467" font-size="230" letter-spacing="-9">copy<tspan class="a">-</tspan>skills</text>',
        '<rect x="80" y="528" width="8" height="118" class="a"/>',
        f'<text class="n" x="116" y="574" font-size="54">{n} skills for AI coding agents.</text>',
        '<text class="n" x="116" y="634" font-size="54">Each tested against the same agent without it.</text>', marks,
        f'<text class="m" x="80" y="822" font-size="34">{d} design</text>'
        f'<text class="m" x="{dash_x:.1f}" y="822" font-size="34">{c} copywriting</text>']
    return svg(1600, 900, f"{NAME}: {n} skills for AI coding agents", desc, body)


def test_gate(f):
    t = f["totals"]
    n_skills = len(t["skills"])
    n_marg = len(t["marginal"])
    n_plain = n_skills - n_marg
    x0, x1, gap = 80, 1520, 4
    width = x1 - x0 - 2 * gap
    seg = [round(width * t[k] / t["tasks"]) for k in ("wins", "losses")]
    seg.append(width - sum(seg))
    xs = [x0, x0 + seg[0] + gap, x0 + seg[0] + seg[1] + 2 * gap]
    nums = [("wins", "wins with the skill", AMBER, "f"), ("losses", "losses", PAPER, "f"), ("ties", "ties", MUTED, "m")]
    body = [f'<text class="w" x="80" y="100" font-size="46" letter-spacing="-1.5">{WORD}</text>',
            '<text class="n" x="80" y="166" font-size="40">Each skill against the same agent without it, on held-out tasks</text>']
    for (key, label, colour, cls), x in zip(nums, xs):
        body.append(f'<text class="w" x="{x}" y="366" font-size="150" letter-spacing="-6" style="fill:{colour}">{t[key]}</text>')
        body.append(f'<text class="{cls}" x="{x}" y="426" font-size="40">{label}</text>')
    fills = (AMBER, PAPER, BAR_TIE)
    body.append('<g aria-hidden="true">' + "".join(
        f'<rect x="{x}" y="450" width="{w}" height="64" fill="{c}"/>' for x, w, c in zip(xs, seg, fills)) + "</g>")
    body += [f'<text class="f" x="80" y="590" font-size="36">{t["tasks"]} held-out tasks where the skill loaded.</text>',
             '<text class="m" x="80" y="636" font-size="36">A different model judged each pair blind, in both orders.</text>']
    step = (1500 - 80) / max(n_skills - 1, 1)
    step = min(step, 46)
    marks = []
    for i in range(n_skills):
        x = 80 + i * step
        marks.append(f'<rect x="{x:.1f}" y="682" width="20" height="20" class="a"/>' if i < n_plain else
                     f'<rect x="{x + 1.5:.1f}" y="683.5" width="17" height="17" fill="none" stroke="{AMBER}" stroke-width="3"/>')
    body.append('<g aria-hidden="true">' + "".join(marks) + "</g>")
    plain_label = plural(n_plain, "plain pass", "plain passes")
    marg_x = max(80 + n_plain * step, 80 + 0.56 * 32 * len(plain_label) + 40)
    body.append(f'<text class="m" x="80" y="762" font-size="32">{plain_label}</text>'
                f'<text class="m" x="{marg_x:.1f}" y="762" font-size="32">'
                f'{plural(n_marg, "marginal pass", "marginal passes")}, labelled</text>')
    lost = f["pulled"]
    if lost:
        body.append(f'<text class="f" x="80" y="836" font-size="34">{number_word(len(lost))} more '
                    f'{"skill" if len(lost) == 1 else "skills"} did not pass and {"is" if len(lost) == 1 else "are"} '
                    'not in the library.</text>')
    title = (f"{n_skills} skills against the same agent without them: {t['wins']} wins, {t['losses']} losses, "
             f"{t['ties']} ties")
    desc = (f"Dark card. The {NAME} wordmark with amber hyphens, an italic serif line, then three large numbers over a "
            f"proportional bar of {t['tasks']} held-out tasks where the skill loaded: {t['wins']} wins with the skill "
            f"in amber, {t['losses']} losses in off-white, {t['ties']} ties in grey. Below: a different model judged "
            f"each pair blind, in both orders. A strip of {n_skills} marks: {n_plain} solid amber for plain passes and "
            f"{n_marg} outlined for marginal passes."
            + (f" A last line says {number_word(len(lost)).lower()} more "
               f"{'skill did not pass and is' if len(lost) == 1 else 'skills did not pass and are'} not in the library."
               if lost else ""))
    return svg(1600, 900, title, desc, body)


def family_map(f):
    fams, marginal = f["families"], f["totals"]["marginal"]
    n = sum(len(x["skills"]) for x in fams)
    d, c = len(f["design"]), len(f["copy"])
    body = [f'<text class="w" x="80" y="104" font-size="52" letter-spacing="-2">{WORD}</text>',
            f'<text class="n" x="80" y="166" font-size="38">{n} skills in {len(fams)} families: '
            f'{d} design and {c} copywriting.</text>']
    col_w, x0, y_rows = 360, 80, (232, 556)
    for i, fam in enumerate(fams):
        x, y = x0 + (i % 4) * col_w, y_rows[i // 4]
        kind = "copywriting" if fam["kind"] == "copy" else "design"
        body.append(f'<text class="w" x="{x}" y="{y}" font-size="27" letter-spacing="-.5">{esc(fam["name"])}</text>')
        body.append(f'<text class="m" x="{x}" y="{y + 30}" font-size="19">{kind} · {len(fam["skills"])} skills</text>')
        for j, s in enumerate(fam["skills"]):
            yy = y + 68 + j * 30
            mark = (f'<rect x="{x + 1.5}" y="{yy - 14.5}" width="13" height="13" fill="none" stroke="{AMBER}" '
                    'stroke-width="3"/>' if s in marginal else f'<rect x="{x}" y="{yy - 16}" width="16" height="16" class="a"/>')
            body.append(f'<g aria-hidden="true">{mark}</g><text class="f" x="{x + 28}" y="{yy}" font-size="21">{esc(s)}</text>')
    body.append(f'<g aria-hidden="true"><rect x="80" y="842" width="16" height="16" class="a"/>'
                f'<rect x="441.5" y="843.5" width="13" height="13" fill="none" stroke="{AMBER}" stroke-width="3"/></g>'
                f'<text class="m" x="108" y="857" font-size="22">plain pass on held-out tasks</text>'
                f'<text class="m" x="468" y="857" font-size="22">marginal pass, labelled in Results</text>')
    parts = []
    for fam in fams:
        names = ", ".join(s + (" (marginal)" if s in marginal else "") for s in fam["skills"])
        kind = "copywriting" if fam["kind"] == "copy" else "design"
        parts.append(f"{fam['name']} ({kind}, {len(fam['skills'])}): {names}.")
    desc = (f"Map of the library: {n} skills in {len(fams)} families, {d} design and {c} copywriting, each skill "
            "marked as a plain or a marginal pass. " + " ".join(parts))
    title = f"{n} skills in {len(fams)} families"
    return svg(1600, 900, title, desc, body), desc


# ---------- family cards ----------

CARD_CSS = f"""*{{box-sizing:border-box;margin:0}}
html,body{{width:1600px;height:900px;background:{INK};color:{PAPER};font-family:{SANS}}}
.card{{padding:56px 72px;height:900px;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:baseline;color:{MUTED};font-size:24px}}
.word{{font-weight:800;color:{PAPER};letter-spacing:-.5px}}.word b{{color:{AMBER}}}
h1{{font-size:60px;font-weight:800;letter-spacing:-2px;margin-top:22px}}
.changes{{font-family:{SERIF};font-style:italic;font-size:30px;margin-top:8px}}
.skills{{color:{MUTED};font-size:22px;margin-top:14px}}
.pair{{display:flex;gap:40px;margin-top:30px;flex:1;min-height:0}}
.side{{flex:1;display:flex;flex-direction:column;min-width:0}}
.label{{font-size:24px;font-weight:700;margin-bottom:12px}}.with .label{{color:{AMBER}}}
.shot{{flex:1;min-height:0;border-radius:10px;overflow:hidden;border:2px solid #3a3b40}}
.with .shot{{border-color:{AMBER}}}
.shot img{{width:100%;display:block}}
.quote{{flex:1;border-left:6px solid #3a3b40;padding:4px 0 0 24px;font-size:34px;line-height:1.36}}
.with .quote{{border-color:{AMBER}}}.quote p+p{{margin-top:16px}}
.foot{{color:{MUTED};font-size:21px;margin-top:22px;line-height:1.4}}"""


def card_html(fam, root):
    entry = fam["entry"]
    w, l_, t = entry.tally
    pick = "the task with the largest judged difference in the skill's favor"
    skill_line = ", ".join(fam["skills"])
    sides = []
    for side, label in (("without", "Without the skill"), ("with", "With the skill")):
        if entry.answer_kind == "build":
            shot = next(i for i in entry.meta["images"] if i["side"] == side)
            src = Path("..") / ".." / "before-after" / entry.skill / shot["file"]
            inner = f'<div class="shot"><img src="{esc(src.as_posix())}" alt="{esc(shot["alt"])}"></div>'
        else:
            inner = '<div class="quote">' + "".join(f"<p>{esc(x)}</p>" for x in fam["lines"][side]) + "</div>"
        sides.append(f'<div class="side {side}"><div class="label">{label}</div>{inner}</div>')
    shown = ("Stored screenshots, top of the page." if entry.answer_kind == "build"
             else "Lines quoted word for word from the stored answers, not rewritten.")
    foot = (f"Example: {entry.skill}, held-out task {entry.meta['task_id']}, sample {entry.sample + 1}. {shown} "
            f"Chosen as {pick}, so it is a favorable example. Judged difference {entry.gap:+.2f} on the 5-point "
            f"rubric; over its loaded tasks the skill won {w}, lost {l_} and tied {t}.")
    kind = "copywriting" if fam["kind"] == "copy" else "design"
    return "\n".join([
        "<!DOCTYPE html>", '<html lang="en"><head><meta charset="utf-8">',
        f"<title>{esc(fam['name'])}: what the skills change</title>", f"<style>{CARD_CSS}</style></head><body>",
        '<div class="card">',
        f'<div class="top"><span class="word">design<b>-</b>and<b>-</b>copy<b>-</b>skills</span>'
        f"<span>{kind} family · {len(fam['skills'])} skills</span></div>",
        f"<h1>{esc(fam['name'])}</h1>", f'<p class="changes">{esc(fam["changes"])}</p>',
        f'<p class="skills">{esc(skill_line)}</p>', '<div class="pair">', *sides, "</div>",
        f'<p class="foot">{esc(foot)}</p>', "</div>", "</body></html>", ""])


def card_alt(fam):
    entry = fam["entry"]
    head = (f"Card for the {fam['name']} family ({', '.join(fam['skills'])}): {fam['changes']} Example from "
            f"{entry.skill}, without the skill on the left and with it on the right. ")
    if entry.answer_kind == "build":
        shots = {i["side"]: i["alt"] for i in entry.meta["images"]}
        body = f"Left: {shots['without']} Right: {shots['with']}"
    else:
        body = (f"Left: \"{' '.join(fam['lines']['without'])}\" Right: \"{' '.join(fam['lines']['with'])}\"")
    return head + body + f" Judged difference {entry.gap:+.2f}."


def card_caption(fam):
    entry = fam["entry"]
    what = "the stored screenshots" if entry.answer_kind == "build" else "lines quoted from the stored answers"
    return (f"**{fam['name']}.** {fam['changes']} Shown with {entry.skill}: {what}, from the task with its largest "
            f"judged difference ({entry.gap:+.2f}).")


# ---------- README and ALT.md blocks ----------

def md_alt(text):
    return gallery.alt(text)


def families_block(f):
    fams = f["families"]
    lines = [f"![{md_alt(f['map_desc'])}](docs/launch/skill-families.svg)", "",
             f"The map groups the {len(f['design']) + len(f['copy'])} skills by what they change in the answer; on "
             "disk they sit in two folders, `skills/` and `copy-skills/`. A solid mark is a plain pass and an outlined "
             "mark a marginal one. Each card below shows one real example from the family, taken from "
             "[More before and after examples](#more-before-and-after-examples): stored screenshots for a page the "
             "model built, or a few lines quoted word for word for a written answer. Each example is the skill's task "
             "with the largest judged difference, so the cards show the clearest cases, not typical ones. The family "
             "names and the one-line summaries are this README's grouping, not test results.", "",
             "| | |", "|---|---|"]
    for a, b in zip(fams[0::2], fams[1::2]):
        lines.append("| " + " | ".join(f"![{md_alt(card_alt(x))}](docs/launch/families/{x['slug']}.png)" for x in (a, b)) + " |")
        lines.append("| " + " | ".join(card_caption(x) for x in (a, b)) + " |")
    return lines


def cards_block(f):
    n, t = len(f["design"]) + len(f["copy"]), f["totals"]
    return ["Three cards in the same style as the banner, drawn by `scripts/make_share_images.py` from the skill "
            "folders and the results files. Each is a plain SVG with a PNG copy at 1600 x 900.", "",
            f"![{md_alt(f['desc']['hero'])}](docs/launch/hero.png)", "",
            f"*The library: {n} skills, {len(f['design'])} for design and {len(f['copy'])} for copywriting.*", "",
            f"![{md_alt(f['desc']['test-gate'])}](docs/launch/test-gate.png)", "",
            f"*The record: {t['wins']} wins, {t['losses']} losses and {t['ties']} ties over the {t['tasks']} held-out "
            f"tasks where a skill loaded; {len(t['marginal'])} of the {len(t['skills'])} passes are marginal.*", "",
            f"![{md_alt(f['map_desc'])}](docs/launch/skill-families.png)", "",
            f"*The map: every skill in one of {len(f['families'])} families, the same map as in "
            "[What each family changes](#what-each-family-changes).*"]


def alt_block(f):
    cell = results_table.cell
    rows = [("`docs/img/banner.svg`", f["desc"]["banner"]),
            ("`docs/launch/hero.svg` (PNG copy: `docs/launch/hero.png`)", f["desc"]["hero"]),
            ("`docs/launch/test-gate.svg` (PNG copy: `docs/launch/test-gate.png`)", f["desc"]["test-gate"]),
            ("`docs/launch/skill-families.svg` (PNG copy: `docs/launch/skill-families.png`)", f["map_desc"])]
    rows += [(f"`docs/launch/families/{x['slug']}.png` (source: `docs/launch/families/{x['slug']}.html`)", card_alt(x))
             for x in f["families"]]
    return ["| File | Alt text |", "|---|---|"] + [f"| {a} | {cell(b)} |" for a, b in rows]


def banner_block(f):
    return [f'<p align="center"><img src="docs/img/banner.svg" alt="{esc(f["desc"]["banner"])}" width="720"></p>']


# ---------- assembly ----------

def facts(root):
    live = live_skills(root)
    f = {"design": live["design"], "copy": live["copy"], "totals": totals(root), "pulled": pulled(root, live)}
    f["families"] = load_families(root, live)
    return f


def desc_of(svg_text):
    return html.unescape(re.search(r'<desc id="d">(.*?)</desc>', svg_text, re.S).group(1))


def outputs(root):
    """{relative path: text} for every generated file, plus the README and ALT.md blocks."""
    f = facts(root)
    files = {"docs/img/banner.svg": banner(f), "docs/launch/hero.svg": hero(f), "docs/launch/test-gate.svg": test_gate(f)}
    map_svg, f["map_desc"] = family_map(f)
    files["docs/launch/skill-families.svg"] = map_svg
    f["desc"] = {"banner": desc_of(files["docs/img/banner.svg"]), "hero": desc_of(files["docs/launch/hero.svg"]),
                 "test-gate": desc_of(files["docs/launch/test-gate.svg"])}
    for fam in f["families"]:
        files[(CARD_DIR / f"{fam['slug']}.html").as_posix()] = card_html(fam, root)
    blocks = {"banner": banner_block(f), "families": families_block(f), "cards": cards_block(f), "alt": alt_block(f)}
    return files, blocks


def replace_block(text, name, lines, where):
    start, end = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    i, j = text.find(start), text.find(end)
    if i < 0 or j < i:
        raise ValueError(f"{where} is missing the {start} ... {end} markers")
    return text[:i + len(start)] + "\n" + "\n".join(lines) + "\n" + text[j:]


def to_png(source, png, width, height):
    """Render an SVG (through an <img> page) or an HTML card to a PNG at its own size, offline."""
    source, png = Path(source).resolve(), Path(png).resolve()
    with tempfile.TemporaryDirectory(prefix="share-png-") as tmp:
        page = source
        if source.suffix == ".svg":
            page = Path(tmp) / "page.html"
            page.write_text(f'<!DOCTYPE html><html><body style="margin:0;background:{INK}">'
                            f'<img src="{source.as_uri()}" width="{width}" height="{height}" style="display:block">'
                            "</body></html>", encoding="utf-8")
        render.render(page, png, width=width, height=height)


CARD_SIZE = (1600, 900)
NO_PNG = {"docs/img/banner.svg"}  # the README shows the banner as SVG; it has no PNG copy


def png_copies(files):
    """[(source rel, png rel, (width, height))] for every generated image that has a PNG copy."""
    copies = []
    for rel, text in files.items():
        if rel in NO_PNG:
            continue
        if rel.endswith(".svg"):
            size = tuple(map(int, re.search(r'width="(\d+)" height="(\d+)"', text).groups()))
        else:
            size = CARD_SIZE
        copies.append((rel, Path(rel).with_suffix(".png").as_posix(), size))
    return copies


def stale_pngs(root, files):
    """['<png> <reason>'] for each PNG copy that is missing or was not rendered from the current source."""
    out = []
    for rel, png, _ in png_copies(files):
        reason = pngstamp.stale(Path(root) / png, files[rel], (Path(root) / rel).parent)
        if reason:
            out.append(f"{png} {reason}")
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    p.add_argument("--check", action="store_true", help="exit 1 if a generated file or block is out of date")
    p.add_argument("--png", action="store_true", help="also render every image to a PNG next to it (needs Chrome)")
    args = p.parse_args(argv)
    root = Path(args.root)
    try:
        files, blocks = outputs(root)
        targets = {}
        for rel, text in files.items():
            targets[rel] = text
        for key, (rel, marker) in BLOCKS.items():
            current = targets.get(rel) or (root / rel).read_text(encoding="utf-8")
            targets[rel] = replace_block(current, marker, blocks[key], rel)
    except (OSError, ValueError, KeyError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    stale = [rel for rel, text in targets.items()
             if not (root / rel).is_file() or (root / rel).read_text(encoding="utf-8") != text]
    if args.check:
        pngs = stale_pngs(root, files)
        if stale or pngs:
            print("out of date: " + ", ".join(stale + pngs) + "; run: python3 scripts/make_share_images.py --png")
            return 1
        print("share images, map, family cards and their PNG copies are up to date")
        return 0
    for rel in stale:
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(targets[rel], encoding="utf-8")
        print(f"wrote {rel}")
    if args.png:
        try:
            for rel, png, (w, h) in png_copies(files):
                to_png(root / rel, root / png, w, h)
                pngstamp.stamp(root / png, pngstamp.source_digest(files[rel], (root / rel).parent))
                print(f"rendered {png}")
        except render.RenderError as e:
            print(f"render failed: {e}", file=sys.stderr)
            return 1
    elif stale_pngs(root, files):
        print("PNG copies are out of date; run: python3 scripts/make_share_images.py --png")
    if not stale:
        print("share images, map and family cards are up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
