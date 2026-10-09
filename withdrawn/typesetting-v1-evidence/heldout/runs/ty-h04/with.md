**Why it jitters**

Most fonts use proportional figures by default, so each digit has its own width. A "1" is much narrower than a "0" or "8". Each 100ms tick swaps in different digits, so the string's total width changes. If the text is centered, the whole thing shifts. If it's left-aligned, anything to its right shifts. The tenths digit changes on every tick, so it's the most visible. Two things beyond digit width add to it:

- **Length changes.** `998` becomes `1,204`, which adds a digit and a comma. `9:59.9` becomes `10:00.0`, which adds a character.
- **Fallback fonts.** If the font has no tabular figures, or a fallback font kicks in, the width still varies.

**What to do**

1. **Use tabular lining figures.** Every digit then takes the same width.
   ```css
   .timer, .score {
     font-variant-numeric: tabular-nums;
   }
   ```
   Check that your face actually has a `tnum` feature. If it doesn't, switch the numerals to a face that does, or to a monospace. Don't try to force it.

2. **Keep the number of characters stable, or reserve space for it.**
   - Always show the tenths digit: `12:48.3`, never `12:48` on some ticks.
   - Pad the minutes if the format can change width, for example `09:59.9` to `10:00.0`.
   - Give the element a fixed width sized to the widest value, such as `min-width: 7ch`. `ch` is the width of a "0", which is exactly the digit width under tabular figures.

3. **Align scores on the right edge.** Use `text-align: right` in a fixed-width box, so `998` and `1,204` share the same right edge and the digit columns line up. The comma is narrower than a digit, so only compare values with the same digit count. Reserve width for the largest score you expect.

4. **Anchor the layout.** Don't center a changing value in a flexible container. Left-align the timer in a fixed-width box and put labels or icons outside it. Then nothing next to the number moves.

5. **If you're not in CSS** (a canvas, or an engine with no OpenType features):
   - Measure the widest digit once.
   - Draw each digit in a fixed-width cell of that size.
   - Draw the separators (`:`, `.`, `,`) at their own fixed positions.
   - Unity TextMeshPro has `<mspace=…>` for this.

For your game, I'd use `tabular-nums` on both the timer and the score. I'd right-align the score in a box wide enough for its maximum, and give the timer a fixed `ch` width with the tenths always shown. If you tell me the font and the platform (web, Unity, canvas), I can write the exact code.
