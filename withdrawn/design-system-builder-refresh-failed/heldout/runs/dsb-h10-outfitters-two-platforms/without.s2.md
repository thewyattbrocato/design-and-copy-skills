**Recommendation: (b), a single token file in the repo that generates both outputs. Add the designer's export from (a) as an optional later step.**

**Why not the others**
- **(c) shared doc:** this is how you got here. Humans retyping hex values drift again, and nothing fails when they do.
- **(a) export and copy:** the design tool becomes the source of truth, which is reasonable. But the "devs copy them over" step is the part that drifts, and it's manual on two platforms.
- **(b):** drift becomes impossible by construction. At your size the build tooling is a small cost, and you can review a token change in a PR like any other code.

**How to start**

1. **Pick the canonical orange first.** This is a design decision, not a tooling one. Have the designer choose, then record it in the file. Do this before writing any tooling.
2. **Create `tokens.json`** in a shared location (a `design-tokens/` folder at the repo root if you have a monorepo, or in one repo with the other consuming it). Use the [W3C Design Tokens format](https://tr.designtokens.org/format/) (`$value`, `$type`) so it's compatible with the design tool's plugins later. Start small: colors, spacing, maybe radii and type sizes.
   ```json
   {
     "color": {
       "brand": { "primary": { "$type": "color", "$value": "#D9622B" } }
     },
     "space": {
       "md": { "$type": "dimension", "$value": "16px" }
     }
   }
   ```
3. **Use [Style Dictionary](https://styledictionary.com)** to generate both outputs. It's the standard tool, and it has built-in CSS custom properties and iOS Swift formats. Configure two targets:
   - web: `tokens.css` with `--color-brand-primary: #D9622B;`
   - iOS: `DesignTokens.swift` with `static let` constants (or a `Color` extension)
4. **Commit the generated files**, or generate them in CI and fail the build if they differ from the committed ones. Committing them is simpler for 3 devs.
5. **Migrate incrementally.** Replace hard-coded values with tokens screen by screen, starting with the colors that have drifted. Add a lint rule or a PR habit of "no raw hex in components" so new drift doesn't creep in.
6. **Bring the designer in.** Once it's stable, have the designer's variables match the token names. Later, a plugin such as Tokens Studio (for Figma) can export into `tokens.json`, or the designer can open PRs against it. Until then, they can edit the JSON, or ask a dev, for the handful of changes a month.

**One caveat:** iOS often wants light/dark variants and asset catalog colors. Style Dictionary can emit those, but if you rely heavily on the asset catalog, expect a bit of custom config for that target.

If you tell me which design tool you use and whether web and iOS are in one repo or two, I can sketch the Style Dictionary config and folder layout.
