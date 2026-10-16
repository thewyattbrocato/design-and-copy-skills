Here's the updated CSS. Only the `header .inner` and `main` rules changed.

```css
body { margin: 0; font: 17px/1.55 Georgia, serif; color: #222; background: #fbfaf7; }
header { background: #1d3b2a; color: #fff; padding: 20px 0; }
header .inner { padding: 0 1rem; max-inline-size: 70ch; margin-inline: auto; }
main { padding: 40px 1rem; max-inline-size: 70ch; margin-inline: auto; }
main p, main li { margin: 0 0 1em; }
pre { background: #efece4; padding: 16px; overflow: auto; }
img { width: 100%; }
```

- **Big monitors:** `main` and the header's `.inner` now stop at 70 characters wide and sit centered. The header's green bar still spans the full width, and its content lines up with the text below it.
- **Phones:** `1rem` of side padding keeps the text off the screen edges. The vertical padding is still 40px in `main` and 0 in `.inner`.
- **Nothing else changed:** colors, fonts, spacing between paragraphs, `pre` and `img` are as before. `pre` still scrolls sideways on its own if code is wide, so it won't push the page sideways on a phone.

I couldn't see your HTML, so I assumed `.inner` is the wrapper inside `<header>` and that `<main>` holds the page text directly. If the markup differs, the same two properties (`max-inline-size` and `margin-inline: auto`) go on whichever element wraps the content.

On a laptop, 70ch is about 700px with this font. If your laptop view currently looks wider than that, raise the cap to something like `76ch` so it matches what you like.
