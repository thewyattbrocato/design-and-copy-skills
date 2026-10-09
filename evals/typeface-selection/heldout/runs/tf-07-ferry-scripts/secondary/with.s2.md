**Short answer:** use one sans family per script, all of them designed to sit together, and let the browser or OS pick the glyphs for each character. Don't pick a Latin font and hope the Arabic and Japanese fall into place.

I'm assuming a web or hybrid app, no locked brand typeface, and that you can self-host. If you're native, the same roles apply, but you'd use each platform's system fonts and check them on device.

## Roles

| Role | Latin | Arabic | Japanese |
|---|---|---|---|
| Alerts and departures (UI) | Noto Sans | Noto Sans Arabic | Noto Sans JP |
| Stop names in Latin, inside other scripts | Noto Sans (same face as above) | | |
| Times and numbers | Latin digits, tabular | Same, unless the client wants Arabic-Indic digits | Same |

I chose Noto because its Latin, Arabic and Japanese cuts are drawn as one system, so the weights and sizes match without tuning. Confirm the license and the exact glyph coverage with the foundry or the font's own files before you ship. I haven't verified either here.

## Stack

```css
:root {
  --font-ui: "Noto Sans", system-ui, sans-serif;
}
:lang(ar) { font-family: "Noto Sans", "Noto Sans Arabic", "Geeza Pro", Tahoma, sans-serif; }
:lang(ja) { font-family: "Noto Sans", "Noto Sans JP", "Hiragino Sans", "Yu Gothic", sans-serif; }
```

Put the Latin face first in each stack. The browser picks the first font that has each character, so Latin stop names come from the Latin face, and Arabic or Japanese characters fall through to the script face.

## Alert card

- Set `lang` on each text element, and `dir="rtl"` on Arabic blocks. Use logical properties (`margin-inline-start`, `text-align: start`) so the layout mirrors correctly.
- Wrap each Latin stop name inside Arabic text in `<bdi>`. Without it, punctuation such as hyphens and slashes reorders the sentence.
- Give Arabic and Japanese more line height than Latin. Arabic has tall marks and small x-height, so it needs extra room to look the same size.
- Don't italicize Arabic or Japanese. Use weight or color for emphasis.

## Departures list

- Put times in their own column with `font-variant-numeric: tabular-nums` so the digits align across rows.
- Give stop names a fixed column or a truncation rule. Japanese and Arabic names often run longer than their English equivalents.
- Match apparent size by eye on a real device, not by point size. Arabic and Japanese usually need a slightly larger size than Latin to look equal.

## Loading

- Self-host, subset each script with `unicode-range` so a rider downloads only the glyphs on screen, and serve WOFF2.
- Noto Sans JP is large even subset. If the file weight is a problem, use the system Japanese font for that screen and accept the platform difference.
- Set `font-display: swap` and tune the fallback metrics so the swap doesn't jump the list.
- Test with the font blocked. Check that the Arabic and Japanese fallbacks look intentional, not like a default serif.

## Open questions

- Arabic-Indic digits or Western digits in times? This is a client decision, and I'd default to Western digits to match the stop names and the English timetable.
- Do you need to ship the fonts with the app, or can the app rely on system fonts?

If you point me at the alert card and departures components, I can apply the stacks and `lang`/`dir` markup directly.
