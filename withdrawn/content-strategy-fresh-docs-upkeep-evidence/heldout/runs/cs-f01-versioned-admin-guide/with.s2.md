**The problem:** one fix has to be made three times, and nobody is responsible for making sure it is. The change is to keep one source for the guide and write down only the places where versions really differ.

I'm assuming the guide is in text files or something you can diff, and that you have no tooling yet. If it's in Word or Google Docs, steps 1 and 2 still apply. Only the build in step 3 changes.

## Week 1: Find out what actually differs

1. Put the three copies side by side. If they are text files, `diff` does this. Otherwise use your editor's compare feature.
2. Give each section an ID and sort it into one of three buckets:
   - **Same in all three.** This is probably most of the guide.
   - **Differs on purpose.** A feature, menu, option or step really changed between versions.
   - **Differs by accident.** One copy got a fix the others missed. This is the drift you're seeing now.
3. For the accidental differences, decide which text is correct and fix it. This is the one-off cleanup. It also gives you your first real count of how much is duplicated, so you don't have to guess.

**Output:** a sheet with section ID, bucket, and owner.

## Weeks 2–3: Merge into one source

4. Make one master copy of the guide. Keep the shared text once. Mark each version-specific passage with a tag such as `v6 only`, `v7+` or `v8 only`. A short note for a small difference is better than a second page.
5. In the option and setting reference, add "added in" and "removed in" to each entry.
6. Build three outputs from the master: guide 6, guide 7 and guide 8. Readers still get a per-version guide, but you maintain only one.
   - If you use Markdown, AsciiDoc or Sphinx, conditional blocks do this natively.
   - If you have no tooling, the minimum is one master document with the tags, plus a script or manual export for each version. Choose a tool based on what you already write in. Don't adopt a new one just for this.
7. Freeze the old three copies as read-only. After the merge, nobody edits them.

**Until the merge is done:** keep a single fix log. Every correction goes in with a line saying which of 6, 7 and 8 it applies to, and you don't close an entry until all of them are fixed. It's a stopgap, but it ends the situation where a fix lands in one copy and the others stay wrong.

## Two rules to adopt now

- **Ripple check.** Before any changed value, name or step ships, search the master for every place it appears, including screenshots. Tag each place with the versions it affects.
- **Run the risky steps.** Any procedure that could lose data or change access gets run on the actual version by a named person before it ships. That covers upgrade, backup and restore, migration, and permissions. Reading it through doesn't count. If it hasn't been run, mark the page "unverified" and ship it that way.

## Owners

With two writers, split by chapter, not by version. Each chapter has one owner, and that owner covers all three versions of it. One of you also owns the version policy and the tags. The key point is that chapter owners handle every version. If you split by version instead, you rebuild the same problem.

| Item | Owner |
|---|---|
| Chapters, first half | Writer A |
| Chapters, second half | Writer B |
| Version policy, tags, build | `[Writer A or B]` |
| Run-the-steps check on risky pages | `[named person, probably someone in support or engineering]` |

## Version policy

Write this on one page:

- Which versions get docs.
- How a page is marked when a feature doesn't exist in the reader's version, and which release added it.
- When a version's docs retire. Use your end-of-support date, `[v6 end-of-support date]`. After that date, v6 stops getting updates and links to the current guide.

## Keeping it right

- **Trigger:** every release. The release owner tells the doc owner, and the product change isn't done until its doc change ships.
- **Feedback:** put "Report an error" on each page. It goes to the chapter owner, who logs the symptom, the page and the fix.
- **Review date:** show "last reviewed" on each page, not "last edited".

## What to stop

Stop maintaining three separate full guides, starting now. When v6 passes its support end date, stop producing the v6 build too.

**Worth measuring:** the diff in step 2 will tell you how much of the guide really differs between versions. If it's a small share, this plan is easy. If it's large, you may need to restructure the guide, not just tag it.
