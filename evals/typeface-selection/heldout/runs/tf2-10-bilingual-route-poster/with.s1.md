**Assumptions:** one A3 portrait sheet, and one PDF with the fonts embedded. If you ship a separate phone layout, the same logic applies but the sizes change.

## Type choice

- **Use one family that covers both scripts.** The best-known option is Noto Sans with Noto Sans Devanagari. Both are open-licensed, but confirm that on the foundry page before you rely on it. Hindi and English then share stroke weight and proportions, and no Latin face has to supply Devanagari glyphs it lacks.
- **Pick a sturdy sans in a medium, semibold and bold.** Avoid light weights. Devanagari's fine joins and the shirorekha (the headline bar) thin out at small sizes and on phone screens.
- **Embed the fonts in the PDF** so phones never substitute them. For anything in HTML, set `lang="hi"` and `lang="en"` on the right elements.
- **Use real bold only.** Devanagari has no italic tradition, so don't italicise Hindi. Use weight or a tint for emphasis in both scripts.
- **Give route numbers and times tabular (fixed-width) figures** so columns align. Pick one numeral system. Western digits (0–9) are the usual choice for transit, and the Hindi lines should use them too.

## What gets bigger

Roughly, from the biggest to the smallest, at A3:

| Element | Size at A3 | Weight |
|---|---|---|
| Route numbers | 150–250 pt, the largest thing on the sheet | Bold |
| Headline ("Route change") | 60–80 pt | Bold |
| Stop names | 28–36 pt | Semibold |
| New times | 28–36 pt | Semibold, tabular figures |
| Explanatory lines, dates, contact | 16–20 pt | Regular |

- **Route numbers are what people look for first.** Put them in a bold block, or on a coloured chip with strong contrast, so they work from a few metres away.
- **Times matter as much as stop names.** Keep them out of running sentences and put them in a table or aligned columns.
- **Set the smallest text no lower than about 14 pt on the A3 sheet.** On the phone PDF, A3 gets scaled down to roughly a quarter of its width. Anything under about 20 pt on the page then becomes unreadable without zooming. Put the essentials (routes, stops, times) at 28 pt or above and keep the small print short.

## Handling the two scripts

- **Match apparent size, not point size.** Devanagari at the same point size as Latin usually looks smaller and denser, so set it about 10–15% larger (or check by eye) so the two lines look equal. Treat that figure as a starting point to check by eye.
- **Give Hindi more line height.** It has tall marks above and below the line, so 1.5–1.6 is a good start, against about 1.3 for English.
- **Don't mix scripts within a line when you can avoid it.** Put Hindi and English in parallel blocks with the same structure, in one of these layouts:
  - side by side in two columns, or
  - Hindi on top and English below, per section.
- **Choose which language leads.** The leading language should be the one most of your readers use. Keep the order the same everywhere.
- **Keep the two versions the same length.** Hindi runs longer than English. Check that the stop names and times still line up row by row.
- **Keep stop names in the way people see them on the bus.** If the signage is in Hindi, use that spelling on the notice.
- **Put proper nouns in both scripts** (stop names, route names), so people can match them to what they see.

## Before you print

1. Print a test page at A3 and stand about two metres back. Route numbers should read instantly.
2. Open the PDF on a phone and check that the Hindi marks aren't breaking up, and that you can read the times without zooming.
3. Check that the fonts are embedded (File → Properties → Fonts in a PDF reader).

I can also draft the layout as HTML/CSS with the font stacks, if you tell me which tool you're using for the notice.
