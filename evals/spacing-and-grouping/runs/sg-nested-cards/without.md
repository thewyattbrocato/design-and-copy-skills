The problem is nested containers: four layers of border, shadow and padding all say "this is a group," so none of them stand out. I'd do this:

**1. Make the outer panel a plain layout region, not a card.**
Remove its border and shadow. Keep the padding only if it aligns with the rest of the page, otherwise drop it to 0. The three inner cards are then the only elevated surfaces. If you want the outer panel to stay visible, give it a flat background tint (e.g. a slightly darker neutral) and no border or shadow.

**2. Simplify the inner cards.**
- Use a border or a shadow, not both. I'd keep a 1px light border and drop the shadow. That's lighter and prints and screenshots better. If you prefer shadows, use one very soft one and no border.
- Reduce padding from 24px to 16px. Use 20px only for cards with a lot of content.

**3. Widen the gaps between cards.**
8px is too tight, especially with shadows that bleed into each other. Use 16px, or 24px if the cards are large. Gap size is what tells people which things belong together. Space between groups should be clearly larger than space inside them.

**4. Rebalance heading spacing.**
16px above and 16px below makes a heading float equally between two things. Use more space above than below so it attaches to the content it labels, e.g. 32px above and 12px below. If the heading is the first thing in the panel, drop the top margin to 0.

**5. Establish a spacing scale and stick to it.**
For example:
- 12px: heading to its content
- 16px: padding inside cards, and gaps between cards
- 32px: between sections

**Result:** one visible container level (the three cards), a lighter edge treatment, and spacing that does the grouping instead of borders.

**Quick check:** after the change, squint at the page. You should see three distinct blocks, with headings clearly attached to their sections. If the cards still feel heavy, drop the borders and use only a faint background tint on a slightly different page background.

If you share the CSS or component code, I can make these changes directly.
