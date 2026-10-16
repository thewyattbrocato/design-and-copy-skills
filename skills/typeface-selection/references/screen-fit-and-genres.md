# Screen fit and mood

Load when the face must survive real screens: dense interface text, tiny labels, a delicate or mandated brand face, a thin or blurry render, or a name-only brief ("elegant", "quiet", "warm").

## 1. Will it survive the smallest real use?

Drop any candidate that fails these, then choose by voice among the rest: it covers the real text (set the actual names, currencies and diacritics, not the specimen line); it has the styles used (regular, medium or semibold, bold, true italic); it has tabular figures and a distinct 0/O and 1/l/I where data appears; the file that ships is affordable and licensed.

**Small interface text** (labels, tooltips, table cells, status chips, chart annotations): about 12px is the floor, in regular weight or heavier, never a light or condensed cut. Errors, prices and instructions are not small text; they stay at body size (see typesetting). If 12px looks weak, change the face before the size: a sturdy sans with open apertures and a larger x-height. Keep the body family unless it fails; a second face for labels is a last resort.

**Delicate and mandated faces.** A hairline, ultralight or high-contrast display face (a fat-face or Didot-style serif, a thin geometric) is a display tool. Use it big, short and in a heavy-enough weight on a clean ground; give the small text a sturdy partner. When a guideline demands it everywhere, state the downside in one line (small sizes and low-density screens break it up), keep it for headings and marks, and name the partner for body and UI as the exception to propose.

Before/after for "elegant headline, warm body":

- Before: ultrathin high-contrast serif at every size, with a thin script for subheads.
- After: the same serif for the headline only, at 40px or more and a weight whose hairlines still show on a cheap, dim screen; a warm text serif or humanist sans for body and captions. Expected failure to name: below about 24px the hairlines vanish, so the headline never wraps into small sizes and never sits on photos.

## 2. Which mood family?

Pick the family from the product, then the specific face. These are tendencies, not guarantees.

- **Data tool or admin screen:** a grotesque or humanist sans with plain letters and mid contrast. Reads as exact and restrained; can go bland, so avoid near-clone pairs. Mono only for code and aligned columns.
- **Editorial or documentation:** a sturdy text serif. Reads as calm and credible; stiff if pushed into dense controls.
- **Consumer or family product:** a humanist or rounded sans with open, soft shapes. Reads as friendly; weak authority for money or legal text.
- **Luxury, fashion or a poster:** a high-contrast or expressive display face, big and short only, with a plain partner for small text. Breaks on small and dim screens.

For a brief like "quiet", choose a plain, mid-contrast, mid-weight text face without distinctive letters, and say which family it came from.

## 3. Prove it

Set a real specimen on the real background: the longest label in the data, a form row with an error, a column of prices, one paragraph at the smallest size. Two minutes on that beats any list of attributes.

Then look at three renderings: a low-density Windows screen (thin strokes fatten or break), a mid-range Android phone, and light text on a dark ground (it looks bolder; step down a weight or grade). If body looks thin or blurry on Windows, the cause is a light or hairline cut, a high-contrast face, or a mismatched web file, not the size; switch to a regular-weight, lower-contrast cut before touching CSS.

Fallbacks: choose per platform the one whose letters sit closest in size and width, then in style. Pair the web font with a metric-tuned local fallback (`size-adjust` and the override descriptors) so a swap does not shift the layout; `font-size-adjust: from-font` (or a fixed ratio) keeps the visual size steady when a fallback with a different x-height takes over, and it is safe to include where unsupported.
