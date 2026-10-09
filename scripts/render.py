#!/usr/bin/env python3
"""Render a local HTML file to a PNG with headless Chrome.

Rendering is offline: every non-local host name is blocked, so remote fonts,
scripts and images never load. Generated pages must use system fonts or
open-licensed fonts shipped next to the page (referenced by relative path).
"""
import argparse
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path

CHROME = os.environ.get("CHROME_BIN", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


class RenderError(RuntimeError):
    pass


def chrome_args(url, out, width, height, profile):
    return [
        CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
        "--no-default-browser-check", "--disable-extensions", "--disable-background-networking",
        "--force-device-scale-factor=1", "--font-render-hinting=none", "--disable-lcd-text",
        "--run-all-compositor-stages-before-draw", "--virtual-time-budget=3000",
        "--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE localhost",
        f"--window-size={width},{height}", f"--user-data-dir={profile}",
        f"--screenshot={out}", url,
    ]


def wait_for_screenshot(proc, out, timeout):
    """Chrome often lingers after writing the screenshot, so stop once the file is complete and stable."""
    deadline, last = time.monotonic() + timeout, -1
    while time.monotonic() < deadline:
        size = out.stat().st_size if out.is_file() else -1
        if size > 0 and size == last and out.read_bytes().startswith(PNG_MAGIC):
            return
        if proc.poll() is not None:
            return
        last = size
        time.sleep(0.3)


def render(html, out, width=1280, height=800, timeout=60):
    html, out = Path(html).resolve(), Path(out).resolve()
    if not html.is_file():
        raise RenderError(f"{html} does not exist")
    if not Path(CHROME).exists():
        raise RenderError(f"Chrome not found at {CHROME} (set CHROME_BIN)")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.unlink(missing_ok=True)
    profile = tempfile.mkdtemp(prefix="render-profile-")
    proc = subprocess.Popen(chrome_args(html.as_uri(), out, width, height, profile),
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                            stdin=subprocess.DEVNULL, start_new_session=True)
    try:
        wait_for_screenshot(proc, out, timeout)
    finally:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            # macOS refuses killpg once the group leader has exited and is only a zombie; kill what is left directly.
            try:
                proc.kill()
            except (ProcessLookupError, PermissionError):
                pass
        proc.wait()
        shutil.rmtree(profile, ignore_errors=True)
    if not out.is_file() or not out.read_bytes().startswith(PNG_MAGIC):
        raise RenderError(f"no screenshot produced for {html} within {timeout}s")
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("html")
    p.add_argument("out")
    p.add_argument("--width", type=int, default=1280)
    p.add_argument("--height", type=int, default=800)
    p.add_argument("--timeout", type=int, default=60)
    args = p.parse_args(argv)
    try:
        render(args.html, args.out, args.width, args.height, args.timeout)
    except RenderError as e:
        print(f"render failed: {e}", file=sys.stderr)
        return 1
    print(args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
