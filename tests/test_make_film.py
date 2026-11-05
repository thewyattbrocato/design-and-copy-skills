import re
import tempfile
import unittest
from pathlib import Path

from helpers import load_script, tiny_png

ROOT = Path(__file__).resolve().parent.parent
film = load_script("make_film")
results_table = load_script("results_table")


class FilmTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = film.gather(ROOT)
        cls.scenes = film.build_scenes(cls.data)

    def test_record_matches_the_readme_headline(self):
        r = self.data["record"]
        headline = results_table.headline_lines(ROOT)[0]
        for part in (f"Across {r['skills']} skills", f"({r['tasks']} in all)", f"{r['wins']} wins, {r['losses']} losses and {r['ties']} ties",
                     f"{r['marginal']} of the {r['skills']} passes are marginal"):
            self.assertIn(part, headline)

    def test_length_is_between_sixty_and_ninety_seconds(self):
        self.assertGreaterEqual(film.total_seconds(self.scenes), 60)
        self.assertLessEqual(film.total_seconds(self.scenes), 90)

    def test_captions_are_ordered_and_inside_their_scene(self):
        for scene in self.scenes:
            starts = [s for s, _ in scene["captions"]]
            self.assertEqual(starts, sorted(starts))
            self.assertEqual(starts[0], 0.0)
            self.assertLess(starts[-1], scene["dur"])

    def test_every_move_has_a_saved_pair_and_a_real_tally(self):
        self.assertEqual(len(self.data["moves"]), 6)
        for m in self.data["moves"]:
            self.assertTrue(Path(m["run"]).is_dir())
            self.assertRegex(m["tally"], r"^\d+ wins?, \d+ loss(es)?, \d+ ties?$")
            self.assertIn("with", m["scores"])

    def test_frames_build_without_a_browser(self):
        for scene in self.scenes:
            for t in (0.0, scene["dur"] - 0.04):
                doc = film.frame_html(scene, t, self.data)
                self.assertIn("class='cap'", doc)

    def test_rle_collapses_held_frames(self):
        self.assertEqual(film.rle(["a", "a", "b", "a"]), [("a", 2), ("b", 1), ("a", 1)])

    def test_slide_titles_read_both_answer_styles(self):
        self.assertEqual(film.slide_titles('1. **"One"** (~1 min)\n   - x'), [(1, '"One"')])
        self.assertEqual(film.slide_titles("**2. Two things**\n- y"), [(2, "Two things")])

    def test_shorten_marks_a_cut(self):
        self.assertEqual(film.shorten("short text", 50), "short text")
        self.assertTrue(film.shorten("word " * 40, 30).endswith("[…]"))

    def test_quoted_caption_phrases_are_verbatim_from_the_saved_task_or_answers(self):
        for scene in self.scenes:
            if "move" not in scene:
                continue
            m = scene["move"]
            saved = m["prompt"] + "".join(f.read_text(encoding="utf-8") for f in Path(m["run"]).glob("*.md"))
            for _, cap in scene["captions"]:
                for phrase in re.findall("\u201c([^\u201d]+)\u201d", cap):
                    self.assertIn(phrase, saved, f"{m['id']}: {phrase!r} is not in the saved prompt or answers")

    def test_digest_is_the_same_in_any_checkout_and_follows_the_screenshots(self):
        digest = film.film_digest(ROOT, self.data, self.scenes)
        self.assertRegex(digest, r"^[0-9a-f]{64}$")
        self.assertEqual(digest, film.film_digest(ROOT, self.data, self.scenes))
        prefix = ROOT.resolve().as_uri() + "/"
        pages = [doc for doc, _ in film.frame_plan(self.scenes, self.data)]
        self.assertTrue(any(prefix in doc for doc in pages), "frames load saved screenshots by file URI")

    def test_stale_media_names_each_file_without_the_digest(self):
        pngstamp = load_script("pngstamp")
        with tempfile.TemporaryDirectory() as tmp:
            mp4, poster, still = film.media_paths(tmp)
            self.assertEqual(film.stale_media(tmp, "a" * 64), [mp4.name, poster.name, still.name])
            mp4.parent.mkdir(parents=True)
            mp4.write_bytes(b"....moov....comment source-sha256:" + b"a" * 64 + b"....")
            for png in (poster, still):
                png.write_bytes(tiny_png())
                pngstamp.stamp(png, "a" * 64)
            self.assertEqual(film.stale_media(tmp, "a" * 64), [])
            self.assertEqual(film.stale_media(tmp, "b" * 64), [mp4.name, poster.name, still.name])

    def test_committed_film_poster_and_still_carry_the_current_digest(self):
        self.assertEqual(film.stale_media(ROOT, film.film_digest(ROOT, self.data, self.scenes)), [])

    def test_transcript_is_current_and_lists_every_caption(self):
        text = film.transcript(self.data, self.scenes)
        for scene in self.scenes:
            for _, cap in scene["captions"]:
                self.assertIn(cap, text)
        self.assertEqual((ROOT / "docs" / "launch" / "skills-at-work.md").read_text(encoding="utf-8"), text)


if __name__ == "__main__":
    unittest.main()
