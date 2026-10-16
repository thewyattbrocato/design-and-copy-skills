No, the fonts aren't okay for the audience you described. The playful intent is right for a children's museum, but the body text will be hard to read on a phone.

**What works**
- A playful display voice suits a kids' museum. Bangers for the main heading fits that.
- Josefin Sans is a clean, friendly sans, which is a sensible choice for body text.

**What fails**
1. **Body text is weight 100 at 13px.** This is the biggest problem. Hairline strokes at a small size turn faint and blurry on phone screens, especially outdoors or on cheaper devices. Parents scanning for prices will struggle.
2. **The opening hours are the worst-treated text on the page.** They are the most important thing for your audience. They're set in Pacifico, a script face, at 11px. Script faces fall apart when small, and the hours are the smallest text on the page.
3. **Four decorative families at once.** Lobster, Pacifico and Bangers are all loud display faces, and Pacifico and Lobster are both brush scripts that look nearly the same. Together they look chaotic, not playful. Each one also adds to the download time on mobile.
4. **No fallbacks.** If Google Fonts is slow or blocked, the page drops to the browser's default serif. That would look like a mistake.

**Fix**
- Use Josefin Sans (or a sturdier sans) at 400 weight and at least 16px for body text.
- Put opening hours and prices in the same body face, at 16px or larger, in a medium or bold weight. Make them easy to find.
- Keep one display face, Bangers, for the h1 and maybe the h2. Drop Pacifico and Lobster. If the tagline needs flair, set it in Bangers or in bold Josefin.
- Add fallbacks.

```css
@import url('https://fonts.googleapis.com/css2?family=Bangers&family=Josefin+Sans:wght@400;700&display=swap');

body { font-family: 'Josefin Sans', system-ui, sans-serif; font-weight: 400; font-size: 16px; }
h1, h2 { font-family: 'Bangers', 'Josefin Sans', system-ui, sans-serif; font-weight: 400; }
.tagline { font-family: 'Josefin Sans', system-ui, sans-serif; font-weight: 700; }
.opening-hours { font-family: 'Josefin Sans', system-ui, sans-serif; font-weight: 700; font-size: 18px; }
```

Bangers only comes in one weight, so I set it to 400 to stop the browser faking a bold.

I haven't seen the page rendered, so check it on a real phone. Josefin Sans is a bit narrow and geometric. If the body text still feels thin at 400, a sturdier sans would be better for the prices. The main fixes are the weight, the size, and the opening hours.
