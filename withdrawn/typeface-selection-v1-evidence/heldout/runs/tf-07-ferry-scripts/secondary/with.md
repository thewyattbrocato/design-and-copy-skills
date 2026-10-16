**Short answer:** use one coordinated family, Noto, across all three scripts. Noto Sans, Noto Sans Arabic and Noto Sans JP are designed to pair, so the Latin stop names inside Arabic and Japanese text come from the same design as the Arabic or Japanese around them. Then match size, weight and line height per script so none of them reads as a fallback. I haven't checked licensing or current file sizes for these fonts, so confirm those before shipping.

**Why this works**
- A single stack lets the browser pick the right face per character. Each script has its own glyphs, so the Latin face handles "Kasuga Pier" inside Arabic text, and the Arabic face handles the Arabic.
- Stop names stay in the same face as the surrounding text, so they don't jump in weight or x-height.

**Roles**
- **Alert card:** the headline needs a true bold in every script. Body text sits at the same size in each locale, with more line height for Arabic and Japanese than for English.
- **Departures list:** times are the scanning column, so use tabular figures for Latin digits. Keep times as Latin digits in all three locales, which is common in transit, and state that as an assumption.

**Starting CSS**

```css
:root {
  --font-transit: "Noto Sans", "Noto Sans Arabic", "Noto Sans JP", system-ui, sans-serif;
}
.alert, .departure { font-family: var(--font-transit); }

[lang="ar"] { font-family: "Noto Sans Arabic", "Noto Sans", sans-serif; line-height: 1.7; }
[lang="ja"] { font-family: "Noto Sans JP", "Noto Sans", sans-serif; line-height: 1.6; }

.time { font-variant-numeric: tabular-nums; }
.stop { unicode-bidi: isolate; }   /* keeps Latin stop names from reordering Arabic punctuation */
[dir="rtl"] { text-align: start; }
font-synthesis: none;              /* no faked bold or italic in any script */
```

Set `lang` and `dir` on each string so the browser picks the correct glyph variants and mirrors the layout. Wrap the stop names and times in `<bdi>` if you're not using a span with `unicode-bidi: isolate`.

**Things that will make it look like an afterthought if skipped**
- **Size:** Arabic and Japanese often look smaller than Latin at the same point size. Adjust by eye with a real long alert, not a short specimen.
- **Line height:** Arabic diacritics and Japanese density need room. Clipped marks look broken.
- **Japanese weight:** Noto Sans JP is large. Subset it to the glyphs you use, or use `unicode-range` so it only loads when Japanese appears.
- **Fallback:** test offline with the web fonts blocked, and check the longest stop name in each language.

**Assumptions:** this is a web app with self-hosted fonts and no installed fonts beyond system ones. If it's a native app, drop the web loading and use the system Arabic and Japanese fonts, which ship with the OS.

I can write the `@font-face` loading setup or a test page with your longest real stop names if you tell me the stop list.
