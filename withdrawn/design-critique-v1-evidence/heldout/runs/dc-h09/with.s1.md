**Verdict:** nothing on the page is more important than anything else, so nothing leads the eye. Almost every element is styled to look equally important, and several styles are inconsistent for no reason.

**Findings, in fix order**

1. **Major: three near-identical headings.**
   - The headline (28px), the date (26px) and the intro's first sentence (24px) are all bold and all dark red. They sit within 4px of each other, so they read as three competing titles instead of a headline, a date and a lede.
   - The 24px bold first sentence also splits the paragraph into two different styles.
   - Fix: make the headline clearly dominant, around 40–48px. Make the date a visibly secondary line, such as regular weight or a smaller size. Set the intro as a normal 16–18px paragraph.

2. **Major: four buttons, four styles, no priority.**
   - "Get tickets" is outlined, "Vendor list" is filled, "Map" is a text link in a pill, and "Subscribe" is filled in a second red.
   - The main action, tickets, has the weakest treatment (outline), so it looks less important than "Vendor list".
   - Fix: use one filled primary button for "Get tickets". Use one secondary style (outline) for "Vendor list" and "Map". Make "Subscribe" a quiet link or a secondary button in the same red. Keep one red.

3. **Major: five identical boxes.**
   - About, vendors, food, parking and tickets all get the same 1px border and drop shadow. This adds visual noise, and it ranks the sections equally.
   - Tickets is the goal of the page, but it looks like parking.
   - Fix: drop the borders and shadows, and separate sections with spacing and a heading. Give tickets alone a distinct treatment, such as a tinted band.

4. **Moderate: single-color palette.**
   - Text, headings, buttons and accents are all #8b0000 on pink, so color can't signal anything. Two reds on the buttons make it look like a mistake.
   - Fix: use a near-black for body text. Keep one red for the primary action and a few accents. Contrast is probably fine. I estimate dark red on a pale pink at around 8:1, but I don't have the exact pink, so I haven't measured it.

5. **Moderate: vendor photos in different sizes.**
   - Uneven sizes look unplanned, and they make the grid ragged.
   - Fix: crop all of them to one aspect ratio and size, such as 4:3, in an even grid.

6. **Minor, and partly taste: everything is centered.**
   - Centering suits the headline and date. It makes longer text, like the intro and the parking and food details, harder to scan because the line starts ragged on both sides.
   - Fix: left-align body text and keep the header centered.

**What works and should stay**
- The section order (about, vendors, food, parking, tickets) follows what a visitor needs to know.
- The 16px body size is readable.
- The warm red-on-pink palette suits a winter market. The problem is how it's applied, not the colors themselves.

**Overall:** the page has four font sizes (three within 4px of each other), four button styles, and five identical boxes. Items 1–3 will make the biggest change, because they set the hierarchy.

I judged this from your description, not a screenshot. I didn't check spacing, mobile layout or image quality. A screenshot or the HTML would let me check those.
