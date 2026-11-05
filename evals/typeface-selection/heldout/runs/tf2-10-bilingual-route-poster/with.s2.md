**Assumptions:** the notice is A3 portrait and the fonts are open-licence. Check the licence for print and PDF embedding, and check that every glyph in your copy renders.

## Typefaces

- **Use one superfamily that covers both scripts.** Choose for Devanagari first, then match the Latin to it. Noto Sans plus Noto Sans Devanagari is designed as a matched set. Mukta is a single family with both scripts. Either gives you real weights and avoids a mismatched fallback.
- **Use sturdy weights.** Regular, Medium or SemiBold, and Bold. Avoid Light, because thin Devanagari strokes and the headline bar (shirorekha) break up at small sizes and on phone screens.
- **Don't add a second family.** The hierarchy comes from size and weight.
- **Embed the fonts in the PDF.** Otherwise a phone may substitute a Devanagari font that doesn't match.

## What gets bigger

Rank by what a rider needs at a glance. These are starting sizes for A3, so test them on a print proof.

| Element | Starting size |
|---|---|
| Route numbers | Largest, about 120 pt or more, in a solid block |
| Title ("Route change" in both languages) | 60–72 pt Bold |
| Stop names | 28–36 pt, Medium |
| New times | 28–36 pt, Bold, tabular figures so columns align |
| Explanatory text and dates | 20–24 pt |
| Fine print (helpline, website) | Not below 16–18 pt |

The route number is the same in both languages, so show it once.

## Handling the two scripts

- **Match apparent size, not point size.** Devanagari usually looks smaller than Latin at the same point size. Set it about 10–15% larger, and compare by eye.
- **Give Hindi more line height.** Use about 1.5–1.6 for Hindi and about 1.3 for English. Matras above and below the line need the room. Clipped marks are the usual failure.
- **Pair the languages line by line.** Put the Hindi and English stop name together, one above the other. Don't make two full columns that repeat the whole table. Print each time once.
- **Pick one order.** Put the language most of your riders read first, and keep that order everywhere.
- **Tell the scripts apart by script alone.** Use the same weight and colour for both.
- **Don't italicise, track out or capitalise Hindi.** Devanagari has no italic or case tradition. Letter-spacing breaks the joined headline bar and the conjuncts. Use weight for emphasis.
- **Choose one digit style.** Western digits (0–9) for route numbers and times is common on Indian transit signage. Use them throughout, and confirm against your agency's convention.
- **Set the `lang` attribute** (`hi` and `en`) if the PDF is generated from HTML or tagged, so glyph variants and fallbacks are chosen correctly.

## The phone PDF

A3 shown on a phone is scaled to roughly a fifth of its size. A 16 pt note ends up about 3–4 pt, and even the 30 pt stop names are small. Two options:

1. **Best:** make a separate phone layout. Use a single column at a narrower page size, with one card per route. Keep the type sizes and weights above.
2. **If you must reuse the A3 file:** raise the minimum text size to about 24 pt. Keep the text live and selectable, not outlined or flattened to an image, so people can pinch-zoom and screen readers can use it.

If you want, I can mock up the type specs as CSS or a print-ready HTML template once you share the copy.
