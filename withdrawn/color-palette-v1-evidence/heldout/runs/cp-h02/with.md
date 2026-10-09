The colors feel off because nothing has a clear job, and several pairs are hard to read. I computed these contrast ratios with the WCAG formula, and they're approximate.

## What's wrong, by impact

1. **Delayed badge is nearly unreadable.** White on `#fab005` is about 1.9:1, and the floor is 4.5:1. This is the status dispatchers most need to see.
2. **Muted metadata fails.** `#b5b5b5` is about 2.0:1 on the panel and 1.9:1 on the page background, with 12px text. It reads as disabled, not secondary.
3. **Too many loud hues, none leading.** The screen has blue, green, orange and purple, plus three status colors. That's seven hues at similar saturation, so nothing reads as the primary action. The orange secondary button and purple "new" tag compete with the blue primary button.
4. **Status colors collide with UI colors.**
   - `--link` green (`#0b8a42`) sits right next to `--on-time` green. A link and an "on time" badge look like the same signal.
   - `--failed` red and `--accent` orange are close in hue, so a failed shipment and a secondary button look alike.
5. **White text on the other status fills is weak.** White on `--on-time` is about 2.6:1 and on `--failed` about 3.3:1. The orange button is about 3.6:1. Only the blue (4.65:1) and purple (about 5.5:1) pass.
6. **Link green is borderline.** It's about 4.45:1 on white and about 4.05:1 on the `#f4f4f4` page background. It also doesn't match the blue brand, so the screen has two "clickable" colors.
7. **Neutrals are dead gray.** They have no tint, so the white panel on the `#f4f4f4` background feels flat next to the saturated accents.
8. **Status may rely on color alone.** Nothing in the CSS shows a label or icon beside the fill. Red and green are hard to tell apart for color-blind users.

## What I'd change

```css
:root {
  --bg: #f3f5f8;        /* cool-tinted neutral, leans toward the brand blue */
  --panel: #ffffff;
  --text: #1f2430;
  --text-muted: #5b6372; /* ~5.5:1 on panel, ~5:1 on bg */
  --border: #d9dee7;

  --brand: #1f6feb;      /* keep: 4.65:1 with white */
  --brand-ink: #1a5fd0;  /* links and text-sized blue, replaces the green */
  --brand-tint: #e7f0ff;

  --on-time: #12b886;    /* fill, with dark text ~5.5:1 */
  --delayed: #fab005;    /* fill, with dark text ~7.6:1 */
  --failed: #c92a2a;     /* white text, roughly 6:1 */
}
.btn-primary   { background: var(--brand); color: #fff; }
.btn-secondary { background: var(--panel); color: var(--brand-ink); border: 1px solid var(--border); }
.tag-new       { background: var(--brand-tint); color: var(--brand-ink); }
.status-delayed{ background: var(--delayed); color: var(--text); }
.status-ontime { background: var(--on-time); color: var(--text); }
.status-failed { background: var(--failed); color: #fff; }
.meta          { color: var(--text-muted); font-size: 12px; }
```

- **One lead:** blue does the work. Links, the secondary button and the tag are quiet steps of that same blue instead of new hues. Delete `--accent`, `--accent-2` and the green `--link`.
- **Status keeps its hues,** since green, amber and red are what dispatchers expect. Status colors now belong only to status. Failed is a deeper red, well away from any UI color.
- **Dark text on light status fills** fixes delayed and on-time. Failed is dark enough for white text.
- **Add an icon or word to every status badge,** such as ✓ On time, ⚠ Delayed and ✕ Failed.
- **Muted text** moves to a tinted gray that clears 4.5:1 on both the panel and the page background.

I didn't re-measure the new values, so check `--brand-ink` on `--brand-tint` and `--failed` with white before shipping. If you have hover or selected row states, the same rule applies: check contrast on the tinted ground, not on white.
