Your palette is already good, and I wouldn't change the core colors. Ink on warm paper with one rust accent is a classic letterpress look. Most of what reads as "premium" will come from how you use these colors, plus a few small additions.

**One fix: Sage fails as text.** I calculated these contrast ratios against Paper:

| Pair | Ratio | Verdict |
|---|---|---|
| Ink on Paper | ~13:1 | Excellent |
| Muted on Paper | ~4.9:1 | Passes AA |
| Rust on Paper | ~4.8:1 | Passes, but only just |
| Sage on Paper | ~3:1 | Fine for rules, too faint for text |

You use Sage for tags, so if any tag has text in it, that text will be hard to read. Keep #7c9082 for rules and borders. For tag text, use a deeper sage around #4f6556, or put Ink text on a pale sage tint.

**Small additions that add polish**
- **A darker Rust for hover and pressed states**, around #8f3720. Links and buttons then respond without introducing a new color.
- **A second paper tone** for cards, the footer, or alternating price-list rows, around #ece4d3. Subtle tonal layering looks more refined than boxes and borders.
- **A hairline color**, such as Ink at 15–20% opacity, for dividers and table rules. It's softer than solid Ink or Sage and looks closer to a printed fine rule.

**Usage matters more than the hex values**
- **Keep Rust rare.** Use it for links and the main button, not headings, borders, and icons as well. The scarcity is what makes it feel deliberate.
- **Avoid pure white and pure black.** Any white you need, such as input fields, should be a lighter paper (#fbf8f1), not #fff.
- **Let typography carry it.** A good serif for headings, generous line spacing, wide margins, and small caps or letterspacing on labels will do more for the premium feel than any color tweak.

**Print note.** Screen hex values won't match the printed price list. Proof them on your actual stock. Cream paper will shift Paper and Sage noticeably. If you print the price list in one or two ink colors, Ink and Rust are the natural pair, and Sage could become a tint or drop out.

I can mock up a CSS variables file with these additions if you'd like.
