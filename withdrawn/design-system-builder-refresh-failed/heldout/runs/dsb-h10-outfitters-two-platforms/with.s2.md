**Go with (b): one token file in the repo that generates both the CSS and the Swift.** Make the designer's variables a mirror of that file, not a separate source.

- **(a) fails because it's still hand copying.** Copying is what produced the two oranges. It also puts the designer on the critical path for every change.
- **(c) fails because a shared doc has no enforcement.** Nothing breaks when the doc and the code disagree.
- **(b) works because drift becomes a build failure.** With three devs, a JSON file and a small generator is a light setup.

**How to start**

1. **Inventory what exists.** Pull every distinct color, spacing value, radius, and font size from the web and iOS code, with counts. Report near-duplicates, such as the two oranges and any grays one step apart. Don't merge anything yet. The designer picks the canonical orange, and you check its text and background contrast before committing to it.
2. **Keep the first token set small.**
   - **Colors:** semantic roles such as `color.text.primary`, `color.surface.raised`, `color.accent` and `color.danger`, over a short raw palette.
   - **Spacing:** 8 to 10 steps.
   - **Radii:** 2 to 4.
   - **Type:** 4 to 6 roles.

   Components should reference roles, never raw values like `orange-500`.
3. **Create `tokens/tokens.json`.** Use the W3C design-tokens format, which Style Dictionary and most design-tool plugins read.
4. **Add Style Dictionary.** It has two outputs:
   - `tokens.css` with CSS custom properties for the React app.
   - A Swift file (or an asset catalog for colors, which gives you dark mode support) for iOS.
5. **Add a CI check.** It regenerates the outputs and fails if they differ from what's committed. Also add a lint that flags raw hex values and magic numbers in new code.
6. **Migrate in order.** Do the orange first, since it's the visible bug. Then do the rest of the colors, then spacing. Anything that doesn't map to a token is either a deliberate, marked exception or a candidate to merge into an existing token.
7. **Agree on how the designer participates.** The simplest option is for the designer to import the JSON into the design tool as variables, using Tokens Studio or a similar plugin. They propose changes as a PR or a short request, and a dev merges. The rule is that a value isn't real until it's in the JSON.

**Assumptions to check**

- I'm assuming web and iOS can see the same repo. If they're in separate repos, put the tokens in a small third repo or package and have each app pull the generated files.
- I'm assuming a single brand with no dark mode yet. If you need dark mode, the roles get remapped per theme, not inverted. It's easier to build that in now than to retrofit it.

If you point me at the web and iOS code, I can run the inventory and draft the first `tokens.json` and generator config. The working directory I'm in is empty, so I have nothing to scan yet.
