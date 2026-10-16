**Go with Option B.**

- **Size:** 17px is comfortable body size on both laptops and phones. A is 14px, which is too small for a 600–900 word read. C is 22px, which is oversized for body text and makes a story run very long on a phone.
- **Line length:** `36rem` at 17px is about 65 characters per line, which is in the 45–75 range for continuous reading. A has `max-width: none`, so lines would stretch across a whole laptop screen. C's `30rem` at 22px gives only about 40 characters per line, which is choppy.
- **Line height:** 1.55 is near the 1.5 standard for screen body text. A's 1.3 is cramped, and C's 1.95 is so loose that lines drift apart.

Two optional tweaks:
- Use rem instead of px for the size (`1.0625rem`) so it respects users' browser font settings.
- Add `text-wrap: pretty` for nicer line endings.
