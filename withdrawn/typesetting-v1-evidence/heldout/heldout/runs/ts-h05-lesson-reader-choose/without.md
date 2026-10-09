**Pick B**, with a few tweaks.

**Why B wins**

- **Line length:** `40rem` at 18px is about 720px, which comes to roughly 65–75 characters per line. That's the usual comfortable range for sustained reading. A's 1100px at 14px runs past 150 characters, so eyes lose their place on the return sweep. C's 28rem at 24px gives about 30 characters, so lines break constantly and a 600-word lesson turns into a very long scroll.
- **Size and spacing:** 18px with 1.6 line-height is a good fit for tablets held at arm's length. A's 14px with 1.3 line-height and 4px paragraph gaps is a dense wall of text. That's especially hard on adult learners, who are more likely to have presbyopia or tired eyes. C is oversized and over-spaced (2.1 line-height). Paragraphs blur into evenly spaced lines, which weakens grouping.
- **Contrast and hierarchy:** B's `#1f2328` on white is high contrast without the harshness of pure black. A's `#444` at 14px is mediocre for small text. C's `#000` is fine but isn't needed at that size. B's heading scale (2rem / 1.375rem / 1.125rem body) is clear, and the heading margins put more space above a heading than below it, so each heading attaches to the text it introduces. A's h1 is 15px against 14px body, and h2 is the same size as body, so there is almost no hierarchy.
- **Relative units:** B uses `rem` throughout, so it respects the user's browser font-size setting. That matters for an adult-education audience. A uses `px`, which is less friendly to scaling.

**Small tweaks**

1. **Use `ch` for the measure:** `max-width: 65ch` ties line length to the font, so it stays right if the size changes. Alternatively, keep `40rem` and cap it at about 70ch.
2. **Add side padding:** add `padding: 0 1rem` and `margin: 0 auto`. Without padding, the text touches the screen edge on narrow tablets and phones. The stylesheet also doesn't center the column yet.
3. **Fluid body size:** `font-size: clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem)` keeps laptops and tablets comfortable without a media query.
4. **Add the missing declarations:** set `font-weight` on h1 and h2 explicitly, and add `text-wrap: balance` to headings and `text-wrap: pretty` to paragraphs to avoid orphaned words.
5. **Soften the pure white:** use an off-white background such as `#fdfdfc`. It's optional, but it cuts glare during long reading sessions. Check the contrast ratio if you change the text color too. `#1f2328` has plenty of margin.
6. **Add `max-width: 100%; height: auto` on images** and list styles (`ul, ol { margin: 0 0 1rem; padding-left: 1.5rem }`), since B doesn't cover them.

**A caveat:** this is a judgment from established readability guidelines, not from testing with your learners. If the team still disagrees after this, a quick check on real devices with a few learners (including someone using larger system text) will settle it faster than more debate.
