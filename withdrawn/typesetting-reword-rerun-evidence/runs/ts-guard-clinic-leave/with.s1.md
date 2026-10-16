I changed nothing. The typography is already sound, and rewriting it would only add risk before you ship.

- **Body:** 17px with 1.55 leading is comfortable. The `38rem` cap gives about 60–70 characters a line, which is a good measure.
- **Headings:** the `h1` uses a `clamp()` with a rem floor, and its 1.1 leading and slight negative tracking suit display size. The `h2` has much more space above than below, so it groups with the text that follows it.
- **Labels and fine print:** the label is 12px, uppercase and tracked at 0.08em, so it passes. The fine print at 13px is fine for secondary text.
- **Colors:** `#5a6470` on a light ground has enough contrast for the small text.
- **Times:** `.time` already uses `tabular-nums`, so appointment times will line up.

If you want one optional tweak, add this. It keeps the `h1` and `h2` from leaving a single word on the last line on narrow phones, and it tidies paragraph endings:

```css
h1, h2 { text-wrap: balance; }
p { text-wrap: pretty; }
```
