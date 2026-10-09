The palette's main problem is that it has no roles. Several colors carry meaning that clashes with how they're used, and a lot of the text is too low-contrast to read.

## What's wrong

**1. Status colors and decorative colors overlap.**
- `--link` is green (`#0b8a42`), and `--on-time` is also green. On a dispatch screen, green means "on time", so a link looks like a status.
- `--accent` orange sits between `--delayed` amber and `--failed` red. A secondary button in that orange reads as a warning.
- Purple for "new" adds one more hue with no job to do.
- The result is seven saturated hues (blue, green, orange, purple, plus the three status colors) competing at the same intensity. Dispatchers can't tell which colors mean something.

**2. Contrast failures.** These are approximate WCAG ratios:

| Pair | Ratio | Needs |
|---|---|---|
| white on `--delayed` `#fab005` | ~1.9 | 4.5 |
| white on `--on-time` `#12b886` | ~2.5 | 4.5 |
| white on `--failed` `#fa5252` | ~3.3 | 4.5 |
| white on `--accent` `#e8590c` | ~3.6 | 4.5 |
| `--muted` `#b5b5b5` on `--bg` (12px) | ~1.9 | 4.5 |
| `--link` on `--bg` | ~4.0 | 4.5 |

The "delayed" badge is the worst case. It's the one dispatchers most need to read, and it's white text on yellow. The 12px muted metadata is nearly invisible on the gray background.

**3. The hierarchy is flat.** The primary and secondary buttons are both solid, saturated fills with white text. The secondary action competes with the primary one. Secondary buttons are usually neutral or outlined.

**4. Status is carried by color alone.** Green, amber and red are a classic problem for red-green color blindness. The CSS shows no icon or label backing them up.

**5. Weak surface separation.** `#f4f4f4` against `#fff` with no border or shadow gives panels little definition. That's minor, but it adds to the washed-out feel.

## What I'd change

- **Give each color one job.**
  - Blue is the only interactive color: buttons, links and focus rings.
  - Green, amber and red mean status only.
  - Everything else is neutral.
- **Drop orange and purple**, or keep one as a rare highlight. "New" can be a blue-tinted tag.
- **Make links brand blue**, underlined.
- **Use dark text on light status fills** (a tinted background with a dark same-hue text), and add an icon or label to each status.
- **Darken `--muted`** to about `#6b6b6b` or darker.
- **Make secondary buttons outlined or neutral.**

```css
:root {
  --bg: #f4f5f7;
  --panel: #ffffff;
  --border: #d9dce1;
  --text: #1f2328;
  --muted: #5f6670;          /* ~5.6:1 on white, ~5:1 on bg */

  --brand: #1f6feb;          /* all interactive things */
  --brand-strong: #1a5fcc;   /* hover/pressed */
  --link: var(--brand);

  /* status: tinted fill + dark text, always paired with icon/label */
  --on-time-bg: #d3f4e6;  --on-time-fg: #0a5c3e;
  --delayed-bg: #fff0c2;  --delayed-fg: #7a4b00;
  --failed-bg:  #ffdcdc;  --failed-fg:  #9c1c1c;
}

.btn-primary   { background: var(--brand); color: #fff; }
.btn-secondary { background: transparent; color: var(--brand);
                 border: 1px solid var(--brand); }
.tag-new       { background: #dbe8fd; color: #123e85; }

.status-on-time { background: var(--on-time-bg); color: var(--on-time-fg); }
.status-delayed { background: var(--delayed-bg); color: var(--delayed-fg); }
.status-failed  { background: var(--failed-bg);  color: var(--failed-fg); }

.panel { background: var(--panel); border: 1px solid var(--border); }
.meta  { color: var(--muted); font-size: 12px; }
a      { color: var(--link); text-decoration: underline; }
```

I estimated the contrast ratios by hand and haven't run them through a checker. Please verify the new pairs with one before shipping. The status badges' foreground colors are the ones most worth checking.

If you also use these status colors in charts or map markers, keep the saturated versions for small marks, like dots and lines. Use the tinted versions for badges.
