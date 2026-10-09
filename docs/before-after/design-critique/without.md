The page has no clear hierarchy, and it has several competing styles where it should have one consistent one. Nothing tells the eye where to start or what matters most, and the page looks like it was assembled piece by piece.

[...]

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

[...]
