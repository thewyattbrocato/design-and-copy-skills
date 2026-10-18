The page probably feels amateur because nothing tells the eye what matters first, and several small styling choices each signal "template defaults" to a visitor. Roughly in order of impact:

1. **The type hierarchy is flat at the top.** The headline (28px), date (26px), and lead sentence (24px) are all large and bold, so they compete. The date line is nearly the size of the title, and the lead sentence is bigger than the paragraph it belongs to. Good hierarchy uses clear steps, such as a title at 40px or more, the date at around 20px semibold, and body text at 16 to 18px. The lead sentence should be a slightly larger regular-weight line, not a bold fragment inside the paragraph.

2. **The four buttons don't form a system.** You have four different treatments: outlined, filled, text-in-a-pill, and filled in another red. Visitors can't tell which action matters. "Get tickets" should be the single primary button, "Vendor list" a secondary outline, and "Map" a plain text link. "Subscribe" is the worst offender because it adds a second accent color and a second filled button that competes with the ticket CTA.

3. **Five identical bordered, shadowed boxes.** Every section gets the same weight, so nothing stands out, and the box-with-shadow treatment is a common default card style. Spacing, a heading, or a thin divider would separate the sections more cleanly and let the page breathe.

4. **Everything is one color.** Using #8b0000 for headlines, body, dates, and buttons, with a pale pink background, makes the page monotone. Keep the red as an accent for the CTA and headings, and use a near-black or warm neutral for body text so the red is reserved for things that matter.

5. **Centered text throughout.** Centering the whole page is fine, but centering multi-line paragraphs makes them harder to read because the line starts jump around. Left-align the body copy and keep centering only for the headline or hero.

6. **The vendor photos are different sizes.** Mismatched image sizes make the grid look unfinished, and photos are where visitors look for quality signals. Give them a fixed aspect ratio and use `object-fit: cover` so they crop to a uniform size.

If you want to fix them in order of effort, start with the type scale and the button hierarchy, since those two changes will do the most. Then remove the shadows and the box borders, and fix the photo ratios. If you share the CSS or the page source, I can point to the exact rules to change.
