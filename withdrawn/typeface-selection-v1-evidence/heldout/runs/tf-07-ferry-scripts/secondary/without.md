The simplest approach that holds up is one font family per script, all from the Noto family, which was designed to pair across scripts. Put Latin stop names in the same Latin face in all three languages so they look identical whatever text surrounds them.

**Font choices**

- **Latin (English and stop names everywhere):** Noto Sans.
- **Arabic:** Noto Sans Arabic. Its Latin glyphs match Noto Sans, so Latin stop names inside Arabic text stay consistent.
- **Japanese:** Noto Sans JP. It is large, so see the bundling note below.

Noto is licensed under the SIL OFL, so you can bundle it.

**Fallback stack, with language tags**

```css
body {
  font-family: "Noto Sans", "Noto Sans Arabic", "Noto Sans JP", system-ui, sans-serif;
}
:lang(ar) { font-family: "Noto Sans Arabic", "Noto Sans", system-ui, sans-serif; }
:lang(ja) { font-family: "Noto Sans JP", "Noto Sans", system-ui, sans-serif; }
```

Set `lang` on each text element, not just on `<html>`. A stop name in English inside an Arabic alert should carry `lang="en"`, and a Japanese line needs `lang="ja"` so the browser picks the Japanese glyph variants for shared Han characters. On native platforms, the equivalent is setting the locale on each text view.

**Mixed-direction text (the Arabic case)**

- Set `dir="rtl"` on Arabic blocks.
- Wrap each Latin stop name in `<bdi>` or `<span dir="ltr">` so that punctuation and digits next to it don't flip. Without this, something like "Harbor Point (Dock 3)" inside an Arabic sentence can reorder badly.
- Decide early on digits. Western digits (0–9) are the usual choice for timetables. If your Arabic-speaking riders expect Eastern Arabic-Indic digits, pick that deliberately and apply it everywhere.

**Sizing and metrics**

- Arabic and Japanese do not look the same size as Latin at the same `font-size`. Arabic often needs a slightly larger size and taller line-height (about 1.6–1.8). Japanese usually works at about 1.5–1.7.
- Mixed-script lines need the taller line-height, so set line-height per language and do not reuse the English value.
- Use `@font-face { size-adjust: … }` if one script looks visibly bigger than the others on the same card.
- Don't use italics for Arabic or Japanese, because those scripts have no true italic. Don't use all-caps for them either.
- Arabic needs real bold weights. Japanese bold can look heavy, so test 500–600 for body text.

**Line breaking**

- Japanese has no spaces. Use `word-break: auto-phrase` where supported (Chrome 119+, Safari 17+), and check the result on your target browsers.
- For departure rows, prefer wrapping stop names over truncating them with an ellipsis. Truncating a stop name can make it unidentifiable.

**Bundling and performance**

- Full CJK fonts are several MB. If this is a web app, use a subset (unicode-range) or a variable font, or load the Japanese face only when `lang="ja"` is in use.
- On iOS and Android, the system Japanese fonts (Hiragino, Noto CJK) are good enough and avoid the bundle cost. Only bundle the fonts if you need pixel-exact consistency across platforms.

**Testing before you sign off**

- Use real stop names. Include long names, names with parentheses or slashes, and mixed Arabic and Latin on one line.
- Test with a pseudo-locale or a right-to-left layout check, and at large system text sizes.
- Check the alert card in dark mode, since contrast and weight can shift.

I didn't find project files in the working directory (it isn't a git repo), so these are general recommendations. If you share the card and list components (web, React Native, SwiftUI, or Compose), I can give the exact styles for that stack.
