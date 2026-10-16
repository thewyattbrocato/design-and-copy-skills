Here's a spec you can paste into the ticket. A few values weren't in your Figma notes, so I filled them in and marked them **(assumed)**. Check those before you send it.

---

# Spoke & Chain: Typography Spec

## Principles
- Sizes are in `rem` (1rem = 16px) so the user's browser text setting is respected. Don't use fixed `px`.
- Line heights are unitless, so they scale with the font size.
- Use real font weights only, never faux bold or italic.

## Font family

```css
:root {
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
html { font-family: var(--font-sans); font-synthesis: none; }
```

- Load Inter at weights 400, 500, 600 and 700 (a variable font is fine). Use `font-display: swap`.
- If Inter fails to load, the system font is used with no further tweaks.

## Roles

| Role | Size | Line height | Weight | Tracking | Notes |
|---|---|---|---|---|---|
| Page title | 2rem (32px) | 1.1875 (38px) | 700 | -0.02em | `text-wrap: balance` |
| Section heading | 1.375rem (22px) | 1.2727 (28px) | 600 | 0 | `text-wrap: balance` |
| Body | 1rem (16px) | 1.5 (24px) | 400 | 0 | `text-wrap: pretty` |
| Caption / small print | 0.8125rem (13px) | 1.3846 (18px) | 400 | 0 | Muted gray, see color note |
| Button | 0.9375rem (15px) | 1.25 **(assumed)** | 500 | 0 | Sentence case, no uppercase |
| Section label | 0.75rem (12px) **(assumed)** | 1.333 | 600 **(assumed)** | +0.06em | Uppercase, see below |

```css
:root {
  --text-title: 2rem;      --leading-title: 1.1875;  --track-title: -0.02em;
  --text-section: 1.375rem; --leading-section: 1.2727;
  --text-body: 1rem;       --leading-body: 1.5;
  --text-small: 0.8125rem; --leading-small: 1.3846;
  --text-button: 0.9375rem;
  --text-label: 0.75rem;   --track-label: 0.06em;
}
```

## Details by role

**Page title.** One per page, on the `h1`. The slight tightening (-0.02em) is only for this size. Don't apply negative tracking to anything smaller.

**Section label (e.g. "OPENING HOURS").**
- Write the text in sentence case in the markup and use `text-transform: uppercase`. That keeps screen readers and copy/paste clean.
- Set it at 12px, weight 600, `letter-spacing: 0.06em`, with `font-variant-ligatures: none`.
- Keep labels short (a few words). Don't use all caps for anything longer.
- It sits directly above its section heading or content. Use the muted gray from captions unless the design says otherwise.

**Body.**
- Cap paragraph width with `max-width: 65ch` on the text element, not the page wrapper. This matters on tablet and desktop. On mobile the screen width already limits it.
- Paragraphs are separated by a gap of about 1em (`margin-block: 0 1em`). Don't also indent the first line.

**Caption / small print.**
- The muted gray must reach at least **4.5:1 contrast** against its background. At 13px, a light gray that looks fine in Figma often fails. Please check the hex against WCAG AA.
- Don't use this style for anything the user needs to act on, such as prices, errors or instructions. Those use body size.

**Buttons.** 15px / 500, sentence case, no letter-spacing. Line height and padding come from the button component. The tap target should be at least 44px tall.

**Heading spacing (assumed).** There's more space above a heading than below it, at roughly 2:1. For example, a section heading has 2rem above and 0.75rem below. The heading then sits with the content it introduces. Please confirm against Figma.

## Prices and hours in repair tables

```css
.repair-table td.num,
.repair-table .price,
.repair-table .hours {
  font-variant-numeric: tabular-nums lining-nums;
  text-align: right;
}
```

- Use tabular figures so every digit has the same width and the columns stack. Inter supports this natively.
- Right-align numeric columns, and use the same number of decimals on every row (e.g. all `$12.00`, not a mix of `$12` and `$12.50`).
- Put the same class on the column header cell so the header aligns with the numbers beneath it.
- Use proportional (default) figures everywhere else, including prose.
- Put a non-breaking space between a number and its unit (`2&nbsp;hrs`) so they never split across lines.
- Prices are body size (16px), not caption size.

## Links inside paragraphs

```css
p a {
  color: var(--link);              /* brand blue, hex from Figma */
  text-decoration: underline;
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.15em;
}
p a:hover { text-decoration-thickness: 0.12em; }
p a:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
```

- Keep the underline at rest. Blue alone isn't enough of a cue for everyone.
- The link blue needs at least 4.5:1 contrast on the background.
- Hover, focus and visited states must each look different from the resting state. Never remove the focus outline.

## What to test
- The longest section heading and page title at 320px width, to check wrapping.
- A repair table with mixed values like `$8.00`, `$125.50` and `1.5 hrs`, to check the columns line up.
- A caption that wraps to two lines.
- 200% browser zoom and the largest system text size.
- Fallback rendering with Inter blocked (system font).

---

**Open items for you to fill in before sending:**
1. The label's size and weight. I assumed 12px / 600, since your notes didn't say.
2. Hex values for the muted gray and the link blue. Both need a contrast check.
3. Button line height and the spacing between headings and content.
4. Whether "tightened a bit" in Figma means -2%. I used -0.02em.
