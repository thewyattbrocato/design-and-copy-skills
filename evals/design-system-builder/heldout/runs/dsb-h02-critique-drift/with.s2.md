## What's going on

Nobody made a wrong decision here. The stylesheet has no shared decisions at all. Every rule was written with its own value, so the same decision (a gray, a radius, a card) got made again each time and came out slightly different. Counting the values in your chunk:

| Property | Values in use | What it should be |
|---|---|---|
| Primary blue | `#2f6fed`, `#2e6dea` | 1 |
| Muted text gray | `#8a8f98`, `#8d929b`, `#858a93` | 1 |
| Border gray | `#e3e5e8`, `#e1e4e8` | 1 |
| Success green | 2 backgrounds, 2 text colors | 1 each |
| Radius | 4, 5, 6, 7, 9, 10, 12 (7 values) | 2 or 3 |
| Shadow | 3, two of them near-identical | 2 |
| Control height | input 38, select 40 | 1 |
| Control radius | input 6, select 4, button 5 | 1 |
| Spacing | 9, 11, 12, 13, 14, 17, 18, 19, 22, 26, 34 | 7 or 8 steps |
| Type | 17 is used twice (`h4`, `.btn-big`), and 17 and 19 sit next to each other | 4 sizes |

- **Near-duplicates are the main cause.** Most of these differ by a few units, so people can feel the difference without being able to name it. That is why nobody can say why it feels off.
- **Components that are the same thing have drifted.** `.card` and `.panel` are one concept with different padding, radius, border and shadow. An input and a select sit side by side at different heights and radii.
- **Some of this may be accidental.** The two blues and the three grays look like eyedropper values from different mockups, not intentional choices.
- **Accessibility is a likely problem.** By my estimate `#8a8f98` on white is about 3.3:1, below the 4.5:1 AA minimum for small text. White on `#2f6fed` is about 4.5:1, which is borderline. Check both with a contrast tool.

## What I'd do, in order

**1. Pick the values (about a day, mostly decisions).**
Choose one value per row below. I'd round to the nearest value, not average.

| Old | New token |
|---|---|
| `#2f6fed`, `#2e6dea` | `color.accent` = `#2f6fed` |
| `#8a8f98`, `#8d929b`, `#858a93` | `color.text.secondary` (proposal: darken to about `#6b7078`, then check contrast) |
| `#e3e5e8`, `#e1e4e8` | `color.border.subtle` = `#e3e5e8` |
| Green backgrounds and text | `color.success.bg` and `color.success.text` (keep the darker text, `#1f7a3a`) |
| Radius 4, 5, 6, 7 | `radius.control` = 6 |
| Radius 9, 10, 12 | `radius.surface` = 12 |
| Shadow on card and panel | `shadow.raised` = `0 2px 8px rgba(0,0,0,.12)` |
| Shadow on modal | `shadow.overlay` (keep as is) |
| Spacing 9–14 | 8, 12, 16 |
| Spacing 17–22 | 16, 24 |
| Spacing 26–34 | 24, 32 |
| Type 14, 17/19, 23, 31 | 14, 18, 24, 32 |
| Input and select height | 40 |

Spacing steps are `4, 8, 12, 16, 24, 32, 48`. The rounding above is my proposal, so adjust it to your design.

**2. Add the tokens without changing anything visually.**
Put them in as CSS custom properties on `:root`. Components should use role names like `--color-text-secondary`, not raw ramp names like `--gray-500`.

**3. Migrate by visibility, not by file.**
- Do colors first, because they're the easiest to spot.
- Then controls: buttons, input and select at one height and radius.
- Then `.card` and `.panel` merged into one surface component, with an optional padding modifier if you really need two sizes.
- Spacing goes last, because it touches the most lines.
- Take a before and after screenshot of key screens for each step, so reviewers see small intentional shifts and not surprises.

**4. Stop the drift from coming back.**
Add a stylelint rule (for example `declaration-property-value-allowed-list`, or a plugin that flags raw hex values) so a raw `#2e6dea` or `13px` fails CI. Allow exceptions only with a comment. Without this, the mess returns within a quarter.

**5. Fill in component states.**
Your `.btn` has no hover, focus, disabled or loading styles in this chunk. Specify those once the tokens exist, since each state is then just a token swap.

**6. Governance, kept light.**
Name one owner for the token file. A new value has to replace or merge with an existing one, not add to the list. Design files should read the same token file, so Figma and code can't diverge.

I assumed one brand, one theme and a small team. If you need dark mode, build it by remapping the semantic roles (`text.secondary`, `surface`), never by inverting raw values. Do step 2 first, so the dark theme has roles to remap.

I only saw this chunk. Run the same inventory over the whole repo before fixing the final numbers, because other files will have more variants (`[count from your repo]`).
