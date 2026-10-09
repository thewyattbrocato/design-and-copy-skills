import unittest

from helpers import TempRoot, load_script, run_main, skill_md

mod = load_script("validate_skills")


class ValidateSkillsTest(unittest.TestCase):
    def run_root(self, t):
        return run_main(mod, t.root)

    def test_empty_skills_dir_passes(self):
        with TempRoot() as t:
            t.write("skills/.gitkeep", "")
            self.assertEqual(self.run_root(t)[0], 0)

    def test_missing_skills_dir_passes(self):
        with TempRoot() as t:
            self.assertEqual(self.run_root(t)[0], 0)

    def test_valid_skill_passes(self):
        with TempRoot() as t:
            body = "# Demo\n\nSee [spacing](references/spacing.md).\n\n## When Not To Use\n\nNo.\n"
            t.write("skills/demo/SKILL.md", skill_md(body=body))
            t.write("skills/demo/references/spacing.md", "# Spacing\n\nBack to [skill](../SKILL.md).\n")
            code, out = self.run_root(t)
            self.assertEqual(code, 0, out)

    def test_withdrawn_skill_is_validated_and_counted_separately(self):
        with TempRoot() as t:
            t.write("withdrawn/demo/SKILL.md", skill_md(body="# Demo\n\n## When Not To Use\n\nNo.\n"))
            code, out = self.run_root(t)
            self.assertEqual(code, 0, out)
            self.assertIn("validated 0 skills and 1 withdrawn", out)
            t.write("withdrawn/demo/SKILL.md", "no frontmatter\n")
            code, out = self.run_root(t)
            self.assertEqual(code, 1)
            self.assertIn("withdrawn/demo:", out)

    def test_copy_skill_is_validated_and_counted(self):
        with TempRoot() as t:
            t.write("copy-skills/draft/SKILL.md", skill_md("draft"))
            code, out = self.run_root(t)
            self.assertEqual(code, 0, out)
            self.assertIn("validated 0 skills and 1 copy", out)
            t.write("copy-skills/draft/SKILL.md", "no frontmatter\n")
            code, out = self.run_root(t)
            self.assertEqual(code, 1)
            self.assertIn("copy-skills/draft:", out)

    def test_empty_copy_skills_dir_passes(self):
        with TempRoot() as t:
            t.write("copy-skills/README.md", "# Copy\n")
            t.write("skills/demo/SKILL.md", skill_md())
            code, out = self.run_root(t)
            self.assertEqual(code, 0, out)
            self.assertIn("validated 1 skills, 0 problems", out)

    def test_same_name_in_two_roots_fails(self):
        with TempRoot() as t:
            t.write("skills/demo/SKILL.md", skill_md())
            t.write("copy-skills/demo/SKILL.md", skill_md())
            code, out = self.run_root(t)
            self.assertEqual(code, 1)
            self.assertIn("copy-skills/demo: skill name 'demo' is already used by skills/demo", out)
            t.write("copy-skills/demo/SKILL.md", skill_md("other"))
            code, out = self.run_root(t)
            self.assertEqual(code, 1)
            self.assertIn("name 'other' does not match directory 'demo'", out)

    def test_name_must_match_directory_in_every_root(self):
        for sub in ("skills", "copy-skills", "withdrawn"):
            with TempRoot() as t:
                t.write(f"{sub}/folder/SKILL.md", skill_md("different"))
                code, out = self.run_root(t)
                self.assertEqual(code, 1, sub)
                self.assertIn(f"{sub}/folder: name 'different' does not match directory 'folder'", out)

    def test_folded_description_passes(self):
        with TempRoot() as t:
            t.write("skills/demo/SKILL.md",
                    "---\nname: demo\ndescription: >\n  First part\n  second part.\n---\n# D\n## When not to use\n")
            code, out = self.run_root(t)
            self.assertEqual(code, 0, out)

    def test_missing_section_fails(self):
        with TempRoot() as t:
            t.write("skills/demo/SKILL.md", skill_md(body="# Demo\n\nText.\n"))
            code, out = self.run_root(t)
            self.assertEqual(code, 1)
            self.assertIn("When not to use", out)

    def test_bad_link_fails(self):
        with TempRoot() as t:
            t.write("skills/demo/SKILL.md",
                    skill_md(body="# Demo\n\n[x](references/nope.md)\n\n## When not to use\n"))
            code, out = self.run_root(t)
            self.assertEqual(code, 1)
            self.assertIn("broken link: references/nope.md", out)

    def test_name_mismatch_fails(self):
        with TempRoot() as t:
            t.write("skills/demo/SKILL.md", skill_md(name="other"))
            code, out = self.run_root(t)
            self.assertEqual(code, 1)
            self.assertIn("does not match directory", out)

    def test_non_kebab_and_long_name_fail(self):
        with TempRoot() as t:
            t.write("skills/Bad_Name/SKILL.md", skill_md(name="Bad_Name"))
            long = "a" * 65
            t.write(f"skills/{long}/SKILL.md", skill_md(name=long))
            code, out = self.run_root(t)
            self.assertEqual(code, 1)
            self.assertIn("not kebab-case", out)
            self.assertIn("max 64", out)

    def test_description_problems_fail(self):
        with TempRoot() as t:
            t.write("skills/empty/SKILL.md", skill_md(name="empty", description=""))
            t.write("skills/long/SKILL.md", skill_md(name="long", description="x" * 1025))
            code, out = self.run_root(t)
            self.assertEqual(code, 1)
            self.assertIn("'description' is missing or empty", out)
            self.assertIn("max 1024", out)

    def test_body_over_500_lines_fails(self):
        with TempRoot() as t:
            body = "# Demo\n## When not to use\n" + "line\n" * 500
            t.write("skills/demo/SKILL.md", skill_md(body=body))
            code, out = self.run_root(t)
            self.assertEqual(code, 1)
            self.assertIn("max 500", out)

    def test_unlinked_reference_fails(self):
        with TempRoot() as t:
            t.write("skills/demo/SKILL.md", skill_md())
            t.write("skills/demo/references/orphan.md", "# Orphan\n")
            code, out = self.run_root(t)
            self.assertEqual(code, 1)
            self.assertIn("references/orphan.md is not linked", out)

    def test_broken_link_in_reference_fails(self):
        with TempRoot() as t:
            body = "# D\n[r](references/a.md)\n## When not to use\n"
            t.write("skills/demo/SKILL.md", skill_md(body=body))
            t.write("skills/demo/references/a.md", "[gone](missing.md)\n")
            code, out = self.run_root(t)
            self.assertEqual(code, 1)
            self.assertIn("references/a.md:1: broken link: missing.md", out)

    def test_missing_frontmatter_fails(self):
        with TempRoot() as t:
            t.write("skills/demo/SKILL.md", "# Demo\n## When not to use\n")
            self.assertEqual(self.run_root(t)[0], 1)

    def test_missing_skill_md_fails(self):
        with TempRoot() as t:
            t.write("skills/demo/notes.md", "x")
            self.assertEqual(self.run_root(t)[0], 1)


if __name__ == "__main__":
    unittest.main()
