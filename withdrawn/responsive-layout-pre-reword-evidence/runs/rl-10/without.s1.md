I couldn't see your HTML, so this assumes `header .inner` wraps the header content and `main` holds the page text. The fix is to cap the content width, center it, and add side padding that keeps text off the screen edges:

```css
body { margin: 0; font: 17px/1.55 Georgia, serif; color: #222; background: #fbfaf7; }
header { background: #1d3b2a; color: #fff; padding: 20px 0; }
header .inner { padding: 0; }
main { padding: 40px 0; }
header .inner,
main { max-width: 960px; margin: 0 auto; padding-left: 20px; padding-right: 20px; }
main p, main li { margin: 0 0 1em; }
pre { background: #efece4; padding: 16px; overflow: auto; }
img { width: 100%; }
```

- **Big monitors:** `max-width: 960px` with `margin: 0 auto` keeps the text in a centered column. The header content uses the same rule, so it lines up with the body text. The header's green background still spans the full width.
- **Phones:** the 20px side padding keeps text off the edges. Below 960px the column fills the screen minus that padding.
- **Laptops:** the look should be about the same, apart from a slightly narrower column if your laptop viewport is wider than about 1000px. If you want it to match your current laptop layout exactly, raise `max-width` (for example to `1100px`).
- **Order:** I placed the new rule after `main { padding: 40px 0; }` so its left and right padding wins. The 40px top and bottom padding is unchanged.

If phones still show the desktop layout or tiny text, check that the page `<head>` has `<meta name="viewport" content="width=device-width, initial-scale=1">`. I couldn't check that since I only had the CSS.
