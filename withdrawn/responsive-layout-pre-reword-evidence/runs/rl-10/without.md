Here's the updated CSS. Only the two changed rules differ from yours.

```css
body { margin: 0; font: 17px/1.55 Georgia, serif; color: #222; background: #fbfaf7; }
header { background: #1d3b2a; color: #fff; padding: 20px 0; }
header .inner,
main { box-sizing: border-box; max-width: 800px; margin: 0 auto; padding-left: 20px; padding-right: 20px; }
header .inner { padding-top: 0; padding-bottom: 0; }
main { padding-top: 40px; padding-bottom: 40px; }
main p, main li { margin: 0 0 1em; }
pre { background: #efece4; padding: 16px; overflow: auto; }
img { width: 100%; }
```

- **Big monitors:** `header` and `main` content is now capped at 800px (760px of text) and centered. The header's green background still spans the full width.
- **Phones:** the 20px side padding keeps text off the screen edges. On wide screens it has no visible effect.
- **Unchanged:** colors, fonts, vertical spacing, `pre` and `img` are the same as before.

I haven't viewed this in a browser. The header fix assumes your markup has `.inner` inside `header`. If it doesn't, the header text will still touch the edges on phones.

If 800px feels too narrow or wide, change `max-width` in that one rule.
