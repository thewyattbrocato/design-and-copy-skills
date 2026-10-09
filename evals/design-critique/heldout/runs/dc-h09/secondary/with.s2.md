**Verdict:** Nothing on the page is wrong on its own. It feels amateur because nothing is ranked. The type sizes, the button styles, and the five identical boxes each compete for attention, so the eye has no clear path. The first fix is the button hierarchy, then the type scale.

**Findings, by severity**

1. **High: Four buttons, four styles, and the primary action is the weakest.** "Get tickets" is outlined, while "Vendor list" and "Subscribe" are filled in two different reds, and "Map" is a text link in a pill. The page's main conversion is the least prominent control. Fix: make "Get tickets" the only filled button. Make "Vendor list" and "Map" secondary (outlined or plain text, same style). Make "Subscribe" tertiary. Use one red for all filled buttons.

2. **High: Three large bold sizes compete in the first viewport.** The headline is 28px, the date is 26px, and the lead sentence is 24px, all bold. The headline barely outranks the date, and the lead sentence reads as a second headline. Fix: keep one dominant step. For example, headline 40–48px, date 18–20px semibold or uppercase, lead sentence 20px regular or medium, body 16–18px.

3. **Medium-high: Five identical boxes, each with a border and drop shadow.** Stacked borders and shadows on every section make the page feel like a template, and the identical containers flatten the page into one monotone scroll. Fix: remove the shadows, and use spacing plus a simple section heading to separate sections. Reserve any container treatment for the tickets block if it needs emphasis.

4. **Medium: Vendor photos are different sizes.** The ragged grid reads as unedited. Fix: give all photos one aspect ratio (for example 4:3) and use `object-fit: cover`.

5. **Low-medium (partly taste): Centered body text.** The 16px paragraph is centered, which makes multi-line text harder to scan. Fix: left-align the paragraph and the section text, and keep centering for the headline and date only.

6. **Taste: One color for everything.** All text is #8b0000, so hierarchy has to come from size alone, which is why finding 2 hurts. Fix: keep the red for the headline, buttons, and accents, and set body text in a dark neutral (for example near-black or dark gray) so it reads as text and not as decoration.

**What works and should stay**
- The dark red on pale pink is one coherent brand color, and it is probably legible. I estimate about 8.8:1 for #8b0000 on a pale pink near #FDEEEE, which would pass WCAG AA for body text. This is an estimate: I don't have the exact pink.
- A single centered column keeps the page focused.
- The section order (about, vendors, food, parking, tickets) moves from the event to the purchase.

**Not checked:** the exact pink hex, actual rendering, mobile layout, spacing values, the vendor photo sources, and whether a hero image exists. I judged from your description only, so a screenshot would let me confirm the sizes and layout.
