**Recommendation: a serif for marketing headings, and the system UI sans for body text and the whole product.** A serif reads as established and trustworthy, which suits law firms and money. It also contrasts clearly with the sans, so the pair won't look like a mistake.

```css
:root {
  --font-heading: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  --font-body: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
}

body { font-family: var(--font-body); }
h1, h2, h3 { font-family: var(--font-heading); font-weight: 600; }

/* invoices, ledgers, totals */
.amount, table { font-variant-numeric: tabular-nums; }

html { font-synthesis: none; }
```

**Roles**
- **Marketing headings:** the serif stack, used big and short (h1–h3, hero, section titles). It renders as Iowan Old Style on Apple devices, Palatino Linotype on Windows, and Georgia as the backstop. Don't use it for small text.
- **Body and product UI:** `system-ui` renders as San Francisco on Apple, Segoe UI on Windows and Roboto on Android. It is sturdy, clear at small sizes, and has the weights you need.
- **Product UI:** keep it all sans. Use weight and size for hierarchy, and turn on `tabular-nums` wherever money appears so the columns line up.
- **Mono:** only for invoice numbers, matter IDs or codes, if you show them.

**Caveats**
- The heading will look different on each platform, since each picks the first font it has. Android has none of the named serifs, so it falls to the system serif. Check the site once on Mac, Windows and an Android phone.
- If you want the heading identical everywhere, that needs a loaded font, so it has to wait for legal. When it does, self-host one serif and keep the system sans for body text. Have legal confirm the license covers web and embedding use.
