import unittest

from helpers import TempRoot, load_script, tiny_png

mod = load_script("pngstamp")


def chunk_kinds(data):
    return [kind for kind, _, _ in mod._chunks(data)]


class PngStampTest(unittest.TestCase):
    def setUp(self):
        self.t = TempRoot().__enter__()
        self.addCleanup(self.t.__exit__, None, None, None)
        self.png = self.t.root / "a.png"
        self.png.write_bytes(tiny_png())

    def test_stamp_round_trips_and_keeps_every_other_chunk(self):
        before = self.png.read_bytes()
        self.assertIsNone(mod.read_stamp(self.png))
        mod.stamp(self.png, "ab" * 32)
        self.assertEqual(mod.read_stamp(self.png), "ab" * 32)
        after = self.png.read_bytes()
        self.assertEqual(chunk_kinds(after), [b"IHDR", b"tEXt", b"IDAT", b"IEND"])
        self.assertEqual([c for c in mod._chunks(after) if c[0] != b"tEXt"], list(mod._chunks(before)))

    def test_a_second_stamp_replaces_the_first(self):
        mod.stamp(self.png, "ab" * 32)
        mod.stamp(self.png, "cd" * 32)
        self.assertEqual(mod.read_stamp(self.png), "cd" * 32)
        self.assertEqual(chunk_kinds(self.png.read_bytes()).count(b"tEXt"), 1)

    def test_digest_covers_local_files_the_source_loads_but_not_urls(self):
        self.t.write("shots/x.png", "one")
        text = '<img src="shots/x.png"><img src="https://example.com/y.png">'
        first = mod.source_digest(text, self.t.root)
        self.assertEqual(first, mod.source_digest(text, self.t.root))
        self.t.write("shots/x.png", "two")
        self.assertNotEqual(first, mod.source_digest(text, self.t.root))

    def test_stale_names_the_reason(self):
        text = "<svg/>"
        self.assertEqual(mod.stale(self.t.root / "missing.png", text, self.t.root), "missing")
        self.assertEqual(mod.stale(self.png, text, self.t.root), "has no source stamp")
        mod.stamp(self.png, mod.source_digest("<svg>old</svg>", self.t.root))
        self.assertEqual(mod.stale(self.png, text, self.t.root), "was rendered from a different source")
        mod.stamp(self.png, mod.source_digest(text, self.t.root))
        self.assertIsNone(mod.stale(self.png, text, self.t.root))

    def test_a_file_that_is_not_a_png_has_no_stamp(self):
        self.t.write("b.png", "not a png")
        self.assertIsNone(mod.read_stamp(self.t.root / "b.png"))


if __name__ == "__main__":
    unittest.main()
