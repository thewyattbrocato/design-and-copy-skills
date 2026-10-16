I'm assuming a single-page notice, A3 portrait for print, and the same layout as a PDF on phones. Here's the approach.

**Typeface**
- Pick the Devanagari face first, because it's the harder script, then pick a Latin face that sits well beside it. Noto Sans Devanagari with Noto Sans is a safe default. It's open-licensed, the two are designed as a matched family, and they have real bold weights. Other options are Mukta or Hind, which also pair a Devanagari face with a Latin one. Check that whatever you choose has the weights you need (regular, semibold or bold) and the conjunct and matra shapes you use. Don't let the Latin font supply Hindi glyphs, because a fallback will be substituted and won't match.
- Use one family pair for everything. Hierarchy comes from size and weight, not from extra faces.
- Embed and subset both fonts in the PDF. Phones won't have them, and an unembedded font silently turns into a default.
- Avoid light or thin weights. Devanagari has fine headline-bar and matra details that disappear at small sizes on phone screens.

**What gets bigger**
1. **Route numbers.** These are the largest thing on the page, set in bold. People scan for their number first. Put each in a solid block or badge, and use tabular figures if numbers sit in a column.
2. **New times.** These come second. Make them bold and large, with the old times clearly marked as old, in a smaller size or struck through, so nobody reads them as current.
3. **Stop names.** Make these body-large rather than small print. They're the content people actually read.
4. **Everything else** (explanatory text, dates, contact info) is smaller, but it has to stay readable.

Starting sizes for A3:
- Title: 70–90 pt
- Route numbers: 100 pt or more
- Times: 36–48 pt
- Stop names: 28–36 pt
- Smallest text: 18–20 pt

The PDF scales down on a phone (A3 on a phone screen is about 1/4 size), so the smallest text still has to read at that scale. Test it by opening the PDF on an actual phone.

**Two scripts**
- **Match apparent size, not point size.** Devanagari has a smaller x-height than Latin, so at equal points it looks smaller. Set Hindi about 10–15% larger, then adjust by eye.
- **Line height.** Hindi needs more leading than English because of the headline bar (shirorekha) and the tall matras above and below the line. Use about 1.5–1.6 for Hindi and about 1.3–1.4 for English.
- **Layout.** Pick one pattern and use it everywhere. Either put Hindi and English in two parallel columns, or stack them with Hindi first (if that's the main audience) and English directly below. Don't alternate between the two.
- **Same weight, same hierarchy.** The Hindi and English versions of each element should have the same visual weight so neither looks like a translation of the other.
- **Don't italicize or letterspace Hindi.** Devanagari has no true italic, so the browser or PDF tool will fake a slant, which distorts it. Letterspacing breaks the headline bar and joined letters.
- **Numerals.** Decide up front whether to use Western (0–9) or Devanagari (०–९) digits. Most bus signage uses Western digits for route numbers and times, since that's what riders match against the bus. Use the same digits in both scripts.

**Checks before you send it out**
- Print a draft at A3, or at 50% scale on A4 and view it from arm's length.
- Open the PDF on a low-end phone and confirm that the route numbers and times are still legible without zooming.
- Have a Hindi reader check that no conjuncts or matras are broken.

If you tell me which fonts you have installed, or what tool you're laying this out in, I can be more specific.
