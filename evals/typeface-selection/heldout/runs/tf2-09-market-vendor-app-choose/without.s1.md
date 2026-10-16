**My recommendation is one bundled font, with Roboto (Android's system font) as the fallback.** For "friendly and modern" on this audience, I'd pick **Nunito Sans**, **Figtree**, or **DM Sans**. All three are open-source (OFL) and have rounded, warm letterforms that still read as clean and current.

**Constraints that matter more than the font choice**

- **Bundle the font in the app and don't load it from Google Fonts.** The app has to work offline, and a remote font costs prepaid data and fails on a bad connection. Without bundling, users see a flash of fallback text or the wrong font.
- **Ship one variable font file, or two or three static weights at most.** Regular, Medium and Bold are enough. Subset it to the scripts you need, which usually brings it to roughly 30–100 KB.
- **Use the system font for dense or long text.** Roboto is already on every device, costs nothing, and renders well on mid-range screens. A reasonable split is the custom font for headings, buttons and balances, and system text for everything else. If you want to keep it simple, use the custom font everywhere.

**Things to check before committing**

- **Numerals.** This app is mostly money: contributions, balances, loans. You want clear digits (distinguishable 1/7 and 0/8) and tabular figures (`tnum`) so amounts line up in columns. Inter is the safest choice for this. If you go with one of the friendlier fonts, confirm it supports `tnum`.
- **Language and script coverage.** What languages will the vendors use? Latin with extended diacritics is covered by all the fonts above. For Devanagari, Arabic, Amharic, Thai and similar scripts, you'd need a Noto family or the system font. That could change the whole answer.
- **Legibility on cheap screens.** Test on a real low-end device in sunlight. Use a minimum body size of 16sp, and avoid thin weights and highly stylized rounded display fonts, which blur at small sizes.

**For the founder:** "friendly" will come more from the color palette, icons, spacing, corner radii and wording than from the typeface. A well-set Figtree or Nunito Sans will look friendly without costing anything in data or performance.

If you tell me the target languages and your framework (Flutter, React Native, native Android), I can give you specific font files and the setup.
