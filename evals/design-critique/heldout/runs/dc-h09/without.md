The page has no clear hierarchy, and it has several competing styles where it should have one consistent one. Nothing tells the eye where to start or what matters most, and the page looks like it was assembled piece by piece.

**Type: three sizes that are almost the same**
- The headline (28px), date (26px) and intro sentence (24px) are all bold and within 4px of each other. They compete, and none of them wins.
- The bold 24px first sentence jumps to 16px regular for the rest of the paragraph. That drop is steeper than the one between the headline and the date, so the intro reads as a glitch rather than a lead-in.
- Fix: pick a real scale, such as 40 / 20 / 16. Make the headline clearly dominant, and make the date a smaller secondary line, ideally in a lighter weight or color. Drop the bold-sentence trick, or make the intro a consistently larger paragraph.

**Color: one red for everything**
- Text, headings, borders and buttons are all #8b0000 on pink. Because everything has the same emphasis, nothing stands out. It also feels heavy and monotone.
- Fix: use a near-black or dark neutral for body text. Keep the red as an accent for the primary action and a few key moments. Make the background a calmer off-white, with pink as a tint rather than the whole field.

**Layout: everything centered, everything boxed**
- Centered text is fine for a headline. It's tiring for the paragraphs, parking directions and vendor lists, because the ragged left edge makes them hard to scan.
- Five sections each get a border and a drop shadow, so they all have equal weight. Parking looks as important as tickets. Borders plus shadows are also redundant, and the boxes add clutter.
- Fix: left-align the body content. Drop the boxes and separate sections with whitespace and headings. If you keep cards, use one treatment (a border or a soft shadow, not both) and give tickets more prominence.

**Buttons: four styles, no primary**
- You have an outlined button, a filled button, a text link in a pill, and a filled button in a second red. Visitors can't tell which action matters, and the different reds look like a mistake.
- Fix: use one primary style (filled) for "Get tickets" and one secondary style (outlined) for "Vendor list" and "Subscribe". Make "Map" a plain text link, or give it the secondary style. Use one red throughout.

**Images: mismatched sizes**
- Vendor photos at different sizes break the grid and read as unfinished. This is probably the biggest single giveaway.
- Fix: crop them all to one aspect ratio (square or 4:3) in a consistent grid with even gaps. Use `object-fit: cover` to do this in CSS.

**Priority order**
1. Photo sizes and button styles (quick fixes, big payoff).
2. A real type scale.
3. Neutral text color with a single red accent.
4. Removing the boxes and left-aligning body text.

If you share the HTML/CSS, I can make these changes directly.
