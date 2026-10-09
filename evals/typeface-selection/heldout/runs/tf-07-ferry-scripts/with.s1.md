**Use one family system with a face per script, and set the Latin face first in every stack.** That puts the stop names in the same Latin letterforms in all three languages. I'd start with IBM Plex or Noto, since each has Latin, Arabic and Japanese members under open licenses. Confirm the license terms, and that the weights you need are all there, before you commit.

## Stacks

```css
:root {
  --latin: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --arabic: "IBM Plex Sans Arabic", "Geeza Pro", "Segoe UI", "Noto Sans Arabic", sans-serif;
  --japanese: "IBM Plex Sans JP", "Hiragino Sans", "Yu Gothic UI", "Noto Sans JP", sans-serif;
}

:lang(en) { font-family: var(--latin); }
:lang(ar) { font-family: var(--latin), var(--arabic); }
:lang(ja) { font-family: var(--latin), var(--japanese); }
```

The Latin face has no Arabic or Japanese glyphs, so the browser falls through to the next family per character. The Latin face supplies the Latin letters, and the script face supplies the rest. Arabic and Japanese faces usually carry their own Latin letters, and those rarely match the weight or proportions of the rest. Listing the Latin face first avoids that mismatch.

Put `lang="en|ar|ja"` and `dir` on every text container. This selects the right Han glyph variants for Japanese and the right fallback fonts.

## Making the three scripts look equal

- **Size:** Arabic usually needs about 10–15% more size than Latin to look the same, and Japanese needs a slightly larger line height. Set size and line-height per `:lang()` and judge by eye, not by equal points.
- **Line height:** Arabic marks are tall and stack above and below. Leave roughly 1.6–1.7 for Arabic and Japanese, and about 1.4–1.5 for Latin.
- **Weight:** Match the visual weight, not the number. Japanese at 700 often looks heavier than Latin at 700. Use two weights (regular and semibold or bold) across all three scripts.
- **No italics, letter-spacing or uppercase tricks in Arabic or Japanese.** Letter-spacing breaks Arabic joining. Use weight or color for emphasis. Add `font-synthesis: none`.
- **Digits:** Choose Western or Arabic-Indic numerals for Arabic and use that choice everywhere. For the departures list, use `font-variant-numeric: tabular-nums` so the time columns align.

## Latin stop names inside Arabic and Japanese

- **Arabic:** Wrap each stop name in `<bdi>`, or use `dir="ltr"` on a span. Otherwise punctuation and neighbouring numbers can reorder around the Latin run.
- **Japanese:** Keep the Latin text inline. Check that it doesn't look undersized next to the kanji. If it does, nudge only the span's size, not the Latin face.
- **Departures list:** In the RTL layout, keep the time column LTR and test it on a real device with a mixed row such as `Cobalt Harbour ← 14:35`.

## Loading

Japanese is the heavy one, so don't ship the whole face.

- Self-host WOFF2 with `unicode-range` slices, or use the variable build.
- Use `font-display: swap`.
- Preload only the Latin and the Arabic regular files.
- Let Japanese fall through to the system fonts (Hiragino, Yu Gothic UI) while it loads. Those are good faces, not a downgrade.
- Test with the fonts blocked, because the fallback is what some riders will see.

## Check before you finish

Lay out the alert card in all three languages with real strings: a long stop name, a time, and a one-line warning. Make sure a mixed row doesn't reorder in the Arabic version and that the three cards have equal visual weight. If they look unequal, adjust per-language size and line height before changing the fonts.

I assumed this is a screen-only app with no brand typeface already fixed. If Cobalt Straits has a brand Latin face, keep it as the first font in each stack. Then choose the Arabic and Japanese partners to match its weight and proportions.
