I found two real bugs and a few smaller gaps. This is from reading the markup only, and I haven't run it. There's no file in the working directory, so the fixes below are for you to paste in.

**Fixes**

1. **The disabled row's label never dims.** `input:disabled+*` selects the element *after* the input, and the input is the last child of the label. So only the checkbox fades, not "Product news". Use `:has()` on the row instead.
2. **Dark mode can produce unreadable text.** The panel sets `--text` to a light color in dark mode but never sets a background. If the host page is light, you get light text on light. `color-scheme` also makes the native controls follow the theme. I've added `color-scheme: light dark`. If the panel isn't guaranteed a dark host background, also give it `background: var(--bg)`.
3. **The group has no accessible name.** `role="group"` only has a description, so screen readers announce an unnamed group. Add `aria-labelledby="n-h"`.
4. **Layout polish.** The rows lack `align-items:center`, so the text and switch sit off-center when the row is 44px tall. The checkboxes also ignore `--accent`.

```html
<div role="group" aria-labelledby="n-h" aria-describedby="n-d">
```

```css
:root{color-scheme:light dark;--text:#1d2330;--muted:#5a6475;--line:#d9dde5;--accent:#2457d6}
.row{display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:.875rem 0;border-bottom:1px solid var(--line);min-height:44px}
input[type=checkbox]{accent-color:var(--accent)}
.row:has(input:disabled){opacity:.6}
```

Delete the old `input:disabled+*,input:disabled{opacity:.6}` rule. The new one dims the whole row, including the label text.

**Not shown in the snippet (please check the JS)**
- **Failed saves:** if one fails, revert the toggle or make it clear it didn't stick. "Couldn't save" next to a switch that looks changed is misleading.
- **Status message:** clear "Saved" after a few seconds. Also make sure repeated identical messages are still announced, for example by clearing the node briefly before re-injecting.
- **Duplicate ids:** `n-h`, `n-d` and `n-lock` collide if the panel renders twice on a page.

Leave the `role="status"` plus `aria-live="polite"` pairing alone. It's redundant but harmless. The reduced-motion rule, focus ring and color contrast all look fine.
