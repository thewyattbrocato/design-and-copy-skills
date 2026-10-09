**The page feels amateur mainly because nothing has a clear rank.** Headline, date, and lead sentence are 28, 26, and 24px bold, so three near-identical sizes compete for first read. Four buttons use four styles. Five boxes look identical. Those are the tells.

**Findings, ranked:**

1. **Major: Four buttons, four treatments, and the primary action is the weakest.** "Get tickets" is outlined, while "Vendor list" is filled and "Subscribe" is filled in a second red. "Map" is a pill-shaped text link that reads as a tag. Two filled buttons compete, and the purchase action loses. *Fix:* one filled primary ("Get tickets"), one outlined secondary ("Vendor list", "Map"), and Subscribe as a text link or the same secondary style. Drop the second red.

2. **Major: The type scale is flat.** 28 / 26 / 24 is too close to create hierarchy, and the bold lead sentence adds a fourth emphasis level. The date, which is the most useful fact for a market visitor, is almost as loud as the title. *Fix:* headline around 40px, date around 20px semibold, lead sentence around 20px regular, body at 16px. Remove the bold lead.

3. **Major: Five identical boxes with borders and drop shadows.** Every section gets the same container, so nothing reads as more important, and the shadows date the page. The stack looks like a generic card template. *Fix:* drop most of the boxes. Use one clear heading style and spacing between sections, and keep a box only where it signals something, like tickets.

4. **Moderate: Vendor photos are mismatched sizes.** Ragged edges make the grid look unfinished. *Fix:* a fixed aspect ratio (e.g., 4:3) with `object-fit: cover` on every image.

5. **Moderate: Everything is one red on pink.** Body text, headings, and buttons all use #8b0000, so there is no neutral for reading. Pink plus dark red reads as dated and a little romantic. *Fix:* dark neutral text (near-black or dark gray), with the red used only for the primary button and one accent. Keep the pink as an accent or drop it for an off-white background. This is partly taste, but the lack of a neutral is a function problem.

6. **Minor: Centered layout across all content.** Centering the headline is fine. Centering the long intro paragraph and boxed sections makes multi-line body text harder to read. *Fix:* center the hero only and left-align the rest.

**What works and should stay:** the five sections (about, vendors, food, parking, tickets) are the right information structure for an event page. Dark red on pale pink is legible; by my rough estimate the contrast is well above 4.5:1, but I didn't have the exact pink value, so treat that as an estimate. The date line belongs near the top, so keep it there and make it prominent in a cleaner way.

**Not checked:** I haven't seen a render, so spacing, image crops, and mobile layout are unverified. If you send a screenshot or the CSS, I can check the exact values and give a tighter fix list.
