The likely cause is that Gill Sans uses proportional figures by default. A "1" is narrower than a "0", so right-aligned numbers with different digits end their columns at slightly different widths. That makes the digits drift between rows, and it's most visible in `$119` and `$1,240`.

The fix is to turn on tabular figures, which keeps the typeface and makes every digit the same width:

```css
.plan-table td.price,
.plan-table td.seats {
  font-variant-numeric: tabular-nums;
}
```

You can put it on the whole table if you like: `.plan-table { font-variant-numeric: tabular-nums; }`. If you also want lining figures, use `font-variant-numeric: lining-nums tabular-nums;`.

Two caveats:

- **The font has to include the feature.** `tabular-nums` only works if the font has a `tnum` feature. Some Gill Sans builds, such as the one that ships with macOS, don't have it. If nothing changes, that's why. The fallbacks (Calibri, generic sans-serif) also differ per machine, so people on other platforms may see different results.
- **If the font lacks it,** you have two options that keep a similar look. You can load a humanist webfont that has `tnum` and apply it only to the numeric cells. Gill Sans Nova and Source Sans 3 both have it, and Fira Sans and Lato are close. Or you can leave the numbers alone and align them with a fixed-width approach, such as wrapping digits in spans. I'd avoid that unless you have no other choice.

To check what's actually rendering, open DevTools, select a price cell, and look at the Computed → Rendered Fonts panel. It shows which font is used, and you can toggle the property to see if the widths change.

If you tell me which platform you're seeing this on, I can say more about whether your Gill Sans supports `tnum`.
