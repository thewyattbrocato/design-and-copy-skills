I'd pick one family that covers all three scripts, then tune the metrics per script. Two practical options:

- **Noto Sans + Noto Sans Arabic + Noto Sans JP** is the safest default. The three share design principles and weight ranges, and they're available as variable fonts.
- **IBM Plex Sans + Plex Sans Arabic + Plex Sans JP** has more character and is also designed as a set. It suits signage-like UI well.

If you're shipping native apps rather than web, system fonts are fine: SF Pro, SF Arabic and Hiragino Sans on iOS, and Roboto plus Noto on Android. In that case most of the work below is about line height and mixed runs, not font choice.

**Mixed-script runs**
- Put the Latin font first in the stack. Arabic and Japanese fonts usually have weaker Latin glyphs, and this way stop names look the same in all three languages. The CJK or Arabic font then only supplies what the Latin font lacks:
  ```css
  font-family: "Plex Sans", "Plex Sans Arabic", "Plex Sans JP", sans-serif;
  ```
- Set `lang="ar"` and `lang="ja"` on the elements. Japanese needs it so the browser picks Japanese kanji forms, not Chinese ones.
- In Arabic text, wrap each Latin stop name in `<bdi>` (or `dir="auto"`). Otherwise adjacent punctuation and numbers can jump to the wrong side of the name in RTL.
- For Japanese, `text-autospace: normal` adds a small gap between kana/kanji and Latin.

**Optical matching**
- Arabic at the same `font-size` looks smaller than Latin. Try +8–12% via `size-adjust` or a `:lang(ar)` size bump.
- Arabic needs more line height, about 1.6–1.7. Japanese works at about 1.6, and Latin at about 1.4. Set these per `:lang()` so cards don't collide or look uneven.
- Match weights by visual density, not number. Bold Japanese and Arabic get heavy fast, so 400, 500 and 600 are often enough.
- Never add `letter-spacing` to Arabic, because it breaks the letter joins. Don't use italics or uppercase for emphasis in Arabic or Japanese. Use weight or color instead.

**Numerals**
- Departure times matter most here. Choose Western (0–9) or Eastern Arabic-Indic (٠–٩) digits for the Arabic UI deliberately, based on your audience, and use the same ones everywhere.
- Turn on tabular figures (`font-variant-numeric: tabular-nums`) so the departures list columns align in every language.

**Layout**
- Use logical CSS properties (`margin-inline-start`, `text-align: start`) so RTL mirrors properly. Mirror icons that imply direction, such as arrows and "next departure".
- For Japanese wrapping, use `line-break: strict` and `word-break: auto-phrase` where supported. Arabic should wrap at word boundaries, not truncate mid-word. Truncating with an ellipsis is risky in the alert card, so let it grow or clamp by lines.

**Performance**
- Japanese fonts are large. Use sliced subsets with `unicode-range` (Google Fonts does this) or self-host a subset, and use `font-display: swap`. Set fallback metrics (`size-adjust`, `ascent-override`) to reduce layout shift.

**Testing**
Build the alert card and departures row with real worst-case strings: a long Arabic alert with two Latin stop names, a Japanese one with a Latin name at the start and one at the end, and times next to Latin text in RTL. Review all three at your smallest and largest text sizes before settling the type scale.

Is this web, native, or both? I can turn this into a concrete CSS or type-scale setup for your stack.
