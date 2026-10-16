It's good, and I'd roll it out Monday with only small edits. It already has the fields that usually go missing: a dated source of truth, one named owner, a retire condition and a "not covering" list.

**Worth changing**

1. **Split the owner and tester field.** "Owner (one name) and who will test the steps" asks for two people in one line. People often put the owner's name in both, and then nobody has checked the steps. Make it two fields: `Owner (one name)` and `Tester (someone other than the writer)`.
2. **Make the re-check date work on events too.** A six-month default catches slow drift. It misses a release or plan change that breaks the article next week. Reword it to: `Re-check by: (date, default 6 months) or sooner if: (the change that would break it, e.g. UI redesign, pricing change)`. This also gives "Retire this article if" a partner, since one covers wrong and the other covers needs checking.
3. **Add a "why now" line.** Something like `What prompted this: (ticket tags, search terms with no results, a person's request)`. Without it, the brief can't tell a needed article from one someone just felt like writing. It's also the first thing you'd check when you decide whether to retire it. If you can fit it in, ask for the customer's own words for the problem. Those make better titles and search terms than internal names.

**Optional**

- Put `Existing articles it replaces or links to` first or second. If an old article can be updated, nobody should write a new one, and that is easier to see before the audience and goal sections.
- Add a "Done when" checkbox, such as "tester followed the steps and the source of truth confirmed the final draft". Skip this if you'd rather keep the brief to one page.

The rest I'd leave alone, including the "who it's for" and "what they should be able to do" fields.
