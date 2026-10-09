**Short answer: keep the palette. It's already restrained, with one accent and warm neutrals. Premium will come more from type, spacing, and paper than from new hex values. Three small fixes are worth making.**

Contrast ratios below are WCAG 2.x, calculated by hand and rounded. Check them with a checker before you publish.

| Pair | Ratio | Verdict |
|---|---|---|
| Ink on Paper | 13.1:1 | Pass, all text |
| Muted on Paper | 4.9:1 | Pass for body text |
| Rust on Paper | 4.8:1 | Pass for body text, but thin margin |
| White on Rust (buttons) | 5.4:1 | Pass |
| Sage on Paper | 3.0:1 | Fails as text, passes for non-text edges |
| Ink on Sage | 4.3:1 | Fails body text, passes large text |

**Findings, by impact**

1. **Sage tags with text fail.** Sage is too light to carry words on Paper. Keep Sage for rules and tag borders, and set tag labels in Ink. For a tag with a Sage hairline border and Ink text, the 3.0:1 border passes the non-text threshold. If you want Sage-coloured tag text, use `#5e7265` instead, which measures 4.6:1 on Paper.
2. **Rust links need a darker hover.** Rust passes at 4.8:1, but any tint or card that is darker than Paper will push it under 4.5:1. Use the base Rust for links and set hover to a darker value such as `#963b22`. Don't lighten hover. Only recheck Rust if you ever place it on a tinted panel.
3. **Print needs a proof, not the hex.** Screen hex values don't map to ink. Ask your printer for a match proof of Rust and Ink, and specify spot colour if you're printing with a letterpress-style ink. For the cream background, print on cream stock and don't print a Paper-coloured block. Keep Sage rules at 0.5 pt or heavier so they don't disappear, and keep Muted captions at 8 pt or larger.

**Optional, if the friend's "premium" note still bothers you:** Rust reads a little bright on screen for a letterpress brand. You could try `#a5442a`, but it's a taste call and not a contrast fix. Test it beside your real layouts before deciding.

Two assumptions: I assumed the site's button text is white on Rust, and I didn't check the print colours against any real stock.
