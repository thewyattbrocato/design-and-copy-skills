#!/usr/bin/env python3
"""Draw the README results chart (docs/img/results.svg) from the held-out results files.

One row per listed skill, best first: a bar from zero for the mean rubric difference (with the skill minus without),
the loaded-only wins / losses / ties and the number of tasks that had a loaded sample. The numbers come from
evals/*/heldout/results.json through the functions of scripts/results_table.py, including its marginal rule; a marginal
pass is drawn as a hollow bar and tagged. Output is deterministic. With --check nothing is written; the exit code is 1
when the committed SVG differs from what the results files produce (CI uses this). With --png the SVG is also
rendered at 2x with scripts/render.py (needs Chrome). Standard library only.
"""
import argparse
import math
import sys
import tempfile
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render  # noqa: E402
import results_table as rt  # noqa: E402

DEFAULT_OUT = Path("docs") / "img" / "results.svg"
WIDTH = 960
MARGIN = 24
NAME_X = MARGIN
PLOT_LEFT, PLOT_RIGHT = 280, 640
WLT_X, TASKS_X = 800, 920
TOP, ROW = 128, 26
BAR_H = 14
NUMBER_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
                10: "ten", 11: "eleven", 12: "twelve"}

CSS = """\
:root{--bg:#ffffff;--ink:#1f2328;--muted:#59636e;--rule:#d1d9e0;--grid:#eaeef2;--gain:#1b7f79;--loss:#b35a1f}
@media (prefers-color-scheme:dark){:root{--bg:#0d1117;--ink:#e6edf3;--muted:#9198a1;--rule:#3d444d;--grid:#21262d;--gain:#3fb8af;--loss:#e0905a}}
text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;fill:var(--ink);font-size:13px;font-variant-numeric:tabular-nums}
.title{font-size:22px;font-weight:700}
.sub,.head,.tick,.note,.tag{fill:var(--muted)}
.sub{font-size:14px}
.head,.tick{font-size:12px}
.name{font-size:13px}
.val{font-weight:700}
.tag{font-size:12px;font-style:italic}
.bar-gain{fill:var(--gain)}
.bar-loss{fill:var(--loss)}
.hollow-gain{fill:var(--gain);fill-opacity:.12;stroke:var(--gain);stroke-width:1.5}
.hollow-loss{fill:var(--loss);fill-opacity:.12;stroke:var(--loss);stroke-width:1.5}
.zero{stroke:var(--muted);stroke-width:1.5}
.grid{stroke:var(--grid);stroke-width:1}
.row{stroke:var(--grid);stroke-width:1}
.panel{fill:var(--bg);stroke:var(--rule);stroke-width:1}
"""


def stats(root):
    """[dict] for every listed skill with a held-out result, plus the names of those without one."""
    rows, pending = [], []
    for name, _, _ in rt.live_rows(root):
        results = rt.load_json(Path(root) / "evals" / name / "heldout" / "results.json")
        outcome = rt.loaded_outcome(results) if isinstance(results, dict) and isinstance(results.get("summary"), dict) else None
        if outcome is None:
            pending.append(name)
            continue
        tally, mean_with, mean_without = outcome
        summary = results["summary"]
        rows.append({"name": name, "diff": mean_with - mean_without, "wins": tally["with_wins"],
                     "losses": tally["without_wins"], "ties": tally["ties"],
                     "tasks": tally["tasks_with_loaded_sample"], "suite": len(results.get("verdicts", [])),
                     "marginal": bool(rt.marginal_reasons(results)),
                     "all_pairs": summary.get("protocol", 1) != 2, "judge": summary.get("judge"),
                     "model": summary.get("model")})
    rows.sort(key=lambda r: (-r["diff"], r["name"]))
    return rows, pending


def model_label(value):
    """`claude:opus` -> `Opus`, `sonnet` -> `Sonnet`; several different values -> joined with `/`."""
    names = sorted({str(v).split(":")[-1].capitalize() for v in value if v})
    return "/".join(names) or "unrecorded"


def suite_label(rows):
    sizes = {r["suite"] for r in rows}
    if len(sizes) != 1:
        return "task counts vary by skill"
    count = sizes.pop()
    return f"{NUMBER_WORDS.get(count, count)} tasks per skill"


def signed(value):
    text = f"{value:+.2f}"
    return "0.00" if text in ("+0.00", "-0.00") else text.replace("-", "−")


def fmt(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")


def draw(rows, pending):
    n = len(rows)
    diffs = [r["diff"] for r in rows] or [0.0]
    lo, hi = math.floor(min(0.0, min(diffs)) * 10) / 10, math.ceil(max(0.0, max(diffs)) * 5) / 5
    scale = (PLOT_RIGHT - PLOT_LEFT) / (hi - lo)

    def x_of(v):
        return PLOT_LEFT + (v - lo) * scale

    zero = x_of(0)
    bottom = TOP + ROW * n
    more_wins = sum(1 for r in rows if r["wins"] > r["losses"])
    notes = [
        f"Loaded-only: counts only runs where the skill actually loaded; {suite_label(rows)}; "
        f"judge {model_label([r['judge'] for r in rows])}, generator {model_label([r['model'] for r in rows])}.",
        f"Hollow bar = marginal pass: rubric edge under +{rt.MARGINAL_ADVANTAGE:.2f}, fewer than {rt.MARGINAL_TASKS} "
        "tasks with a loaded sample, or a win margin of one task or less.",
    ]
    if any(r["all_pairs"] for r in rows):
        notes.append("† One answer per side; the rubric mean covers every pair, the wins / losses / ties are loaded-only.")
    if pending:
        notes.append("No held-out result yet: " + ", ".join(pending) + ".")
    height = bottom + 28 + 22 * len(notes) + 12
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" width="{WIDTH}" height="{height}" '
           'role="img" aria-labelledby="t d">',
           "<title id=\"t\">Held-out results for every listed skill, loaded runs only</title>",
           f'<desc id="d">Horizontal bars from zero showing the mean rubric difference with the skill minus without it, '
           f'best first, with each skill\'s loaded-only wins, losses and ties. {more_wins} of {n} skills won more tasks '
           f'than they lost.</desc>',
           f"<style>\n{CSS}</style>",
           f'<rect class="panel" x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="10"/>',
           f'<text class="title" x="{MARGIN}" y="46">With the skill loaded, {more_wins} of {n} skills won more tasks than they lost</text>',
           f'<text class="sub" x="{MARGIN}" y="70">Mean rubric score with the skill minus without it, on tasks the skill writers never saw. Best first.</text>',
           f'<text class="head" x="{PLOT_LEFT}" y="{TOP - 34}">Rubric difference (bars start at zero)</text>',
           f'<text class="head" x="{WLT_X}" y="{TOP - 34}" text-anchor="end">Wins / losses / ties</text>',
           f'<text class="head" x="{TASKS_X}" y="{TOP - 34}" text-anchor="end">Loaded tasks</text>']
    tick = math.ceil(lo * 5 - 1e-9) / 5
    while tick <= hi + 1e-9:
        x = x_of(tick)
        if abs(tick) > 1e-9:
            out.append(f'<line class="grid" x1="{fmt(x)}" y1="{TOP - 8}" x2="{fmt(x)}" y2="{bottom}"/>')
        out.append(f'<text class="tick" x="{fmt(x)}" y="{TOP - 14}" text-anchor="middle">'
                   f'{"0" if abs(tick) < 1e-9 else signed(tick)}</text>')
        tick += 0.2
    for i, r in enumerate(rows):
        top = TOP + ROW * i
        mid = top + ROW / 2
        out.append(f'<line class="row" x1="{MARGIN}" y1="{top + ROW}" x2="{WIDTH - MARGIN}" y2="{top + ROW}"/>')
        out.append(f'<text class="name" x="{NAME_X}" y="{fmt(mid + 4.5)}">{escape(r["name"])}</text>')
        gain = r["diff"] >= 0
        end = x_of(r["diff"])
        left, width = (zero, max(end - zero, 2)) if gain else (min(end, zero - 2), max(zero - end, 2))
        style = ("hollow-" if r["marginal"] else "bar-") + ("gain" if gain else "loss")
        out.append(f'<rect class="{style}" x="{fmt(left)}" y="{fmt(mid - BAR_H / 2)}" width="{fmt(width)}" height="{BAR_H}" rx="2"/>')
        tag = '<tspan class="tag" dx="6">marginal</tspan>' if r["marginal"] else ""
        mark = "†" if r["all_pairs"] else ""
        out.append(f'<text class="val" x="{fmt(max(end, zero) + 6)}" y="{fmt(mid + 4.5)}">{signed(r["diff"])}{mark}{tag}</text>')
        out.append(f'<text x="{WLT_X}" y="{fmt(mid + 4.5)}" text-anchor="end">{r["wins"]} / {r["losses"]} / {r["ties"]}</text>')
        out.append(f'<text x="{TASKS_X}" y="{fmt(mid + 4.5)}" text-anchor="end">{r["tasks"]}</text>')
    out.append(f'<line class="zero" x1="{fmt(zero)}" y1="{TOP - 8}" x2="{fmt(zero)}" y2="{bottom}"/>')
    for i, text in enumerate(notes):
        out.append(f'<text class="note" x="{MARGIN}" y="{bottom + 28 + 22 * i}">{escape(text)}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def light_only(svg):
    """The SVG without its dark-scheme block, so a PNG looks the same whatever theme the renderer runs in."""
    return "\n".join(ln for ln in svg.splitlines() if not ln.startswith("@media (prefers-color-scheme:dark)")) + "\n"


def to_png(svg_path, png_path):
    """Render the SVG at 2x, light theme, through scripts/render.py (an <img> in a throwaway page, offline)."""
    with tempfile.TemporaryDirectory(prefix="results-png-") as tmp:
        text = Path(svg_path).read_text(encoding="utf-8")
        w = int(text.split('width="', 2)[2].split('"', 1)[0])
        h = int(text.split('height="', 2)[2].split('"', 1)[0])
        light = Path(tmp) / "light.svg"
        light.write_text(light_only(text), encoding="utf-8")
        page = Path(tmp) / "page.html"
        page.write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:#fff}}'
                        f'img{{display:block;width:{w * 2}px;height:{h * 2}px}}</style><img src="{light.name}">',
                        encoding="utf-8")
        render.render(page, png_path, width=w * 2 + 2, height=h * 2 + 2)  # the headless viewport comes out 2px short


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    p.add_argument("--out", default=None, help=f"SVG path relative to --root (default {DEFAULT_OUT})")
    p.add_argument("--check", action="store_true", help="exit 1 if the SVG differs from what the results files produce")
    p.add_argument("--png", help="also render the SVG at 2x to this PNG path (needs Chrome)")
    args = p.parse_args(argv)
    out = Path(args.root) / (args.out or DEFAULT_OUT)
    new = draw(*stats(args.root))
    current = out.read_text(encoding="utf-8") if out.is_file() else None
    if args.check:
        if current != new:
            print(f"{out.name} is out of date; run: python3 scripts/make_results_chart.py")
            return 1
        print(f"{out.name} is up to date")
        return 0
    if current != new:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(new, encoding="utf-8")
    print(f"{out.name} {'written' if current != new else 'unchanged'}")
    if args.png:
        try:
            to_png(out, args.png)
        except render.RenderError as e:
            print(f"render failed: {e}", file=sys.stderr)
            return 1
        print(args.png)
    return 0


if __name__ == "__main__":
    sys.exit(main())
