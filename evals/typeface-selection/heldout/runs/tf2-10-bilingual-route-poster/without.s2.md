## What gets bigger

Size things by what a person standing at a stop needs first.

1. **Route numbers**: the biggest thing on the page, ideally in a badge or box. They're the same in both languages, so show them once and don't repeat them per language.
2. **Effective date and "what changed"**: second largest. Most readers only need to know whether their bus is affected.
3. **Times**: large, in a table with tabular (fixed-width) figures so the columns line up.
4. **Stop names**: next down. They're the longest strings, and Devanagari names run wide.
5. **Fine print**: contact details, reasons and so on. Set it no smaller than about 18 pt on A3.

For a rough scale on A3, use 150 pt or more for route numbers, 48–72 pt for the date headline, 32–40 pt for times and stop names, and 20–24 pt for everything else. People read it standing 1–2 m away, so test by pinning a draft to a wall and stepping back.

## Print and phone need different treatment

A3 is about 297 mm wide and a phone screen is about 65 mm, so everything shrinks to roughly a fifth. 24 pt on A3 looks like 5 pt on a phone. People can pinch-zoom, but they shouldn't have to. I'd do one of these:

- **Best:** make a second, phone-specific PDF with the same content, in a single portrait column at about A5 size or a narrow custom page (for example 105 × 200 mm). Keep the same type hierarchy and the same file content.
- **If you must use one file:** keep the A3 layout simple, with big blocks and few columns, so zooming in on one block works.

In either case, keep the text as live text rather than outlines or images, and embed the fonts. That keeps it searchable, lets it work with screen readers, and lets it reflow when zoomed. Export the print file as CMYK (PDF/X) and the phone file as RGB, with a small file size.

## Handling the two scripts

**Size**
- Devanagari looks smaller than Latin at the same point size. Set it about 10–15% larger, or match the visual height of the two scripts by eye.
- Give Devanagari more line height, about 1.4–1.6. The headline bar and the marks above and below the letters collide at tight leading.

**Font**
- Use a family designed as a pair, such as Noto Sans + Noto Sans Devanagari, or Mukta or Hind, which have matching Latin.
- Use Regular or Medium weights and avoid thin ones. Thin strokes break up in print and on phone screens.

**Emphasis**
- Use weight, size or colour. There are no capitals in Devanagari, and italics and letter-spacing both distort it. Letter-spacing in particular breaks the joined letterforms.

**Layout**
- Give both languages equal prominence and the same hierarchy. Hindi shouldn't read as a small translation under the English.
- On A3 landscape, side-by-side columns work. On the phone version, stack them within each block (for example, one route's Hindi then English) rather than putting all of Hindi first and all of English second. That way people don't scroll to find their language.
- Make sure the Hindi and English line up block by block, so that each route and its times sit at the same position on both sides.

**Numerals and names**
- Use one numeral system. Western digits (0–9) are the usual on bus signage and avoid confusion with times. Don't mix them with Devanagari digits.
- Make the stop names match the signs at the stops exactly, in both scripts. Check the transliterations against what's on the physical signage.
- Spell out time conventions, for example 24-hour or AM/PM. If you use AM/PM, include Hindi equivalents consistently.

**Contrast**
- Use dark text on a white or very light background, and don't put text over photos or tinted blocks. Use colour for route badges only, and make sure they still read in greyscale.

If you send me the content, I can lay out a size scale or a table template with the specifics.
