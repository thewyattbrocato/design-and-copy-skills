**Go with Option B.**

- **Size and leading:** 17px at 1.55 is comfortable on both laptops and phones. Its leading sits right at the ~1.5 target for screen body text.
- **Line length:** `max-width: 36rem` at 17px works out to roughly 60–70 characters per line. That's the best range for 600–900 word stories.
- **Why not A:** 14px with 1.3 leading is small and tight. With `max-width: none`, lines would run across the whole laptop screen, which is hard to follow.
- **Why not C:** 22px at 1.95 leading in a 30rem column gives only about 35–40 characters per line. On a phone that means a lot of scrolling and choppy reading.

One optional tweak: write the size as `1.0625rem` instead of `17px`, so it respects users' browser font settings.
