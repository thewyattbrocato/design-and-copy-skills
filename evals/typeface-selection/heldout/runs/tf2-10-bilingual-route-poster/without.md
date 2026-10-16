**Short version:** make the route numbers the biggest thing on the page, and treat Hindi and English as two equal-weight settings of the same content. Don't make one the main text and the other a translation underneath. Then make a second, phone-specific layout for the PDF instead of shrinking the A3.

## What gets bigger

Rank by what a person at the stop needs first. Rough A3 sizes, assuming people read it from 1–2 m:

| Element | Size (pt) |
|---|---|
| Route numbers | 120–200, in a bold block or badge |
| "What changed" headline (Hindi and English) | 60–80 |
| New times | 40–50, bold, with tabular figures so columns line up |
| Stop names | 28–36 |
| Dates, contact, small print | 20–24 minimum |

Nothing should go below about 20pt on the A3. Old times should either be dropped or shown small and struck through. They shouldn't compete with the new ones.

## The two scripts

- **Size by visual weight, not point size.** Devanagari has a shirorekha (the top bar) and marks above and below the line. At the same point size it reads smaller than Latin. Set Hindi about 10–15% larger, or match the x-height and the look of the Latin at a glance.
- **Give Hindi more line spacing.** Use about 1.4–1.5, against about 1.2 for English. Tighter spacing makes the marks collide.
- **Pick a family with matched Latin and Devanagari.** Noto Sans and Noto Sans Devanagari, or Mukta or Hind, work well. Use medium or semibold weights. Thin Devanagari strokes disappear in print at distance and on phone screens.
- **Don't letterspace, italicise, or fake-bold Devanagari.** Letterspacing breaks the joined top bar. Italics and synthetic bold distort the letterforms. There are no capitals in Devanagari, so all-caps styling only affects the English.
- **Check conjuncts.** Make sure your layout tool shapes Devanagari correctly (HarfBuzz-based, or InDesign with the World-Ready Composer). Look at the export for broken half-forms.
- **Use one numeral system.** Use 0–9 for route numbers and times in both languages, which is also what bus signage usually does. Keep route numbers identical in both versions.
- **Match the stop signs.** Use the same Hindi spellings and English transliterations that appear on the physical signs and in the timetable. Don't re-translate names.
- **Structure for both languages at once.** For each stop, put the Hindi and English names in one row and show the time once. Don't duplicate the whole table per language. If you do separate blocks, mirror them exactly and give them the same size and weight.

## Phone PDF

A3 is 297 mm wide and a phone screen is about 65 mm, so the page shrinks to roughly a fifth. A 24pt line becomes about 5pt, and people will have to pinch-zoom to read the stop names.

- **Make a second layout.** Use single-column portrait at A5, or a phone-ish ratio, with body text of at least 16–18pt at that page size. Stack Hindi over English in each item. Keep the route numbers large at the top.
- **Use real text.** Embed the fonts and don't convert text to images or outlines, so it's selectable, searchable, and screen-reader friendly.
- **Don't rely on colour alone** to show what's new or changed. Add a label like "नया / New". It also survives black-and-white printing.
- **Keep contrast high.** Dark text on a light background, with no text over photos or tints.

## Quick checks

Print the A3 at 100% and read it from 2 m away. Open the phone PDF on an actual phone at default zoom. If you can't read the route numbers, times, and stop names in both tests, the sizes need to go up.
