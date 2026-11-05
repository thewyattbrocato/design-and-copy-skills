# Plan: one source, three published versions

Fixes need to land once and reach all three guides. That means one set of source files with version-specific bits marked inline. A build then produces the v6, v7 and v8 guides from it. The alternatives (a "sync fixes" checklist, or versioning tools that snapshot copies) just recreate the problem.

I don't know your current format or toolchain, so the tool choice in step 2 is my assumption.

## Step 1: Measure the differences (about 1 day)
Diff v8 against v7, and v7 against v6, page by page. Sort every page into one of three groups:
- **Identical:** merge immediately.
- **Small differences:** a few steps, a menu name, a path, a flag. These become inline conditionals.
- **Mostly different:** for example, a rewritten install flow. These stay as separate per-version files.

This tells you how big the job is. In most docs sets like this, the large majority of pages are identical or nearly so.

## Step 2: Pick the tooling (about 1 day)
Requirements: the source lives in git as plain text, supports conditional content, and can build a filtered output per version.
- **Markdown today:** MkDocs with the `macros` plugin, or Docusaurus or Hugo with a build-time filter. Mark blocks like `{% if version >= 7 %}…{% endif %}`.
- **AsciiDoc or reStructuredText:** use `ifdef` (Antora or Asciidoctor) or `only` (Sphinx). Both have this built in.
- **Word or Confluence:** move to Markdown first. Conditional content isn't realistic there.

Choose whatever is closest to what you use now. The tool matters less than the single source.

## Step 3: Merge (about 1–2 weeks for two people)
1. Put the docs in one git repo if they aren't already. One of you owns the repo setup and the other starts the merge.
2. Use v8 as the base. Fold in v7, then v6, using your step 1 sorting.
3. Move values that change between versions into one variables file: product name, default ports, paths, UI labels, and version numbers. This removes many of the conditionals.
4. Wrap the remaining differences in conditionals. Keep them at block level (a step, a note, a table row). Don't put them mid-sentence, because those are hard to read and review.
5. For mostly-different pages, keep per-version files (`install-v6.md`, `install-v8.md`) and include the right one per build.
6. Build all three outputs and diff each against the original copy. Any differences left should be intentional, and typos fixed along the way count as intentional.
7. Split the work by section so you don't collide. One of you takes the first half of the pages and the other takes the second half.

## Step 4: Add guardrails (about 2 days)
- **CI:** build all three versions on every pull request. Fail on broken links, unclosed conditionals, and undefined variables.
- **PR template:** one question, "Does this apply to all versions? If not, which?" This puts the decision in front of the author when they make the change.
- **Preview links:** have the PR build publish all three outputs. Reviewing a v6-only change then takes seconds.
- **Retire the old copies:** make them read-only or delete them the day you cut over. If they stay editable, someone will edit them.

## Step 5: Ongoing rules
- **Fixes:** edit the shared text. If the fix is version-specific, put it in a conditional.
- **New version (v9):** add it to the version list, then review only the conditionals and the mostly-different pages.
- **End of life:** when a version is dropped, delete its conditionals and per-version files. Do this on a schedule, for example once per release. Otherwise the conditionals pile up.
- **Conditional budget:** if a page has more than about five conditionals, split it into per-version files. That's easier to read than heavy conditionals.

## Timeline and risks
Expect roughly 2–3 weeks to cut over, with both of you part-time. The main risk is a merge that quietly drops a real version difference. The step 3 diff of each build against its original guards against that, so don't skip it. The second risk is old copies staying editable, which step 4 covers.

If you tell me your current format and where the docs live, I can turn this into a concrete tool choice and a repo layout. If the files are in this directory, I can run the step 1 diff and report how much actually differs.
