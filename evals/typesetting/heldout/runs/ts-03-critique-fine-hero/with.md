The paragraph text is fine. The sizes (16px body, 20px lead, 1.5 leading) and the 56px headline at 1.05 leading are reasonable for a hero. What's wrong is the eyebrow, the stats, and a couple of smaller things.

**Real problems**

1. **The stats are the worst part.**
   - **Figures don't align.** Right-aligned, stacked numbers need tabular figures. Without `tabular-nums`, "1,284", "97" and "12,060" use proportional digit widths, so the commas and digits drift against each other down the column.
   - **No labels.** Three bare numbers say nothing. You know they're drills, streak days and strokes scored, but a visitor doesn't. Add a small label to each.
2. **The eyebrow is 11px, all caps, with `letter-spacing: 0`.** Untracked small caps look cramped and are hard to read. Use 12px or more and track it at about 0.08em.
3. **The h1 is a fixed 56px.** On a phone, 42 characters at that size will break badly, probably into three or four lines with a ragged shape. Use `clamp()` and `text-wrap: balance` so the two-line break falls evenly.
4. **The body runs a little long.** At 16px in a 640px box that's about 80 characters per line. Capping it near 65ch is enough. Don't narrow the whole hero.

**Fixes**

```css
.eyebrow { font-size: 0.75rem; letter-spacing: 0.08em; /* rest unchanged */ }
h1 { font-size: clamp(2.25rem, 7vw, 3.5rem); text-wrap: balance; /* rest unchanged */ }
.body { max-width: 65ch; text-wrap: pretty; /* rest unchanged */ }

.stat { font-size: 2rem; font-weight: 700; line-height: 1.1; font-variant-numeric: tabular-nums; }
.stat + .stat { margin-top: 12px; }
.stat-label { display: block; font-size: 0.875rem; font-weight: 400; color: #6b5d3f; }
```

```html
<div class="stat">1,284 <span class="stat-label">drills completed</span></div>
<div class="stat">97 <span class="stat-label">day streak</span></div>
<div class="stat">12,060 <span class="stat-label">strokes scored</span></div>
```

The label wording is my guess from your description, so adjust it to match the app. With `display: block`, each label sits under its number and right-aligns with it.

**Left alone:** the h1 leading and tracking, the lead and body sizes, the colors, and the overall scale of 11, 16, 20, 32 and 56px.
