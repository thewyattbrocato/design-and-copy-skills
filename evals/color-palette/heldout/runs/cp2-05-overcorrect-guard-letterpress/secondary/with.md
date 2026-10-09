**Verdict:** The palette is already restrained and coherent. Warm paper with cool ink is a sound letterpress base, and one rust accent is the right call. Most of the premium lift will come from a few small fixes, not a new palette.

Contrast ratios below are hand-calculated with the WCAG 2.x formula. Please confirm them in a checker before print or launch.

| Pair | Ratio | Verdict |
|---|---|---|
| Ink on Paper | 13.1:1 | Pass |
| Muted on Paper | 4.9:1 | Pass, barely |
| Rust on Paper | 4.8:1 | Pass, barely |
| Paper on Rust (button label) | 4.8:1 | Pass |
| Sage on Paper | 3.0:1 | Fails as text |
| Rust link vs. Ink body text | 2.7:1 | Hue-only distinction |

**Changes, by impact:**

1. **Sage text fails.** Keep `#7c9082` for rules and tag fills only. For tag text, use a deeper sage, `#56695b` (5.2:1 on Paper).
2. **Links rely on color alone.** Rust against Ink is 2.7:1, so underline links in body copy (thin, rust, offset). Keep the rust button for calls to action.
3. **Add a hover state.** Use `#9a3b22` for rust hover and pressed states (6.2:1 with Paper text).
4. **Keep Muted on Paper only.** At 4.9:1 it has no margin, so any tinted card or panel would push it below 4.5:1. Separate sections with Sage rules instead of tinted boxes.
5. **Proof for print.** `#f6f1e7` is a screen value. Your printed paper will be the stock, not this color. Light Sage will print pale, and small Muted type can thin out on uncoated stock. Ask the printer for a proof and match Rust and Sage to spot inks or Pantone, not hex.

**Beyond color:** Premium reads mostly from restraint. Keep rust to links and the one button, use generous margins and leading, and let type do the work. Those choices will do more than any hue change.

Assumptions: I took "Rust" as the only accent for both links and buttons, as you described. The ratios assume the standard body-text threshold of 4.5:1.
