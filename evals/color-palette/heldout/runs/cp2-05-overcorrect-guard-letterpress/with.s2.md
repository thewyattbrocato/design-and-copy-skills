Your palette already works, and I wouldn't change any of the five colors. The ratios below are my own estimates from the hex values, because I can't run a checker here.

| Pair | Ratio | Verdict |
|---|---|---|
| Ink on Paper | ~13:1 | Strong |
| Rust on Paper (links, button fill) | ~4.8:1 | Passes for body text |
| Paper text on Rust button | ~4.8:1 | Passes |
| Muted on Paper | ~4.9:1 | Passes, so captions are readable |
| Sage on Paper | ~3.0:1 | Fine for decorative rules, too weak for text |

It's already restrained in the way that reads as premium. The neutrals are warm and tinted rather than pure black and white, and there is one accent with a clear job. A "more premium" version would come from how you use these colors, not from new ones.

1. **Keep Rust small.** Use it for links, the primary button and perhaps one thin detail. Don't use it for large blocks or section backgrounds. The less area it covers, the more deliberate it looks.
2. **Don't put text in Sage.** Ink on a Sage fill is only ~4.3:1, and Paper on Sage is ~3:1. For tags, use a pale sage tint like `#dde4dc` as the fill with Ink text (~11:1). Keep `#7c9082` for rules and borders.
3. **Add one step between Paper and Ink for surfaces.** A card or footer band in `#ece5d6` gives you depth without a new hue. Rust on that tint drops to about 4.3:1, so keep Rust links on plain Paper, or darken them to the hover color below.
4. **Define a Rust hover/pressed state.** Use `#94361d` (~6.7:1 on Paper). A darker hover reads as a considered detail, and it also gives you a link color that passes on the tinted surface.
5. **Use a hairline color for dividers.** Something like `#d9d1bf` is quieter than Sage or Muted. Fine rules in a soft tone suit a letterpress brand.

On the printed price list, these hex values are screen colors. On press, your actual ink and paper stock set the result. Check a proof against the screen colors, especially Sage, which will look different on uncoated stock.
