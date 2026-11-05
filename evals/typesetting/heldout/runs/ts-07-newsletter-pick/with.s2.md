**Option B.**

```css
.story { font: 17px/1.55 Georgia, serif; max-width: 36rem; }
```

- **Size:** 17px is comfortable on both laptops and phones for a 600–900 word read.
- **Line length:** 36rem is about 576px, which gives roughly 60–70 characters per line. That sits in the ideal range for continuous reading.
- **Leading:** 1.55 is close to the usual 1.5 for screen body text.

Why not the others:
- **A:** 14px is too small for long-form reading. On a laptop, `max-width: none` stretches lines across the whole screen, well past 100 characters. The 1.3 leading is also tight for that line length.
- **C:** 22px with 1.95 leading and a 30rem (480px) column is oversized. Lines would hold only about 30 characters, so the eye keeps jumping to the next line. The leading is loose enough that the lines stop reading as a paragraph.

One optional tweak: use `font-size: 1.0625rem` instead of `17px`, so the text respects users' browser font-size settings.
