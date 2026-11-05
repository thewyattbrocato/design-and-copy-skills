**Decision:** fix and own. Three full copies means every fix has to be made three times, and nobody is responsible for making sure it is. The change is to move to a single source with the version differences marked inline, plus one rule that a fix isn't done until it's checked against all three versions.

## The plan

**1. Merge to one source (weeks 1–3)**
- Pick the version where the guide is in best shape. Probably 8, but you know better than I do. Make it the base.
- Diff 6 and 7 against it, one chapter at a time. Most of the text should be identical. Only the lines that differ get a version marker. The tool is your call. Any docs-as-code setup with conditional blocks or version tags works. If you already have a docs toolchain, use whatever it has.
- Every difference ends up as a tagged block, for example "6–7 only" or "8+". This means each option, step or screen states which release added it or removed it.
- While you diff, fix the typos and wrong steps you find. Log each fix you make. That log is your first record of how far the copies have drifted.
- Publish one page per topic with a version selector. Don't retire the old three copies until the merged output looks right. Then redirect them.

**2. Split the work between the two of you (week 1, one conversation)**

| Item | Owner |
|---|---|
| Chapters A–M (decide the split) | Writer 1 |
| Chapters N–Z | Writer 2 |
| Version policy and tagging conventions | Writer 1 for now, swap later |

Each chapter has one named owner with the right to say no to a change. Put the owner on the page itself.

**3. A short version policy (week 2, one page)**
- Which versions get their own tagged content: 6, 7 and 8.
- What a reader sees when a feature doesn't exist in their version: the release that added it.
- When a version retires and where its readers go. `[version 6 end-of-support date]`: you need to supply this.

**4. Make docs part of done (starts now)**
- A product change isn't finished until its doc change ships with it. Ask engineering to add this to their definition of done.
- Before a changed value, limit, name or step ships, the writer lists every page, screenshot and example that states it. With one source this list is short. Screenshots are the exception, since they will still differ per version.
- Any page that could delete data or change access (backup, restore, upgrade, permissions, authentication) gets a named person to run the steps on the current version before it ships. If nobody has run it, mark it unverified. Reading it through doesn't count.

**5. Keep it current (monthly, 30 minutes)**
- Each page shows when it was last reviewed, not just last edited.
- Add a "report a problem" link that reaches the chapter owner. Set a reply target of `[days]`.
- Log every doc error: symptom, page, fix. Once a month, the two of you look at the log. If one chapter keeps showing up, rebuild it instead of patching.

## What to stop doing
- Stop maintaining three full copies. This is the main cut.
- Stop fixing a page in one place and calling it done. The fix goes into the single source, and the version tag decides who sees it.

## Notes
- I haven't seen the guide, so I don't know how much 6, 7 and 8 differ. Measure it in week 1 by diffing chapters. If some chapters differ heavily, such as install or upgrade, keep those as separate pages inside the single source and merge the rest.
- Screenshots and translated copies, if you have any, will lengthen the ripple list. Tell me if there are translations, because they raise the cost of every wording change.

If you share the file layout or the toolchain you use now, I can turn step 1 into a concrete chapter-by-chapter checklist.
