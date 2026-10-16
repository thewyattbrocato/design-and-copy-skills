# Recipe page: column behavior from phone to ultrawide

## The rule
Only two things change with screen size: how many columns there are, and where the ad goes. The recipe column never gets wider than a comfortable reading width. On a 34-inch screen the extra space becomes empty margin, not stretched text.

## Layout by width

| Viewport | Layout | Notes |
|---|---|---|
| **Phone, 320 px up to ~768 px** (under 48em) | **1 column**, in this order: recipe, newsletter, related recipes, ad | The ad is an in-flow banner. Related recipes sit in a wrapping grid, 2 across when they fit. Page padding is 1rem. |
| **Tablet and small laptop, 48em to 75em** | **2 columns**: recipe plus an 18rem sidebar. The ad becomes a full-width banner below both. | The sidebar is newsletter first, then related recipes. |
| **Laptop and desktop, 75em and up** | **3 columns**: recipe, 18rem sidebar, 300px ad column | This is your current design. The ad column is sticky. |
| **Wide monitor, 34-inch and larger** | Same 3 columns, **centered**, capped at about 86rem total | The recipe column stops at 45rem. Nothing else grows. |

## Decisions for your developer

1. **Source order is recipe, then sidebar, then ad.** That order is also the phone order. Don't reorder with CSS.
2. **Recipe column is `minmax(0, 45rem)`.** The `0` minimum lets long ingredient lines and URLs wrap instead of pushing the page sideways. Paragraphs are also capped at `70ch`.
3. **The ad column is a fixed 300px.** Ad units come in fixed sizes, so it doesn't flex. Reserve its height (`min-block-size`) and label it "Advertisement" so the page doesn't jump when the ad loads.
4. **Only two breakpoints, both in `em`.** They are 48em and 75em. Using `em` means a reader with larger default text, or someone zoomed to 200%, gets the simpler layout. That's the behavior you want.
5. **Sticky only where there's room.** The ad column sticks at 75em and up. On phones and tablets nothing is sticky.
6. **Optional inside the recipe:** when the recipe column is at least 40rem wide, put ingredients in a left rail and method steps on the right. Do this with a container query on the recipe column, not a viewport query. Below 40rem, ingredients stack above the method.

## Starter CSS

```css
*, *::before, *::after { box-sizing: border-box; }
img { max-inline-size: 100%; block-size: auto; }

.page {
  display: grid;
  gap: 2rem;
  justify-content: center;
  padding-inline: max(1rem, env(safe-area-inset-left)) max(1rem, env(safe-area-inset-right));
  grid-template-columns: minmax(0, 1fr);              /* phone: 1 column */
}

.recipe  { min-inline-size: 0; container-type: inline-size; }
.recipe p, .recipe h1, .recipe h2 { max-inline-size: 70ch; }
.recipe, .sidebar, .ad { overflow-wrap: anywhere; }

.related-grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fill, minmax(min(10rem, 100%), 1fr));
}

.ad { min-block-size: 15.625rem; }                    /* reserve space: no layout shift */

/* tablet: recipe + sidebar, ad banner underneath */
@media (min-width: 48em) {
  .page {
    grid-template-columns: minmax(0, 45rem) 18rem;
  }
  .ad { grid-column: 1 / -1; }
}

/* desktop and wide: three columns, centered, capped by the column sizes */
@media (min-width: 75em) {
  .page {
    grid-template-columns: minmax(0, 45rem) 18rem 300px;
    align-items: start;
  }
  .ad {
    grid-column: auto;
    position: sticky;
    inset-block-start: 1rem;
    min-block-size: 37.5rem;                           /* 300x600 unit */
  }
}

/* optional: ingredients beside method when the recipe column has room */
@container (min-width: 40rem) {
  .recipe-body {
    display: grid;
    grid-template-columns: 14rem minmax(0, 1fr);
    gap: 2rem;
  }
}
```

## Checks before launch
- **320 px wide:** no sideways scroll and nothing clipped. Test it with a very long ingredient name and a pasted long URL.
- **200% zoom on a laptop:** it should fall back to the tablet or phone layout and stay readable.
- **2560 px and 3440 px wide:** the three columns sit centered with even margins, and the line length stays the same as on your laptop.
- **Ad slot empty or blocked:** the page should still look intentional, with no big hole.

## Assumptions
- The ad network sells a 300px-wide unit. If you use 160px skyscrapers or a fluid ad, change that column width and the 75em breakpoint will need rechecking.
- Evergreen browsers, so container queries are fine.
- Left-to-right text only.

If you share the current CSS or a screenshot, I can mark which parts already hold up and which need changing.
