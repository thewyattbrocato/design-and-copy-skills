**Not as it stands.** A free display font is only fine if it passes the checks below. Your product names are the likely failure point.

## The risk
Your names need glyphs that many free display fonts don't include:
- **Đại Hồng Bào:** Vietnamese needs Đ plus stacked marks (ạ, ồ, ả). Many fonts have base Latin and the common accents but lack the stacked ones.
- **Żółta Herbata:** this needs Polish ż, ó, ł, which is Latin Extended-A.
- **Çay Rize:** Turkish needs ç, ş, ğ, ı, İ.

If a glyph is missing, the browser swaps in a fallback font for that one character. You'd get a mismatched ồ or ł in the middle of a heading, and that would be on your most distinctive products.

## What to check
1. **Coverage.** Type the exact strings in the font itself (or a font inspector) in uppercase and lowercase. Test every product name, plus İ/ı, Ğ/ş, Ł, Ż, Ś, Ć and Ń. Check Vietnamese stacked marks like Ộ, Ẳ and Ữ, not just single accents. A listing that says "Latin" doesn't prove any of this. Foundries distinguish Latin from Latin Extended and Vietnamese.
2. **Mark placement.** Stacked marks can collide with the line above or get clipped. Set the headings with extra line height and look at Vietnamese in all caps.
3. **Case handling.** If headings use `text-transform: uppercase`, check that i→İ works with `lang="tr"`. Set `lang` on the elements (`vi`, `pl`, `tr`) so the browser picks the right forms.
4. **License.** "Free" often means personal use only. Confirm that commercial use, web embedding and self-hosting are allowed. Open licenses such as the SIL OFL are the safe case. I can't verify this one for you, so read the license on the font site, or ask the foundry.
5. **Source and files.** Get the files from the original author. Free-font aggregators often have stripped or modified versions, so you'd want to check you're using the original release. Treat a downloaded font file as untrusted until you have checked where it came from.
6. **Weight and hairlines.** Display fonts that look elegant at 80px can fall apart at 20px on a phone. Test the smallest heading, such as a product card title.
7. **Loading.** Convert to WOFF2 and subset to the characters you need. Add `font-display: swap`, preload the heading font, and tune a fallback so the swap doesn't shift the layout.

## What to pick
- **Keep the stylish font for big, short text** such as the hero and collection titles, if it passes the coverage test.
- **Use a plain, complete family for everything else.** That means product names in lists, body text, buttons, prices and labels. Pick one with Latin Extended and Vietnamese and a real weight range, plus tabular figures for prices. Open-licensed families such as Noto Sans/Serif, Source Sans/Serif, or Be Vietnam Pro are worth checking against the same coverage test. I haven't verified their coverage here.
- **Give product names the plain family** if the display font only passes in some cases. The names are what customers need to read correctly.
- **If it fails,** ask the designer for a similar font that covers Vietnamese and Latin Extended, or use the stylish one only for strings you control, such as English titles.

## Fallback stack
Name the fallbacks so a missing glyph doesn't land on a random face:

```css
--font-display: "StylishFont", "Noto Serif", Georgia, serif;
--font-text: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

Replace `StylishFont` with the real name, and only list "Noto Serif" if you load it. System fonts cover all three languages, but they look different on each platform.

I haven't seen the actual font, so I can't say whether it passes. If you tell me its name, I can suggest what to test, or compare it against a couple of replacements.
