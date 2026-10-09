The cheap look comes mostly from **justified text in a narrow column**. Justification with `hyphens: none` stretches the word spaces on each line, which leaves visible gaps and rivers. The column is also too narrow for Verdana, which is a wide face.

**Fixes**

```css
.side { width: 22rem; font: 1rem/1.5 Verdana, sans-serif; text-align: left; text-wrap: pretty; }
.tag { font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.5rem; }
```

- **Alignment: `text-align: left`.** Ragged-right keeps word spacing even. Justify only works with wide measures and hyphenation, and this column has neither.
- **Measure: `22rem`, about 38 characters per line.** At 260px, Verdana gives roughly 30 characters, which is cramped. Widening the column brings it into the 35 to 50 range for narrow columns.
- **Size: `1rem` instead of `15px`.** This keeps the body in rem so it scales with the reader's settings.
- **Label: uppercase in CSS, tracked, in rem.** The HTML now keeps sentence case, and `0.08em` tracking makes the small caps readable. Bold is fine at this size, and `700` is explicit.

**Also consider**

- The label "UPCOMING WORKSHOPS AND COMMUNITY GATHERINGS" is 43 characters of tracked capitals, which is heavy for a small label and wraps badly at this width. A shorter label such as "Upcoming" or "Workshops" would read more cleanly. This changes your copy, so it's your call.
- I assumed a screen layout and that Verdana stays. If the newsletter is printed, tell me, because justification with hyphenation becomes a reasonable choice there.
