Here's a spec you can paste into the ticket. Your Figma notes didn't cover a few values, so I filled them in with sensible defaults and marked them **[confirm]**. Check those against Figma before you send it.

---

# Spoke & Chain: Typography Spec

## Font
- **Family:** Inter, falling back to the system UI font.
- **Stack:** `"Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
- Load Inter as a variable font (weights 400–700), self-hosted, with `font-display: swap`. **[confirm]** that this is how Inter is delivered.
- All sizes are in `rem` (1rem = 16px) so the type respects the user's browser font-size setting. Line heights are unitless ratios.

## Type styles

| Token | Size / line-height | Weight | Other | Color |
|---|---|---|---|---|
| `title` | 32 / 38px (2rem / 1.1875) | 700 | letter-spacing `-0.02em` **[confirm]** | text |
| `heading` | 22 / 28px (1.375rem / 1.273) | 600 | none | text |
| `body` | 16 / 24px (1rem / 1.5) | 400 | none | text |
| `caption` | 13 / 18px (0.8125rem / 1.385) | 400 | none | muted gray |
| `button` | 15px (0.9375rem), line-height 1.333 (20px) **[confirm]** | 500 | none | per button style |
| `label` | 12 / 16px (0.75rem / 1.333) **[confirm]** | 600 **[confirm]** | uppercase, letter-spacing `0.08em` | muted gray **[confirm]** |

## Colors
- **Text:** use the existing text color token.
- **Muted gray (captions, labels):** `#6B7280`. It has about 4.8:1 contrast on white, which passes WCAG AA for small text. If Figma uses a different gray, use that one, but don't go lighter than about `#6B7280` on white. **[confirm hex]**
- **Link blue:** `#1D4ED8` **[confirm hex]**, with about 6.7:1 contrast on white.

## Specific behaviors

**Tables (prices and hours)**
- Apply `font-variant-numeric: tabular-nums;` to price and hours cells so digits have equal widths and line up in columns.
- Right-align price columns. Align hours columns consistently, for example left-aligned and all in the same format.
- Inter supports tabular figures through its `tnum` feature. If the font is subset, make sure `tnum` isn't stripped.

**Section labels (e.g. "OPENING HOURS")**
- Use `text-transform: uppercase` in CSS. Don't type the text in capitals in the markup, so screen readers and copy/paste get normal text.
- The wide letter-spacing (`0.08em`) is what makes small caps legible, so keep it.
- Put the label directly above its section heading, with a gap of about 4–8px **[confirm spacing from Figma]**.

**Links inside paragraphs**
- Use the link blue with `text-decoration: underline;`.
- Set `text-underline-offset: 2px;` and `text-decoration-thickness: 1px;` **[confirm]**.
- Hover and focus: darken the blue slightly and keep the underline. Keep a visible focus ring (`:focus-visible`).
- Visited links stay the same blue unless design says otherwise.
- Don't underline buttons or nav links. This applies only to links in running text.

## Reference CSS

```css
:root {
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, sans-serif;
  --color-muted: #6B7280;
  --color-link: #1D4ED8;
}

body { font: 400 1rem/1.5 var(--font-sans); }

.title   { font: 700 2rem/1.1875 var(--font-sans); letter-spacing: -0.02em; }
.heading { font: 600 1.375rem/1.273 var(--font-sans); }
.caption { font: 400 0.8125rem/1.385 var(--font-sans); color: var(--color-muted); }
.button  { font: 500 0.9375rem/1.333 var(--font-sans); }

.label {
  font: 600 0.75rem/1.333 var(--font-sans);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--color-muted);
}

.table-num { font-variant-numeric: tabular-nums; }

p a {
  color: var(--color-link);
  text-decoration: underline;
  text-underline-offset: 2px;
  text-decoration-thickness: 1px;
}
```

## Notes for the dev
- Figma line heights are exact. Please don't round them.
- Don't add other sizes or weights. If something doesn't fit one of these six styles, ask the designer.
- Because the design is mobile-first, there are no desktop size overrides yet. These values apply at all breakpoints unless a later ticket says otherwise.

---

**Values I made up, so please check them:**
- The title's letter-spacing (I used `-0.02em` for "tightened a bit").
- The label's size, weight and color.
- The button's line-height.
- The two hex colors.
- The link underline details.

If Figma has exact numbers for any of these, swap them in.
