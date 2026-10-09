Four things make it look cheap, and they all come from the text setting. The content is fine.

1. **Justified text in a 260px column.** This is the biggest one. At about 35 characters per line, justification opens rivers and uneven word gaps, and `hyphens: none` makes it worse. Use flush-left, ragged-right text.
2. **The all-caps label has no tracking and is long.** "UPCOMING WORKSHOPS AND COMMUNITY GATHERINGS" at 12px bold with `letter-spacing: 0` looks cramped, and it wraps to several lines. Track it at 0.05–0.1em. Better still, shorten it or set it in sentence case, since caps are for short labels.
3. **Verdana at 15px with 1.5 leading.** Verdana is wide and has a large x-height. In a narrow column it makes lines break early, and 1.5 leading is slightly loose for it. Give it about 1.45, or switch to a narrower face if you can.
4. **Nothing separates the paragraphs.** The browser's default 1em margin is the only gap, and the label's 8px gap below doesn't relate to it. The label also needs more space above than below.

```css
.side {
  width: 260px;
  font: 0.9375rem/1.45 Verdana, sans-serif;
  text-align: left;
  hyphens: manual;
  text-wrap: pretty;
}
.side p { margin: 0 0 0.75em; }

.tag {
  font-size: 0.75rem;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  line-height: 1.3;
  margin-bottom: 0.75rem;
}
```

If you keep the label in caps, shorten the copy to something like "Workshops & gatherings" so it fits on one or two lines. If you want it to stay long, drop `text-transform` and set it in sentence case with the same bold weight. I changed the sizes to rem so the text follows the reader's browser settings. The rendered size is unchanged at the default 16px root.
