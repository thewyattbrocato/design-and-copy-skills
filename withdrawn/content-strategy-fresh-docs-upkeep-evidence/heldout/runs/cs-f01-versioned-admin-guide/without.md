# Plan: one source, three published versions

I haven't seen your files, so this assumes the guides are Markdown, AsciiDoc or reStructuredText in a repo or folder. If they're in Word, Confluence or Google Docs, step 1 changes and the rest still holds.

## Recommendation

Keep one set of source files and generate the v6, v7 and v8 guides from it. Text that's the same in all versions is written once. Text that differs is marked with a version condition inside the file. I don't recommend a branch per version with cherry-picks. With two writers, cherry-picking is the same "fix it three times" problem, just in git.

## Step 1: Measure the drift (about half a day)

Before you build anything, find out how different the copies really are:

```
diff -rq guide-v6 guide-v7
diff -rq guide-v7 guide-v8
diff -u guide-v7/install.md guide-v8/install.md | diffstat
```

Sort every file into one of three buckets:
- **Identical across versions.** These merge immediately and are probably most of the guide.
- **Differ by small, specific things.** Examples are a flag name, a menu path, a version number or a screenshot.
- **Substantively different.** These are sections about features that exist in only one or two versions, or that were rewritten.

Put the results in a spreadsheet with one row per file. This also tells you how big the job is.

## Step 2: Choose the tooling (1 day)

Pick one of these:
- **MkDocs with Material and the `mike` plugin, or Docusaurus.** Both are good for Markdown and have built-in version switchers. Use `{% if %}` macros (mkdocs-macros) or MDX components for conditional text.
- **Sphinx** has the `only` directive and `ifconfig`. It's mature and strong on cross-references.
- **AsciiDoc/Antora** has `ifdef` and is built for multi-version docs.

If you already use one of these, stay with it. If you're starting fresh, I'd pick MkDocs + macros for two people. It has the smallest learning curve.

## Step 3: Build the shared base (1–2 weeks)

1. Take **v8 as the base**, since it's the newest and probably the most complete. Move it to a single `docs/` tree.
2. Merge the identical files first. Delete the v6 and v7 copies of those files and check that all three builds still render.
3. For small differences, use inline conditions. For example:
   ```
   {% if version >= 7 %}Run `quill migrate --online`.{% else %}Stop the service, then run `quill migrate`.{% endif %}
   ```
4. For substantively different sections, make separate files such as `upgrade-v6.md` and `upgrade-v8.md`, and include the right one by version. Don't force a conditional that nobody can read.
5. Move version numbers, product names and paths into variables (`{{ latest }}`, `{{ data_dir }}`) so that changing one never means editing prose.
6. Set up the build to produce three outputs, one for each version.

Do the files in order of how often they get edited and how many readers they have: install, upgrade, configuration, backup and restore, then everything else. You can ship partial progress, because files already merged are protected and the rest stay as they are.

## Step 4: Add guardrails (1–2 days)

- **CI build for all three versions on every change.** A broken conditional fails the build and doesn't reach a reader.
- **Link checker** run against each version's output.
- **Pull request template** with a checkbox: "Which versions does this change apply to?" It makes the writer decide each time, and that was the missing step in your current process.
- **Rule for conditionals:** if a file has more than about 3 or 4 conditional blocks, split it into per-version files. Otherwise the shared source gets hard to read.

## Step 5: Set the editing rules for the two of you

- Fixes go in the shared source by default. Writing version-specific text is the exception, and the PR checkbox is where you flag it.
- When a v9 comes, you add `9` to the build list and put conditions in only where it differs from v8.
- When v6 reaches end of support, remove the `version == 6` branches and drop it from the build list. Retiring a version becomes a small cleanup.

## Step 6: Cut over

1. Run the new three-version build in parallel with the old copies for one release cycle. Diff the old v6, v7 and v8 HTML or PDF against the new output. Any difference should be an intentional fix, such as a typo that was already wrong in two copies.
2. Archive the three old folders as read-only and publish from the new build.

## Rough timeline

| Step | Effort |
|---|---|
| Audit | 0.5 day |
| Tooling choice and prototype | 1 day |
| Merge, in priority order | 1–2 weeks alongside normal work |
| CI and templates | 1–2 days |
| Parallel run and cutover | 1 release cycle |

## Two things that would change the plan

- **If the three guides are mostly substantively different**, which the audit will show, then single-sourcing saves less. In that case merge only the stable shared chapters, like backup and security, and leave the rest separate.
- **If the guides are in a wiki or Word**, step 1 includes an export to Markdown or AsciiDoc first (pandoc handles most of it), which adds a few days.

If you tell me the current format and where the files live, I can run the audit diff for you and give you the bucket counts. That would make the estimate real.
