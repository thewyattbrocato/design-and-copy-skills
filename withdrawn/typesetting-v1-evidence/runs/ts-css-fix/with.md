```css
p {
  font-size: 1rem;
  line-height: 1.5;
  max-width: 65ch;
  margin: 0 0 1em;
}
h2 {
  margin: 2em 0 0.75em;
  line-height: 1.2;
  text-wrap: balance;
}
```

- `font-size: 1rem`: this replaces 14px. Blog body text should be at the user's default size, and `rem` follows their browser setting.
- `line-height: 1.5`: this replaces 1.2, which was too tight for body text. Unitless 1.5 is comfortable to read.
- `max-width: 65ch`: this replaces 1100px, which gave lines of 150+ characters. About 65 characters per line is easier to read, and the cap sits on the paragraph rather than the page wrapper.
- Removed `text-align: justify`: justified text without hyphenation leaves uneven gaps and rivers on screen. Left-aligned, ragged-right is the default for the web.
- Removed `text-indent: 2em`: paragraphs were separated by both an indent and a 1em gap. I kept the gap, since using both is redundant.
- `h2` margin `2em 0 0.75em`: the old 24px above and below made the heading float between paragraphs. It now has about twice as much space above as below, so it attaches to the text it introduces.
- `h2` `line-height: 1.2`: headings should be tighter than body text, especially when they wrap.
- `h2` `text-wrap: balance`: this stops a wrapped heading from ending on a single orphaned word.

If the first paragraph after an `h2` ever needs different spacing, that is a separate tweak. With the indent gone, nothing needs it now.
