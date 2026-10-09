I kept your selectors and made small changes. The size, measure (about 60 to 65 characters) and leading were already sound.

[...]

What changed and why:
- **Headings:** Slightly tighter tracking gives the large type a more set, editorial look. `text-wrap: balance` stops one-word last lines. Paragraphs get `text-wrap: pretty` for the same reason.
- **Blockquote:** It had a border, an indent and italics. I dropped the gray bar and kept the italics and indent, and made the quote slightly larger. This is the biggest visible change. If your partner likes the rule, put the `border-left` back and remove the italics instead.
- **Kicker:** I gave it a muted gray (`#666`) so it recedes from the headline.
- **Figures:** Georgia's default numerals are old-style, which look uneven in a stat. `lining-nums` fixes that, and `font-synthesis: none` prevents faux bold or italic.

I assumed a light background and a screen-only page. Nothing here depends on a webfont. A real editorial serif such as Source Serif or Newsreader would change the feel more than any CSS tweak.
