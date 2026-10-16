Most of the sheet already follows good text practice. The "plain" feel comes mainly from headings set at regular weight with no tracking, and from no lede to open the essay. Here is a revision that addresses those:

```css
.essay {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 1.125rem;
  line-height: 1.65;
  max-width: 36rem;
  margin: 0 auto;
  padding: 0 1.25rem;
  color: #222;
  font-synthesis: none;
}
.essay h1 {
  font-size: clamp(2rem, 5vw, 2.75rem);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.015em;
  text-wrap: balance;
  margin: 0 0 0.5em;
}
.essay h2 {
  font-size: 1.5rem;
  font-weight: 700;
  line-height: 1.25;
  text-wrap: balance;
  margin: 2.2em 0 0.6em;
}
.essay p { margin: 0 0 1em; text-wrap: pretty; }
.essay .lede {
  font-size: 1.25rem;
  line-height: 1.5;
}
.essay .kicker {
  font: 600 0.75rem/1 system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 1rem;
}
.essay blockquote {
  margin: 1.5em 0;
  padding-left: 1.25rem;
  border-left: 3px solid #bbb;
  font-style: italic;
}
.essay .stat { font-variant-numeric: tabular-nums; }
```

**Changes**

- **`font-synthesis: none`** on `.essay`: stops the browser from faking bold or italic if a real face is missing.
- **Headings `font-weight: 700`** (h1 and h2): the main reason the page reads as plain. Georgia's bold gives the headings a clear presence without changing their sizes.
- **h1 `letter-spacing: -0.015em`**: display sizes look tighter and more deliberate at this size.
- **`text-wrap: balance`** on headings: stops a two-line h1 or h2 from leaving a single word on its second line.
- **`text-wrap: pretty`** on paragraphs: avoids orphans at the end of paragraphs. It doesn't change the measure or the leading.
- **`.lede`**: a new optional class for the opening paragraph, at 1.25rem with 1.5 leading. This is the most visible editorial device here. Add `class="lede"` to the first paragraph in the markup, or delete this rule if you don't want it.

**Left alone, because they already work**

- Body size, measure (36rem is about 60 to 68 characters in Georgia at this size), and the 1.65 leading, which is within range.
- The h2 spacing. The space above is about four times the space below, which keeps each section clearly separate.
- The kicker, the blockquote and `.stat`.

A bigger change, such as a display serif for the headings, would change the typeface, which is a separate decision. I haven't rendered this, so check the headings at your real content width before you ship.
