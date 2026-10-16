**Go with Option B.**

```css
.story { font: 17px/1.55 Georgia, serif; max-width: 36rem; }
```

- **Size:** 17px is comfortable on both laptops and phones for 600–900 word stories. Option A's 14px is too small for long reading.
- **Line length:** 36rem is about 576px, which gives roughly 65–70 characters per line. That's the best range for continuous reading. Option A has no cap, so lines run across the whole laptop screen. Option C's 30rem at 22px gives only about 35 characters per line, which breaks up the reading rhythm.
- **Line height:** 1.55 suits body text at this size. Option C's 1.95 is so loose that lines stop reading as a block. Option A's 1.3 is too tight for long passages.

One optional tweak: use `rem` instead of `px` (`font: 1.0625rem/1.55 Georgia, serif;`) so the text respects users' browser font-size settings. It's not required.
