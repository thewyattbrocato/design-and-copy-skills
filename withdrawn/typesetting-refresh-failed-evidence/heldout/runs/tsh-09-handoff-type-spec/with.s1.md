# Spoke & Chain: Typography Spec

Sizes are in `rem` (1rem = 16px) so the user's browser text-size setting is respected. Line heights are unitless.

## Font

```css
:root {
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
body { font-family: var(--font-sans); font-synthesis: none; }
```

- Load only the weights we use: 400, 500, 600, 700.
- Use `font-display: swap`.
- `font-synthesis: none` stops the browser faking a weight we haven't loaded. A missing weight should be a bug we notice.
- The file must include Inter's tabular figures (see Prices and hours). The Google Fonts and official Inter builds do.

## Type roles

| Role | Size | Line height | Weight | Other |
|---|---|---|---|---|
| Page title | 2rem (32px) | 1.1875 (38px) | 700 | letter-spacing `-0.02em`, `text-wrap: balance` |
| Section heading | 1.375rem (22px) | 1.2727 (28px) | 600 | `text-wrap: balance` |
| Body | 1rem (16px) | 1.5 (24px) | 400 | `text-wrap: pretty` |
| Caption / small print | 0.8125rem (13px) | 1.3846 (18px) | 400 | muted gray (see Color) |
| Button | 0.9375rem (15px) | 1 (or the button's height) | 500 | sentence case |
| Section label | 0.75rem (12px) | 1.333 (16px) | 600 | uppercase, `letter-spacing: 0.08em` |

```css
:root {
  --text-title: 2rem;
  --text-section: 1.375rem;
  --text-body: 1rem;
  --text-button: 0.9375rem;
  --text-small: 0.8125rem;
  --text-label: 0.75rem;
}

h1, .page-title   { font-size: var(--text-title);   line-height: 1.1875;  font-weight: 700; letter-spacing: -0.02em; text-wrap: balance; }
h2, .section-head { font-size: var(--text-section); line-height: 1.2727;  font-weight: 600; text-wrap: balance; }
body, p           { font-size: var(--text-body);    line-height: 1.5;     font-weight: 400; }
p                 { text-wrap: pretty; max-width: 65ch; }
.caption, small   { font-size: var(--text-small);   line-height: 1.3846;  color: var(--color-text-muted); }
.button           { font-size: var(--text-button);  font-weight: 500; }
```

- Roles are classes, not tags. Pick the heading level (h1, h2, h3) for the document outline, then apply the look with a class.
- Don't add other sizes. If something doesn't fit a role, ask me.
- Don't set the page title in all caps.

## Section labels ("OPENING HOURS")

```css
.section-label {
  font-size: var(--text-label);      /* 12px minimum; don't go smaller */
  line-height: 1.333;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-variant-ligatures: none;
}
```

- Write the label text in normal sentence case in the markup ("Opening hours") and let `text-transform` do the capitals. Screen readers then read it normally.
- Use labels for one to three words only.
- Don't track anything else. Body and headings stay at 0, apart from the title's tightening.

## Prices and hours in repair tables

```css
.table-figures, td.price, td.hours {
  font-variant-numeric: tabular-nums lining-nums;
  text-align: right;
}
```

- Tabular figures make every digit the same width, so columns line up. Apply this to any numeric column or any number that updates in place.
- Right-align numeric columns, and align the column header to match.
- Show the same number of decimals on every row ($12.50 next to $8.00, never $12.5).
- If every row uses the same currency, put it in the column header. Otherwise repeat it per row.
- Keep a time and its am/pm together with a non-breaking space (`9&nbsp;am`).
- Write ranges with an en dash: `9 am–5 pm`.
- Never truncate a price or an hour. Let it wrap or restructure the layout.
- Body prose keeps normal proportional figures.

## Links inside paragraphs

```css
p a {
  color: var(--color-link);
  text-decoration: underline;
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.15em;
}
p a:hover   { text-decoration-thickness: 0.12em; }
p a:visited { color: var(--color-link-visited); }
p a:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
```

- Keep the underline. Color alone isn't enough.
- Hover, visited and focus states must each look different from the resting state.
- Never remove the focus outline.

## Color

I need the exact hex values from Figma for these. Placeholders are marked.

| Token | Value | Requirement |
|---|---|---|
| `--color-text-muted` | *(Figma gray)* | At least 4.5:1 contrast against its background. Captions are small, so this matters. |
| `--color-link` | *(Figma blue)* | At least 4.5:1 against the page background. |
| `--color-link-visited` | *(pick one)* | Visibly different from the link color. |

If the Figma gray fails 4.5:1, darken it rather than making the text bigger.

## Please test with

- The longest real page title at 320px wide. It should wrap cleanly with no mid-word break.
- A table with mixed prices (`$8.00`, `$125.50`) to confirm the digits line up.
- 200% browser zoom and a raised default font size.
- Captions in the muted gray on every background they appear on.

## Open items for the designer

These are items I filled in or that need a Figma check before handoff:

1. **Section label size, weight and tracking** weren't in your notes. I proposed 12px / 600 / 0.08em. Replace them if Figma differs.
2. **"Tightened a bit" on the title** is `-0.02em` here. Check the Figma value.
3. **Body measure cap** (`65ch`) is my addition so paragraphs don't run too wide on desktop. Skip it if the layout already constrains width.
4. **Muted gray and link blue hexes**, plus the visited color, as noted above.
5. **Button type** is sentence case at 15px. That's a fifth size alongside 13 and 16, which is fine, but it's why it has its own token.
