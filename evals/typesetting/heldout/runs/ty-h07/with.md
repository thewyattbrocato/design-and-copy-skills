Your instinct is right. Three things make it look cheap, and they all come from the two rules.

**1. Justified text in a 260px column.** This is the biggest one. At about 33 characters per line, justification stretches the word spaces into rivers and gaps. `hyphens: none` makes it worse, because the browser can't break long words to even out the lines.
- Fix: use `text-align: left`, so the right edge is ragged. If you really want justified text, you need `hyphens: auto`, a `lang` attribute and a wider column. A column this narrow can't carry it.

**2. The label is a long all-caps line with no tracking.** "UPCOMING WORKSHOPS AND COMMUNITY GATHERINGS" is 43 characters of 12px bold capitals with `letter-spacing: 0`. It's tight, hard to read and it wraps awkwardly. Caps only work for short, tracked labels.
- Fix: either set it in sentence case, or keep the caps, shorten it and track it at 0.05–0.1em. Keeping your wording, sentence case is simplest.

**3. Small details.**
- 15px Verdana is wide and sits a little large for a 260px column. It's workable, so I'd leave the size alone.
- Paragraphs have the browser's default margins. Set the spacing deliberately: about half a line between paragraphs, and more space above the label than below it.
- The label sits only 8px above the text, so it doesn't read as a heading. Give it a bit more room below it than that, and separate it from whatever comes before it.

Suggested CSS:

```css
.side {
  width: 260px;
  font: 15px/1.5 Verdana, sans-serif;
  text-align: left;
  text-wrap: pretty;
}
.side p { margin: 0 0 0.75em; }

.tag {
  font-size: 13px;
  font-weight: bold;
  line-height: 1.3;
  text-wrap: balance;
  margin: 24px 0 10px;
}
```

For the label, change the markup to sentence case: "Upcoming workshops and community gatherings". If you'd rather keep the caps, set `text-transform: uppercase; letter-spacing: 0.06em;` and shorten the text to something like "Upcoming events", because the full phrase is too long for caps.

I haven't touched your copy beyond that capitalization. Also, `.tag` is a `div`. If this is a heading in the page outline, make it an `h2` and keep the same class.
