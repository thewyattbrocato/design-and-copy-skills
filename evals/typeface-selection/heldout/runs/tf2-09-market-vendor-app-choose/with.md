**Use one family, bundled inside the app: Nunito Sans.** It's an open-license (SIL OFL) humanist sans with softly rounded forms, which gives the "friendly and modern" look. It's sturdy enough for small text on mid-range screens.

**Roles**
- **Everything (headings, body, buttons, labels):** Nunito Sans in Regular 400, SemiBold 600 and Bold 700. Hierarchy comes from weight and size, not a second font.
- **Money and balances:** the same family with tabular figures turned on, so contributions and totals line up in columns. Check that the build you bundle includes `tnum`.
- **Fallback:** `Roboto, sans-serif`. Roboto is already on Android, so if the font fails to load, the app still looks close to intended.
- **No monospace and no second family.** Nothing in a savings-group app needs them.

**Why this fits your constraints**
- **Offline and prepaid data:** package the font files in the APK or app bundle instead of downloading them at runtime. That way there's no data cost, nothing fails offline, and there's no flash of the wrong font. Ship only 3 weights, or one variable file, and subset to the scripts you need to keep the app small.
- **Mid-range screens:** it has a generous x-height and open shapes, and the digits and the I/l/1 and O/0 shapes stay distinguishable. A hairline or thin geometric font would look faint on these phones.
- **Friendly but not childish:** I'd avoid fully rounded display fonts like Nunito itself or Quicksand for body text. They get fuzzy at small sizes and make money screens look like a toy. The slightly softened Nunito Sans reads as warm without that.

**Starting sizes:** body 16sp, secondary text no smaller than 14sp, balances 20–24sp in SemiBold, screen titles 20–22sp in Bold.

**Assumptions to confirm**
- I assumed Latin script. If your vendors read another script such as Arabic, Devanagari or Amharic, choose the font for that script first. Noto Sans has the broadest coverage, and Nunito Sans won't cover those scripts.
- Confirm that the specific font build includes tabular figures and every character your languages need, including accents.
- The SIL OFL license allows app embedding, but check the license text for your exact files.

I haven't rendered it. Before you commit, put a real screen with amounts, names and a paragraph on an actual low-end Android phone at 1x brightness.
