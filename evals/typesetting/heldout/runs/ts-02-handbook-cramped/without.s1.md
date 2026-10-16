Here's a revised stylesheet. Colors and HTML are untouched, and only type size, spacing, and measure changed.

```css
body { font: 17px/1.6 Arial, sans-serif; color: #2b2b2b; background: #fbfaf7; margin: 0; }
.page { max-width: 68ch; margin: 0 auto; padding: 40px 24px; }
h1 { font-size: 32px; line-height: 1.2; margin: 0 0 16px; }
h2 { font-size: 22px; line-height: 1.3; margin: 32px 0 8px; }
p { margin: 0 0 16px; }
.note { font-size: 14px; color: #777; }
```

What I changed and why:

- **Line length:** `max-width: 68ch` with `margin: 0 auto` centers the content in a column of about 68 characters. Paragraphs running edge to edge on a 1440px screen were the main cause of the tiring read, because the eye has to travel too far to find the next line. The `24px` side padding keeps text off the edges on narrow screens.
- **Body size:** 13px is small for long reading, so I raised it to 17px.
- **Line height:** 1.2 is too tight for paragraphs. 1.6 gives the lines room to breathe.
- **Paragraph spacing:** 6px between paragraphs barely separated them, so I raised it to 16px.
- **Headings:** I enlarged them (h1 32px, h2 22px) and gave h2 more space above (32px) than below (8px). That ties each heading to the section it introduces and makes the page easy to scan.
- **Notes:** `.note` was 10px, which is hard to read, so it's now 14px. I left its color `#777` alone as you asked. Its contrast on the cream background is borderline (about 4.2:1), so you may want to darken it later if accessibility matters.

One caveat: I couldn't see your HTML, so if `.page` isn't the wrapper around the handbook text, move the `max-width` and `margin` to whichever element is.
