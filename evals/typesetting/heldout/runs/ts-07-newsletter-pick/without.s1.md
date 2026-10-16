**Go with Option B.**

- **Size (17px):** It's comfortable on both laptops and phones without zooming. Option A's 14px is small for 600–900 words of continuous reading.
- **Line height (1.55):** It's roomy enough to follow lines easily without the text feeling loose. A's 1.3 is tight for long passages, and C's 1.95 is so airy that the text starts to fall apart into separate lines.
- **Line length (36rem):** At 17px that's about 60–75 characters per line, which is the usual comfortable range. A's `max-width: none` stretches lines across a wide laptop screen, which is hard to read. C's 30rem is narrow enough to give choppy lines.
- **Typeface (Georgia):** It's a good serif for long-form stories and suits a warm community newsletter. Helvetica/Arial is fine for UI but less inviting for narrative.

Option C is the "large and airy" version. At 22px with 1.95 line height, a 900-word story would run very long and need a lot of scrolling, especially on phones.

One small suggestion: add `max-width: 100%` or padding on small screens so B's 36rem cap doesn't cause horizontal overflow. In practice `max-width` already shrinks to fit, so you'll just want some side padding on the container.
