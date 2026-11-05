# Plan: one source, three builds

**Core change:** stop keeping three guides. Keep one set of source files with version-conditional sections, and build the v6, v7 and v8 guides from it. A typo fix then happens once and shows up in all three.

I haven't seen your files, so I'm assuming the guides are text-based (Markdown, AsciiDoc, RST) and not Word or Confluence pages. If they aren't, the first step is to convert them.

## Week 1: Measure the real differences

1. Put all three copies in one git repo if they aren't already. Everything below depends on version control.
2. Diff v6 against v7 and v7 against v8, chapter by chapter.
3. Sort every difference into one of three groups:
   - **Accidental drift:** typos and fixes that only landed in one copy. Fix these once, using the best wording.
   - **Small real differences:** a renamed setting, a different path, one extra step.
   - **Large real differences:** a whole feature that exists only in v8, or a redone install flow.

The mix of these groups decides how much conditional logic you need. In most cases drift is the biggest group. That's good news, because it means the merge is mostly deleting duplicates.

## Week 2: Pick tooling and merge

**Tooling.** Stay in your current format and add a build step that supports conditionals and variables. Some common choices:
- **MkDocs Material with `mkdocs-macros`:** lightest option if you're on Markdown. It uses `{% if version >= 7 %}…{% endif %}`.
- **Sphinx:** has an `only` directive and good multi-version support if you're on RST.
- **AsciiDoc/Antora:** has attributes and includes built in if you're on AsciiDoc.

Avoid Docusaurus-style versioning. It snapshots a full copy per version, which is the problem you have now.

**Merge.**
1. Use v8 as the base, since it's the most complete.
2. Fold v7 and v6 in with three tools:
   - **Variables** for things like product name, default paths, port numbers and CLI command names (`{{ cfg_path }}`).
   - **Inline conditionals** for single steps or sentences that differ.
   - **Separate files with shared includes** for chapters that are mostly different. Don't contort one file with a dozen conditionals. If a section needs more than about three, split it.
3. Set a rule so the conditionals stay readable: each conditional block gets a one-line comment saying why it differs, such as `<!-- v6 only: legacy installer -->`.

## Week 3: Build, check and cut over

1. Add a CI job that builds all three outputs on every pull request.
2. Add checks that fail the build on broken links, unresolved variables, and any leftover conditional markers in the output.
3. Spot-check each chapter in all three outputs against the old copies. For 6 and 7 you can diff the rendered text against the old versions. The only differences should be fixes you meant to make.
4. Publish the three builds at the same URLs as before. Archive the old copies read-only, then delete them after a release cycle.

## Ongoing workflow for two writers

- **One place to edit.** Every fix is a pull request against the single source. Reviewer checks: does this apply to all versions, and if not, is it wrapped in a conditional?
- **PR template question:** "Which versions does this affect?" It takes ten seconds and catches most mistakes.
- **Preview builds:** CI posts all three rendered outputs, so the reviewer can see v6 and v8 side by side.
- **New release (v9):** add the version to the build config and write only the new conditionals. When v6 reaches end of support, delete its conditionals and drop it from the build.
- **Ownership:** you each take half the chapters for the merge, then rotate who reviews.

## Risks

- **Over-conditionalizing:** if a page is unreadable in source, split it into separate files.
- **Silent wrong-version content:** the CI checks and side-by-side previews guard against this. Don't skip them.
- **Engineers editing the old copies:** announce the cutover date and make the old copies read-only the same day.

## Effort

For two people this is roughly 2–3 weeks part-time, depending on how much real divergence the diff shows. The payoff comes immediately after cutover, when each fix is one edit.

If you tell me the current format and where the files live, I can write the diff script for week 1 and draft the build config.
