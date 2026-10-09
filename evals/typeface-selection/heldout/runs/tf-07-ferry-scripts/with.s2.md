**Recommendation:** use one family system across all three scripts and choose it for Arabic and Japanese first. Latin is the easy one to match.

**Starting pick (open-license, so you can self-host):** IBM Plex Sans (Latin), IBM Plex Sans Arabic, and IBM Plex Sans JP. They share a skeleton and weight range, so the three scripts read as one voice. Noto Sans / Noto Sans Arabic / Noto Sans JP is the fallback option if Plex's Japanese weights are too limited. I haven't verified current weights or glyph coverage for either family, so check the files and licenses before committing.

```css
:root {
  --latin: "IBM Plex Sans", system-ui, sans-serif;
  --ar: "IBM Plex Sans Arabic", "Geeza Pro", "Segoe UI", Tahoma, sans-serif;
  --ja: "IBM Plex Sans JP", "Hiragino Sans", "Yu Gothic UI", Meiryo, sans-serif;
}
:lang(en) { font-family: var(--latin); }
:lang(ar) { font-family: var(--latin), var(--ar); line-height: 1.7; }
:lang(ja) { font-family: var(--latin), var(--ja); line-height: 1.65; }
html { font-synthesis: none; }
```

**Stop names inside Arabic and Japanese text**
- Put the Latin face first in the Arabic and Japanese stacks, as above. It has no Arabic or kana glyphs, so those characters fall through to the right face, while Latin runs get your chosen Latin design. Japanese fonts' built-in Latin is often the weakest part, so this matters most for Japanese.
- Check by eye that the Latin x-height matches the neighbouring script. If it looks too big or small, use a `@font-face` with `size-adjust` rather than a different point size.
- Wrap each stop name in `<bdi lang="en">` inside Arabic text. This stops the bidi algorithm from shuffling punctuation and neighbouring numbers around it.
- Put `lang` and `dir` on every text element, not just `<html>`. That selects the correct glyph variants. It matters for Japanese in particular, because without `lang="ja"` the browser can pick Chinese glyph forms.

**Alert card**
- Size by eye, not by equal points. Arabic usually needs about 1.1× the Latin size to look equal, and Japanese often needs a touch more leading.
- Use weight and color for emphasis. Don't use italics in Arabic or Japanese, and keep `font-synthesis: none` so nothing is faked.
- Don't use a hairline weight for Arabic or Japanese at small sizes, because thin strokes break up on low-density screens. Make 400 the lightest text weight.
- Mirror the card layout for RTL with logical properties (`margin-inline-start` and so on). Don't flip it by hand.

**Departures list**
- Use `font-variant-numeric: tabular-nums` on times and counts so columns align. Check that your chosen files actually have tabular figures.
- Make one decision up front: Western digits (0–9) or Arabic-Indic digits (٠–٩) in the Arabic UI. Whichever you pick, use it consistently across all times. Gulf and many Maghreb audiences differ, so ask whoever owns the Arabic copy.
- Set times as LTR runs (`<bdi>` or `unicode-bidi: isolate`) so "14:05" doesn't reorder inside an RTL row.
- Give each language row the same minimum height. Arabic and Japanese lines are taller, and mismatched rows make one script look squeezed in.

**Loading**
- Subset per script and serve WOFF2. Japanese is the big file, so load it only when the locale needs it (`unicode-range` or per-locale CSS).
- Use `font-display: swap`, and preload only the file for the user's active locale.
- Test with the web fonts blocked. The fallback stacks above should still render all three scripts acceptably.

**Assumptions:** this is a sans-serif UI for a mobile or web app, and the app can self-host fonts. If you're on native iOS or Android, tell me. The system fonts there (SF with Arabic and Hiragino, or Roboto with Noto) are a reasonable default, and you'd only need to tune the Latin-in-Arabic and Latin-in-Japanese sizing.
