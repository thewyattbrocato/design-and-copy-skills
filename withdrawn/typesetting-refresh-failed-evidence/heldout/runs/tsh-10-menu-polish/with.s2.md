The "amateur" feeling comes mostly from typewriter punctuation and unaligned prices. Your wording is untouched. I only swapped characters for their typographic forms and added CSS.

**HTML**

```html
<h1 class="title">Fennel &amp; Ash</h1>
<p class="sub">Autumn tasting menu — 5 courses, 7:00–9:30pm</p>
<ul class="menu">
  <li><span class="dish">Charred leek, “smoked” cream, hazelnut</span> <span class="price">$14.00</span></li>
  <li><span class="dish">Beetroot cured in juniper, ½ pear</span> <span class="price">$16.50</span></li>
  <li><span class="dish">Chef’s choice of 2&nbsp;×&nbsp;river fish</span> <span class="price">$28.00</span></li>
  <li><span class="dish">Slow lamb shoulder, anchovy &amp; rosemary</span> <span class="price">$34.00</span></li>
  <li><span class="dish">Burnt honey tart with crème fraîche</span> <span class="price">$12.00</span></li>
</ul>
<p class="foot">Pairings from $45 (3–5 glasses). Please tell us about allergies — we’ll happily adapt.</p>
```

**CSS**

```css
body {
  font-size: 1rem;
  line-height: 1.5;
  font-synthesis: none;
}

.title,
.sub,
.menu,
.foot { max-width: 36rem; }

.title {
  font-size: clamp(2rem, 5vw, 2.5rem);
  line-height: 1.1;
  letter-spacing: -0.015em;
  margin: 0 0 0.5rem;
  text-wrap: balance;
}

.sub {
  font-size: 1.125rem;
  margin: 0 0 2rem;
}

.menu {
  list-style: none;
  padding: 0;
  margin: 0 0 2rem;
}

.menu li {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1.5rem;
  padding: 0.75rem 0;
  border-bottom: 1px solid currentColor; /* swap for a soft tint of your text colour */
}

.dish { text-wrap: pretty; }

.price {
  flex: none;
  text-align: right;
  font-variant-numeric: tabular-nums lining-nums;
}

.foot {
  margin: 0;
  text-wrap: pretty;
}
```

**What changed and why**
- **Punctuation:**
  - `--` became an em dash.
  - The `7:00-9:30pm` and `3-5` ranges now use en dashes.
  - Straight quotes and apostrophes are curly.
  - `2 x` is now `2 ×`, with non-breaking spaces so it can't split across lines.
  - `1/2` is now `½`.
  - `&` is escaped as `&amp;` in the HTML.
- **Prices:** they're right-aligned with tabular figures, so the decimals stack in a column, and they sit on the same baseline as the dish names.
- **Sizes:** there are only four, each with a job (title, subtitle, body, footer). The footer stays at body size because it carries the allergy instruction.
- **Spacing and measure:** the title has tighter leading and slight negative tracking. The page is capped at 36rem so the dish and price don't drift far apart on wide screens.
- **Wrapping:** the title balances and the longer lines wrap more cleanly (`text-wrap`).

I didn't set a typeface because none was specified. If the page is still in the browser default, a good serif or a refined sans will add more polish than anything above. The border colour is a placeholder, so tint it to your palette.
