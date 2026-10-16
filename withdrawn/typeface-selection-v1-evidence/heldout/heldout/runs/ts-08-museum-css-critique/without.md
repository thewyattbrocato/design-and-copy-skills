Honestly, no. The fonts have personality, but they get in the way of what parents on phones need.

**Biggest problems**
1. **The opening hours are the hardest thing to read.** They're set in Pacifico, a looping script font, at 11px. That's the information your audience came for, and it's the smallest, fanciest text on the page.
2. **The body text is too thin and too small.** Josefin Sans at weight 100 (hairline) and 13px will look faint on a phone, especially outdoors in sunlight. Ticket prices are presumably in this text too.
3. **There are too many display fonts.** Bangers (comic-book), Pacifico (retro script) and Lobster (another script) are three loud fonts with different moods. Pacifico and Lobster look similar enough that the difference reads as a mistake, not a choice.
4. **There are no fallback fonts.** If Google Fonts is slow, the text flashes or falls back to the browser default. Loading four families also slows the page on mobile data.

**What I'd do**
- Keep one playful font for headings. That's enough to feel like a children's museum.
- Use a plain, sturdy font for everything practical (hours, prices, directions) at 16px or larger, weight 400.
- Drop the third display font, or reuse the heading font for the tagline.

Something like:

```css
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Josefin+Sans:wght@400;700&display=swap');

body { font-family: 'Josefin Sans', system-ui, sans-serif; font-weight: 400; font-size: 16px; line-height: 1.5; }
h1, h2, .tagline { font-family: 'Pacifico', cursive; font-weight: 400; }
.opening-hours { font-family: inherit; font-size: 18px; font-weight: 700; }
```

Josefin Sans is a fine choice for body text once the weight is 400. Your friend's instinct for a friendly, quirky look is good. It just needs to be limited to the headings, with the practical info kept plain and readable.
