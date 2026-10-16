Your CSS has several problems that stack on top of each other, and together they explain the cramped, cheap look.

**What's wrong**

1. **Line-height of 1.15 on body text.** This is the main cause of the cramped feel. Body copy needs about 1.5–1.7. At 1.15 the lines nearly touch, especially in a serif with descenders.
2. **Letter-spacing of 0.04em on body text.** Tracking out lowercase text hurts readability and looks amateurish. Body text should sit at 0 (or very slightly positive at small sizes).
3. **`text-align: justify` with no hyphenation.** At 14px, justified text creates uneven word gaps and "rivers" of white space. This is a big contributor to the cheap look.
4. **14px base size.** It's small for long-form reading. Aim for 17–20px for a recipe blog, where people read from a distance in the kitchen.
5. **1100px fixed width.** At 14px that's roughly 150+ characters per line, far above the comfortable 50–75. Long lines combined with tight leading make it hard for the eye to find the next line. A fixed pixel width also breaks on mobile.
6. **h1: line-height 1.5 and letter-spacing 0.06em.** Headings should have tighter leading (about 1.1–1.25), because a multi-line heading with 1.5 looks loose. Positive tracking on a 56px bold heading looks off. Large type usually wants 0 or slightly negative tracking.
7. **`h2.tag`: uppercase with `letter-spacing: 0`.** This is backwards. All-caps small text *needs* added tracking (about 0.06–0.1em). At 11px it's also too small to read comfortably.
8. **Blockquote: italic + bold + uppercase together.** Stacking three emphasis styles is shouty and hard to read. Pick one, usually italic alone.
9. **Links with no underline and `color: inherit`.** Readers can't tell what's clickable until they hover. That's a usability problem as well as a style one.
10. **`.price, .qty` set to Georgia.** This is redundant, since it's already inherited. If these are meant to line up in ingredient lists, use `font-variant-numeric: tabular-nums`. Georgia's old-style (lowercase-height) numerals look uneven in columns.
11. **Color #333 on an unspecified background.** This is fine, but check contrast if the background isn't white or near-white.

**Suggested replacement**

```css
body {
  font-family: Georgia, serif;
  font-size: 18px;
  line-height: 1.6;
  letter-spacing: 0;
  text-align: left;
  color: #333;
}
.post {
  max-width: 680px;       /* ~65 characters per line */
  width: 100%;
  margin: 0 auto;
  padding: 0 20px;
  box-sizing: border-box;
}
h1 {
  font-size: clamp(32px, 5vw, 48px);
  line-height: 1.15;
  letter-spacing: -0.01em;
  font-weight: 700;
}
h2.tag {
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 600;
}
a {
  color: inherit;
  text-decoration: underline;
  text-underline-offset: 0.15em;
  text-decoration-thickness: 1px;
}
a:hover { color: #c0392b; }
.price, .qty { font-variant-numeric: lining-nums tabular-nums; }
blockquote {
  font-style: italic;
  margin-left: 0;
  padding-left: 1em;
  border-left: 3px solid #ddd;
}
```

**If you change only three things**, make them line-height (1.15 → 1.6), letter-spacing (0.04em → 0), and the post width (1100px → max-width around 680px). Those three account for most of the problem.

Two caveats. Georgia's numerals are old-style, so `lining-nums` may not take effect in it, because the font has no lining set. If aligned numbers matter, set `.price, .qty` in a different font. And if you really want justified text, use `text-align: justify; hyphens: auto;` with `lang="en"` on `<html>`, but left-aligned is the safer choice at this width.
