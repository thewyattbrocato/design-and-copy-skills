# Type for a bilingual A3 bus notice (also read as a phone PDF)

## What gets bigger
Size by what the reader needs to act on, not by how important the notice feels.

1. **Route numbers** are the largest element, about 100pt or more at A3. Put them in a solid badge so they work as an anchor.
2. **What changed** is the headline, about 60–80pt. For example, "Route 42 timings change from 1 Nov."
3. **Times and stop names** come next, at 32–44pt. Use tabular (monospaced) figures so times line up in columns. Bold the new times and show the old ones smaller or struck through.
4. **Reasons, contact details and the effective date** can be 20–26pt. Nothing at A3 should go below about 18pt.

## The two scripts
- **Make Hindi larger than English.** At the same point size, Devanagari looks smaller than Latin because its x-height is lower. Set Hindi about 10–15% larger, or optically match the two. Check by eye rather than by number.
- **Give Hindi more line height.** Use about 1.4–1.5 for Devanagari, against 1.2–1.3 for English. Matras above and below the line collide if it's tighter.
- **Use a matched family.** Noto Sans plus Noto Sans Devanagari is the safe pairing. Mukta, Hind, or Inter with Noto Devanagari also work. Avoid light weights, because Devanagari's thin strokes and headline bar break up in print and on small screens. Use Regular or heavier, and use a real bold, never a synthesised one.
- **Don't use italics, all caps or letter-spacing on Hindi.** Hindi has no caps, italics are poor in Devanagari, and tracking breaks the connected headline bar. Use weight and size for emphasis instead.
- **Use the same digits in both languages.** Western digits (0–9) are the norm on Indian transit signage and are the easiest to scan. Don't mix them with Devanagari numerals.
- **Keep the languages in separate blocks.** Use two columns or stacked panels with the same structure, so each row matches across languages. Avoid mixing scripts inside one line, except for route numbers and times. Give Hindi and English equal weight, and put Hindi first if it's the main audience.
- **Transliterate stop names carefully.** Check them against the official stop signage and the Hindi names people actually use.

## The A3 and phone problem
A3 is 297 mm wide and a phone screen about 65 mm, so a straight scale-down is around 22%. A 40pt stop name becomes about 9pt, and the 20pt fine print becomes about 4pt. That's readable only by pinching and zooming.

- **Best option:** make a second, phone-specific layout. Use a single column, a portrait page about 100 × 180 mm, and a body size of about 11–12pt. Show one route per block, with times in a simple list.
- **If you must ship one PDF:** keep it to a single column and put the route number and new times at the top. Make sure the important content is still legible when the page is fit to width.

## PDF checks
- Embed all fonts, because Devanagari conjuncts and matras can reflow or break if a substitute font is used.
- Keep the text live rather than outlined, so it's searchable and screen readers can read it.
- Tag the PDF and set the document language, with Hindi and English marked on their respective spans.
- Check contrast (at least 4.5:1 for small text) and don't use colour alone to mark what changed.
- Proof the Hindi on an actual phone and a printed A3 proof. Look for broken conjuncts, clipped matras and wrapped stop names.

If you tell me the layout tool (InDesign, Figma, Canva, LaTeX or something else), I can give exact settings.
