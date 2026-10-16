Not automatically. Check it before you commit, because free display fonts often fail on exactly your three markets.

## What to check

**1. Glyph coverage, the main risk**
- **Polish** needs Latin Extended-A: Ż ó ł ą ę ś ź ć ń.
- **Turkish** needs Ç Ş Ğ İ ı Ö Ü. The dotted capital İ and dotless ı are the ones most often missing.
- **Vietnamese** is the hardest. It needs Đ/đ, ơ, ư, and the Latin Extended Additional block (ạ ả ầ ồ ộ ử ữ and so on), including stacked marks like ệ and ỗ. Many stylish display fonts only cover Basic Latin plus a few Western European accents.
- If a glyph is missing, the browser silently swaps in a fallback font for that character. You get a mismatched letter in the middle of "Đại Hồng Bào", which looks broken on a product page.

**2. Test with real strings.** Have the designer render this in the actual font, at heading sizes, in every weight and style you'll use:
`Đại Hồng Bào · Żółta Herbata · Çay Rize · İstanbul ığş ĞÜŞ · ỆỮỲ ẶẲẴ`
Also test it in ALL CAPS if headings are uppercase.

**3. Licence**
- Many "free font" sites mean free for personal use only. Check for a commercial licence that explicitly allows web embedding (`@font-face`). SIL OFL or Apache-licensed fonts are the safe category.
- Keep a copy of the licence. Fonts downloaded from aggregator sites are sometimes re-uploaded with the wrong terms, so trace them back to the original foundry or designer if you can.

**4. Vertical metrics**
- Stacked Vietnamese marks are tall. Tight line-heights or `overflow: hidden` on headings can clip them, and some fonts' marks collide with the line above.

**5. Turkish casing**
- Set `lang="tr"` on Turkish content. Then `text-transform: uppercase` gives i → İ instead of I. Without it, Turkish names get wrong capitals.
- Likewise set `lang="pl"` and `lang="vi"` where applicable.

**6. Technical delivery**
- **Subsetting:** don't subset to "Latin" only. Include `latin-ext` and `vietnamese` ranges, ideally with `unicode-range` so each visitor only downloads what they need.
- **Format:** serve WOFF2 with `font-display: swap`, and set a fallback with `size-adjust` to limit layout shift.
- **Unicode form:** store product names in NFC (precomposed). Mixed decomposed forms can render differently and break search.

## What to pick

If the stylish font fails the test, there are two options:
- Ask the designer for the same look from a family with full coverage.
- Use a Google Fonts family with the *Vietnamese* subset listed. Playfair Display, Cormorant, and Fraunces are elegant serif options that include it, and Be Vietnam Pro is a sans option. Confirm the subsets and weights on the font's page.

A good compromise is to use the display font only for decorative text that never contains product names, such as "Our Story" or a hero tagline. Set product names and anything user-facing in a font with proven coverage. Keep the original spellings, since that's a selling point for single-estate teas.
