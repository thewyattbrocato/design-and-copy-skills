I found a few things the earlier passes missed, and one is a real bug. This is the pasted snippet only, so I haven't run anything, and I didn't see the save JS.

**Fixes**

1. **Disabled dimming doesn't reach the label.** `input:disabled+*` selects the element *after* the input, but the label text `<span>` comes *before* it. So "Product news" renders at full strength while only the control dims. Use `:has()` on the row instead.
2. **Dark mode can render unreadable text.** Dark mode sets a light `--text` but the panel has no background. On a white host page you get light text on white. Set `color-scheme` and a `--bg` on the panel.
3. **The `role="group"` has no accessible name.** It has `aria-describedby` but nothing names it, so screen readers announce an unlabeled group. Add `aria-labelledby="n-h"`.
4. **Smaller polish.**
   - Rows lack `align-items:center`.
   - The native control isn't tinted with the accent color.
   - The status line collapses when empty, so the layout jumps when "Saved" appears.

```html
<section aria-labelledby="n-h" class="panel">
  <h2 id="n-h">Notifications</h2>
  <p class="hint" id="n-d">Choose what we email you about. Changes save automatically.</p>
  <div role="group" aria-labelledby="n-h" aria-describedby="n-d">
    <label class="row"><span>Order updates</span><input type="checkbox" role="switch" checked></label>
    <label class="row"><span>Weekly digest</span><input type="checkbox" role="switch"></label>
    <label class="row"><span>Product news</span><input type="checkbox" role="switch" disabled aria-describedby="n-lock"></label>
    <p class="hint" id="n-lock">Product news is managed by your workspace admin.</p>
  </div>
  <p class="status" role="status" aria-live="polite"><!-- "Saved" or "Couldn't save. Try again." injected here --></p>
</section>
<style>
:root{color-scheme:light dark;--bg:#fff;--text:#1d2330;--muted:#5a6475;--line:#d9dde5;--accent:#2457d6}
@media (prefers-color-scheme:dark){:root{--bg:#141922;--text:#e8ebf2;--muted:#a3adbf;--line:#2e3646;--accent:#7aa2ff}}
.panel{max-width:34rem;padding:1.5rem;color:var(--text);background:var(--bg)}
.row{display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:.875rem 0;border-bottom:1px solid var(--line);min-height:44px}
.row input{accent-color:var(--accent)}
.row:has(input:disabled){opacity:.6;cursor:not-allowed}
.hint{color:var(--muted);font-size:.875rem}
.status{min-height:1.5em}
input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
```

**Things to check in the save logic**
- **Failed saves:** when a save fails, revert the toggle or make clear it didn't change. "Couldn't save" next to a switch that looks on is misleading.
- **Status text:** clear the status message when the next toggle starts, so a stale "Saved" doesn't linger.
- **Focus:** don't move focus on save. The live region is enough.

**Left as is**
- `role="switch"` on a checkbox input is valid.
- The 44px rows meet the touch-target size.
- The disabled hint is wired up correctly.
- The `role="status"` region starts empty, which is correct.
