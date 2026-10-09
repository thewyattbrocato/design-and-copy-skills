#!/usr/bin/env python3
"""Stub generator, judge and renderer for the eval tests; never calls a model.

Usage (selected through EVAL_GENERATOR_CMD / EVAL_JUDGE_CMD / EVAL_RENDER_CMD):
  mock_eval_cmd.py generate        JSON on stdin -> answer text
  mock_eval_cmd.py judge           JSON on stdin -> judge reply; behaviour set by EVAL_MOCK_JUDGE
  mock_eval_cmd.py render IN OUT   writes a small PNG; a page headed "SKILLED|PLAIN <task>/<arm>/<n>" is marked "<arm>:<n>"
EVAL_MOCK_RUN_SCORES='{"with": [3, 5, 4], "without": [2, 2, 2]}' makes the judge score marked pages per run.
Every generator call is appended to the file named by EVAL_MOCK_LOG when set (one "<task>/<arm>" line per call).
The generator reports the skill as loaded in every WITH answer, as JSON {"answer", "skills_invoked"}, except where
EVAL_MOCK_NOT_LOADED='{"t1": 1, "t2#1": 99}' says a task (or "task#sample") fails to load for that many leading
attempts (99 = never). EVAL_MOCK_SAMPLE_VERDICTS='{"t0": ["with", "with", "without"]}' makes the judge pick
the named arm for each sample of a text task (anything else follows EVAL_MOCK_JUDGE).
"""
import json
import os
import re
import struct
import sys
import zlib


def png(width=1280, height=800, marker=b""):
    def chunk(tag, data):
        body = tag + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body))
    raw = b"".join(b"\x00" + b"\x20\x40\x80" * width for _ in range(height))
    text = chunk(b"tEXt", b"run\x00" + marker) if marker else b""
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
            + text + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


def generate(req):
    log = os.environ.get("EVAL_MOCK_LOG")
    if log:
        with open(log, "a") as f:
            f.write(f"{req['task_id']}/{req['arm']}\n")
    if req["kind"] == "probe":
        names = ["dataviz", "init"] + ([req["skill"]] if req["arm"] == "with" else [])
        return ", ".join(names)
    tag = "SKILLED" if req["arm"] == "with" else "PLAIN"
    if req["kind"] == "build":
        return f"```html\n<!doctype html><html><body><h1>{tag} {req['task_id']}</h1></body></html>\n```"
    text = f"{tag} answer for {req['task_id']} [s{req.get('sample', 0)}]"
    if req["arm"] == "with":
        return json.dumps({"answer": text, "skills_invoked": [req["skill"]] if loads(req) else []})
    return text


def loads(req):
    """Whether this WITH attempt loads the skill: EVAL_MOCK_NOT_LOADED gives the failing leading attempts."""
    table = json.loads(os.environ.get("EVAL_MOCK_NOT_LOADED") or "{}")
    sample = req.get("sample", 0)
    failing = table.get(f"{req['task_id']}#{sample}", table.get(req["task_id"], 0))
    return req.get("attempt", 0) >= failing


def judge(req):
    prompt = req["prompt"]
    run_scores = os.environ.get("EVAL_MOCK_RUN_SCORES")
    if run_scores and req.get("images"):
        table, n = json.loads(run_scores), len(re.findall(r"^\d+\. ", prompt, re.M))
        side_scores = {}
        for side, name in (("A", "a.png"), ("B", "b.png")):
            arm, idx = re.search(rb"run\x00(\w+):(\d+)", open(os.path.join(req["dir"], name), "rb").read()).groups()
            side_scores[side] = float(table[arm.decode()][int(idx)])
        verdict = "tie" if side_scores["A"] == side_scores["B"] else max(side_scores, key=side_scores.get)
        return json.dumps({"verdict": verdict, "notes": "mock notes",
                           "scores": {s: [v] * n for s, v in side_scores.items()}})
    answers = dict(re.findall(r"=== ANSWER ([AB]) ===\n(.*?)(?=\n\n=== ANSWER|\n\nPick the better)", prompt, re.S))
    n = len(re.findall(r"^\d+\. ", prompt, re.M))
    mode = os.environ.get("EVAL_MOCK_JUDGE", "prefer_with")
    table = json.loads(os.environ.get("EVAL_MOCK_SAMPLE_VERDICTS") or "{}")
    found = re.search(r"answer for ([\w-]+) \[s(\d+)\]", " ".join(a for a in answers.values() if a))
    if found and found[1] in table:
        mode = table[found[1]][int(found[2])]
        mode = {"with": "prefer_with", "without": "prefer_without"}.get(mode, mode)
    if mode == "always_a":
        verdict = "A"
    elif mode == "tie":
        verdict = "tie"
    else:
        want = "SKILLED" if mode == "prefer_with" else "PLAIN"
        verdict = next((s for s, text in answers.items() if want in text), "tie")
    good, bad = [4] * n, [2] * n
    scores = {"A": good if verdict == "A" else bad if verdict == "B" else [3] * n,
              "B": good if verdict == "B" else bad if verdict == "A" else [3] * n}
    return "Here is my verdict:\n" + json.dumps({"verdict": verdict, "notes": "mock notes", "scores": scores})


def main():
    role = sys.argv[1]
    if role == "render":
        found = re.search(r"(?:SKILLED|PLAIN) [\w-]+/(with|without)/(\d+)", open(sys.argv[2], encoding="utf-8").read())
        with open(sys.argv[3], "wb") as f:
            f.write(png(marker=f"{found[1]}:{found[2]}".encode() if found else b""))
        return
    req = json.load(sys.stdin)
    sys.stdout.write(generate(req) if role == "generate" else judge(req))


if __name__ == "__main__":
    main()
