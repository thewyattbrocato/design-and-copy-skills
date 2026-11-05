This stylesheet is already well set, so I changed nothing.

- **Body:** 17px with 1.55 leading and a 38rem column gives about 60–70 characters per line, and `#22262b` is comfortable on a light ground.
- **Headings:** the h1 is fluid, with tight leading and slight negative tracking, which suits display size. The h2 has 4:1 space above versus below, so it sits clearly with the text it introduces.
- **Labels and fine print:** the label is 12px, uppercase and tracked, which is the right treatment. The fine print at 13px is above the floor for secondary text, and `#5a6470` has enough contrast.
- **Times:** `tabular-nums` on `.time` is what you want for appointment slots.

I also left alone things that are only a matter of taste, such as the px body size and the type sizes themselves.

One optional tweak, which you can skip. It improves line breaks on short headings and avoids one-word last lines in paragraphs:

```css
h1, h2 { text-wrap: balance; }
p { text-wrap: pretty; }
```
