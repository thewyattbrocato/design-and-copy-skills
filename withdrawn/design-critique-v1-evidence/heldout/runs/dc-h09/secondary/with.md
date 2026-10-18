**Verdict:** The page looks amateur because nothing tells the eye what matters most. Type sizes are nearly identical, the four buttons are four different styles, and every section gets the same boxed treatment. Each choice is reasonable alone, but together they read as a stock template with no hierarchy.

**Findings, ranked**

1. **High: No type hierarchy.** The headline (28px), date (26px), and intro lead (24px) are all bold and within 4px of each other, a ratio of about 1.08 per step. Nothing is clearly first, and the date, which is the key fact for an event, gets no emphasis of its own. Fix: make the headline clearly larger (about 40px+), set the date as a distinct label (smaller, caps or a different weight), and drop the bold lead-in or cap it near 20px. Aim for three sizes total: display, body, and small label.

2. **High: Buttons compete and the primary action is the weakest.** "Get tickets" is outlined, while "Vendor list" is filled, so the secondary action has more visual weight than the purchase. "Subscribe" uses a second red, so the page has two competing calls to action. Fix: make "Get tickets" the one filled button in #8b0000, "Vendor list" outlined, "Map" a plain text link, and "Subscribe" a quiet secondary (outlined or text) in the same red or neutral. Four buttons should be two or three styles at most, with one primary.

3. **Medium: Five identical boxes.** Each section has a 1px border and a drop shadow, so border and shadow double up and every section carries equal weight. The stacked cards are the most template-looking part of the page. Fix: remove the boxes and separate sections with spacing and a heading style, or use one subtle background tint for only the tickets section if it needs emphasis.

4. **Medium: Vendor photos are ragged.** Mismatched sizes make the grid look unfinished. Fix: give every photo the same aspect ratio (for example 4:3) with `object-fit: cover`, and use a consistent column count.

5. **Medium (taste, partly function): Everything is one dark red on pink.** Long body text in #8b0000 looks tinted and heavy. Contrast is probably fine (roughly 8:1 if the pink is near white, but I haven't checked the exact pink). Fix: set body text in a dark neutral and keep the red as an accent for the headline, primary button, and key labels.

6. **Low: Centered running text.** Centering the whole page is fine for a hero, but centered paragraphs are harder to scan. Fix: left-align body copy and keep centering for the header and the tickets block.

**What already works and should stay**
- A single centered column with a clear order: about, vendors, food, parking, tickets. Visitors' questions map to that order.
- The date is on the page near the top, so the key facts are present; they just need more emphasis.
- One accent hue. The red is a good brand color; it just needs to be used for fewer things.

**Not checked:** The exact pink value, mobile layout, font family, spacing values, and real photo content. The top two fixes (type scale and button hierarchy) should resolve most of the "amateur" feeling even if the rest stays as it is. I haven't changed any code or design.
