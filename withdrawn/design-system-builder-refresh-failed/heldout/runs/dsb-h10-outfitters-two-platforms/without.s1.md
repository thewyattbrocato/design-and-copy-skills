**Do (b): one token file in the repo that generates both the CSS and the Swift.** Treat (a) as an input to it, not an alternative.

**Why not the others**
- **(c) shared doc:** this is what you have now. Someone still types the values by hand, so they'll drift again.
- **(a) export and copy:** it's better than a doc, but the copying is still manual. Each platform gets updated at a different time, which is how your two oranges happened.
- **(b):** the file is the source of truth, and a build step produces both outputs. Drift becomes impossible, and a color change is a one-line PR that updates web and iOS together.

**Handling the designer**
A JSON file in git is awkward for someone who lives in the design tool. There are two ways to handle it:
1. **Start simple:** the designer owns the values and sends changes as an export or a message. A dev updates the JSON. This is fine for a team your size.
2. **Automate later:** if the design tool supports exporting variables as JSON (Figma does, via Tokens Studio or a variables export plugin), the designer's export can go into the same file, ideally through a PR. Don't build this until the manual flow actually hurts.

**How to start**
1. **Pick the canonical values.** Sit down with the designer and decide which orange is correct. Do this for the full set of colors and spacing, not only the orange. It's the one step that needs a human decision.
2. **Create `tokens/tokens.json`** in a place both projects can reach. If the web and iOS code are in separate repos, put it in the repo that's easier to share, or make a tiny `ridgeback-tokens` repo.
3. **Use [Style Dictionary](https://styledictionary.com).** It's the standard tool for this. It has built-in outputs for CSS variables and iOS Swift, and you can customize the Swift format to match your code style.
4. **Start with colors and spacing only.** Skip typography, shadows, and radii until the pipeline works.
5. **Generate the files and commit them:**
   - Web: `tokens.css` with custom properties (`--color-brand-orange`).
   - iOS: `Tokens.swift` with a `Color` extension or a constants enum.
   Committing the generated files means nobody needs the build tooling just to pull and run.
6. **Migrate gradually.** Replace hand-typed values with tokens one screen or component at a time. Name tokens by role (`color.action.primary`) rather than appearance (`color.orange`). Then a rebrand changes the value and not the name.
7. **Add a CI check** that regenerates the tokens and fails if the committed output differs. That stops someone from editing the generated files by hand.

For a rough sense of effort, expect about a day to set up the pipeline and a few days of cleanup spread over normal work.

I can scaffold the Style Dictionary config and a starter `tokens.json` for you. If you do want that, tell me where the web and iOS code live and I'll set it up around that.
