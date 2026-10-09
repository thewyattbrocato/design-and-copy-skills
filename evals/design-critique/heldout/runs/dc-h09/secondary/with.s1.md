**Verdict:** The page feels amateur because it has no clear order of importance. Three things compete at once: the type, the buttons, and the boxes. The biggest problem is that the main action, "Get tickets," is the weakest button on the page.

**Findings**

1. **Major: The primary CTA is visually the weakest button.** "Get tickets" is outlined, while "Vendor list" is filled, so the eye goes to the secondary action first. Ticket sales are presumably the page's goal. *Fix:* Make "Get tickets" the only filled button in the brand red. Make "Vendor list" outlined or ghost, and keep "Map" as a text link.

2. **Major: Four buttons use four styles, and two reds compete.** Outlined, filled, pill-shaped text link, and filled in a second red. Each one looks like a different system. *Fix:* Use two styles at most: one primary (filled) and one secondary (outlined or text). Give "Subscribe" the secondary style, not a second red.

3. **Major: The type hierarchy is flat at the top.** The headline is 28px, the date is 26px, and the first intro sentence is 24px bold. Everything is bold, the sizes are within 15% of each other, and the color is the same, so nothing reads as the title. Four sizes appear in the first screen. *Fix:* Make the headline clearly dominant (around 40px or more). Set the date one step down and differentiate it with weight or case. Make the intro lead a smaller bold or semibold (around 20px). Keep body text at 16–18px. Don't make the lead bold by changing its size.

4. **Moderate: Five identical boxes make the page feel like a form.** Every section is a bordered card with a drop shadow. The shadow and card stacking make the page look dated, and the sections all have equal weight. *Fix:* Remove the boxes and shadows. Separate sections with spacing and one consistent heading style. Keep the boxes only if one section is genuinely a different kind of content, like tickets.

5. **Moderate: Vendor photos in different sizes make the grid look unfinished.** *Fix:* Give every photo the same aspect ratio (for example 4:3 or 1:1) with `object-fit: cover`.

6. **Minor (taste): All text is #8b0000.** On a pink background this makes the whole page one color tone, and long body paragraphs in dark red are tiring to read. *Fix:* Keep the red for the headline, the primary button, and maybe section headings. Set body text to a near-black or dark neutral.

**What works and should stay**
- **Single brand red on a pale ground.** It's a coherent palette. Keep the family and reduce how often it appears.
- **Centered single-column layout.** It suits a small event page on mobile and desktop.
- **Section order (about, vendors, food, parking, tickets).** It matches how a visitor decides whether to come.

**Fix order:** 1) button hierarchy, 2) type scale, 3) remove boxes and shadows, 4) photo ratios, 5) body text color.

**Notes:** I assumed the pale pink is around #ffe4e1. Dark red #8b0000 on that background is roughly 8:1, so contrast passes AA. I haven't checked the real background value. I also haven't seen the rendered page or mobile breakpoints, so the findings above come from your description.
