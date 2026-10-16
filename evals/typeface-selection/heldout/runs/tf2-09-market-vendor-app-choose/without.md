**My recommendation:** bundle one friendly, highly legible sans-serif as a variable font, and fall back to the system font (Roboto on Android). I'd use **Figtree**. **Nunito Sans** is a good alternative if the founder wants something softer.

**Why this fits your constraints**

- **Bundle the font in the app and don't load it from a CDN.** Google Fonts or other web fonts would fail offline and cost vendors data. A single variable font file is typically tens of KB, and you can subset it to the characters you need.
- **Limit the weights.** Regular, Medium and Bold cover almost everything. A variable font gives you those in one file.
- **Figtree reads as friendly and modern.** It has geometric shapes with warmth, a generous x-height that stays readable on small, lower-resolution screens, and clear numerals. Numerals matter most in a savings app.
- **Nunito Sans is the softer option.** Nunito (the version with rounded terminals) is friendlier still, but it can look a bit childish for a money app. Nunito Sans keeps most of the warmth with less of that risk.

**Things that matter more than the font choice**

- **Numerals:** Turn on tabular figures (`tnum`) for amounts and balances so columns line up. Check that 1/l/I and 0/O are easy to tell apart.
- **Size:** Use at least 16sp for body text and larger for amounts. Many users may be older, and screens are often used in sunlight.
- **Contrast:** Use strong contrast, because thin weights wash out outdoors. Avoid Light weights.
- **System font scaling:** Respect Android's font-size setting, and test your layouts at 130–150%.
- **Fallback:** If the custom font fails to load, Roboto is a fine default and costs nothing.

**What I need to know first:** which languages and scripts will the app support? Figtree and Nunito Sans cover Latin well, including extended Latin for languages like Swahili or Yoruba. If you need Devanagari, Arabic, Amharic or similar, the answer changes. Noto Sans has the broadest coverage, but each script adds file size. Pairing Figtree for Latin with the matching Noto script as a fallback is usually the best approach.

Before committing, put a few candidate fonts on an actual low-end Android phone and compare them with real data, such as a member list, contribution amounts and a long name.
