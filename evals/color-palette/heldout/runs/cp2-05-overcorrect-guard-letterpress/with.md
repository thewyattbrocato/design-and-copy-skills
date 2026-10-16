Your palette already works, so I'd change very little. Your friend's "more premium" most likely comes from how the colors are used, not from the hex values. I had no way to run code here, so the ratios below are hand-calculated estimates (WCAG 2).

**What already works**
- Ink on Paper is about 13:1. The ink has a slight green-gray cast and the paper is warm, so the pair feels printed, not default black on white.
- Rust is the only warm, saturated color, so it reads as the one accent. Rust on Paper is about 4.8:1, which passes for links. Paper-colored text on a Rust button gets the same ratio.
- Muted on Paper is about 4.9:1, so captions pass.

**Changes, most important first**
1. **Sage can't carry text.** Sage on Paper is about 3.0:1, which is fine for thin rules but too low for tag text. Paper text on a Sage fill is also about 3:1, and Ink on Sage is only about 4.3:1. For tags, use Ink text on a pale sage tint (`#e3e9e3`, roughly 11:1), with a Sage `#7c9082` hairline border if you want an edge. Keep solid Sage for rules and ornaments.
2. **Add one lighter surface for cards and price-list panels:** `#fbf8f1`. A lighter panel reads like a heavier stock sitting on the page. A darker tint would be the wrong move, because Muted drops to about 4.4:1 on `#ece5d6` and fails.
3. **Add a Rust hover/pressed state:** `#963a20`, about 6.5:1 on Paper. Without it, hover has to change the accent's lightness or opacity, which looks cheap.
4. **Add a hairline color for dividers and table rules:** Ink at about 15% over Paper, which is about `#d3d2cb`. This is a rule, not a text color. It gives a subtler, more refined line than a full-strength rule.

**Usage habits that make it feel premium**
- Keep Rust small: links, the primary button and maybe one detail per page. Don't use it for headings or large blocks.
- Use Ink for headings, not Rust, and put the generous space around them.
- Use Sage sparingly, as a short rule under a heading or a small ornament.

**Print:** these are screen values. Rust and Sage will shift on press, and a letterpress spot ink or a duotone stock won't match the hex exactly. Proof against your actual ink swatches before treating the screen and the price list as a match.
