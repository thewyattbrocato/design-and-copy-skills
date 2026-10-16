**Short answer:** This palette already reads as premium. It has a warm paper ground, deep ink, and one accent, which is most of the work. I'd change only two things: don't set sage as text, and give rust a darker hover state. The rest is print prep.

Ratios are computed by hand from the WCAG 2.x formula, so treat them as ±0.1:

| Pair | Ratio | Verdict |
|---|---|---|
| Ink on Paper | 13.1:1 | Passes everything |
| Muted on Paper | 4.9:1 | Passes body text, with a thin margin |
| Rust on Paper (and Paper on Rust buttons) | 4.8:1 | Passes body text, barely |
| Sage on Paper | 3.0:1 | Fails text; fine for rules and decoration |

**Findings, by impact**

1. **Sage text fails (3.0:1).** If tags carry labels, keep the text Ink on a light sage tint, or use a darker sage for the text. `#5a6d5f` measures about 4.9:1 on Paper. Keep `#7c9082` for rules and tag fills.
2. **Rust needs a hover/pressed step.** Right now a hover state would have to be a small shift from the base color. Use `#963820` (about 6.5:1 on Paper) so the state change reads clearly.
3. **Print is a separate job.** Screen hex is not a print value. Ask your printer for a proof, or for Lab or Pantone matches for Rust, Sage, and Ink, before you commit to the price list. If the stock is cream, let the paper be the background and don't print a Paper-colored flood, which doubles the tint and muddies it.
4. **Sage hairlines may drop out in print.** Make printed rules at least about 1 pt, or use the darker sage for them.
5. **Muted captions** should be at least 8 pt on print, because light gray type loses definition under dot gain.

**Keep as is:** Ink, Paper, Muted, and Rust as the sole accent. Don't add a second accent to chase a "richer" feel. Premium here will mostly come from type, spacing, and restraint, not more color.

**Assumption:** I treated the sage tags as text-bearing. If they're purely decorative, finding 1 doesn't apply.
