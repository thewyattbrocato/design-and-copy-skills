**The base is sound.** Warm paper, deep ink, and one accent is the right structure. Three things would make it read more polished, and the first two are contrast failures.

**Contrast, measured on WCAG 2.x (computed by hand; confirm with a checker)**

| Pair | Ratio | Verdict |
|---|---|---|
| Ink on Paper | 13.1:1 | Pass |
| Muted on Paper | 4.9:1 | Pass, narrow margin |
| Rust on Paper (links) | 4.8:1 | Pass, narrow margin |
| Paper on Rust (buttons) | 4.8:1 | Pass for normal text |
| Sage on Paper | 3.0:1 | **Fails for text**; fine for rules |
| Muted on a tinted card (#ece5d6) | 4.4:1 | **Fails** |
| Rust on that card | 4.3:1 | **Fails** |

**Changes, by impact**

1. **Sage text is the main problem.** Use sage only for rules and borders. For tags, use Ink text in a sage outline, or Ink on a light sage tint. If sage text is essential, a darker text-safe variant is **#4f6556** (5.6:1 on Paper).
2. **Deepen Muted to #535e61.** It gives 5.9:1 on Paper and 5.3:1 on a card, so captions survive a tinted panel. If you add cards, keep Rust and Muted text on Paper only.
3. **Optional: a deeper Rust for text.** Use **#a33f24** (5.7:1) for links and small rust text, and keep #b4472a for button fills. This is only worth doing if you put rust text on tints or small type.

**Print**

- Hex values are screen values. Ask your printer for spot-ink matches on your actual stock, and proof Rust and Sage on it. Cotton stock shifts both.
- Don't print the Paper color as a background. Let the stock provide it.
- Sage hairlines can break up on letterpress. Keep sage rules at a weight that holds, and never use sage for text on the price list.

**Notes**

- Ink, Paper, and the Rust button pair already pass. Those can stay as they are.
- Premium comes mostly from restraint: one accent per view and generous space. That is a layout decision, not a palette one.
