**Use one family, bundled inside the app: Figtree, as a variable font.** I haven't checked its script coverage or its tabular figures, so confirm both before you commit (details below).

- **Why it fits "friendly and modern":** it has soft, open, geometric shapes and a sturdy build. That holds up on mid-range LCD screens, where thin rounded faces like Nunito can look weak at small sizes.
- **Offline:** bundle the font file in the app (an Android `res/font` resource, or your framework's asset bundle). Don't load it from the web, since prepaid data and spotty signal would break that. Subset it to the scripts you need and ship one variable file, which keeps the app small.
- **Hierarchy:** use weight and size within the one family.
  - Body text: Regular (400), at 16sp or larger.
  - Labels and buttons: Medium or SemiBold.
  - Headings and balances: Bold.
  - Don't use Light for anything. Don't use faux bold or italic.
- **Money:** contribution amounts and balances should line up in columns. Turn on tabular figures (`tnum`) if the font has them. The `0`, `O`, `1` and `l` should also be easy to tell apart.
- **Fallback:** Figtree, then `Roboto`, then `sans-serif`. Roboto is on virtually all Android phones, so the app still looks intentional if the font fails.
- **No second family:** the app is mostly forms, lists and numbers, so a display face or a mono face has no job here.

**Two things to check:**
1. **Languages.** I assumed Latin script. If your vendors read Swahili, Hindi, Arabic, Amharic or another script, check that the font covers it, including diacritics. If it doesn't, switch to **Noto Sans**, which is open-licensed and designed to cover many scripts. It's a bit plainer, but it never falls back to a mismatched glyph.
2. **Licence and tabular figures.** Figtree is distributed under an open licence, but confirm that it permits embedding in an app. Check the font file itself for `tnum` support. If it lacks `tnum`, Noto Sans is the alternative here too.

Whichever you pick, test a real screen of your app on an actual low-end Android phone at the smallest text size. Do this before you settle the choice.
