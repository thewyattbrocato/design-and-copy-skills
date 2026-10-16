# Fonts for the English, Arabic and Japanese alert card and departures list

I'd use one superfamily that was designed across all three scripts, and let one Latin face set every stop name. I'm assuming screen only and that you can bundle or self-host fonts.

## Pick: IBM Plex Sans, Plex Sans Arabic, Plex Sans JP

Plex Sans has Arabic and Japanese companions built to match its Latin. That keeps stroke weight, proportions and tone consistent across the three scripts. The alternative is Noto Sans, Noto Sans Arabic and Noto Sans JP, which is more neutral, has wider coverage and is a safe fallback. Check the license and web/app embedding rights for whichever you pick. I haven't verified them here.

Because I chose for the Arabic and Japanese first, a few things follow:

- **Weights:** Regular, Medium and Bold in all three. Use weight for hierarchy, such as the alert title, departure time and status.
- **No italics:** Neither Arabic nor Japanese has an italic tradition. Use weight or color for emphasis in all three languages, and set `font-synthesis: none`.
- **No letter-spacing on Arabic:** Tracking breaks the joins between letters. Keep any uppercase tracking on Latin labels only.
- **Japanese file size:** The Japanese font is the big one. Subset it, or serve it in unicode-range slices, and ship WOFF2 only.

## Latin stop names inside Arabic and Japanese

Put the Latin face first in every stack. The Latin font has no Arabic or Japanese glyphs, so those characters fall through to the right script face. A stop name like "Cobalt Quay" then renders in the same Plex Latin whether it sits in an English, Arabic or Japanese sentence.

```css
:root {
  --font-ui: "IBM Plex Sans", "IBM Plex Sans Arabic", "IBM Plex Sans JP",
             system-ui, -apple-system, "Segoe UI", "Geeza Pro",
             "Hiragino Sans", "Yu Gothic", sans-serif;
}
:lang(ar) { line-height: 1.7; }
:lang(ja) { line-height: 1.6; }
:lang(en) { line-height: 1.45; }
body { font-family: var(--font-ui); font-synthesis: none; }
```

Fix these three things as well:

1. **Direction:** Wrap each stop name in `<bdi>` (or `dir="auto"`) inside Arabic text. Otherwise punctuation and neighboring numbers jump to the wrong side of a Latin name.
2. **Language tags:** Set `lang="ar"`, `lang="ja"` and `lang="en"` on each block. Japanese especially needs this so the browser picks Japanese glyph variants rather than Chinese ones. Tag the embedded Latin stop name `lang="en"`.
3. **Apparent size:** Arabic usually looks smaller than Latin at the same point size, and Japanese is visually dense. Don't use one size for all three. Use `size-adjust` in each script's `@font-face` (or per-`:lang` sizes) and check by eye. Start with Arabic around 5–10% larger, then tune on a real device.

## Numbers in the departures list

Decide on digits once, with whoever owns the content. Western digits (0–9) are common in transport UIs across much of the Arab world, but this is a content and audience call. Whichever you choose, turn on tabular figures (`font-variant-numeric: tabular-nums`) for times so the columns align. Keep times and platform numbers in LTR runs inside the Arabic rows.

## Check before you call it done

- **Real strings:** Test the longest real stop names and alert text at your smallest size, in all three languages.
- **Row heights:** Arabic and Japanese need more line height. If row heights are fixed, the Arabic text gets clipped first.
- **Fallback:** Block the web fonts and check what falls back on iOS and Android. Each system stack above should render all three scripts acceptably.
- **Mirroring:** In the Arabic layout, mirror the card and the departures list, but not the times.

I can turn this into the full `@font-face` setup with subsetting and `size-adjust` values if you tell me whether the app is web, native or both.
