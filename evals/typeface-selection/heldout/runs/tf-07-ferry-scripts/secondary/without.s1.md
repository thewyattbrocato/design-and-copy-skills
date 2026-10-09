Treat each script as its own typographic system with shared sizes and colors, rather than one font with fallbacks. Noto is a good base because its Latin, Arabic, and Japanese faces were designed together and are under the OFL, so you can bundle and subset them freely.

**Font stack**

- **Latin (English, and stop names everywhere):** Noto Sans.
- **Arabic:** Noto Sans Arabic. Use it as the first fallback for Arabic text, so the Latin stop names inside Arabic lines still come from Noto Sans and match the English text.
- **Japanese:** Noto Sans JP. It's large (several MB), so subset it. Either split by `unicode-range` into chunks or ship only the glyphs you need from your stop list and fixed UI strings.
- **Stack:** `font-family: "Noto Sans", "Noto Sans Arabic", "Noto Sans JP", sans-serif;` with the script set per element via `lang`.

**Per-script rules**

- **Set `lang` on every element** (`lang="ar"`, `lang="ja"`). Japanese glyph variants are chosen by `lang`, so without it CJK text can render with Chinese forms.
- **Arabic:**
  - Use `dir="rtl"` on the containing element.
  - Wrap each Latin stop name in `<bdi>` or an isolate (U+2066 LRI … U+2069 PDI). Without this, punctuation and times around the names reorder incorrectly.
  - Never set letter-spacing on Arabic. It breaks joining.
  - Never italicize Arabic. Noto has no true italic, so the browser fakes it.
  - Use a larger line-height, roughly 1.6–1.8, so diacritics don't clip.
  - Arabic often looks small next to Latin at the same px size, so try +1–2px.
- **Japanese:**
  - Use `line-break: strict` (and `word-break: normal`) so line breaks follow Japanese rules.
  - Use medium weight for body text instead of bold. Bold CJK can look heavy and blotchy at small sizes.
  - Half-width Latin stop names inside Japanese lines will look cramped, so consider full-width spacing around them or a thin space.
- **Times and numbers in all scripts:** `font-variant-numeric: tabular-nums`, so departure columns line up.

**Preventing layout jumps**

Fallback fonts have different ascent and descent, so rows can shift when a line switches script. In each `@font-face`, set `size-adjust`, `ascent-override`, `descent-override`, and `line-gap-override` so the faces share metrics. Then check that rows with mixed scripts keep the same height.

**Card and list layout**

- Don't use fixed row heights. Japanese runs wider and Arabic runs taller, so budget about 30% extra room for those scripts.
- For the alert card, give the headline and the "what to do" line the most space, and keep each script's line height independent so one language can't crowd another.
- Check contrast separately for each script. Thin Arabic strokes and small Japanese glyphs fail WCAG more easily than Latin at the same size.

**Testing**

Render the card and list with real stop names (long ones, and ones with mixed scripts), in both directions, at the platform's largest text setting, and on a low-resolution Android device. System fonts on iOS and Android would save bytes, but they vary by OS version, so bundling is the more reliable choice for alerts people need to act on.

I can't see your app's code here, because this directory isn't a git repo and I haven't looked at any files. If you share the card and list components or your CSS, I can apply these rules directly: the `@font-face` block, the per-`lang` styles, and the `bdi` wrapping for stop names.
