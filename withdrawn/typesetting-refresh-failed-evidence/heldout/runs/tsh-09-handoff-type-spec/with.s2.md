# Spoke & Chain: Typography Spec

Paste-ready for the ticket. Values come from the Figma file. Anything I had to decide myself is marked **(proposed)** so you can overrule it before handoff.

## Font

```css
--font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

- Load the weights 400, 500, 600 and 700. Don't rely on the browser to fake a weight: set `font-synthesis: none` on `body`.
- Keep Inter's `tnum` OpenType feature if the font is self-hosted or subsetted. The table alignment below depends on it.
- All sizes are in `rem` so the user's browser text-size setting is respected. Never set a pixel size on the root.

## Type scale

| Role | Size / line | rem values | Weight | Tracking | Notes |
|---|---|---|---|---|---|
| Page title | 32 / 38 px | `2rem` / `1.1875` | 700 | `-0.02em` | Tightened. `text-wrap: balance` |
| Section heading | 22 / 28 px | `1.375rem` / `1.275` | 600 | 0 | `text-wrap: balance` |
| Body | 16 / 24 px | `1rem` / `1.5` | 400 | 0 | `text-wrap: pretty` |
| Caption / small print | 13 / 18 px | `0.8125rem` / `1.385` | 400 | 0 | Muted gray. See contrast note |
| Button label | 15 px | `0.9375rem` | 500 | 0 | Sentence case. One line, `line-height: 1.2` **(proposed)** |
| Section label | 12 px | `0.75rem` / `1.33` | 600 | `+0.08em` | Uppercase. See below **(proposed)** |

```css
:root {
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;

  --text-title: 2rem;        --leading-title: 1.1875;   /* 32/38 */
  --text-section: 1.375rem;  --leading-section: 1.275;  /* 22/28 */
  --text-body: 1rem;         --leading-body: 1.5;       /* 16/24 */
  --text-small: 0.8125rem;   --leading-small: 1.385;    /* 13/18 */
  --text-button: 0.9375rem;
  --text-label: 0.75rem;     --leading-label: 1.33;

  --track-title: -0.02em;
  --track-label: 0.08em;
  --measure: 65ch;
}

body {
  font: 400 var(--text-body)/var(--leading-body) var(--font-sans);
  font-synthesis: none;
}
h1 { font-size: var(--text-title);   line-height: var(--leading-title);   font-weight: 700; letter-spacing: var(--track-title); text-wrap: balance; }
h2 { font-size: var(--text-section); line-height: var(--leading-section); font-weight: 600; text-wrap: balance; }
p  { max-width: var(--measure); text-wrap: pretty; }
.caption { font-size: var(--text-small); line-height: var(--leading-small); color: var(--color-text-muted); }
button, .btn { font-size: var(--text-button); font-weight: 500; line-height: 1.2; letter-spacing: 0; }
```

## Prices and hours in repair tables

```css
.table-num {
  font-variant-numeric: tabular-nums lining-nums;
  text-align: right;
}
```

- Apply `.table-num` to every price, time and quantity cell, **and** to its column header, so the header sits over the digits.
- Use the same decimals on every row ("12.50" and "8.00", never "12.5"). Put the currency symbol in the column header if every row uses it. Otherwise keep it attached to the number.
- Write hour ranges with an en dash: "9:00–17:00". Use a non-breaking space between a time and AM/PM, and between a number and its unit (`5&nbsp;min`).
- Body prose keeps Inter's default proportional figures. Only table cells and any other column of numbers use tabular figures.

## Section labels ("OPENING HOURS")

```css
.label {
  font-size: var(--text-label);       /* 12px: the minimum for all-caps */
  line-height: var(--leading-label);
  font-weight: 600;
  letter-spacing: var(--track-label);
  text-transform: uppercase;
  font-variant-ligatures: none;
}
```

- **Proposed:** your notes didn't give a size, weight or tracking for these. All-caps needs tracking, or it looks cramped. 12 px is the smallest I'd go.
- Write the source text in normal case ("Opening hours") and let `text-transform` do the capitals. That keeps screen readers and copy-paste sensible.
- Use it for short labels only, one to three words. Never set a sentence in caps.

## Links in paragraphs

```css
p a, li a {
  color: var(--color-link);           /* the Figma blue */
  text-decoration: underline;
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.15em;
  text-decoration-skip-ink: auto;
}
p a:hover { text-decoration-thickness: 0.12em; }
p a:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
```

- Keep the underline. Colour alone isn't enough to mark a link.
- Don't remove the focus outline.

## Contrast: check before you hand off

- **Muted gray captions** at 13 px need at least 4.5:1 against the background. I don't have your hex values, so please check them. A gray like `#6B7280` on white passes, at about 4.8:1. Anything lighter probably won't.
- **Link blue** needs 4.5:1 against the page background too.

## Spacing (proposed)

You didn't specify spacing, so here is what I'd tell the dev:

- Put about **twice as much space above a heading as below it**. For example, section `h2`: `margin-block: 2rem 0.75rem`.
- Separate paragraphs with a gap of `0.75rem` to `1rem`. Don't indent the first line.
- Keep the label tight to the heading it introduces: `margin-bottom: 0.25rem`.

If Figma already has spacing values, those win.

## Fixed vs. flexible

- **Fixed:** the role sizes, line heights, weights and tracking above. There's no fluid scaling, because 32 px is already comfortable on a phone.
- **Flexible:** the width of prose (capped at `65ch`) and the table column widths.

## What to test

1. The longest page title on a 320 px-wide screen. It should wrap cleanly with no mid-word break.
2. A repair table with mixed price values (for example 8.00, 12.50 and 125.00). The digits should stack by place.
3. 200% browser zoom and a larger system text size. Nothing should clip or overlap.
4. A button with a long label. It should wrap or grow, not truncate.
5. Never truncate a price, an hour or an error message. Let them wrap.

**One note on the scale:** the 15 px button and 13 px caption sit close together. That's fine because they're different roles and the button is medium weight. If they ever look muddy on a real device, make the caption 12 px or the button 16 px. I wouldn't change either unless you see the problem.
