**Go with B.**

```css
article { font-size: clamp(1rem, 0.92rem + 0.4vw, 1.25rem); max-width: 68ch; }
```

**Why B wins**

- **It respects the reader's settings.** The floor and ceiling are in `rem`, so someone who has raised their browser's default text size gets larger text. The `0.92rem` term also keeps a rem component, so zoom and text-size changes still take effect.
- **It scales smoothly with bounds.** The size runs from 16px up to 20px and no further. Here is what that looks like at a few widths:
  - 320px wide: about 16px (the floor).
  - 800px wide: about 19px.
  - 1000px wide and above: 20px (the ceiling).
- **It caps the line length.** `68ch` keeps lines at roughly 60–70 characters, which is the readable range for long recipe text. Neither A nor C limits line length.

**Why not the others**

- **A (`2.2vw`)** is the worst of the three.
  - On a 320px phone the text comes out around 7px, which is unreadable.
  - On a 1920px monitor it comes out around 42px, which is huge.
  - Pure `vw` units also ignore the reader's text-size preference, and browser zoom barely changes the size. That is an accessibility failure.
- **C (16px, then 20px above 1200px)** is acceptable but weaker.
  - It uses pixels, which ignore a user's raised default text size.
  - Text jumps in size at the breakpoint instead of scaling.
  - It still has no line-length cap.
  - If you did want this approach, write it as `1rem` and `1.25rem` with the breakpoint in `em` (`75em`).

**One caveat on B:** `max-width: 68ch` is measured in the article's own font size, so the column grows a little as the text grows. That is usually what you want. Keep the cap on text elements and leave any wrapper or image grid around the article free to be wider.
