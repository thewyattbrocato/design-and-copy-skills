I changed two rules and left everything else alone:

```css
header .inner { padding: 0 max(1rem, (100% - 70ch) / 2); }
main { padding: 40px max(1rem, (100% - 70ch) / 2); }
```

- **Big monitors:** the text now stops at about 70 characters per line and sits centered. The extra width becomes equal side margins. The header's inner content uses the same rule, so its left edge lines up with the text.
- **Phones:** there is always at least 1rem (about 17px) of space on each side, so the text no longer touches the screen edges.
- **Widths I checked by reasoning, not in a browser:** at 320px the side padding is 1rem and the text column is about 286px. At 1000px the 70ch cap is wider than the screen, so the 1rem minimum applies. At 2560px the text column is about 70ch with large equal margins.

The vertical padding (40px) is unchanged, and so are fonts, colors, `pre` and `img`. I haven't seen your HTML, so this assumes `main` and `header .inner` wrap the page content. If the header text isn't inside `.inner`, the header won't line up with the body. Code blocks inside `main` also get the 70ch cap, and they still scroll sideways when a line is longer.
