**Decision:** fix and own. You have three copies of one guide, so a correction has to be made three times and nobody is responsible for making sure it is. The change is to keep one source for the guide and mark the lines that differ by version.

## What to change

**1. Merge into one source with version markers.**
- Keep one admin guide. Where a step, option or screen differs, mark that block with the versions it applies to, for example `[6]`, `[7, 8]` or `[8+]`.
- Build the three published guides from that source. A docs-as-code tool with conditional content or includes can do this, such as MkDocs with a macros or include plugin, Sphinx, or Docusaurus versioning. Which one fits depends on what you write in today (`[current format and tooling]`).
- A fix to shared text is then made once and appears in all three versions.

**2. Write the version policy on one page.** It should answer:
- Which versions get their own published guide (6, 7 and 8).
- How a page is marked when it applies to only some versions.
- What a reader sees when they open a page for a feature that doesn't exist in their version. Link it to the release that added the feature, or redirect.
- When version 6 retires, and where its pages point afterward. Take the date from your support policy: `[v6 end-of-support date]`.

**3. Name an owner for each group of pages.**
- Split the guide's sections between the two of you. Each section gets one named person who can say no to a change.
- Put the owner in the source file header so it can't go missing.

**4. Make docs part of "done."** A product change isn't finished until its doc change ships with it. Log doc errors as defects: the symptom, the page, the fix. The section owner triages them.

**5. Add two checks.**
- **Ripple list:** before a changed value, limit, name or step ships, list every page, example and screenshot that states it. Single sourcing shortens the list but doesn't replace it. Screenshots will still differ by version.
- **Run risky steps.** If following a page could delete data or change access or security, such as backup, restore, upgrade or permissions, someone runs the steps on the current version before it ships. Otherwise the page ships marked unverified.

**6. Show freshness and take replies.**
- Each page shows when it was last reviewed, not last edited.
- Add a feedback link that reaches the section owner. The owner sets a reply target of `[days]` and notes what each message changed.

## What to stop
- Stop editing the three copies directly. Once the merge is done, make the old copies read-only or delete them. If they stay editable, they will drift again.
- Don't add a review committee. The owner plus the risky-step run is enough for two people.

## Order of work

| Step | Who | Produces |
|---|---|---|
| 1. Diff the three copies and sort every difference into "typo or drift" or "real version difference" | Both of you, split by section | A list of differences with an ID for each |
| 2. Pick the tool and build one pilot chapter | One of you | A working chapter that builds all three versions |
| 3. Write the version policy and the owner table | The other | One page each |
| 4. Merge the remaining chapters, taking the newest correct text and marking real differences | Section owners | One source, three builds |
| 5. Retire the old copies and add the "docs are part of done" step to your release checklist | Both | The old copies gone and the checklist updated |

**Start this week with step 1.** The diff will show how much of the three copies is real difference and how much is drift, and that decides how long the merge takes. I haven't seen the guides, so I can't estimate it. If you give me the file format and where the copies live, I can run the diff and sort it for you.

**Notes**
- Assumption: the guides are in a format that can be built from one source. If they're in a word processor or a wiki with no includes, the tool choice in step 2 becomes the main decision.
- Measure: after the diff, count real version differences against drift. If most of the guide differs by version, merge only the shared chapters.
