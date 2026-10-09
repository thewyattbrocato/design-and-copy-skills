"""Shared fixtures for the script tests."""
import contextlib
import importlib.util
import io
import sys
import tempfile
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
# Put scripts/ on the path at import time so a test module can import evalkit directly,
# whichever test file the runner happens to load first.
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_main(mod, root):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = mod.main(["--root", str(root)])
    return code, out.getvalue()


class TempRoot:
    def __enter__(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        return self

    def __exit__(self, *exc):
        self._tmp.cleanup()

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path


def skill_md(name="demo", description="Does a thing.", body="# Demo\n\n## When not to use\n\nNever.\n"):
    return f"---\nname: {name}\ndescription: {description}\n---\n\n{body}"
