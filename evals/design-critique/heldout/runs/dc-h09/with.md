**The page has no hierarchy and no system.** Everything is shouting at the same volume, and nothing repeats consistently enough to look deliberate.

**1. Three bold headings compete (high).**
- The headline is 28px bold, the date is 26px bold, and the intro's first sentence is 24px bold. That is a 2px and 4px step, which reads as a mistake and not as a hierarchy.
- A visitor can't tell what to read first. The date is the most important fact for a market, and it ties with the title.
- A bold sentence at the start of a paragraph is a fourth heading in disguise.
- Fix: make the headline about 40–48px, the date about 20–22px at a lighter weight or in a contrast color, and the intro plain 18px. Aim for three sizes, with each step at least 1.25×.

**2. One color does every job (high).**
- #8b0000 is used for headings, body text, and presumably borders and buttons. Because color carries no meaning, it can't mark importance.
- Dark red on pale pink is a one-hue page. Contrast should be fine: against white it computes to about 10:1, and on pale pink I'd estimate somewhat lower but still passing. I didn't check the exact pink.
- Fix: set body text in a near-black neutral. Keep the red for the headline, the primary button, and links. Use a warm off-white or cream background, which also looks less like a default.

**3. Four buttons, four styles, no primary (high).**
- "Get tickets" is outlined, "Vendor list" is filled, "Map" is a text link in a pill, and "Subscribe" is filled in a second red.
- The main goal is ticket sales, and the ticket button is the weakest-looking of the four. The "Subscribe" red is a second accent color with no reason behind it.
- Fix: make "Get tickets" the single filled primary. Give "Vendor list" and "Map" the same secondary style (outlined). Make "Subscribe" a quiet text link or put it in the footer. That leaves two button styles.

**4. Five identical boxes (medium).**
- Each of the about, vendors, food, parking and tickets sections gets a 1px border and a drop shadow. Giving all five the same weight says they are equally important, which they aren't. Tickets and vendors matter more than parking.
- The drop shadows also add visual noise and look dated.
- Fix: remove the borders and shadows, and separate sections with spacing (for example 64–96px) and a heading. Keep a card only for content that needs a container, such as a vendor tile. Give tickets a distinct band.

**5. Vendor photos at different sizes (medium).**
- Mismatched sizes break the edges and spacing, and they are probably the clearest "unfinished" signal on the page.
- Fix: crop them all to one aspect ratio (for example 4:3 or square) and put them in a grid.

**6. Centered everything (medium, partly taste).**
- Centered text works for a short title block. For the multi-line paragraphs, food and parking details, and vendor lists, it gives a ragged left edge that is hard to scan.
- Fix: keep the hero centered, and left-align the body sections in a column about 60–70 characters wide.

**Keep these:**
- The warm red is a good seasonal choice for a winter market. It only needs a neutral and a better background to support it.
- The sections themselves (about, vendors, food, parking, tickets) cover what visitors need.
- Having a distinct date line is the right instinct. It just needs the right rank.

**Fix order:** buttons (3), then type scale (1), then color (2). After that, remove the boxes (4) and normalize the photos (5). The first three changes account for most of the amateur look.

I'm working from your description, not a screenshot, so I didn't check spacing, mobile layout, or the exact pink. Send a screenshot or the HTML/CSS if you want those covered.
