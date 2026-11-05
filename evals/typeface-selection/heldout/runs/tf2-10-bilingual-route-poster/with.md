**Assumptions:** the PDF is vector with fonts embedded, and the printed A3 and the phone PDF come from the same file.

## Fonts

- **Pick the Devanagari face first, then a Latin face to match it.** The Devanagari set is the smaller choice, and the Latin has to sit beside it.
- **Prefer one family that covers both scripts.** Noto Sans / Noto Sans Devanagari is the usual option. It is an open license, but confirm that on the foundry's page. Other Hindi-and-Latin families exist, such as Mukta and Hind. Check that the family has real regular, medium and bold weights in both scripts. If you use two separate fonts, pick ones with a similar stroke weight and x-height.
- **Choose a sturdy sans with a plain, open shape.** The notice has to be read quickly and from a distance, so avoid thin, ornamental or calligraphic Devanagari. Avoid light weights in both scripts. Phone screens and A3 print at distance both punish thin strokes.
- **Don't let a Latin-only font supply Hindi glyphs.** The system will swap in an unmatched face. Embed both fonts in the PDF.
- **Use bold or color for emphasis, not italics.** Devanagari has no italic tradition, and a slanted Hindi font is usually a fake.

## What gets bigger

Make the information people act on the largest, and set the rest in small, calm type.

1. **Route numbers are the largest.** They are the first thing people scan for. Put them in a bold weight, in a block or badge, and keep them identical in both languages.
2. **Then the headline,** such as "Route changed from [date]". Give it in both scripts.
3. **Then stop names and new times.** This is the main content, so keep it large enough to read at a distance. Set the times in tabular figures, so columns align, and use a consistent 24-hour or AM/PM format.
4. **Small text last:** reason for the change, helpline, validity dates and contact. Small text should still be readable on a phone.

Starting sizes for A3 are a guide only, so test them on a printout:

| Role | A3 print |
|---|---|
| Route number | 150–250 pt |
| Headline | 56–80 pt |
| Stop names and times | 28–40 pt |
| Detail text | 16–20 pt |

For the phone PDF, the same layout scales down to about 1/3 on a 6-inch screen. That means the detail text will be around 6–7 pt there. Either make it larger than the table suggests, or set the phone version in a single column with the key content first.

## Handling the two scripts

- **Give Devanagari more size and more line height.** At the same point size it looks smaller than Latin. Start with Hindi at about 10–15% larger than English. Use about 1.5× line height for Hindi, versus about 1.2–1.3× for English. The headline and matras (the marks above and below the line) need room, and tight leading makes them collide.
- **Don't letter-space Hindi.** Tracking breaks the headline bar (shirorekha) and the joined conjuncts.
- **Use the same hierarchy in both languages.** Both should carry the same weight and size roles. Neither should look like a footnote.
- **Pick one layout for the two languages:** side by side for A3 (Hindi on the left, English on the right, or the reverse), and stacked for the phone PDF. If you have to choose one language to go first, put Hindi first, since it is probably the main audience.
- **Don't translate the numerals unless you have to.** Use the same figure style in both languages. If the local audience reads Devanagari digits, use them in the Hindi text and Western digits for route numbers and times, and make that decision once. Don't mix them in one line.
- **Keep stop names in their native script,** with the other script as a secondary line. This also helps people who can read only one script.
- **Set the language tag** (`lang="hi"` and `lang="en"`) if the file is made in HTML, so the right glyph forms are chosen.

## Checks before you send it

- Print one page at 100% and read it from 2–3 metres.
- Open the PDF on a phone and check that route numbers and times are readable without zooming.
- Look at the PDF's font list to confirm that both fonts are embedded and none was substituted.
- Check Hindi conjuncts and matras by eye. Broken conjuncts (e.g. in क्ष, त्र, श्र) or detached marks mean a font or rendering problem.

If you tell me the tool you're using (InDesign, Word, Canva, HTML to PDF) and which fonts you have installed, I can give you exact settings.
