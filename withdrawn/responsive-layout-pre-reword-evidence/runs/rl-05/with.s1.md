# Recipe page layout spec

The recipe column stays at a readable width and the other columns come and go around it. It never stretches to fill the screen. There are two breakpoints, both set where the content stops fitting rather than at a device size.

## Behavior by width

| Viewport | Layout | Notes |
|---|---|---|
| **Phone, 320 to ~47em (~750px)** | **One column.** Order: recipe, newsletter, related recipes, ad. | Page padding is `clamp(1rem, 4vw, 2rem)`. The ad is a 300×250 slot inline at the bottom, not a column. |
| **Tablet / small laptop, 48em to ~84em (~770 to 1340px)** | **Two columns.** Recipe on the left. The right rail is 18rem and stacks newsletter, related, then ad. | The recipe takes the remaining space, capped at 44rem. |
| **Laptop / desktop, 85em and up (~1360px+)** | **Three columns.** Recipe, then a 18rem rail with newsletter and related, then a 300px ad column. | The ad column is sticky and spans the full height. |
| **Ultra-wide (34", 3440px)** | **Same three columns, capped at 90rem and centered.** | Extra width becomes side margins. Don't widen text or add columns. |

The reasoning behind the widths:
- **Recipe column:** a line of text reads best at 60 to 70 characters, which is about 44rem. A recipe stretched across a 34-inch screen is what readers are complaining about.
- **Ad column:** ad units come in fixed pixel sizes (300×250, 300×600), so 300px is the one place pixels are right.
- **Breakpoint at 85em:** it is the narrowest width where 44rem + 18rem + 300px + gaps fits. The 48em breakpoint is where a 18rem rail still leaves the recipe at least ~28rem, which is comfortable to read.
- **Newsletter after the recipe on phones:** a box before the ingredients pushes the content down and annoys readers.

## CSS

```css
.recipe-page {
  --rail: 18rem;
  --ad: 300px; /* ad units are fixed pixel sizes */
  display: grid;
  gap: 2rem;
  grid-template-columns: minmax(0, 1fr);
  grid-template-areas: "recipe" "newsletter" "related" "ad";
  max-inline-size: 90rem;
  margin-inline: auto;
  padding-inline: clamp(1rem, 4vw, 2rem);
}

.recipe     { grid-area: recipe;     max-inline-size: 44rem; min-inline-size: 0; overflow-wrap: anywhere; }
.newsletter { grid-area: newsletter; }
.related    { grid-area: related; }
.ad         { grid-area: ad; justify-self: center; min-block-size: 250px; } /* reserve space, no layout shift */

/* Two columns: the rail has room beside the recipe */
@media (min-width: 48em) {
  .recipe-page {
    grid-template-columns: minmax(0, 44rem) var(--rail);
    grid-template-rows: auto auto 1fr;
    grid-template-areas:
      "recipe newsletter"
      "recipe related"
      "recipe ad";
    justify-content: center;
  }
  .ad { align-self: start; }
}

/* Three columns: the ad gets its own column */
@media (min-width: 85em) {
  .recipe-page {
    grid-template-columns: minmax(0, 44rem) var(--rail) var(--ad);
    grid-template-rows: auto 1fr;
    grid-template-areas:
      "recipe newsletter ad"
      "recipe related    ad";
  }
  .ad { position: sticky; inset-block-start: 1rem; align-self: start; }
}
```

The HTML source order should be `recipe, newsletter, related, ad`. That order is the phone order, and it is also the reading and tab order for everyone.

## What the developer should check
- **320px wide:** no sideways scroll, and the ad slot doesn't overflow.
- **200% text size:** the columns drop to fewer columns rather than overlapping. Em-based breakpoints do this automatically.
- **Very long ingredient or URL strings:** `min-inline-size: 0` and `overflow-wrap: anywhere` on the recipe column keep them from pushing the grid wider.
- **1280, 1440 and 3440px screens:** a 1280px laptop gets two columns, and 1440px and wider get three. If most readers are on 1280, drop the three-column breakpoint to ~80em and narrow the rail to 16rem.

## Optional extra for ultra-wide
If you want to use the space on very large screens, keep the page width as it is and add a layout change inside the recipe. From about 100em, put the ingredients list in a sticky left sub-column beside the method steps, so cooks can see both at once. Skip this if you want the first version simple.

## Assumptions
- Evergreen browsers, plain CSS, left-to-right, and a 320px minimum width.
- The ad network serves 300px-wide units. If it serves 160×600 skyscrapers or 728×90 banners, the ad column and the inline slot change width accordingly.
- The newsletter box and related-recipes list are each a single block, not tied to the recipe's own layout.
