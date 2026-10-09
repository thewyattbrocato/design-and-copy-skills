import tempfile
import unittest
from pathlib import Path
from unittest import mock

from helpers import load_script

render = load_script("render")
PAGE = """<!doctype html><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter">
<body style="margin:0;background:#123;color:#fff;font:40px system-ui">Offline render</body>"""


class RenderArgsTest(unittest.TestCase):
    def test_chrome_args_block_the_network_and_fix_the_scale(self):
        args = render.chrome_args("file:///x.html", "/o.png", 1280, 800, "/prof")
        self.assertIn("--force-device-scale-factor=1", args)
        self.assertIn("--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE localhost", args)
        self.assertIn("--window-size=1280,800", args)
        self.assertIn("--headless=new", args)

    def test_missing_input_is_an_error(self):
        with self.assertRaises(render.RenderError):
            render.render("/nonexistent/page.html", "/tmp/never.png")


@unittest.skipUnless(Path(render.CHROME).exists(), "Chrome is not installed")
class RenderChromeTest(unittest.TestCase):
    def test_renders_deterministically_without_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            html = Path(tmp) / "p.html"
            html.write_text(PAGE, encoding="utf-8")
            a, b = Path(tmp) / "a.png", Path(tmp) / "b.png"
            render.render(html, a, 640, 400, timeout=40)
            render.render(html, b, 640, 400, timeout=40)
            self.assertTrue(a.read_bytes().startswith(render.PNG_MAGIC))
            self.assertEqual(a.read_bytes(), b.read_bytes())

    def test_survives_killpg_refusing_on_an_exited_group_leader(self):
        with tempfile.TemporaryDirectory() as tmp:
            html = Path(tmp) / "p.html"
            html.write_text(PAGE, encoding="utf-8")
            with mock.patch.object(render.os, "killpg", side_effect=PermissionError):
                render.render(html, Path(tmp) / "a.png", 640, 400, timeout=40)
            self.assertTrue((Path(tmp) / "a.png").read_bytes().startswith(render.PNG_MAGIC))


if __name__ == "__main__":
    unittest.main()
