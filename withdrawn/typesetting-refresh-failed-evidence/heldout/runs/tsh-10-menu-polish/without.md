The wording can stay exactly as it is. What's making it look amateur is mostly the typographic characters, plus a few layout issues.

**Why it looks amateur**
- **Typewriter characters.** Straight quotes (`"smoked"`, `Chef's`), `--` for a dash, a hyphen in the ranges (`7:00-9:30pm`, `3-5`), the letter `x` for a multiplication sign, and `1/2` typed as three characters are all typewriter habits. Each has a proper glyph.
- **Bare `&`.** This is also invalid HTML. It should be `&amp;`.
- **Prices.** They aren't aligned in a column, and the digits are probably proportional, so the figures don't line up.
- **Hierarchy and spacing.** Everything is probably one size and weight, with default line spacing and no limit on line length.

**HTML** (same words, correct glyphs)

```html
<h1 class="title">Fennel &amp; Ash</h1>
<p class="sub">Autumn tasting menu — 5 courses, 7:00–9:30pm</p>
<ul class="menu">
  <li><span class="dish">Charred leek, “smoked” cream, hazelnut</span> <span class="price">$14.00</span></li>
  <li><span class="dish">Beetroot cured in juniper, ½ pear</span> <span class="price">$16.50</span></li>
  <li><span class="dish">Chef’s choice of 2 × river fish</span> <span class="price">$28.00</span></li>
  <li><span class="dish">Slow lamb shoulder, anchovy &amp; rosemary</span> <span class="price">$34.00</span></li>
  <li><span class="dish">Burnt honey tart with crème fraîche</span> <span class="price">$12.00</span></li>
</ul>
<p class="foot">Pairings from $45 (3–5 glasses). Please tell us about allergies — we’ll happily adapt.</p>
```

**CSS**

```css
body {
  max-width: 34rem;
  margin: 4rem auto;
  padding: 0 1.5rem;
  font-family: "Cormorant Garamond", Georgia, "Times New Roman", serif;
  font-size: 1.125rem;
  line-height: 1.5;
  color: #2a2623;
  background: #faf7f2;
  text-rendering: optimizeLegibility;
  font-kerning: normal;
  hanging-punctuation: first;
}

.title {
  margin: 0 0 .5rem;
  font-size: 2.75rem;
  font-weight: 500;
  letter-spacing: .02em;
  line-height: 1.1;
  text-align: center;
}

.sub {
  margin: 0 0 3rem;
  text-align: center;
  font-size: .8rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #6f665e;
}

.menu {
  list-style: none;
  margin: 0 0 3rem;
  padding: 0;
}

.menu li {
  display: flex;
  align-items: baseline;
  gap: .5rem;
  padding: .6rem 0;
}

/* dotted leader between dish and price */
.menu li::after {
  content: "";
  order: 1;
  flex: 1;
  border-bottom: 1px dotted #b8aea3;
  transform: translateY(-.25em);
}
.dish  { order: 0; }
.price {
  order: 2;
  font-variant-numeric: lining-nums tabular-nums;
  white-space: nowrap;
}

.foot {
  font-size: .9rem;
  font-style: italic;
  text-align: center;
  color: #6f665e;
  text-wrap: balance;
}
```

**What changed**
- **Glyphs:**
  - `--` is now an em dash (—).
  - Number ranges use an en dash (–).
  - Quotes and apostrophes are curly.
  - `x` is now `×`.
  - `1/2` is now `½`.
  - `&` is now `&amp;`.
- **Hierarchy:** the title is large and centered. The subtitle is small, letterspaced caps in a muted color. The footer is small italic.
- **Prices:** a flex row with a dotted leader and tabular lining numerals puts all the prices in one aligned column.
- **Readability:** a serif face, a narrow measure of about 34rem, and generous line spacing.

Two things to check:
- Cormorant Garamond needs to be loaded (Google Fonts or self-hosted). Without it, the page falls back to Georgia, which still looks fine.
- I left `$14.00` and `$16.50` as written. If you ever want a cleaner look, dropping the `.00` from the prices would be a content decision, so I didn't make it.
