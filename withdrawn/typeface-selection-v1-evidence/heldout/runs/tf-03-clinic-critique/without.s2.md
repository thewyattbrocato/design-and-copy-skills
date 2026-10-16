Your site uses six different typefaces, which is almost certainly why it looks messy. A site like this normally needs one or two.

**What's wrong**

1. **Too many families.** Open Sans, Playfair Display, Montserrat, Lora, Poppins and Courier New are all in play. Each has different proportions, stroke weight and personality, so the page looks like it was assembled from several different sites.
2. **Similar fonts that clash.** Open Sans, Montserrat and Poppins are all sans-serifs, but they're different enough to look like a mistake instead of a deliberate contrast. Playfair Display and Lora are both serifs and have the same problem. Good pairings contrast clearly, and these don't.
3. **Inconsistent headings.** h1 is a high-contrast display serif, h2 is a geometric sans, and h3 is a different serif. The heading levels switch style as you go down the page instead of forming one hierarchy.
4. **Buttons and nav don't match the content.** Poppins on buttons and navigation is a third sans-serif next to the body text, so the parts people click look unrelated to the rest of the page.
5. **Monospace phone numbers.** Courier New looks like a typewriter or code. It's the most jarring choice for the most important piece of contact information. It's also a system font, so it won't match the rest of your web fonts.
6. **Readability for older patients.** Playfair Display has thin hairlines that get hard to read at small sizes or on low-contrast screens. Montserrat and Poppins are wide and geometric, and their letterforms can be harder to tell apart. That matters when people are reading appointment times and dates.

**Suggested fix**

Use one family, or one pairing with a clear role for each font:

```css
body, h2, h3, .btn, nav a, .doctor-name, .phone-number {
  font-family: 'Open Sans', sans-serif;
}
h1 {
  font-family: 'Lora', serif;  /* optional: the only contrasting font */
}
.phone-number {
  font-weight: 700;
  font-variant-numeric: lining-nums tabular-nums;
}
```

Or, simpler still, use Open Sans everywhere and create hierarchy with weight and size alone.

**Other things to check for this audience**

- Body text should be at least 18px, with a line-height around 1.5–1.6.
- Use strong contrast between text and background.
- Avoid light font weights (300 or lighter).
- Avoid all-caps and italics for appointment details.
- Make the phone number a tappable `tel:` link, in bold and at a larger size.

I can only see the CSS you pasted, so I can't confirm sizes, colors or spacing. Those could also be contributing to the messy look. If you share the full stylesheet or the site's files, I can check them and make the changes.
