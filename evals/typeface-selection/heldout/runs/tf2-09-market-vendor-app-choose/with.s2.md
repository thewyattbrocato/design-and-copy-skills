**Recommendation: one family, bundled inside the app and used at a few weights.** I'm assuming Latin script, an Android app, and a "friendly" brief from the founder.

**Primary choice: Nunito Sans.** It's a humanist sans with soft, open shapes, so it reads as friendly without turning childish. It has a real weight range (Regular, SemiBold, Bold) and true italics.
- Use Regular for body, SemiBold for labels and buttons, and Bold for headings.
- Digits and I/l/1/O/0 need to be checked at your smallest size on a real mid-range screen.
- Turn on tabular figures for money and contributions: `font-variant-numeric: tabular-nums`, or the platform equivalent.

**Why bundle it instead of loading from the web:**
- Offline use and prepaid data rule out any runtime font download. Ship one variable file, or 3–4 static WOFF2/TTF files, inside the app package. That adds roughly one file's weight to the install, not to each session.
- Subset it to the characters you need. Add the accents your languages use, plus currency symbols.
- Don't load from Google Fonts at runtime. It costs data, and it fails offline.

**Fallback (the stack has to look fine if the font fails):**
```css
--font-ui: "Nunito Sans", system-ui, Roboto, "Noto Sans", sans-serif;
```
On Android this falls back to Roboto, which is clean and has the same x-height behavior, so layouts won't shift much. Don't use a bare `sans-serif` as the whole stack.

**What I'd avoid:**
- **Rounded or display faces for body text.** Quicksand, Fredoka and Baloo look friendly in headlines but get fuzzy at small sizes on low-density screens.
- **A second family.** It would add weight and offer no extra role. Get hierarchy from size and weight.
- **Thin weights.** Nothing lighter than Regular, because light strokes break up on cheap screens in sunlight.
- **Faux bold.** Ship the weights you use, and set `font-synthesis: none`.

**Zero-cost alternative:** if app size or maintenance matters most, use the system font (Roboto on Android). It costs nothing, always works offline, and covers every language. It's less "friendly," but it's sound. You could also use Nunito Sans only for the logo and large headings, with the system font for everything else.

**Two checks before committing:**
1. **Languages.** If vendors use a non-Latin script or Vietnamese-style stacked diacritics, tell me, because the pick changes. Choose for the harder script first. Noto Sans has the widest coverage.
2. **License.** Nunito Sans is distributed under an open license, but confirm the terms for app embedding with the source you download it from.

I can also put together a quick type scale (sizes for body, labels, and money amounts) tuned for small Android screens, if that would help.
