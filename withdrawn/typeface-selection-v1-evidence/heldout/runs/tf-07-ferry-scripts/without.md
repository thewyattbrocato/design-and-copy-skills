**Recommendation:** use one designed-together family for all three scripts, and put the Latin face first in every font stack so stop names always render in it.

**1. Pick the family**
- **IBM Plex** (Sans, Sans Arabic, Sans JP) or **Noto** (Sans, Sans Arabic, Sans JP) both have matched weights and proportions across the three scripts. Plex has more character. Noto is the safest and has the widest weight range.
- If this is a native app, the system fonts (SF Pro, SF Arabic and Hiragino Sans on iOS; Roboto and Noto on Android) cost nothing and look native. Bundle a family only if you want a distinct brand voice.

**2. Stack order matters for the mixed text**
- Japanese fonts ship their own Latin glyphs, and they are often clumsy: wide, uneven spacing and a different x-height. Arabic fonts' Latin glyphs are often weak too.
- Put the Latin font first, then the script font: `"Plex Sans", "Plex Sans Arabic", sans-serif`. Latin characters then take the first font and Arabic or Japanese characters fall through to the next.
- For the Latin in Arabic and Japanese text, scale it to match visually. Arabic usually needs about 10–15% more size than Latin at the same nominal size. On the web, use `size-adjust` on the `@font-face` or `font-size-adjust`.

**3. Per-script typography (don't share one set of values)**
- **Line-height:** about 1.3–1.4 for Latin, 1.5–1.7 for Arabic (tall ascenders and marks) and 1.5–1.7 for Japanese. A card that looks right in English will clip Arabic.
- **Arabic:** no letter-spacing, no uppercase transforms (they break joining), and no italics. Use weight or color for emphasis. Use italics sparingly in Japanese too.
- **Japanese:** always set `lang="ja"`. Without it, some platforms pick Chinese glyph variants for shared Han characters. Use `line-break: strict` and `word-break: auto-phrase` where supported.
- **Weights:** pick two (Regular and Semibold or Bold) that exist in all three scripts. Some Japanese fonts are heavy at "Bold".

**4. Bidi handling**
- Wrap each Latin stop name inside Arabic text in `<bdi>` or `dir="ltr"` so adjacent punctuation and numbers don't flip. In native code, use isolate marks (U+2066 or U+2068 … U+2069).
- Decide on digits once. Western digits (0–9) are the safe default for times and platform numbers, and Arabic-Indic digits are a content choice. Use tabular lining figures in the departures list so the time column aligns.

**5. Layout**
- Mirror the departures list for RTL with logical properties (`start`/`end`). Keep times and platform numbers in a fixed LTR cell.
- Design for expansion. Arabic strings are often longer, Japanese ones shorter but taller. Avoid fixed heights on the alert card and truncate with care.
- Give each script its own tuned size and line-height tokens (for example, `--lh-ar`, `--lh-ja`) and key them off `lang`.

**6. Size and loading**
- Japanese fonts are big. On the web, use a variable font with unicode-range subsets (Google Fonts' slicing does this). In a native app, bundle only the weights you use.

**7. Testing**
Test with real content: your longest stop names, a three-line alert in each language, mixed Arabic + Latin + digits in one line, and an RTL departures row. Do it on a low-end Android device as well, since fallback fonts show up there first.

Is this native or web? That decides whether to use system fonts or bundle a family, and I can then give you concrete font stacks or tokens.
