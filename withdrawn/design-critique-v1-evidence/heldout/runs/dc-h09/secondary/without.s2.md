The page feels amateur mainly because nothing on it is ranked. Several things compete at the same level, so the eye has no clear path. Roughly in order of impact:

1. **The type scale is too flat.** The headline (28px), date (26px), and lead sentence (24px) are nearly the same size, and all three are bold. The date and the lead sentence each read as a second headline. Good hierarchy needs bigger jumps between levels, roughly 1.25x or more. Something like a 44px headline, a 18-20px uppercase date line, a 20px medium lead, and 16-18px body would separate them. Bolding the first sentence of a paragraph is a run-in heading, which reads as a mistake here.

2. **One color does all the work.** Headline, dates, body, buttons, and borders are all #8b0000, so color can't signal anything. Dark red body text on pink is also tiring to read at length. Keep the red for the headline and a few accents, and set body text in a near-black or warm charcoal.

3. **The four buttons have four treatments.** "Get tickets" is outlined and "Vendor list" is filled, so the secondary action looks stronger than the main conversion. "Map" is a pill-shaped text link, and "Subscribe" is a different red that looks like a mistake. Use one primary style (filled, for "Get tickets"), one secondary style (outlined), and one text link, all with the same height, radius, and padding.

4. **Five identical bordered, shadowed boxes.** Stacked cards with a border and a drop shadow look like a generic template, and combining both effects is redundant. Removing the boxes and separating sections with spacing, a thin rule, or a consistent section heading would make the page read as one piece.

5. **Ragged vendor photos.** Mixed sizes break the grid and make the section look unfinished. Give every image the same aspect ratio (for example 4:3) with `object-fit: cover`.

6. **Centered text, if the paragraphs are centered too.** A centered column is fine, but multi-line centered body text is harder to read. Left-align the paragraphs and keep centering for the headline and date if you want.

If you want, paste the CSS or the page template and I'll make these changes directly.
