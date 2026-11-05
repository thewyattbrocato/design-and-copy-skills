import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+\.(?:png|svg|gif|jpe?g))\)|<img [^>]*src=\"([^\"]+)\"[^>]*alt=\"([^\"]*)\"")
MEDIA = re.compile(r"\((docs/[^)\s]+\.(?:mp4|gif|png|svg|jpe?g))\)")


def readme_images():
    """[(path, alt)] for every image the README shows."""
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    out = []
    for m in IMAGE.finditer(text):
        out.append((m.group(2), m.group(1)) if m.group(2) else (m.group(3), m.group(4)))
    return out


class AltTextTest(unittest.TestCase):
    def test_every_readme_image_has_real_alt_text_and_an_alt_md_row(self):
        alt_md = (ROOT / "docs" / "img" / "ALT.md").read_text(encoding="utf-8")
        images = readme_images()
        self.assertGreater(len(images), 10)
        for path, alt in images:
            self.assertGreaterEqual(len(alt.split()), 8, f"{path}: alt text {alt!r} is too short to describe it")
            self.assertIn(f"`{path}`", alt_md, f"{path} has no row in docs/img/ALT.md")

    def test_every_media_file_the_readme_links_exists(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for path in sorted(set(MEDIA.findall(text))):
            self.assertTrue((ROOT / path).is_file(), f"README links {path}, which is not in the repo")

    def test_alt_md_rows_name_files_that_exist(self):
        alt_md = (ROOT / "docs" / "img" / "ALT.md").read_text(encoding="utf-8")
        for path in re.findall(r"^\| `([^`]+)`", alt_md, re.M):
            self.assertTrue((ROOT / path).is_file(), f"docs/img/ALT.md has a row for {path}, which is not in the repo")


if __name__ == "__main__":
    unittest.main()
