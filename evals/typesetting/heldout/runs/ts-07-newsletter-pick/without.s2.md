**Option B.**

- **Size:** 17px is comfortable on both laptops and phones. A's 14px is small for 600–900 words, and C's 22px is oversized.
- **Line length:** `36rem` is about 576px, or roughly 60–70 characters per line. That's the usual range for comfortable reading. A has no max-width, so lines run very long on a laptop and are tiring to follow. C's `30rem` is narrow enough that lines get choppy.
- **Line height:** 1.55 suits body text at this size. A's 1.3 is cramped for long reading. C's 1.95 is so loose that paragraphs look like separate lines instead of blocks.
- **Typeface:** Georgia is a readable serif for long-form stories, and it fits a garden newsletter's tone.

One small suggestion: add a fallback stack such as `Georgia, "Times New Roman", serif`. You could also use `max-width: 36rem; width: 100%` with some side padding so text doesn't touch the screen edge on phones.
