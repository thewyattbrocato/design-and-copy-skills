Your page has a handful of specific problems, and most of them trace back to one cause: nothing on it has a clear priority.

**1. Contrast is too low (the biggest issue)**
- Body text is `#9a9a9a` on `#f6f1e7`, which is roughly 2.5:1. WCAG AA needs 4.5:1. The paragraph, headline, and buttons are all in that grey, so the whole page looks faded.
- Fix: use something like `#2b2b2b` or a warm dark brown for text.

**2. The hierarchy is inverted**
- The `h1` is 18px and the paragraph is 20px, so the paragraph is larger than the headline. Nothing reads as the title.
- The nav, at 12px on a heavy dark bar, is the most visually dominant thing on the page.
- Fix: make the `h1` around 40–56px, and keep body text around 18px.

**3. The buttons don't look like actions**
- They are 11px, in grey text with a thin grey border and no fill. They look disabled.
- "Book a class" is the main action but looks identical to the other two.
- Fix: give the primary button a solid fill with a strong contrast color, and keep the other two as outlined secondary buttons. Use at least 16px text and more padding.

**4. The paragraph is too dense**
- It's one long sentence listing five offerings, set at `max-width:1100px` with `line-height:1.2`. That's about 130+ characters per line, when 60–75 is comfortable, and the lines are packed tight.
- Fix: set `max-width` to about 60ch and `line-height` to 1.5–1.6. Better still, cut it to one short sentence and move the offerings into a small list or cards.

**5. The nav is overloaded**
- It has nine items at the same weight, and "Gift cards" and "Studio rental" repeat the hero buttons.
- Fix: trim to four or five top-level items (Classes, Studio rental, About, Contact), put the cart on the right, and move the rest to a footer or sub-pages. The nav links also have no `href`, so they aren't focusable or clickable. Add real `href`s.

**6. Spacing and polish**
- The hero has `padding:30px 10px`, so text sits almost against the left edge, with no breathing room. Use something like `80px 24px` with a centered, constrained container.
- There's no imagery. For a pottery studio, a photo of your work or the studio would do more than any CSS change.
- The page has no `<meta viewport>`, `<html lang>`, or `<title>`. Mobile will render it tiny.

**A quick starting point:**
```css
body { color:#2b2b2b; }
.hero { padding:80px 24px; max-width:720px; margin:0 auto; }
.hero h1 { font-size:48px; line-height:1.1; margin:0 0 16px; }
.hero p { font-size:18px; line-height:1.6; max-width:60ch; }
.btns a { padding:12px 22px; font-size:16px; }
.btns a:first-child { background:#2b2b2b; color:#f6f1e7; border-color:#2b2b2b; }
```

The warm cream background and serif type are a good base for a pottery studio. The problem is the contrast, scale, and focus, not the palette.
