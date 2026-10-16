The panel is in good shape. The switch markup, the disabled-reason link, the live region and the 44px rows all work, and I left them alone. Four things still needed fixing.

```html
<div role="group" aria-labelledby="n-h" aria-describedby="n-d">
```

```css
:root{--bg:#fff;--text:#1d2330;--muted:#5a6475;--line:#d9dde5;--accent:#2457d6}
@media (prefers-color-scheme:dark){:root{--bg:#141926;--text:#e8ebf2;--muted:#a3adbf;--line:#2e3646;--accent:#7aa2ff}}
.panel{max-width:34rem;padding:1.5rem;color:var(--text);background:var(--bg)}
.row{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:.875rem 0;border-bottom:1px solid var(--line);min-height:44px}
.row:has(input:disabled){opacity:.6;cursor:not-allowed}
.status{min-height:1.5em}
```

Remove the old `input:disabled+*,input:disabled{opacity:.6}` rule.

1. **Dark theme text was unreadable.** `.panel` set a light text color in dark mode but no background, so on a white page the text was near-invisible. I added a `--bg` token for both themes. Check the surface this panel sits on. If the page already paints a matching dark background, you can drop `--bg`.
2. **The group had no accessible name.** It only had a description, so screen readers announced an unnamed group. I added `aria-labelledby="n-h"`.
3. **"Product news" wasn't dimmed when disabled.** `input:disabled+*` matches the element after the input, and nothing follows it, so only the checkbox dimmed. The new `:has()` rule dims the whole row. Its reason text is a separate `<p>`, so it stays at full contrast.
4. **Rows now center their switches vertically.** The status line also reserves its height, so the layout doesn't jump when "Saved" appears.

**Not covered:** the save script wasn't in what you sent. Check that a failed save reverts the toggle or clearly shows it's unsaved, so the switch doesn't say "on" while the message says "Couldn't save." Also check that a rapid second toggle doesn't leave a stale "Saved". I haven't tested with a screen reader or in a browser.
