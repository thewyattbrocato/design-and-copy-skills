Several things are working against the page, and most come from the same cause: nothing on it says what matters most.

**1. Text contrast is too low (the biggest problem)**
- Body text is `#9a9a9a` on `#f6f1e7`, which is roughly 2.4:1. WCAG AA needs 4.5:1. The paragraph reads as faded, and the button text and borders are just as faint.
- Fix: use something like `#2b2b2b` or `#3a332b` for text. Keep the grey for minor details only.

**2. The hierarchy is inverted**
- The `h1` is 18px, and the paragraph under it is 20px. The paragraph is larger than the heading, so "Welcome to Tidewell" looks like a caption.
- Fix: make the headline about 40–56px, and the intro text about 18px.

**3. The headline says nothing**
- "Welcome to Tidewell" doesn't tell a visitor what you do or why they should care. Something like "Learn to throw clay on the harbor" would do more.

**4. The paragraph is a wall of text**
- It's one 60-word sentence listing five offerings, with a 1100px max width and 1.2 line-height. That makes lines of about 130 characters, which is hard to track.
- Fix: set `max-width` to about 60ch and `line-height` to about 1.5. Then split the offerings into a short list or cards (classes, wheel nights, workshops, parties, rental).

**5. The nav has too many items, and they're tiny**
- It has nine items at 12px in a dark bar, with no logo or brand name. Gift cards and studio rental appear in both the nav and the buttons.
- Fix: put "Tidewell" on the left. Keep about five items (Classes, Studio rental, Gift cards, About, Contact). Move Blog and Glaze library into a footer or a "More" menu. Raise the font size to 15–16px.

**6. The buttons don't look like buttons, and there's no primary one**
- They're 11px, with a thin grey border, no fill, and grey text. All three look equally unimportant.
- Fix: make "Book a class" a solid filled button with a clear color, about 16px text, and generous padding. Style the others as quieter secondary buttons.

**7. The look doesn't match the studio**
- The charcoal nav bar and grey text feel corporate and cold against a warm cream background. There's no imagery, no color from the craft, and no sign of the harbor or the clay.
- Fix: add a hero photo of your work or the studio. Pick one accent color, such as a glaze blue-green or terracotta, and use it for the primary button and links.

**8. Smaller issues**
- The hero padding is 30px 10px, so the content sits almost against the left edge. Add a centered container with 24–48px side padding.
- The anchors have no `href`, so they aren't keyboard-focusable or clickable. Add real links and visible `:focus` styles.
- The page has no `<meta name="viewport">`, no `<title>`, and no `lang` attribute. Mobile rendering will be poor without the viewport tag.

If you fix only three things, fix the contrast, the heading size, and the primary button. Those will change how the page feels more than anything else. I can rewrite the CSS with those changes if you'd like.
