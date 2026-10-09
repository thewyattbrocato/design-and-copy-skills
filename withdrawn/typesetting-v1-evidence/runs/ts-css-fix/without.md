```css
p {
  font-size: 18px;
  line-height: 1.6;
  max-width: 65ch;
  text-align: left;
  margin: 0 0 1em;
}
h2 {
  margin: 1.5em 0 0.5em;
  line-height: 1.3;
}
```

- **font-size: 14px → 18px:** 14px is small for long-form reading; 16–20px is the comfortable range for blog body text.
- **line-height: 1.2 → 1.6:** Tight leading makes paragraphs dense and hard to track; 1.5–1.7 suits body copy.
- **max-width: 1100px → 65ch:** Lines of ~1100px run well over 100 characters; 45–75 characters per line is the readable measure, and `ch` scales with the font.
- **text-align: justify → left:** Justification without hyphenation creates uneven word gaps and "rivers" on the web; left-aligned text avoids that.
- **text-indent removed:** Indent plus a paragraph margin is redundant. Use one or the other, and spacing is the standard web convention.
- **h2 margin: 24px 0 → 1.5em 0 0.5em:** Equal space above and below makes a heading float between sections. More space above and less below ties it to the text it introduces.
- **h2 line-height: 1.3 added:** Headings that wrap need tighter leading than body text, or they look loose.
