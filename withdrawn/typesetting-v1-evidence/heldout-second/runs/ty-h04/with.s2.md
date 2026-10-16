Your stylesheet is mostly sound. The measure is about 64 characters, body leading is comfortable, the heading spacing is right and the kicker is tracked. So I changed only the details that make it look plain, and the sizes and layout stay as they were.

```css
.essay {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 1.125rem;
  line-height: 1.6;
  max-width: 36rem;
  margin: 0 auto;
  padding: 0 1.25rem;
  color: #222;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  font-kerning: normal;
}
.essay h1 {
  font-size: clamp(2rem, 5vw, 2.75rem);
  line-height: 1.12;
  letter-spacing: -0.015em;
  margin: 0 0 0.5em;
  text-wrap: balance;
}
.essay h2 {
  font-size: 1.5rem;
  line-height: 1.25;
  letter-spacing: -0.01em;
  margin: 2.2em 0 0.6em;
  text-wrap: balance;
}
.essay p {
  margin: 0 0 1em;
  text-wrap: pretty;
}
.essay .kicker {
  font: 600 0.75rem/1 system-ui, sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #8a2b1d; /* swap for your brand accent */
  margin-bottom: 1rem;
}
.essay blockquote {
  margin: 1.75em 0;
  padding: 0;
  font-size: 1.3125rem;
  line-height: 1.45;
  font-style: italic;
  text-wrap: balance;
}
.essay .stat { font-variant-numeric: tabular-nums lining-nums; }
```

What changed and why:
- **Headings:** slightly tighter tracking and `text-wrap: balance` stop orphaned last words, which is the most noticeable editorial cue.
- **Blockquote:** I replaced the gray bar with a larger italic. A quote should be set off by one device, and the bar plus italic was two. The larger italic reads more like a pull quote.
- **Kicker:** it now has an accent color and a little more tracking. `#8a2b1d` is a placeholder, so use your brand color.
- **Body:** leading drops from 1.65 to 1.6 to keep the page tighter. `text-wrap: pretty` and `font-synthesis: none` clean up rag and prevent faux bold or italic.

If your partner wants more, one optional tweak is a drop cap, `.essay h1 + p::first-letter`, or a larger lead paragraph. I held back because both need markup decisions on your side.
