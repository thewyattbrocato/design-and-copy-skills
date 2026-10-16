The fonts aren't okay for your audience. The personality is fine for a children's museum, but the readability problems are real, and they land on the information parents came for.

**Biggest problems**

1. **Body text is the thinnest weight at a tiny size.** `font-weight: 100` at `13px` is hairline-thin and hard to read on a phone, especially outdoors or for anyone over 40. It's the main text, so it's the most important fix.
2. **Opening hours are the smallest text on the page and in a script font.** `Pacifico` at `11px` is hard to read even at normal sizes. Hours are the main thing parents are looking for, so they should be among the easiest things to read.
3. **There are too many display fonts.** Bangers (comic-book), Pacifico (brush script) and Lobster (another bold script) are all loud, and Pacifico and Lobster look alike. Using three together looks chaotic rather than playful. One display font plus one clean text font is plenty.
4. **There are no fallbacks.** If Google Fonts is slow or blocked, the page drops to the browser default. Add `sans-serif` or `cursive` after each font name.
5. **It loads more than it needs.** Four font families slow down the page on mobile data. Josefin is only loaded at weight 100, so any bold text will be a browser-faked bold.

**What's fine**

- Josefin Sans is a good, friendly body font. It just needs a normal weight.
- A playful display font for the main heading suits a children's museum.

**Suggested fix**

```css
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Josefin+Sans:wght@400;700&display=swap');

body { font-family: 'Josefin Sans', sans-serif; font-weight: 400; font-size: 17px; line-height: 1.5; }
h1, h2 { font-family: 'Pacifico', cursive; font-weight: 400; }
.tagline { font-family: 'Josefin Sans', sans-serif; font-weight: 700; }
.opening-hours { font-family: 'Josefin Sans', sans-serif; font-weight: 700; font-size: 18px; }
```

This keeps one playful font for headings, drops Bangers and Lobster, and makes hours and prices plain and legible. If your friend wants more punch in the headline, they could use Bangers for the h1 instead of Pacifico, but I'd still stick to one display font.

For your friend, the rule of thumb is that decorative fonts are for big headings. Anything a parent needs to read quickly, like hours, prices and directions, should be in the plain font at 16px or larger.
