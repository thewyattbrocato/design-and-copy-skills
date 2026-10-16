Here's a spec you can paste into the ticket. Your Figma values are used as given. Anything you didn't specify is marked **[CONFIRM]** with a proposed default, so check those against Figma before handing off. They're collected at the bottom.

---

# Typography Spec: Spoke & Chain

## 1. Font family

**Inter**, with the system UI font as fallback:

```css
--font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

- Load Inter as a variable font (self-hosted woff2 preferred) with `font-display: swap`.
- Weights used: 400, 500, 600, 700.
- Apply `--font-sans` on `body`. Buttons and inputs don't inherit it by default, so set `font-family: inherit` on them.

## 2. Type scale

Sizes are in px with the rem equivalent (assuming a 16px root). Use rem so user font-size settings are respected. Use unitless line-heights.

| Token | Size / Line height | Weight | Other | Color |
|---|---|---|---|---|
| `title` (page title, h1) | 32 / 38 (2rem / 1.1875) | 700 | `letter-spacing: -0.02em` **[CONFIRM]** | `--text` |
| `heading` (section, h2) | 22 / 28 (1.375rem / 1.2727) | 600 | none | `--text` |
| `body` | 16 / 24 (1rem / 1.5) | 400 | none | `--text` |
| `caption` (small print) | 13 / 18 (0.8125rem / 1.3846) | 400 | none | `--text-muted` |
| `button` | 15 (0.9375rem) | 500 | line-height **[CONFIRM]** 1.2 | inherits from button style |
| `label` (uppercase eyebrow) | 12 / 16 (0.75rem / 1.3333) **[CONFIRM]** | 600 **[CONFIRM]** | `text-transform: uppercase; letter-spacing: 0.08em` **[CONFIRM]** | `--text-muted` **[CONFIRM]** |

```css
:root {
  --text: #111827;        /* [CONFIRM] */
  --text-muted: #6B7280;  /* [CONFIRM] 4.8:1 on white, passes AA for small text */
  --link: #1D4ED8;        /* [CONFIRM] */
}
```

## 3. Semantics

- Use real elements: the page title is the single `<h1>`, section headings are `<h2>`, and so on. Style by class or token, not by tag, so visual size doesn't dictate heading level.
- Labels like "OPENING HOURS" should be **typed in normal case in the HTML** and uppercased with CSS (`text-transform`). This keeps screen readers from spelling out letters. If a label introduces a section, keep the real `<h2>` beneath it and make the label a `<p>` or `<span>`. Don't use it as the heading.

## 4. Numbers in repair tables (prices and hours)

Prices and hours must line up in columns:

```css
.table-num {
  font-variant-numeric: tabular-nums;
  text-align: right;
}
```

- Apply to every price cell and every hours/time cell.
- Right-align price columns so decimal points line up. Always show two decimals (e.g. `$8.00`, not `$8`) so alignment holds.
- Use the same format for hours throughout (e.g. `9:00 – 17:00`). Tabular figures only align if the strings have the same shape.
- Inter's tabular figures are included in the standard web build. If you subset the font, keep the `tnum` feature.

## 5. Links in paragraphs

```css
.prose a {
  color: var(--link);
  text-decoration: underline;
  text-underline-offset: 0.15em;
}
.prose a:hover { /* [CONFIRM] hover style */ }
.prose a:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
```

- Links stay underlined at rest, since color alone isn't enough to mark them as links.
- Link text inherits the surrounding size and weight.
- Link color must have at least 4.5:1 contrast against the background. `#1D4ED8` on white is about 6.7:1.

## 6. Responsive behavior

All sizes above are the mobile-first base values. **[CONFIRM]** whether anything scales at larger breakpoints. If it doesn't, leave these values unchanged at every width.

## 7. Acceptance checklist

- [ ] Inter loads, and the fallback stack renders without layout breakage when it doesn't
- [ ] All six styles match the table above, in rem
- [ ] Browser font-size increase to 200% doesn't clip or overlap text
- [ ] Price and hour columns align digit-for-digit in the repair tables
- [ ] Caption and label gray meets 4.5:1 contrast on its background
- [ ] Inline links are blue and underlined, with a visible keyboard focus state
- [ ] Uppercase labels are CSS-transformed, not typed in caps

---

## Open items to confirm before sending

These weren't in your notes, so I filled them in with reasonable defaults:

1. **Title tracking:** you said "tightened a bit." I used `-0.02em`. Replace it with your Figma value (Figma shows it as a %, which maps directly to em).
2. **Uppercase label:** size, weight, tracking and color weren't specified. I proposed 12/16, 600, 0.08em, muted gray.
3. **Colors:** the hex values for text, muted gray and link blue are placeholders. Paste your actual values.
4. **Button line-height:** only the size (15) was given.
5. **Link hover state:** not specified.
6. **Breakpoints:** confirm whether anything scales up on larger screens.
