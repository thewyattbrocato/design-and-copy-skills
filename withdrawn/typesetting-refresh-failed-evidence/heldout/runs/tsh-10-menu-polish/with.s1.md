The page looks amateur mostly because of the character-level details and the lack of a layout, not the wording. Here is the cleaned-up version. Every word is unchanged.

```html
<h1 class="title">Fennel &amp; Ash</h1>
<p class="sub">Autumn tasting menu—5 courses, 7:00–9:30pm</p>
<ul class="menu">
  <li><span class="dish">Charred leek, “smoked” cream, hazelnut</span> <span class="price">$14.00</span></li>
  <li><span class="dish">Beetroot cured in juniper, ½ pear</span> <span class="price">$16.50</span></li>
  <li><span class="dish">Chef’s choice of 2&nbsp;×&nbsp;river fish</span> <span class="price">$28.00</span></li>
  <li><span class="dish">Slow lamb shoulder, anchovy &amp; rosemary</span> <span class="price">$34.00</span></li>
  <li><span class="dish">Burnt honey tart with crème fraîche</span> <span class="price">$12.00</span></li>
</ul>
<p class="foot">Pairings from $45 (3–5 glasses). Please tell us about allergies—we’ll happily adapt.</p>
```

```css
body {
  font-family: Georgia, "Times New Roman", serif; /* swap in your house face */
  font-size: 1rem;
  line-height: 1.5;
  font-synthesis: none;
  color: #222;
  background: #fbf9f5;
  max-width: 36rem;
  margin: 0 auto;
  padding: 4rem 1.5rem;
}

.title {
  font-size: 2.5rem;
  font-weight: 400;
  line-height: 1.1;
  letter-spacing: -0.01em;
  margin: 0 0 0.5rem;
  text-wrap: balance;
}

.sub {
  margin: 0 0 2.5rem;
  color: #666;
}

.menu {
  list-style: none;
  margin: 0 0 2.5rem;
  padding: 0;
}

.menu li {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1.5rem;
  padding: 0.875rem 0;
  border-bottom: 1px solid #e3ded4;
}

.menu li:first-child { border-top: 1px solid #e3ded4; }

.dish { text-wrap: pretty; }

.price {
  font-variant-numeric: tabular-nums lining-nums;
  white-space: nowrap;
  text-align: right;
}

.foot {
  margin: 0;
  color: #444;
  text-wrap: pretty;
}
```

**Text fixes (characters only, no wording changes)**
- `--` is now an em dash. I used one dash style throughout.
- `7:00-9:30pm` and `3-5` now use en dashes, which is the correct mark for ranges.
- Straight quotes are now curly (“smoked”, Chef’s, we’ll).
- `1/2` is now ½, and `2 x` is now `2 × `. The non-breaking spaces keep “2 × river fish” from splitting across lines.
- `&` is now `&amp;`, which is valid HTML.

**Layout fixes**
- **Prices:** they sit in a right-aligned column with tabular lining figures, so the decimals stack. Each price is on the same baseline as its dish and can't wrap.
- **Measure:** the page is capped at 36rem, so lines stay short and the menu reads as a single column.
- **Sizes:** there are only two, a 2.5rem title and 1rem for everything else. Titles have tighter leading (1.1) and body text has 1.5.
- **Spacing:** the rhythm is consistent, with hairline rules between courses. The allergy note stays at body size because guests act on it.

**Assumptions:** this is for screen with a light background, and I used Georgia as a stand-in for your real typeface. If you have a house font, put it in the `font-family` line.
