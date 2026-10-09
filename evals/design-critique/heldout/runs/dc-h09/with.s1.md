**The page has no hierarchy.** Almost everything is the same size, weight, color and treatment, so nothing tells the eye where to start. That is the "amateur" feeling, and a few other inconsistencies add to it.

**Findings, ranked**

1. **The type scale is flat (high severity).**
   - The headline is 28px bold, the date is 26px bold, and the intro's first sentence is 24px bold. Those sizes are within 4px of each other and all bold, so three things claim to be the title.
   - The date, which is what people look for first, is almost as loud as the event name.
   - The bold first sentence jumps to 24px and then drops to 16px. That reads as a mistake rather than a deliberate lead-in.
   - **Fix:** Use a clear ladder, for example headline 40–48px, date 20–24px in regular or medium weight, and intro at 18px with no bold. Keep the 16px body.

2. **There is one color and no emphasis (high).**
   - Everything is #8b0000 on pale pink, so color can't mark importance. The text is probably readable. I estimate about 8:1 against a typical pale pink, but I haven't checked it against your actual background value.
   - The problem is monotony and a slightly dated look, not legibility.
   - **Fix:** Use dark red only for the headline and the primary button. Set body text in a near-black or dark neutral, and make the background a neutral off-white or a much paler tint.

3. **The buttons have no system (high).**
   - You have four buttons in four styles: outlined, filled, a text link in a pill, and filled in a second red.
   - "Get tickets" is probably the main goal of the page, and it is the weakest-looking one, because it is outlined while "Vendor list" is filled.
   - **Fix:** Pick one primary style (filled) for "Get tickets" only. Use one secondary style (outlined) for "Vendor list" and "Map". Make "Subscribe" secondary, or a plain link, in the same red. Drop the second red entirely.

4. **Every section is boxed the same way (medium).**
   - Five sections each get a 1px border plus a drop shadow, so they all have equal weight. Tickets and parking look equally important.
   - Border and shadow together is redundant, and the five heavy frames make the page feel like stacked cards.
   - **Fix:** Remove the boxes and separate sections with spacing and headings. If you keep containers, use one (a subtle fill or border, not both) and give tickets a different treatment.

5. **The vendor photos are different sizes (medium).**
   - They break the grid and look unplanned, which is the most visible craft error on the page.
   - **Fix:** Crop them all to one aspect ratio (4:3 or 1:1) with `object-fit: cover`, in an even grid with consistent gaps.

6. **Everything is centered (medium, partly taste).**
   - Centered headlines are fine. Centered paragraphs and section content are harder to scan, because the left edge changes on every line.
   - **Fix:** Keep the hero centered if you like. Left-align body text and the section content, and cap line length at about 60–70 characters.

**What works and should stay**
- **The section order.** About, vendors, food, parking, tickets is a sensible visitor sequence. You may want tickets higher, or a ticket button in the hero.
- **The warm red palette.** It suits a winter market. It needs discipline in how it's used, not replacing.
- **The 16px body size.** It is a comfortable reading size.

**Fix order:** type scale (1), then buttons (3), then color (2), then photos (5). Those four changes will remove most of the amateur feel. Then handle the boxes (4) and alignment (6).

Assumptions: the visitors are the public deciding whether to attend, and the page is high fidelity. I haven't seen the page itself, only your description, so spacing, image quality and mobile behavior are not checked.
