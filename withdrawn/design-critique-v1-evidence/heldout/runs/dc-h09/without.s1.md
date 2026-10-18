It feels off mainly because nothing is prioritized and everything is shouting. Here's what's going on, roughly in order of impact.

**1. Hierarchy is flattened**
- Headline 28px, date 26px, and intro lead sentence 24px are all bold and almost the same size. The eye has no clear entry point, and three things compete as "the title."
- The lead sentence at 24px bold, followed by 16px text, reads as a jarring jump, not a deliberate lead-in.
- Fix: pick one dominant element (headline around 40-48px). Make the date clearly secondary (about 20px, medium weight, or styled as a label). Make the intro one size, around 18px regular.

**2. One color does every job**
- Dark red text on pale pink, with everything in #8b0000, means headings, body, borders, and buttons all look the same. There's no contrast between "important" and "background."
- Red on pink is also lower contrast and harder to read than a neutral dark text color would be, especially for body copy.
- Fix: use a near-black or warm dark-brown for body text. Keep the red as an accent for the headline, links, and the primary button only. Consider a cream or off-white background so the red reads as intentional.

**3. Every section is boxed and shadowed**
- Five identical bordered, shadowed cards make the page feel like a form or a dashboard, not an inviting market. The boxes also add visual noise, and since they're all equal, no section stands out. Tickets is probably the most important and looks the same as parking.
- Fix: drop the borders and shadows. Use spacing and subtle background bands or dividers to separate sections. If you keep a card, reserve it for one thing, like tickets.

**4. Buttons have no system**
- Four buttons, four treatments: outlined, filled, a text link in a pill, and a filled button in a different red. Users can't tell which is the main action, and the second red looks like a mistake next to #8b0000.
- Fix: define one primary (filled), one secondary (outlined), and one tertiary (plain text link). "Get tickets" should be the primary. "Vendor list" and "Map" can be secondary. "Subscribe" should use the same red or sit in a distinct footer area. Use one shape and one corner radius for all.

**5. Vendor photos at different sizes**
- Mismatched image sizes look unfinished and break the grid rhythm. This is probably the single biggest "amateur" tell, since it's so easy to spot.
- Fix: crop all of them to the same aspect ratio (for example 4:3 or square) with `object-fit: cover`, and put them in a consistent grid with even gaps.

**6. Everything is centered**
- Centered alignment works for a short headline and date, but it's hard to read for paragraphs and for lists like vendors, food, and parking. Ragged left and right edges slow reading.
- Fix: center the hero only. Left-align body text and section content, and use a constrained line length of about 60-70 characters.

**Quick priority order if you only have time for a few changes:**
1. Equalize and crop the vendor photos.
2. Make one clear headline size and shrink the date and intro lead.
3. Remove the boxes and shadows.
4. Standardize the buttons.
5. Switch body text to a neutral dark color and keep red as an accent.

If you share the HTML/CSS or a screenshot, I can suggest specific changes.
