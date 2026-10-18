**Verdict:** The page feels amateur because nothing tells the eye what matters most. Three bold type sizes, four button styles, and five identical boxes all compete at the same volume, and the one action that matters, buying tickets, is the least prominent button on the page.

**Findings, most severe first**

1. **High: The primary action is visually weakest.** "Get tickets" is outlined, while "Vendor list" and "Subscribe" are filled, and the two filled buttons are different reds. A visitor who came to buy tickets sees two stronger buttons before the one they need. *Fix:* make "Get tickets" the only filled button, in the brand red. Make "Vendor list" a secondary outline and "Subscribe" a text link.

2. **High: The type scale is flat at the top.** The headline is 28px, the date 26px, and the first sentence of the intro 24px, all bold. That is three near-equal display levels, and the date (key info) is almost as loud as the title. The intro's first sentence reads as a second headline. The ratio between the top sizes is about 1.08, too small to create hierarchy. *Fix:* headline around 36–40px bold; date around 20px semibold; intro lead 20px regular, or drop the bold; body 16–18px. Four sizes total, with the top one clearly dominant.

3. **High: Five identical boxes with borders and shadows flatten the page.** Every section gets the same chrome, so the page reads as a stack of cards and no section is more important than the others. Tickets, the key conversion section, looks the same as parking. *Fix:* remove the boxes and shadows from most sections and separate them with spacing and a single rule. Keep a box only for tickets, if anything.

4. **Medium: Four button treatments on one small page.** Outlined, filled, a text link in a pill, and a second filled red are four different systems. The pill-shaped text link matches nothing else. *Fix:* two styles only: primary (filled) and secondary (outline). Text links for low-priority actions.

5. **Medium: Vendor photos at different sizes make the grid look unfinished.** *Fix:* a fixed aspect ratio (for example 4:3) with `object-fit: cover`, so every tile is identical in size.

6. **Medium (taste): Centered body text.** Centering works for the headline and date. For the multi-line intro and section text, centered lines have ragged starts and ends and are harder to scan. *Fix:* keep the header centered and left-align the body copy within a narrow column.

7. **Low (taste): Everything is one hue.** Headline, body, borders, and buttons are all #8b0000, so color carries no meaning and hierarchy depends on size alone. Dark red on pale pink is legible, so this is not an accessibility problem. *Fix:* set body text in a near-black or warm gray and reserve the red for the headline and the primary button.

**What works and should stay**
- **Contrast:** dark red on pale pink should pass comfortably. My estimate is about 8:1, assuming a background near #ffe4e6; the exact pink was not supplied, so treat that number as an estimate.
- **Single centered column:** a narrow, focused layout suits a one-day event page.
- **Section order:** about, vendors, food, parking, tickets is a logical sequence. Tickets is last, so the buy action sits at the bottom. Consider a visible ticket button near the top as well.

**Not checked:** the actual background hex, section heading sizes, mobile layout, and the rendered page. The critique is based on your description, not a screenshot.
