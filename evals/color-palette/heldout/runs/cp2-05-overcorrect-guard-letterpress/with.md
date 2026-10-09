Your palette already works, so I'd keep all five colors. It has one accent, a warm paper and a tinted ink instead of black. Those are the usual signs of a premium letterpress look. Most of "premium" will come from how you use the colors: lots of paper, a small amount of rust, and thin rules.

I couldn't run code here, so the ratios below are hand-calculated estimates.

| Pair | Ratio | Verdict |
|---|---|---|
| Ink on Paper | ~13:1 | Strong |
| Muted on Paper | ~4.9:1 | Passes for captions |
| Rust on Paper (links) | ~4.8:1 | Passes, just barely |
| Paper on Rust (button text) | ~4.8:1 | Passes |
| Sage on Paper | ~3.0:1 | Fine for rules, fails for text |
| Ink on Sage | ~4.3:1 | Just under 4.5 |

**Changes, by impact**
1. **Sage tags with text in them.** Ink on a `#7c9082` fill is about 4.3:1, which is slightly under the 4.5:1 target for small text. Use a pale sage fill `#dfe5db` with Ink text (~11:1) and a 1px `#7c9082` border. That looks more refined than a solid fill. Keep `#7c9082` for the thin rules.
2. **Rust hover and pressed state.** Add `#983a21` (~6.3:1 on Paper). It gives buttons and links a deliberate hover state and keeps the single accent.
3. **Optional card surface.** If you need cards or a price-list panel, use `#ece5d5`, a slightly darker paper. That adds depth without a new hue. Ink on it is about 11:1. Rust links are only about 4.3:1 there, so use `#983a21` for links on that surface.

**Usage that adds polish**
- Keep rust to buttons, links, and maybe one detail per page. If it covers more than about 5% of a screen, it stops looking like an accent.
- Don't use Sage or Muted for body text. Muted is for captions only, at a normal weight and not too small.

**Print:** these are screen values. For the printed price list, rust and ink will shift depending on your stock and ink mix, so proof them on the actual paper. If you print rust as a spot ink, match the hex to a physical swatch instead of trusting the screen.
