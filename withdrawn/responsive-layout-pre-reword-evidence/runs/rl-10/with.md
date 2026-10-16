Both problems come from the content having no width limit and no side padding. This CSS fixes both, and I haven't run it in a browser:

```css
body { margin: 0; font: 17px/1.55 Georgia, serif; color: #222; background: #fbfaf7; }
header { background: #1d3b2a; color: #fff; padding: 20px 0; }
header .inner { max-width: 70ch; margin-inline: auto; padding: 0 1rem; }
main { max-width: 70ch; margin-inline: auto; padding: 40px 1rem; }
main p, main li { margin: 0 0 1em; }
pre { background: #efece4; padding: 16px; overflow: auto; }
img { width: 100%; }
```

- **Big monitors:** `main` and `header .inner` are capped at `70ch`, about 70 characters per line, and centered. The header's green band still spans the full width, and its content lines up with the body text.
- **Phones:** `1rem` of side padding on both keeps text off the screen edges. The cap only applies on wide screens, so phones are unaffected by it.
- **At 320px:** the text column is about 288px wide with no sideways scroll. `pre` already scrolls inside itself, and `img` stays capped at its container's width.

Colors, fonts, vertical spacing and the `pre` and `img` rules are unchanged.

I assumed the header has a `.inner` wrapper, since your CSS targets one, and that `main` holds all the page text. If the header text isn't inside `.inner`, move the `max-width`, `margin-inline` and `padding` onto whatever element wraps it.
