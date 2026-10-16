The page looks amateur because of two things: typewriter-style punctuation and no typographic system (no hierarchy, alignment, or number styling). Neither needs a wording change.

## HTML

The text is the same, but the characters are correct.

```html
<h1 class="title">Fennel &amp; Ash</h1>
<p class="sub">Autumn tasting menu — 5&nbsp;courses, 7:00–9:30pm</p>
<ul class="menu">
  <li><span class="dish">Charred leek, “smoked” cream, hazelnut</span> <span class="price">$14.00</span></li>
  <li><span class="dish">Beetroot cured in juniper, ½&nbsp;pear</span> <span class="price">$16.50</span></li>
  <li><span class="dish">Chef’s choice of 2&nbsp;×&nbsp;river fish</span> <span class="price">$28.00</span></li>
  <li><span class="dish">Slow lamb shoulder, anchovy &amp; rosemary</span> <span class="price">$34.00</span></li>
  <li><span class="dish">Burnt honey tart with crème fraîche</span> <span class="price">$12.00</span></li>
</ul>
<p class="foot">Pairings from&nbsp;$45 (3–5 glasses). Please tell us about allergies — we’ll happily adapt.</p>
```

What changed:
- `--` became an em dash (—).
- The ranges `7:00-9:30` and `3-5` now use en dashes (–).
- Straight quotes and apostrophes became curly: “smoked”, Chef’s, we’ll.
- `1/2` became ½.
- `2 x` became `2 × `, a real multiplication sign.
- `&` is now `&amp;`, which is valid HTML.
- Non-breaking spaces stop orphans like a lone "pear" or "$45" wrapping onto its own line.

## CSS

You didn't include any, so this is a starting point. Swap in your own fonts if you have them.

```css
body {
  max-width: 34rem;
  margin: 4rem auto;
  padding: 0 1.5rem;
  font-family: "Iowan Old Style", Georgia, serif;
  font-size: 1.0625rem;
  line-height: 1.5;
  color: #222;
  background: #faf8f4;
  text-rendering: optimizeLegibility;
  font-kerning: normal;
  hanging-punctuation: first;
}

.title {
  font-size: 2.5rem;
  font-weight: 400;
  letter-spacing: 0.02em;
  line-height: 1.1;
  margin: 0 0 0.5rem;
  text-align: center;
}

.sub {
  text-align: center;
  font-size: 0.8125rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #6b655c;
  margin: 0 0 3rem;
}

.menu { list-style: none; padding: 0; margin: 0 0 3rem; }

.menu li {
  display: flex;
  align-items: baseline;
  gap: 1rem;
  padding: 0.9rem 0;
  border-bottom: 1px solid #e4dfd6;
}
.menu li:last-child { border-bottom: 0; }

.dish { flex: 1; text-wrap: balance; }

.price {
  font-variant-numeric: tabular-nums lining-nums;
  white-space: nowrap;
  color: #6b655c;
}

.foot {
  font-size: 0.9375rem;
  font-style: italic;
  color: #6b655c;
  text-align: center;
  text-wrap: balance;
}
```

The CSS does these things:
- **Hierarchy:** the title is large, the subtitle is small spaced caps, the dishes are regular size, and the footer is muted italic. The original probably had everything at similar weight.
- **Alignment:** prices sit flush right with tabular figures, so the decimals line up in a column.
- **Measure and rhythm:** the narrow column, consistent line height, and row dividers keep it readable.
- **Colour:** warm off-white and softened greys instead of pure black on white.

Optional, and it would change the text: many fine-dining menus drop the `.00` and the `$` entirely (`14`, `16.50`). I left it since you said the wording is final.
