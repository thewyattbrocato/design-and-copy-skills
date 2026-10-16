Proportional digits are the likely cause. Most text fonts, Gill Sans included, give each digit its own width: a "1" is narrower than a "0". Right-aligned numbers then shift sideways from row to row. Turning on tabular figures gives every digit the same width without changing the typeface:

```css
.plan-table td.price,
.plan-table td.seats {
  font-variant-numeric: tabular-nums;
}
```

Your existing `text-align: right` will then line the digits up in a column. Commas stay narrower than digits, but that doesn't cause misalignment here because every row ends in the same place.

If the digits still move after this, the font you're actually getting probably doesn't include tabular figures, so the browser ignores the setting. Check which face renders in DevTools (the Computed panel shows the font in use). If it's the fallback, install or self-host the real Gill Sans, or use a font that has a tabular numeral set for just those two columns. I can't check your font files from here, so I haven't verified which numeral variants your installed Gill Sans includes.
