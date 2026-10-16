**It feels amateur because nothing on the page is ranked.** Every element is styled to look equally important, so the eye has no path, and several choices look accidental rather than decided.

**Findings, ranked**

1. **Three competing headlines (major).** The title is 28px bold, the date is 26px bold, and the intro's first sentence is 24px bold. That's a 2px and 2px step between three bold lines, which reads as a mistake rather than a hierarchy. A visitor can't tell what to read first. The bolded first sentence also turns into a fourth headline, then drops to 16px, a 33% size drop mid-paragraph.
   - **Fix:** Make the title about 40px+. Make the date a clearly subordinate line, around 20px, regular or medium weight. Set the intro at 16–18px with no bold sentence.

2. **One color for everything (major).** Text, headings and buttons are all #8b0000 on pink, so color can't signal importance or action. The page is also one hue, and I'd call that a taste issue. Pink with dark red can suit a winter market, but it needs a neutral and a second accent to work. (Contrast not checked, since the exact pink wasn't given.)
   - **Fix:** Use a near-black warm neutral for body text. Keep the red for the title and the single primary action.

3. **Four buttons in four styles, with no primary (major).** You have outlined, filled, a text link in a pill, and a filled button in a different red. Visitors can't tell which one matters. For a market, "Get tickets" is the main action, yet it's the outlined, weakest-looking one. "Subscribe" is more prominent than tickets.
   - **Fix:** Make "Get tickets" the only filled button. Make "Vendor list" and "Map" the same secondary style, and "Subscribe" a quiet tertiary. That gives two styles instead of four, and one red.

4. **Five identical boxes, each with a border and a shadow (moderate).** Treating about, vendors, food, parking and tickets alike says they matter equally, and they don't. Tickets is the goal and parking is reference material. A border plus a shadow on every one is also redundant, and it makes the page feel like a stack of cards.
   - **Fix:** Drop the borders and use one subtle treatment, or none, with spacing doing the grouping. Give tickets visual emphasis. Consider reordering so tickets sits near the top.

5. **Vendor photos in different sizes (moderate).** Ragged edges are one of the clearest signs of an unfinished page, and they break any grid alignment.
   - **Fix:** Use one aspect ratio, such as 4:3 or 1:1, with `object-fit: cover` and consistent gaps.

6. **Everything centered (minor to moderate).** Centered text is fine for the title and date. For paragraphs and the food and parking details, ragged left and right edges are harder to scan.
   - **Fix:** Center the header only, and left-align body text in a column of about 60–70 characters.

**What works, so keep it**
- **The content split.** About, vendors, food, parking and tickets are the right questions a visitor has, so keep the sections.
- **A restrained palette.** One hue family is cohesive and seasonal. It needs hierarchy, not replacing.
- **The 16px body size.** It's a sound base for everything else to scale from.

**Fix order:** 1 (type scale), then 3 (buttons), then 2 (color roles). Those three should remove most of the "off" feeling. Then do 5, 4 and 6.

I worked from your description, not a screenshot, so spacing, line length and image quality weren't assessed. Send a screenshot or the HTML if you want those checked.
