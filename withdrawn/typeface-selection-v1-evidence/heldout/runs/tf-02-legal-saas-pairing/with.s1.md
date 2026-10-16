**Pairing:** a system serif for marketing headings and the system UI sans for body and the product. The serif gives a law-firm feel (credible, established), and the sans keeps the interface plain and legible.

```css
--font-heading: "Iowan Old Style", Charter, "Bitstream Charter", Georgia, serif;
--font-body: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace; /* only if you show IDs or code */

h1, h2, h3 { font-family: var(--font-heading); font-weight: 700; font-synthesis: none; }
body { font-family: var(--font-body); font-synthesis: none; }
.amount, td.num { font-variant-numeric: tabular-nums lining-nums; }
```

- **Marketing site:** serif headings, large and short, over sans body text. This is where the "bland" feeling goes away.
- **Product UI:** keep the sans for everything, and use the serif at most for page titles. Dense billing tables read better in a sturdy sans.
- **Money:** always set `tabular-nums` so invoice columns align. Georgia defaults to old-style figures, so `lining-nums` stops amounts looking uneven in headings.

**What it renders as:**
- **Mac and iOS:** Iowan Old Style for headings and San Francisco for body.
- **Windows:** Georgia for headings and Segoe UI for body.
- **Android:** Roboto for body. Neither Iowan, Charter nor Georgia ships there, so headings fall to the generic `serif` (Noto Serif on most devices). It's acceptable, but check it on a real device.

Because the stack renders differently per platform, the site won't look identical everywhere. That's the cost of avoiding web fonts.

**Later upgrade:** once legal clears fonts, swap the first name in each stack for a licensed or open-license face. The fallbacks mean nothing else changes. I haven't checked any license terms, so confirm with the foundry before picking one.

I assumed a Latin-script audience and a screen-only product.
