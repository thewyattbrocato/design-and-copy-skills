The palette mostly works. Only one pair fails, and it's the one that matters most for "polished": sage used as text.

**Contrast on Paper (#f6f1e7), WCAG 2.x, hand-calculated (±0.05):**

| Pair | Ratio | Verdict |
|---|---|---|
| Ink on Paper | 13.1:1 | Passes everything |
| Muted on Paper | 4.9:1 | Passes body text (4.5) |
| Rust on Paper | 4.8:1 | Passes body text, barely |
| White on Rust (buttons) | 5.4:1 | Passes |
| Sage on Paper | 3.0:1 | **Fails body text.** Passes only icons, rules and large text |

**Findings by impact:**

1. **Sage tag text fails (3.0:1).** Keep sage for rules, borders and tag fills, but set tag labels in Ink or Muted. If the sage tags need to read as sage, use a darker hue-matched sage for the text: `#56695d` (about 5.2:1 on Paper).

2. **Rust hover is undefined.** Rust works for links and buttons as is. If you add a hover or pressed state, use `#9a3d24` (about 6.1:1 on Paper), which keeps the same accent with more depth. Don't add a second accent.

3. **Check Muted and Rust on any tinted card or banner.** The 4.9 and 4.8 figures hold only on Paper. A card one step darker than Paper will drop them below 4.5. Measure on the real ground before you tint anything.

4. **Keep the palette otherwise.** These colors already hold together: a warm paper, a dark ink with a cool-green cast, one warm accent, and a quiet sage. I'd leave the rust alone; it has enough chroma to read as deliberate without tipping into orange.

**Premium levers that aren't about hue:**
- Use sage for hairline rules and tags, not for large fills.
- Give Rust a single job (links and primary buttons). When it appears only twice on a page, it feels more deliberate.

**Caveats:**
- I calculated these ratios by hand, so treat them as estimates within about ±0.05. I didn't run code.
- Screen values aren't print values. For the printed price list, check these against a proof on your actual stock, since uncoated paper will shift the Ink and Muted tones.
