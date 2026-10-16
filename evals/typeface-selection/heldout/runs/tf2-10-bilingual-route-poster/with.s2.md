**Assumption:** the notice is read standing, from about 1–2 m, and zoomed in on a phone. I haven't checked any specific fonts against your files.

**Fonts**
- Use one matched pair from the Noto family: **Noto Sans** for English and **Noto Sans Devanagari** for Hindi. Both are open-licence, have real bold weights, and share stroke weight and proportions, so the two scripts look like one voice. **Mukta** and **Hind** are alternatives that were designed to carry both scripts. Check the licence terms for PDF embedding with the foundry.
- Don't use a Latin display face for the English and a separate Hindi face beside it. Don't let a Latin font supply Devanagari glyphs either, because a mismatched substitute will appear.
- **Embed and subset the fonts** in the PDF and keep the text as live text. That keeps it sharp, searchable and readable by screen readers.

**What gets bigger**
Route numbers, then the stop names and times. Everything else is context. Starting sizes at A3:

| Role | English | Hindi |
|---|---|---|
| Route numbers (in a badge) | 150–250 pt bold | same, shared |
| Headline ("Route change") | 60–72 pt | 66–80 pt |
| Stop names and times | 30–36 pt | 34–40 pt |
| Dates, notes | 22–26 pt | 25–29 pt |
| Smallest text (contact, fine print) | 18 pt | 20 pt |

**The two scripts**
- **Size Hindi up by about 10–15%.** At the same point size Devanagari looks smaller, so match them by eye.
- **Give Hindi more line height.** Use about 1.5–1.6, against about 1.3 for English, so the tall marks above and below don't collide.
- **Use bold for emphasis in both scripts.** Devanagari has no true italic or capitals, so never slant it or use all-caps. Faux italics are a common mistake.
- **Use the same layout for both.** Put Hindi and English in matching blocks, side by side or stacked, with the same hierarchy. Don't mix scripts within a line, except for stop names that are already printed in both.
- **Use Western digits (0–9) for route numbers and times.** Use tabular figures so the times line up in columns. Make the same choice for both languages and apply it everywhere.
- **Don't squeeze Hindi into a narrow column.** It runs about 10–30% longer than English, so plan the space for it first.

**Print and phone**
- A3 text is tiny on a phone. The page shrinks to about a quarter of its size, so 30 pt becomes roughly 7 pt. Scaling the poster down won't make it readable.
- I'd make a **second layout for phones**: a single column in the same fonts, with the route number, stops and times large enough to read without zooming. Export it as its own PDF.
- If you must ship one file, keep the table text at 30 pt or more and avoid multi-column layouts. Set the document language tags to `en` and `hi`.

Before you send it, print one page at A3 and view the PDF on an actual phone. Check that the Hindi is readable at both sizes and that no fallback font crept in.
