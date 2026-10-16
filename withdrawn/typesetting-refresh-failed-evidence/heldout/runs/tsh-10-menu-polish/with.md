Part of why it looks amateur is the text itself. It has straight quotes, `--` standing in for dashes, hyphens in ranges, a letter x for ×, `1/2` typed out, and a bare `&`. The CSS side probably has the usual problems too: prices that don't line up, a measure that runs too wide, and no spacing rhythm. I changed only characters and styling, not wording.

```html
<h1 class="title">Fennel &amp; Ash</h1>
<p class="sub">Autumn tasting menu—5&nbsp;courses, 7:00–9:30pm</p>
<ul class="menu">
  <li><span class="dish">Charred leek, “smoked” cream, hazelnut</span> <span class="price">$14.00</span></li>
  <li><span class="dish">Beetroot cured in juniper, ½&nbsp;pear</span> <span class="price">$16.50</span></li>
  <li><span class="dish">Chef’s choice of 2&nbsp;×&nbsp;river fish</span> <span class="price">$28.00</span></li>
  <li><span class="dish">Slow lamb shoulder, anchovy &amp; rosemary</span> <span class="price">$34.00</span></li>
  <li><span class="dish">Burnt honey tart with crème fraîche</span> <span class="price">$12.00</span></li>
</ul>
<p class="foot">Pairings from $45 (3–5&nbsp;glasses). Please tell us about allergies—we’ll happily adapt.</p>
```

```css
body {
  font-size: 1.125rem;          /* body/dish size; no fixed px */
  line-height: 1.5;
  font-synthesis: none;
}

.title, .sub, .menu, .foot { max-width: 34rem; margin-inline: auto; }

.title {
  font-size: 2.5rem;
  line-height: 1.1;
  letter-spacing: -0.01em;      /* tighten display slightly */
  margin: 3rem auto 0.5rem;
  text-wrap: balance;
}

.sub {
  font-size: 1rem;
  margin-block: 0 2.5rem;       /* space after the header block */
}

.menu { list-style: none; padding: 0; }

.menu li {
  display: flex;
  justify-content: space-between;
  align-items: baseline;        /* dish and price share a baseline */
  gap: 1.5rem;
  padding-block: 0.75rem;
  border-bottom: 1px solid #0002;
}

.dish { text-wrap: pretty; }

.price {
  font-variant-numeric: tabular-nums lining-nums;  /* prices stack */
  white-space: nowrap;
  text-align: right;
}

.foot {
  font-size: 1rem;
  margin-block: 2rem 3rem;
  text-wrap: pretty;
}
```

**Text fixes (no wording changes)**
- `--` is now an em dash. `7:00-9:30pm` and `3-5` now use en dashes for the ranges.
- Straight quotes and the apostrophe are now curly: “smoked”, Chef’s, we’ll.
- `2 x` is now `2 ×`, and `1/2` is now `½`.
- `&` is now `&amp;`, which is valid HTML.
- Non-breaking spaces keep “5 courses”, “½ pear”, “2 × river fish” and “3–5 glasses” from splitting across lines.

**CSS**
- There are three sizes (2.5, 1.125 and 1rem) with a clear title/body relationship.
- The column is capped at 34rem, so lines stay short.
- Prices use tabular figures and a shared baseline with the dish, so the decimals line up down the column.
- The spacing has a rhythm: tight under the title, then more room before the list and the footer.

I assumed a screen, a light background, and your existing font. I didn't change the face or colors. The `#0002` divider is a placeholder, so match it to your palette.
