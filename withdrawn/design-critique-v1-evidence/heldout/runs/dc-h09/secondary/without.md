The page feels amateur because nothing on it is ranked. Headline, date, lede, section boxes, and buttons all compete at about the same weight, so the eye has no clear entry point or path. Here's what's driving that, roughly by impact:

1. **The type scale is too flat.** The headline (28px), date (26px), and lede (24px) are within 4px of each other, so they read as three near-equal headings. Bold on all three flattens them further. A scale like 44 / 22 / 18 / 16 would make the headline unmistakable and the date a clear second tier. Keep the lede bold only if it's clearly larger than body text, and avoid the abrupt jump from 24 to 16.

2. **The buttons have no system, and the primary action is the weakest.** You have four styles: outlined, filled, text-in-a-pill, and a second filled red. "Get tickets" is the most important action but is outlined, so "Vendor list" pulls more attention. The near-identical second red on "Subscribe" reads as a mistake rather than a choice. Pick one primary (filled, "Get tickets"), one secondary (outlined, "Vendor list," "Map"), and one tertiary style for "Subscribe," and drop the second red.

3. **Five identical boxes with borders and shadows.** Bordered, shadowed cards are a dated pattern, and when every section gets the same container, tickets carry no more weight than parking. Shadows on a pale pink field also look muddy. Try removing the boxes and separating sections with whitespace and a single heading style, or keep boxes for tickets only.

4. **Centered body text.** Centering a multi-line paragraph and the section content makes it harder to read and gives it a poster or invitation feel. Left-align the body text and keep centering for the headline and date block only.

5. **Vendor photos at different sizes.** Mixed sizes break the grid and make the section look unfinished. Give every image the same aspect ratio (for example 4:3) with `object-fit: cover`.

6. **One color, but no roles.** Using a single dark red for everything is a reasonable palette, but without a size, weight, or tone difference to signal roles, it all reads the same. The pale pink background also makes the page feel soft. For a winter market, you could try a cooler or warmer neutral background and keep the dark red as the single accent for the headline and primary button.

If you want to fix the most with the least work, do 1, 2, and 5 first. They take the most visual noise out and make the hierarchy obvious without a redesign. I can draft the CSS for those changes if you share the stylesheet or markup.
