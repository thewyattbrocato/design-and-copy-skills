#!/usr/bin/env python3
"""Build README-ready before/after image examples from a config file.

For every example the same model gets the same prompt N times without and N times with the skill; every page is
rendered to PNG from HTML and CSS in headless Chrome. A blind, swap-controlled judge scores each run against the
example's rubric, and the pair that is featured is picked by a rule declared in the config before anything runs
(default: the MEDIAN run of each arm by rubric mean, never the best). A contact sheet shows every run of both
arms so the spread is visible. Nothing is edited by hand.

Output: docs/examples/<id>/<model>/{without,with,compare,contact-sheet}.png, without.html, with.html,
runs/<arm>-<n>.html (every run, reused when a rerun resumes after an error) and meta.json.

Config (JSON):
{"model": "sonnet", "mode": "installed", "runs": 3, "judge": "claude:opus", "effort": null,
 "width": 1280, "height": 800,
 "featuring": {"pick": "median", "text": "<rule shown in meta.json>"},
 "examples": [{"id": "landing-hero", "skill": "<skill-name>", "prompt": "...", "rubric": ["...", "..."],
               "width": 1280, "height": 800}]}
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evalkit as ek  # noqa: E402
import render as render_mod  # noqa: E402
from roots import LIVE_ROOTS, find_skill  # noqa: E402

MAX_WIDTH, MAX_BYTES, SHEET_MAX_BYTES = 1000, 250 * 1024, 400 * 1024
WIDTH_STEPS = (1000, 900, 800, 700, 600)
ARMS = ("without", "with")
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DEFAULT_RULE = ("Rank the runs of each arm by the blind judge's rubric mean (two passes with the sides swapped) and "
                "feature the median run of each arm, the lower median when the count is even. The best run is "
                "never chosen. Every run is shown in the contact sheet.")


def png_size(path):
    data = Path(path).read_bytes()[:24]
    return struct.unpack(">II", data[16:24])


def downscale(src, dst, width):
    """Scale a PNG to the given width with sips, or with Chrome when sips is missing."""
    src_w, src_h = png_size(src)
    if src_w <= width:
        shutil.copy(src, dst)
        return
    if shutil.which("sips") and not os.environ.get("EVAL_NO_SIPS"):
        proc = subprocess.run(["sips", "--resampleWidth", str(width), str(src), "--out", str(dst)],
                              capture_output=True, text=True)
        if proc.returncode == 0:
            return
    height = round(src_h * width / src_w)
    with tempfile.TemporaryDirectory(prefix="eval-scale-") as tmp:
        page = Path(tmp) / "scale.html"
        page.write_text(f'<!doctype html><body style="margin:0"><img src="{Path(src).resolve().as_uri()}" '
                        f'width="{width}" height="{height}" style="display:block"></body>', encoding="utf-8")
        ek.render_html(page, dst, width, height)


def optimize(src, dst_dir, stem, widths=WIDTH_STEPS, max_bytes=MAX_BYTES):
    """Write dst_dir/<stem>.png at <= 1000px wide and under max_bytes; fall back to JPEG when PNG stays too large."""
    best = None
    for width in widths:
        out = Path(dst_dir) / f"{stem}.png"
        downscale(src, out, width)
        best = out
        if out.stat().st_size <= max_bytes:
            return out
    if shutil.which("sips"):
        jpg = Path(dst_dir) / f"{stem}.jpg"
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "70", str(best), "--out", str(jpg)],
                       capture_output=True, check=True)
        if jpg.stat().st_size <= max_bytes:
            best.unlink()
            return jpg
        jpg.unlink()
    print(f"warning: {best} is {best.stat().st_size // 1024} KB, over the {max_bytes // 1024} KB target", file=sys.stderr)
    return best


def compare_page(without_png, with_png, shot_w, shot_h, width=2000):
    cell = width // 2 - 20
    img_h = round(shot_h * cell / shot_w)
    html = f"""<!doctype html><meta charset="utf-8"><style>
body{{margin:0;padding:20px;background:#f4f4f5;font:600 22px/1 system-ui,sans-serif;color:#18181b}}
.row{{display:flex;gap:20px}} figure{{margin:0;width:{cell}px}}
figcaption{{padding:0 0 12px}} img{{display:block;width:{cell}px;height:{img_h}px;border:1px solid #d4d4d8}}
</style><div class="row">
<figure><figcaption>Without skill</figcaption><img src="{Path(without_png).resolve().as_uri()}"></figure>
<figure><figcaption>With skill</figcaption><img src="{Path(with_png).resolve().as_uri()}"></figure></div>"""
    return html, width, img_h + 74


def sheet_page(pngs, means, featured, invoked, shot_w, shot_h, width=1000, gap=12):
    """Every run of both arms at thumbnail size: one row per arm, the featured run outlined."""
    runs = len(pngs["with"])
    cell = (width - gap * (runs + 1)) // runs
    img_h = round(shot_h * cell / shot_w)
    rows = []
    for arm in ARMS:
        cells = []
        for i, png in enumerate(pngs[arm]):
            cls = " class=\"pick\"" if i == featured[arm] else ""
            tag = "featured (median) · " if i == featured[arm] else ""
            note = " · skill not invoked" if arm == "with" and invoked[i] is False else ""
            cells.append(f'<figure{cls}><img src="{Path(png).resolve().as_uri()}">'
                         f"<figcaption>{tag}run {i + 1} · rubric {means[arm][i]:.2f}{note}</figcaption></figure>")
        rows.append(f'<h2>{"With skill" if arm == "with" else "Without skill"}</h2><div class="row">{"".join(cells)}</div>')
    html = f"""<!doctype html><meta charset="utf-8"><style>
body{{margin:0;padding:{gap}px;background:#f4f4f5;font:12px/1.3 system-ui,sans-serif;color:#18181b;width:{width - 2 * gap}px}}
h2{{font:600 15px/1 system-ui,sans-serif;margin:6px 0 8px}} .row{{display:flex;gap:{gap}px;margin-bottom:8px}}
figure{{margin:0;width:{cell}px}} img{{display:block;width:{cell}px;height:{img_h}px;border:1px solid #d4d4d8}}
figcaption{{padding-top:4px}} .pick img{{outline:3px solid #2563eb;outline-offset:-1px}} .pick figcaption{{font-weight:700;color:#1d4ed8}}
</style>{"".join(rows)}"""
    return html, width, 2 * (img_h + 52) + 2 * gap + 10


def median_index(means):
    """Index of the median run by rubric mean (the lower median for an even count); ties keep run order."""
    order = sorted(range(len(means)), key=lambda i: (means[i], i))
    return order[(len(order) - 1) // 2]


def judge_pair(example, cfg, index, without_png, with_png, run_dir):
    """Blind, swap-controlled rubric judgment of run `index` of each arm, shown as an anonymous pair.

    Judgments are cached next to the runs, keyed by judge, seed, rubric and the exact pages, so re-rendering
    or re-optimizing images never pays for the judge again."""
    task = {"id": f"{example['id']}/{index}", "prompt": example["prompt"], "rubric": example["rubric"]}
    digest = hashlib.sha256()
    for arm in ARMS:
        digest.update((run_dir / f"{arm}-{index + 1}.html").read_bytes())
    key = {"judge": cfg["judge"], "seed": cfg["seed"], "rubric": example["rubric"], "pages": digest.hexdigest()[:16]}
    cache = run_dir / f"judgment-{index + 1}.json"
    if cache.is_file():
        try:
            saved = json.loads(cache.read_text(encoding="utf-8"))
            if saved.get("key") == key:
                return saved["result"]
        except ValueError:
            pass
    passes = [ek.judge_pass(cfg["judge"], task, order, None, None, with_png, without_png)
              for order in ek.assign_order(cfg["seed"], task["id"])]
    result = ek.combine_passes(passes)
    cache.write_text(json.dumps({"key": key, "result": result}, indent=2) + "\n", encoding="utf-8")
    return result


def build_example(example, cfg, root, out_root, concurrency):
    skill = example["skill"]
    found = find_skill(root, skill)
    if not found:
        raise ek.EvalError(f"{skill}/SKILL.md not found in {' or '.join(f'{s}/' for s in LIVE_ROOTS)}")
    skill_dir = found[1]
    ek.probe_skill(skill, skill_dir, cfg["mode"], cfg["model"], cfg["effort"])
    width, height = example.get("width", cfg["width"]), example.get("height", cfg["height"])
    runs = cfg["runs"]
    out = out_root / example["id"] / cfg["model"]
    run_dir = out / "runs"
    run_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="eval-example-") as tmp:
        tmp = Path(tmp)
        jobs = [(arm, i) for arm in ARMS for i in range(runs)]

        def work(job):
            arm, i = job
            html, meta_file = run_dir / f"{arm}-{i + 1}.html", run_dir / f"{arm}-{i + 1}.meta.json"
            if not (html.is_file() and meta_file.is_file()):  # a finished run is kept so a rerun resumes
                text, meta = ek.generate(example["prompt"], "build", skill, skill_dir, arm == "with", cfg["mode"],
                                         cfg["model"], cfg["effort"], 900, f"{example['id']}/{arm}/{i}")
                html.write_text(text, encoding="utf-8")
                meta_file.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
            png = tmp / f"{arm}-{i}.png"
            ek.render_html(html, png, width, height)
            return html, png, json.loads(meta_file.read_text(encoding="utf-8"))

        results = dict(zip(jobs, ek.pmap(work, jobs, concurrency)))
        pngs = {arm: [results[(arm, i)][1] for i in range(runs)] for arm in ARMS}
        judgments = ek.pmap(lambda i: judge_pair(example, cfg, i, pngs["without"][i], pngs["with"][i], run_dir),
                            range(runs), concurrency)
        means = {arm: [j["rubric_scores"][arm] for j in judgments] for arm in ARMS}
        featured = {arm: median_index(means[arm]) for arm in ARMS}
        invoked = [(skill in results[("with", i)][2].get("skills_invoked", [])) if cfg["mode"] == "installed" else None
                   for i in range(runs)]
        model_id = next((results[k][2].get("model_id") for k in jobs if results[k][2].get("model_id")), None)

        files = {}
        for arm in ARMS:
            shutil.copy(results[(arm, featured[arm])][0], out / f"{arm}.html")
            files[arm] = optimize(pngs[arm][featured[arm]], out, arm).name
        # Both images get the same width so the pair is comparable.
        common = min(png_size(out / name)[0] for name in files.values() if name.endswith(".png"))
        for arm in ARMS:
            if files[arm].endswith(".png") and png_size(out / files[arm])[0] != common:
                files[arm] = optimize(pngs[arm][featured[arm]], out, arm, (common,)).name
        page, w, h = compare_page(pngs["without"][featured["without"]], pngs["with"][featured["with"]], width, height)
        (tmp / "compare.html").write_text(page, encoding="utf-8")
        ek.render_html(tmp / "compare.html", tmp / "compare-full.png", w, h)
        files["compare"] = optimize(tmp / "compare-full.png", out, "compare").name
        page, w, h = sheet_page(pngs, means, featured, invoked, width, height)
        (tmp / "sheet.html").write_text(page, encoding="utf-8")
        ek.render_html(tmp / "sheet.html", tmp / "sheet-full.png", w, h)
        files["contact_sheet"] = optimize(tmp / "sheet-full.png", out, "contact-sheet", (1000,), SHEET_MAX_BYTES).name
    meta = {"id": example["id"], "skill": skill, "prompt": example["prompt"], "prompt_suffix": ek.BUILD_SUFFIX,
            "model": cfg["model"],
            "model_id": model_id, "date": datetime.date.today().isoformat(), "mode": cfg["mode"],
            "effort": cfg["effort"], "width": width, "height": height, "runs_per_arm": runs,
            "judge": cfg["judge"], "seed": cfg["seed"], "rubric": example["rubric"],
            "featuring_rule": cfg["featuring"]["text"],
            "featured_run": {arm: featured[arm] + 1 for arm in ARMS},
            "spread": {arm: means[arm] for arm in ARMS},
            "skill_invoked_in_with_runs": invoked,
            "pairs": [{"run": i + 1, "winner": j["winner"], "position_consistent": j["position_consistent"],
                       "rubric_scores": j["rubric_scores"], "judge_notes": j["judge_notes"]}
                      for i, j in enumerate(judgments)],
            "files": files, "sources": {"without": "without.html", "with": "with.html", "runs": "runs/"}}
    (out / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    return out


def load_config(path):
    try:
        cfg = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise ek.EvalError(f"cannot read config: {e}")
    cfg = {"model": "sonnet", "mode": "installed", "runs": 3, "judge": "claude:opus", "effort": None, "seed": 0,
           "width": 1280, "height": 800, "featuring": {"pick": "median", "text": DEFAULT_RULE}, **cfg}
    examples = cfg.get("examples")
    if not isinstance(examples, list) or not examples:
        raise ek.EvalError("config needs a non-empty 'examples' list")
    seen = set()
    for e in examples:
        if not (isinstance(e, dict) and all(isinstance(e.get(k), str) and e[k].strip() for k in ("id", "prompt", "skill"))):
            raise ek.EvalError("each example needs string 'id', 'prompt' and 'skill'")
        rubric = e.get("rubric")
        if not (isinstance(rubric, list) and rubric and all(isinstance(r, str) and r.strip() for r in rubric)):
            raise ek.EvalError(f"example '{e['id']}' needs a non-empty 'rubric' list of strings")
        if not KEBAB.match(e["id"]) or e["id"] in seen:
            raise ek.EvalError(f"example id '{e['id']}' must be unique kebab-case")
        seen.add(e["id"])
    feat = cfg["featuring"]
    if not (isinstance(feat, dict) and feat.get("pick") == "median" and isinstance(feat.get("text"), str) and feat["text"].strip()):
        raise ek.EvalError("'featuring' must be {\"pick\": \"median\", \"text\": \"<rule>\"}; the best run is never featured")
    if cfg["mode"] not in ("installed", "injected") or not isinstance(cfg["runs"], int) or cfg["runs"] < 1:
        raise ek.EvalError("'mode' must be installed|injected and 'runs' a positive integer")
    return cfg


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("config")
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    p.add_argument("--model", help="model for this run, overriding the config (the same config can run on several)")
    p.add_argument("--runs", type=int, help="samples per arm (default: the config's value, 3)")
    p.add_argument("--judge", help="judge spec, overriding the config")
    p.add_argument("--only", help="comma-separated example ids")
    p.add_argument("--concurrency", type=int, default=2)
    args = p.parse_args(argv)
    try:
        cfg = load_config(args.config)
        for key in ("model", "runs", "judge"):
            if getattr(args, key) is not None:
                cfg[key] = getattr(args, key)
        if not isinstance(cfg["runs"], int) or cfg["runs"] < 1:
            raise ek.EvalError("'runs' must be a positive integer")
        if ek.same_model_judge(cfg["judge"], cfg["model"]):
            raise ek.EvalError(f"judge {cfg['judge']} is the generator's own model ({cfg['model']}); use a different judge")
        wanted = [i for i in (args.only or "").split(",") if i]
        unknown = set(wanted) - {e["id"] for e in cfg["examples"]}
        if unknown:
            raise ek.EvalError(f"unknown example ids: {sorted(unknown)}")
        root = Path(args.root)
        for example in cfg["examples"]:
            if not wanted or example["id"] in wanted:
                print(f"wrote {build_example(example, cfg, root, root / 'docs' / 'examples', args.concurrency)}", flush=True)
    except (ek.EvalError, render_mod.RenderError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
