Your palette is already restrained and suits a letterpress studio. I wouldn't change the core colors. A few refinements would help it feel more deliberate:

1. **Sage fails contrast for text.** Sage on Paper is about 3:1, which is fine for rules and decorative marks but too low for small text. If your tags carry words, set the label in Ink or Muted and use Sage for the tag's border, rule, or a light tint behind it. Use Ink or Muted for anything you need people to read.

2. **Check Rust text and buttons.** Rust on Paper is about 4.8:1, which passes WCAG AA for body text but with little room. Make sure button labels are Paper on Rust and bold, and define a darker Rust for hover and pressed states (roughly #953a22) so the button doesn't just go flat.

3. **Add a second paper tone.** A slightly deeper paper such as #ebe4d4 for cards, the price list block, or footers creates hierarchy without adding a color. Real stationery has this layering, and it reads as more expensive than a single flat background.

4. **Keep Rust rare.** Your "one accent" rule is the most important thing here. Use it for the primary action and maybe one signature element, and nothing else, so it stays meaningful.

5. **Let type and space do most of the work.** Most "premium" impressions come from generous margins, a good serif for headings, and restrained letter-spacing and rules. The palette is the easy part. The layout matters more.

6. **Proof the printed price list.** Hex values don't translate exactly to print. Rust and Sage in particular can shift or go muddy in CMYK. Ask your printer for a color proof, or match to Pantone, before you print a run. Set the price list body text in Ink, not Muted, since light text on textured stock is harder to read.

The contrast figures are my hand calculations, so run them through a checker before you rely on them. I can also draft the CSS variables with these tokens (including the hover, card, and tag styles) if you'd like.
