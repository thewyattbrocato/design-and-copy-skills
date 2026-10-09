**Why it jitters**

Most fonts use proportional digits, so "1" is narrower than "0" or "8". When a digit changes, the text's total width changes. If the text is centered or right-aligned, everything shifts. If it's left-aligned, whatever sits to its right shifts. Both look like horizontal jitter. At 100ms updates the tenths digit changes constantly, so the effect is very noticeable.

Three smaller causes:
- **Separators:** "," and "." are narrower than digits. They also move when the digit count changes, as when 998 becomes 1,204.
- **Layout:** Auto-sized containers or flex/shrink-wrapped elements resize with the text, and that passes the shift on to their neighbors.
- **Fallback fonts:** If a glyph is missing from the primary font, the fallback font's metrics change the width.

**What to do**

1. **Use tabular (fixed-width) figures.** Many fonts include them as an OpenType feature:
   - CSS: `font-variant-numeric: tabular-nums;`
   - SwiftUI: `.monospacedDigit()`
   - Android: `android:fontFeatureSettings="tnum"`
   - Unity/TextMeshPro, Unreal and similar: pick a font with monospaced digits, or set TMP's `<mspace=…>` tag. Unreal's Slate has no tabular option, so use a monospaced font or fixed-width slots.

   If your font has no `tnum` feature, switch to one that does (Inter, Roboto, SF, and most system fonts do), or use a monospace font.

2. **Reserve the width.** Set a fixed or minimum width sized for the widest value, such as "99:59.9" and "9,999,999". Don't let the container size itself to the text.

3. **Pick an alignment and stick with it.**
   - Timer: use a fixed width and left-align it, or center it in that fixed box. With tabular digits the colons and the decimal point then stay put.
   - Scores: right-align them so digits line up by place value. Tabular figures matter most here, because that's how 998 and 1,204 line up in a column.

4. **Handle the separators.** The comma still appears and disappears as the digit count grows. Right-aligned scores take care of this, since the right edge stays fixed. If a score is centered, reserve space for the widest case. For the timer, `:` and `.` are constant, so only the digits need to be fixed-width.

5. **Optionally, smooth the changes.** A rolling-digit animation or a short tween makes score changes read as intentional. This is cosmetic, though. Fix the layout first.

**Quick check:** Temporarily render "00:00.0" and "88:88.8" in your HUD font. If the widths differ, the font isn't tabular, or the feature isn't being applied.

If you tell me the engine or UI framework you're using, I can give you the exact setting. If the code is in this directory, I can also look at it and suggest a patch.
