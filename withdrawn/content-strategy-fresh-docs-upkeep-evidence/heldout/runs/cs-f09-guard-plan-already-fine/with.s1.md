The plan is sound. Each page has an owner, there's a release-time check, and there's a quarterly cut. I'd fix five things before you share it, most important first.

1. **The CI rule will probably misfire.** If every page's version tag must be at least the release tag, then every untouched command page fails at each release. Teams then bump tags in bulk, and the tag stops meaning anything. Decide what the tag means. I'd define it as "the release this page was last checked against." CI should then fail only when a command's code changed since that tag, not on every release. Also say who is allowed to bump a tag without editing the page.

2. **The PR rule covers one page, but a change usually touches several.** "Say which doc page changed" misses the getting-started guide, other commands' examples, screenshots, and the changelog. Ask PRs that rename a command or flag, or change a default or a step, to list every page that mentions it. Also decide whether a reviewer or CI enforces the rule, since a PR description alone only works on trust.

3. **Risky commands aren't run by anyone.** The docs lead runs the getting-started steps each release, which is good. Reference pages for commands that delete or overwrite data, or change credentials or access, get no such check. For those pages, a named person should run the documented steps on the current version before the page ships. Otherwise mark the page "unverified."

4. **The owner rule needs a fallback.** "Whoever last changed it" can be a drive-by typo fix, and it breaks when that person leaves or is on leave. Record the owner on the page or in a single file. Name who takes over when the owner is gone. Name who triages a doc error, and log those errors like product bugs.

5. **Feedback and the quarterly review depend too much on the docs lead.**
   - The docs lead already owns getting-started, the changelog, the release run, the feedback inbox, and the quarterly review. Name a backup for at least the weekly inbox check.
   - Feedback should reach the owner of the page it's about. Set a reply target (`[days]`) and record what each message changed. Show "last reviewed" on pages, not just "last edited."
   - In the quarterly review, a quiet page with several low ratings can matter more than a busy page with one. A short visit to a reference page may just mean the reader found the answer. Say who decides to retire or merge a page, and that retired pages redirect to the current one.

**Missing entirely:** a short version policy. Say which releases keep their own pages and how an old page is marked and linked to the current one. Say what a reader sees if a command doesn't exist in their version. Reference entries should name the release that added or deprecated each option. If Halvard only ever documents the latest release, say so in one line.

Two things would change this advice:
- **Does any Halvard command change or delete data, or touch credentials?** If so, item 3 is required rather than optional.
- **How many people are on the docs team?** If the docs lead is the only one, item 5 is the weakest spot.
