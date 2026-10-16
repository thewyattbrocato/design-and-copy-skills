**Option B.**

- **Size:** 17px is in the comfortable range for reading on both laptops and phones. A is 14px, which is too small for 600–900 word stories. C at 22px is oversized for body text.
- **Line length:** 36rem is about 576px, which gives roughly 60–70 characters per line, the best range for continuous reading. A has no cap, so lines run very long on a laptop. C's 30rem gives about 45 characters, which makes the line breaks choppy.
- **Line height:** 1.55 is right for a serif at this size and measure. A's 1.3 is cramped, and C's 1.95 is so loose that the lines stop reading as a block.

I'd make two small changes, though you didn't ask for them. Use `rem` units instead of `px` so the text respects users' browser font settings. On phones, add `max-width: 100%` and some side padding so the text doesn't touch the screen edge.
