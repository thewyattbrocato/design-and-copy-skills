# Fonts for English, Arabic and Japanese

Pick one matched trio rather than three unrelated fonts, then tune the metrics so the scripts look equally weighted.

## Recommended pairing

**IBM Plex Sans + IBM Plex Sans Arabic + IBM Plex Sans JP.** They were designed as a family, so stroke contrast and weight steps line up. They're OFL-licensed, and they suit signage-style UI like timetables.

Noto Sans, Noto Sans Arabic and Noto Sans JP are the safe alternative. They have the widest coverage and the most predictable fallback, but the Latin looks more generic. If you have a brand Latin face, keep it and pair it with Plex Arabic and Plex JP, or with the Noto equivalents.

## Latin inside Arabic and Japanese text

This is where "afterthought" usually shows up.

- **Put the Latin font first in the stack**, then the script font. `font-family: "Plex Sans", "Plex Sans Arabic", sans-serif` means stop names render in your real Latin face. Otherwise they render in the Arabic or Japanese font's built-in Latin, which is often wider, mismatched in weight, or poorly spaced.
- For Japanese, use `@font-face` with `unicode-range` to guarantee that Latin and digits never come from the JP font.
- Tag the stop names, for example `<span lang="en" dir="ltr">`, or use `<bdi>`. In Arabic this stops bidi reordering from scrambling punctuation and neighbouring numbers, like "Pier 4 – Harbour Quay".
- Pick one numeral style per language. I'd use Western digits for departure times everywhere, with `font-variant-numeric: tabular-nums` so the departures list columns align. Check that each font actually supports tabular figures.

## Matching size and weight

Scripts look different at the same `font-size`.

- Arabic usually looks smaller, so scale it up about 5–15%.
- Japanese has a large em box, so it can look bigger than Latin.
- Use `size-adjust` in `@font-face` (or `font-size-adjust`) to normalise this once, instead of overriding sizes in every component.
- Use weights the three fonts share, for example 400 and 600. Heavy Japanese and Arabic weights get muddy at small sizes. Alerts should get emphasis from color, an icon and position as much as from bold.

## Per-language typography rules

Use `:lang()` selectors.

- **Line-height:** about 1.4 for Latin, 1.6 or more for Arabic (marks and diacritics need room), and 1.5–1.7 for Japanese.
- **Arabic:** no `letter-spacing`, no uppercase, no italics and no faux bold. Letter-spacing breaks the joining between letters.
- **Japanese:** no word spaces, so set `line-break: strict` and try `word-break: auto-phrase` (Chromium) with `text-wrap: balance`. Keep Latin stop names unbroken with `white-space: nowrap` on their spans.
- **Minimum sizes:** don't go below about 12px for Japanese or 14px for Arabic in dense lists.
- Set `lang="ja"` explicitly. Otherwise Han characters can render with Chinese glyph variants.

## Layout

- Use logical properties (`margin-inline-start`, `text-align: start`) so the RTL card mirrors properly.
- Keep times and route numbers LTR inside RTL rows.
- Test with your longest real stop names in all three languages. Arabic often runs longer than English, and Japanese is shorter but wraps differently.

## Delivery

- **Web or webview:** Noto Sans JP is large. Use variable fonts with `unicode-range` slices or a subset, and preload the Latin and Arabic files.
- **Native iOS and Android:** consider system fonts (SF with Hiragino and the system Arabic on iOS, Roboto with Noto on Android). They are free and consistent with the OS. Bundle fonts only if the brand needs it, and then bundle all three.
- Set a fallback stack ending in `sans-serif` so a failed load never produces missing-glyph boxes.

Is the app native, web or a hybrid? That decides bundling versus system fonts, and I can turn the above into concrete `@font-face` and CSS if you'd like.
