Your instinct is right. The page has several problems that add up to "off", and most of them come from hierarchy and contrast.

**1. The text is nearly unreadable.**
`#9a9a9a` on `#f6f1e7` is about 2.5:1 contrast. WCAG AA needs 4.5:1 for body text. Your buttons use the same grey, so the calls to action fade into the background. Try something like `#2b2b2b` for body text. That's also the nav's color, so the page stays consistent.

**2. The hierarchy is upside down.**
The `h1` is 18px and the paragraph is 20px, so the paragraph is bigger than the heading. Nothing tells the eye where to start. Make the h1 something like 44–56px and the paragraph 17–18px.

**3. The paragraph is a wall of text.**
It packs six offerings into one sentence. It's also allowed to run 1100px wide, which at 20px is roughly 120+ characters per line. Comfortable reading is 60–75 characters, so set `max-width: 60ch` or so. With `line-height: 1.2` it's cramped too, and 1.5–1.6 reads better. I'd cut the copy down to one welcoming sentence. The list of offerings could become a small grid or list below it.

**4. The buttons are too weak and too small.**
At 11px with a thin grey outline and no fill, they look disabled. "Book a class" is your primary action, so give it a solid fill (a deep teal or clay would suit a harbor pottery studio) and make it about 16px with more padding. The other two can stay as outlined secondary buttons. Also, they're `<a>` tags with no `href`, so they aren't focusable or clickable. Add real links.

**5. The nav is crowded and tiny.**
It has nine items at 12px, and "Cart (0)" sits in the same row as the page links. Some suggestions:
- Group or trim the links. "Gift cards" and "Studio rental" are already in your buttons, and Blog and Contact could move to the footer.
- Add a Tidewell wordmark on the left.
- Push the cart to the right.
- Raise the font to 14–16px.

**6. Nothing feels like a pottery studio.**
There's no image, no color accent, and no sense of place. A photo of your work or the wheel room would do more than any CSS tweak. Georgia and the cream background are a good start, but the page is grey on cream with a dark bar, so it feels generic.

**7. Smaller things**
- `padding: 30px 10px` is tight. The hero needs more breathing room, like 80px or more vertically and a proper side gutter.
- Missing `<meta name="viewport">`, so it will render badly on phones.
- No `<html lang>`, `<title>`, or `<header>`/`<main>` landmarks.

If you'd like, I can rewrite it with these fixes so you can compare the two versions.
