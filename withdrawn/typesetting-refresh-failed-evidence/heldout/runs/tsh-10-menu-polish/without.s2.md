Most of what reads as amateur here is typewriter habits carried into HTML: straight quotes, double hyphens, `x` for ×, `1/2` for ½, and hyphens in ranges. The CSS side adds to it, because prices that don't align and a default font stack make a menu look like a web form. I haven't changed any words, only the characters and the styling.

**HTML**

```html
<h1 class="title">Fennel &amp; Ash</h1>
<p class="sub">Autumn tasting menu — 5&nbsp;courses, 7:00–9:30pm</p>
<ul class="menu">
  <li><span class="dish">Charred leek, “smoked” cream, hazelnut</span><span class="price">$14.00</span></li>
  <li><span class="dish">Beetroot cured in juniper, ½&nbsp;pear</span><span class="price">$16.50</span></li>
  <li><span class="dish">Chef’s choice of 2&nbsp;×&nbsp;river fish</span><span class="price">$28.00</span></li>
  <li><span class="dish">Slow lamb shoulder, anchovy &amp; rosemary</span><span class="price">$34.00</span></li>
  <li><span class="dish">Burnt honey tart with crème fraîche</span><span class="price">$12.00</span></li>
</ul>
<p class="foot">Pairings from $45 (3–5&nbsp;glasses). Please tell us about allergies — we’ll happily adapt.</p>
```

**CSS**

```css
body {
  max-width: 34rem;
  margin: 4rem auto;
  padding: 0 1.5rem;
  font-family: "Cormorant Garamond", Garamond, "Iowan Old Style", Georgia, serif;
  font-size: 1.15rem;
  line-height: 1.5;
  color: #222;
  text-rendering: optimizeLegibility;
  font-kerning: normal;
  hanging-punctuation: first;
}

.title {
  font-size: 2.75rem;
  font-weight: 500;
  line-height: 1.1;
  letter-spacing: 0.04em;
  text-align: center;
  margin: 0 0 0.5rem;
}

.sub {
  text-align: center;
  font-size: 0.85rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #666;
  margin: 0 0 3rem;
}

.menu {
  list-style: none;
  margin: 0;
  padding: 0;
}

.menu li {
  display: flex;
  align-items: baseline;
  gap: 0.6rem;
  margin-bottom: 1.1rem;
}

/* dotted leader between dish and price */
.menu li::after {
  content: "";
  order: 1;
  flex: 1;
  border-bottom: 1px dotted #aaa;
  transform: translateY(-0.25em);
}
.dish  { order: 0; text-wrap: balance; }
.price { order: 2; font-variant-numeric: lining-nums tabular-nums; white-space: nowrap; }

.foot {
  margin-top: 3rem;
  font-size: 0.9rem;
  font-style: italic;
  color: #555;
  text-align: center;
  text-wrap: balance;
}
```

**What changed in the text (characters only)**
- `--` became an em dash (—) in both places.
- `7:00-9:30pm` and `3-5` now use en dashes (–), which is the correct mark for ranges.
- Straight quotes became curly: “smoked”, Chef’s, we’ll.
- `1/2` became ½, and `2 x` became `2 × `.
- `&` is now `&amp;`, which is valid HTML.
- Non-breaking spaces (`&nbsp;`) keep "5 courses", "½ pear", "2 × river fish" and "3–5 glasses" from splitting across lines.

**What the CSS fixes**
- **Font:** A serif stack replaces the browser default. Swap in whatever face you license for the brand.
- **Title and subtitle:** The title is tracked slightly. The subtitle is small, spaced capitals, which gives a clear hierarchy.
- **Dishes and prices:** Dotted leaders and tabular numerals line the prices up, so the eye can follow from dish to price.
- **Line length:** The measure is capped at about 34rem so lines don't run wide.
- **Wrapping:** `text-wrap: balance` avoids lonely last words.

I used unspaced em dashes only in the sense that the original spaces are kept around them. If you'd rather have a tighter look, remove the spaces on either side, or use thin spaces (`&thinsp;`).
