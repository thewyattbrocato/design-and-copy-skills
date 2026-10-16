Honest answer: no, the fonts aren't okay for what this page has to do. The playful intent is right for a children's museum, but the execution works against the parents who are actually reading it.

**What works**
- A fun display voice suits the brand. Bangers for the main heading is a reasonable idea.

**What fails, and the fix**

1. **Body text is unreadable on a phone.** Josefin Sans at weight 100 is a hairline, and at 13px it will look faint and broken, especially on lower-density screens and in sunlight. Phones also zoom or struggle with text this small.
   Fix: use a sturdy sans at 16px or larger, regular weight (400). You can keep Josefin Sans, but at 400 and 16px. A plain system font is also fine.

2. **Opening hours are the worst-treated text on the page.** It's in Pacifico, a connected script, at 11px. Script faces are hard to read at small sizes, and this is the very information parents came for. Digits in script faces are also easy to misread.
   Fix: set hours and prices in the body font at 16–18px, with a medium or semibold weight so they stand out. Treat them as the most legible text on the page.

3. **Too many display faces.** Bangers, Pacifico and Lobster are three loud, competing personalities. Pacifico and Lobster are both retro scripts, so they look like a mistake rather than a choice. Nothing is calm enough to rest on.
   Fix: use one display face for the h1 (Bangers is okay if it stays big and short) and let everything else be the plain body face. Drop Lobster and Pacifico, or keep just one for a short tagline at a large size.

4. **Loading and fallbacks.** The `font-family` declarations have no fallbacks. If Google Fonts is slow or blocked, the page falls back to the browser default, usually Times. Loading four families for a small page also slows the first view on mobile data.
   Fix: end every stack with a real fallback, for example `'Josefin Sans', system-ui, sans-serif`. The Josefin request only loads weight 100, so changing the weight means changing that URL too.

**A sound version**

```css
@import url('https://fonts.googleapis.com/css2?family=Bangers&family=Josefin+Sans:wght@400;600&display=swap');
body { font-family: 'Josefin Sans', system-ui, sans-serif; font-weight: 400; font-size: 16px; }
h1 { font-family: 'Bangers', 'Josefin Sans', system-ui, sans-serif; font-weight: 400; }
h2 { font-family: 'Josefin Sans', system-ui, sans-serif; font-weight: 600; }
.tagline { font-family: 'Josefin Sans', system-ui, sans-serif; font-weight: 600; }
.opening-hours { font-family: 'Josefin Sans', system-ui, sans-serif; font-weight: 600; font-size: 18px; }
```

I assumed a Latin-script audience and a screen-only site. I haven't seen the page rendered, so check it on a real phone. Josefin Sans is a geometric face with a low x-height. If it still feels small at 16px, a sturdier sans like a system font is a safe swap.

For your friend, the short version is: keep the fun in the big title and make everything parents need to read plain, large and sturdy.
