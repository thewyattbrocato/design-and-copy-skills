**Option B.**

- **Size:** 17px is comfortable for 600–900 word reads on both laptops and phones. A is too small, and C is oversized for body text.
- **Line length:** 36rem is about 576px, which works out to roughly 60–75 characters per line at 17px. That's the usual range for comfortable reading. A has `max-width: none`, so lines would run very long on a laptop. C's 30rem at 22px gives only about 40 characters per line, which makes the eye jump to the next line too often.
- **Line height:** 1.55 suits serif body text at this size. A's 1.3 is cramped for long reading. C's 1.95 is so loose that paragraphs start to come apart.
- **Typeface:** Georgia holds up well on screens at this size and suits a warm community newsletter.

One suggestion: use `max-width: 36rem` together with `width: 100%` or normal block flow. On phones the text will then fill the screen, with a little side padding (e.g. `padding: 0 1rem`) so it doesn't touch the edges.
