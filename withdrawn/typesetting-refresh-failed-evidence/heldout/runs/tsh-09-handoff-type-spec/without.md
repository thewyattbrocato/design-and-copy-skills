Below is the spec, ready to paste. Your Figma notes didn't cover a few values, so I filled them with sensible defaults and marked each one **[confirm]**. Check those against Figma before you hand it over.

---

# Typography Spec: Spoke & Chain

## Font family

```css
--font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

- Use Inter everywhere. If it fails to load, fall back to the system font through the stack above.
- Load Inter as a self-hosted variable font with `font-display: swap`.
- Set `font-family: var(--font-sans)` on `body`. Form controls and buttons don't inherit it by default, so add `font: inherit` to them.

## Type scale

| Token | Size / Line height | Weight | Letter-spacing | Color | Used for |
|---|---|---|---|---|---|
| `title` | 32 / 38 | 700 (bold) | -0.02em **[confirm]** | `--text` | Page title (h1) |
| `heading` | 22 / 28 | 600 (semibold) | 0 | `--text` | Section heading (h2) |
| `body` | 16 / 24 | 400 (regular) | 0 | `--text` | Default text |
| `small` | 13 / 18 | 400 (regular) | 0 | `--text-muted` | Captions, small print |
| `button` | 15 / 20 **[confirm]** | 500 (medium) | 0 | per button style | All buttons |
| `label` | 12 / 16 **[confirm]** | 600 **[confirm]** | +0.08em **[confirm]** | `--text-muted` **[confirm]** | Uppercase section labels |

```css
.title   { font: 700 2rem/2.375rem var(--font-sans); letter-spacing: -0.02em; }
.heading { font: 600 1.375rem/1.75rem var(--font-sans); }
body     { font: 400 1rem/1.5rem var(--font-sans); }
.small   { font: 400 0.8125rem/1.125rem var(--font-sans); color: var(--text-muted); }
.button  { font: 500 0.9375rem/1.25rem var(--font-sans); }
```

Use `rem` for sizes so the type respects the user's browser font-size setting. The values above assume a 16px root.

## Colors

| Token | Value | Notes |
|---|---|---|
| `--text` | **[confirm: Figma hex]** | Primary text |
| `--text-muted` | **[confirm: Figma hex]** | Captions and labels. It must be at least 4.5:1 against its background, because 13px text counts as small. `#6B7280` on white is 4.8:1 if you need a reference. |
| `--link` | **[confirm: Figma hex]** | Inline link blue. It also needs at least 4.5:1 against the background. |

## Numbers in tables (prices and hours)

Prices and hours in the repair tables must line up in columns. Inter's default digits are proportional, so turn on tabular figures:

```css
.table-num, td.price, td.hours {
  font-variant-numeric: tabular-nums;
  text-align: right;   /* prices; see note on hours */
}
```

- `tabular-nums` makes every digit the same width, so decimals and colons align vertically.
- Right-align price columns so the decimal points line up. Left-align hours columns if they're ranges like "10:00 – 18:00". Since every digit has the same width, they will still line up.
- Make sure every price shows the same number of decimals (`$8.00`, not `$8`), or the columns will still look ragged.
- Apply `tabular-nums` to these cells only. Elsewhere, Inter's default proportional digits look better.

## Section labels (e.g. "OPENING HOURS")

```css
.label {
  font: 600 0.75rem/1rem var(--font-sans);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
}
```

- Write the content in normal case ("Opening hours") and let `text-transform: uppercase` do the capitalizing. Screen readers then don't spell out the letters, and the copy stays editable.
- Uppercase text needs positive letter-spacing to stay legible. Don't remove it.

## Links inside paragraphs

```css
p a {
  color: var(--link);
  text-decoration: underline;
  text-underline-offset: 0.15em;
  text-decoration-thickness: 1px;
}
p a:hover { text-decoration-thickness: 2px; }
p a:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
```

- Links are always underlined, not only on hover. Color alone isn't enough for people who can't distinguish the blue.
- This applies to links inside running text only. Buttons and nav links are not underlined and use their own styles.

## Buttons

- Text is 15px, weight 500, with no letter-spacing and no uppercase.
- Make the tap target at least 44px tall (padding handles this, not the line-height).
- Color, padding, and radius belong in the button component spec, not here.

## Open questions for the designer

1. Exact hex values for text, muted gray, and link blue.
2. The title's "tightened a bit". I assumed -0.02em, so please confirm against Figma.
3. Size, weight, and tracking of the uppercase label. Mine are guesses.
4. Button line-height, which wasn't specified.

---

Once you've resolved the **[confirm]** items, the doc has no guesswork left for the dev. If you send me the Figma values, I can drop them in and give you a final version.
