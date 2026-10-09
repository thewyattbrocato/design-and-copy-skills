import unittest

from helpers import TempRoot, load_script, run_main

mod = load_script("check_links")


class CheckLinksTest(unittest.TestCase):
    def test_valid_links_pass(self):
        with TempRoot() as t:
            t.write("README.md", "[docs](docs/a.md) ![img](docs/pic.png) [web](https://example.com) [top](#top)\n")
            t.write("docs/a.md", "[back](../README.md#intro)\n")
            t.write("docs/pic.png", "x")
            code, out = run_main(mod, t.root)
            self.assertEqual(code, 0, out)

    def test_broken_link_and_image_fail(self):
        with TempRoot() as t:
            t.write("README.md", "[a](nope.md)\n\n![b](img/missing.png)\n")
            code, out = run_main(mod, t.root)
            self.assertEqual(code, 1)
            self.assertIn("README.md:1: broken link: nope.md", out)
            self.assertIn("README.md:3: broken link: img/missing.png", out)

    def test_skills_are_scanned(self):
        with TempRoot() as t:
            t.write("skills/x/SKILL.md", "[bad](references/none.md)\n")
            self.assertEqual(run_main(mod, t.root)[0], 1)

    def test_copy_skills_are_scanned(self):
        with TempRoot() as t:
            t.write("copy-skills/x/SKILL.md", "[bad](references/none.md)\n")
            self.assertEqual(run_main(mod, t.root)[0], 1)
            t.write("copy-skills/x/SKILL.md", "[ok](../README.md)\n")
            t.write("copy-skills/README.md", "# Copy\n")
            self.assertEqual(run_main(mod, t.root)[0], 0)

    def test_withdrawn_skills_are_scanned(self):
        with TempRoot() as t:
            t.write("withdrawn/x/SKILL.md", "[bad](references/none.md)\n")
            self.assertEqual(run_main(mod, t.root)[0], 1)

    def test_top_level_and_evals_docs_are_scanned_but_run_folders_are_not(self):
        with TempRoot() as t:
            t.write("CONTRIBUTING.md", "[bad](nope.md)\n")
            t.write("evals/README.md", "[bad](SCHEMA.md)\n")
            t.write("evals/demo/runs/t1/with.md", "[ignored](missing.md)\n")
            code, out = run_main(mod, t.root)
            self.assertEqual(code, 1)
            self.assertIn("CONTRIBUTING.md:1: broken link: nope.md", out)
            self.assertIn("evals/README.md:1: broken link: SCHEMA.md", out)
            self.assertNotIn("runs/t1", out)

    def test_links_in_code_are_ignored(self):
        with TempRoot() as t:
            t.write("README.md", "`[a](nope.md)`\n\n```\n[b](nope.md)\n```\n")
            self.assertEqual(run_main(mod, t.root)[0], 0)

    def test_empty_repo_passes(self):
        with TempRoot() as t:
            self.assertEqual(run_main(mod, t.root)[0], 0)


if __name__ == "__main__":
    unittest.main()
