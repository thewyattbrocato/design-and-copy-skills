**My recommendation is one bundled variable font, Figtree, with the Android system font (Roboto) as the fallback.**

**Why this suits your constraints**
- **Bundle the fonts in the app.** Don't load them from Google Fonts or a CDN. With spotty connections, a web font fails or flashes in a different typeface, and it costs prepaid data. Bundled fonts work offline from the first launch.
- **Keep the font payload small.** Use a variable font file (about 100 KB or less when subset), or at most two static weights (Regular and SemiBold). Don't ship five weights of Poppins.
- **Figtree looks friendly and modern.** It's geometric with soft, open shapes, and it stays legible at small sizes on low-density mid-range screens. Nunito Sans is a good alternative if you want it slightly rounder. Inter is more neutral and corporate, so I'd skip it for this brief.

**Things that matter more than the font choice**
- **Number legibility.** This is a money app, so use a font with clear digits (distinguishable 1/7, 0/O) and enable tabular figures (`font-variant-numeric: tabular-nums` on web, `fontFeatureSettings: 'tnum'` in React Native or Flutter). Contribution and balance columns will then line up.
- **Sizes and weights.** Use at least 16sp for body text and 14sp for secondary text. Avoid Light and Thin weights, because they wash out on cheap LCD screens in sunlight, which is where market vendors will use the app.
- **Language and script coverage.** I don't know which languages your users read. If you need more than Latin (Devanagari, Arabic, Amharic, Swahili with diacritics, and so on), check that Figtree covers it. If it doesn't, use the matching Noto Sans family for that script, or fall back to the system font. Missing glyphs showing as boxes would hurt trust far more than a less trendy typeface.
- **Fallback stack.** Always specify a fallback (`Figtree, Roboto, sans-serif`), so text still renders if the font file fails to load.

**Cheapest alternative:** use Roboto (the system font) for everything and get the "friendly" feel from rounded corners, color, spacing, and illustration. That costs zero bytes and has the widest script coverage. I'd use it if the language list is long.

Which languages and scripts will the app need to support? That's the one thing that could change this recommendation.
