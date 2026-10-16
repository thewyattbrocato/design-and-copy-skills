**Do (b), with the JSON file in the repo as the single source of truth.** The designer's variables should match it, not feed it.

- **(a) copy-over** keeps the hand-typing step that caused the drift. It just moves it to a different person.
- **(c) shared doc** is roughly what you have now. A doc can't fail a build, so it will drift again.
- **(b)** makes drift impossible for anything generated. The web orange and the iOS orange become one value because both files come from the same line.

**How to start**

1. **Inventory before inventing.** List every color, spacing value, radius and font size in use on each platform, with counts. Group them by purpose. The orange mismatch will show up here, along with any near-duplicate grays. Ask the designer to pick the one true orange, since that's a design decision and not a dev one.
2. **Keep the set short.** For a team your size that means:
   - semantic color roles (`text.primary`, `text.secondary`, `surface.default`, `surface.raised`, `border.subtle`, `accent`, `danger`) over a short raw palette
   - about 8 spacing steps
   - 3 radii
   - 4 to 6 type roles

   Components should use the role names, never `orange-500`. Role names also give you dark mode later, because a theme just changes what each role points to.
3. **Write `tokens.json`** in the repo, using the W3C design-tokens format. Here's a sketch (the hex is a placeholder until the designer picks):
   ```json
   {
     "color": {
       "raw": { "orange": { "500": { "$value": "#D9622B", "$type": "color" } } },
       "accent": { "$value": "{color.raw.orange.500}", "$type": "color" }
     },
     "space": { "sm": { "$value": "8px", "$type": "dimension" } }
   }
   ```
4. **Generate both outputs with Style Dictionary.** One run produces CSS custom properties for the React app and a Swift file for iOS (a `Color` extension or an asset catalog). Commit the generated files and add a CI check that fails if they're out of date.
5. **Migrate gradually.** Start with the orange and the text and surface colors. Then do spacing. Any leftover hard-coded value is either a bug or a marked exception.
6. **Bring the designer in.** They create design-tool variables with the same names as the tokens. When they want a change, they open a PR (editing a JSON file on GitHub's web UI is enough) or file an issue, and a dev merges it. If the design file and the JSON disagree, treat it as a bug and fix the JSON or the design file.

**Trade-off:** the designer now works through a PR instead of staying purely in the design tool. If that proves painful, a plugin like Tokens Studio can sync the design tool to the repo file. Don't add it on day one.

I assumed one brand, no dark mode yet, and SwiftUI or UIKit with no existing token layer. The working directory here is empty. If you point me at the web and iOS repos, I can run the inventory in step 1 and draft the first `tokens.json`.
