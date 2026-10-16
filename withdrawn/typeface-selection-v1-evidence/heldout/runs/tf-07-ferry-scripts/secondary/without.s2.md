The short answer: give each script its own font, pick them by `lang`, and handle the mixed-direction and mixed-script cases explicitly. Don't rely on one family or the system fallback chain.

## 1. Choose one font per script and pair them

- **Latin (en):** one neutral sans, such as Inter, Source Sans 3, or IBM Plex Sans. Use it for stop names everywhere, including inside Arabic and Japanese sentences.
- **Arabic:** Noto Sans Arabic, IBM Plex Sans Arabic, or Tajawal. Plex pairs well with a Latin Plex. Check that the weight you need (usually 600–700 for alert titles) actually exists in the file.
- **Japanese:** Noto Sans JP. The full file is large, so serve it subset by `unicode-range` as WOFF2 or use a variable build. On Apple platforms, Hiragino Sans is a good native fallback.

Bundle Noto and Plex; both are OFL-licensed. Don't rely on whatever the OS substitutes, because glyph shapes and metrics vary by platform.

## 2. Select by `lang`, not by content

```css
:lang(ar) { font-family: "Noto Sans Arabic", system-ui, sans-serif; line-height: 1.7; letter-spacing: 0; font-style: normal; }
:lang(ja) { font-family: "Noto Sans JP", "Hiragino Sans", "Yu Gothic", sans-serif; line-height: 1.6; }
:lang(en), .stop-name { font-family: "Inter", system-ui, sans-serif; }
```

- Set `lang` on every element, including the stop-name spans. The `lang` attribute also decides which CJK glyph variants render for shared Han characters, so `lang="ja"` matters.
- Arabic needs taller line-height and no letter-spacing, because tracking breaks joined letters. Don't use faux italics.
- Japanese is fine at 1.5–1.7 line-height. It has no spaces, so use `word-break: normal` and `line-break: strict`, and add `<wbr>` where you want breaks inside long names.

## 3. Handle the bidi mixing explicitly

This is where mixed-script alerts usually break. An Arabic sentence containing "Cobalt Quay 3B" can move punctuation, brackets, and times to the wrong side.

```html
<p dir="rtl" lang="ar">
  الحافلة إلى <bdi lang="en" class="stop-name">Cobalt Quay</bdi> متأخرة ١٠ دقائق
</p>
```

- Wrap every Latin stop name in `<bdi>` (or `unicode-bidi: isolate`) so it keeps its own direction.
- Use `dir="rtl"` on the Arabic container and let the page direction come from locale, not from the content.
- Decide on digits. Transit apps usually use Western digits (0–9) in Arabic too, since riders expect the same times everywhere. If you use Arabic-Indic digits, test that every time string still reads correctly.

## 4. Make the departures list work in both directions

- Use logical CSS properties (`margin-inline-start`, `padding-inline-end`, `text-align: start`) rather than left/right, so the layout mirrors automatically.
- Put times in a fixed-width column with `font-variant-numeric: tabular-nums` so they line up.
- Mirror only directional icons (arrows, chevrons). Don't mirror clocks, route badges, or severity icons.

## 5. Align the metrics

Arabic and Japanese fonts have different ascent and descent, so a mixed line can jump or look cramped. In `@font-face`, use `ascent-override`, `descent-override`, and `size-adjust` to match the fallback metrics to your primary font. Set line-height per script, as above, not one value for the whole card.

## 6. Give the alert card a hierarchy that holds in all three scripts

Don't use font size alone to signal severity. Pair color with an icon and a text label, and check contrast against the card background in each script's weight. Japanese at weight 400 can look thin next to Latin, so bump it to 500 for titles.

## Checking it

Build a test fixture with real strings: the longest stop names, a time, a delay, and a mixed sentence in each language. Look at it on iOS, Android, Windows, and a desktop browser. Check that the Arabic punctuation sits on the correct side, that the Japanese doesn't overflow on narrow widths, and that the times line up in the list.

If you tell me your platform (web, React Native, native iOS/Android) and whether stop names come from data that may include Arabic or Japanese forms, I can give you the exact font-loading setup and the layout code for the card and list.
