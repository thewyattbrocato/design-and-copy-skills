# Recipe page layout spec

## Behavior by width

| Width | Columns | Order and placement |
|---|---|---|
| **320 to 47.99rem** (phones) | 1 | Recipe, newsletter, related recipes, ad. The ad is an in-flow block, not a column. |
| **48rem to 74.99rem** (tablets, small laptops) | 2: recipe plus a 18rem sidebar | Sidebar holds related, newsletter, then ad. |
| **75rem and up** (laptops) | 3: recipe, sidebar, ad | This is today's layout. |
| **Very wide** (34-inch and larger) | Still 3 | The layout stops growing at 100rem and centers. The extra width becomes empty margin. |

The newsletter box goes *before* related recipes on phones, because readers who finish the recipe are most likely to subscribe then. Swap the order if you disagree.

The two breakpoints come from the content, not from devices. Two columns need about 28rem for the recipe plus 18rem for the sidebar plus the gap, which is about 48rem. Three columns also need a ~19rem ad column (a 300px ad unit plus padding), which brings the total to about 75rem. Both are in `rem`, so they follow the reader's text size.

## Rules for the developer

- **Recipe column:** it never gets wider than `46rem`. Paragraphs and instructions are capped at `65ch`. On a giant monitor the recipe stays readable instead of stretching into 200-character lines.
- **Sidebar:** fixed `18rem` at two and three columns. On a phone, related recipes become a wrapping grid (2 or 3 across), not one long stack.
- **Ad column:** fixed `19rem`. Reserve the slot height (`min-block-size`) so the page doesn't jump when the ad loads. It is sticky only in the 3-column layout, never on phones.
- **Side padding:** it scales from `1rem` on a phone up to `2rem`.
- **Zoom:** don't block pinch-zoom, and leave the root font size alone.
- **Long text:** ingredient lines and URLs wrap instead of pushing the page sideways.

## CSS

```css
*, *::before, *::after { box-sizing: border-box; }
img, video { max-inline-size: 100%; block-size: auto; }

.recipe-page {
  container-type: inline-size;       /* lets the layout react to its own width */
  max-inline-size: 100rem;
  margin-inline: auto;               /* centers on very wide screens */
  padding-inline: clamp(1rem, 4cqi, 2rem);
}

.recipe-layout {
  display: grid;
  gap: 2rem;
  grid-template-columns: minmax(0, 1fr);   /* minmax(0,…) stops long content blowing out the column */
  grid-template-areas:
    "recipe"
    "newsletter"
    "related"
    "ad";
}

.recipe     { grid-area: recipe;     min-inline-size: 0; }
.related    { grid-area: related;    min-inline-size: 0; }
.newsletter { grid-area: newsletter; min-inline-size: 0; }
.ad         { grid-area: ad;         min-inline-size: 0; min-block-size: 16rem; /* reserve space */ }

.recipe p, .recipe li, .recipe h1, .recipe h2 {
  max-inline-size: 65ch;
  overflow-wrap: anywhere;
}
.recipe { font-size: clamp(1rem, 0.94rem + 0.25cqi, 1.25rem); }

.related-list {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fill, minmax(min(10rem, 100%), 1fr));
}

/* 2 columns: sidebar appears */
@container (min-width: 48rem) {
  .recipe-layout {
    grid-template-columns: minmax(0, 1fr) 18rem;
    grid-template-areas:
      "recipe related"
      "recipe newsletter"
      "recipe ad"
      "recipe .";
    grid-template-rows: auto auto auto 1fr;
  }
  .related-list { grid-template-columns: 1fr; }
}

/* 3 columns: ad gets its own column */
@container (min-width: 75rem) {
  .recipe-layout {
    grid-template-columns: minmax(0, 46rem) 18rem 19rem;
    justify-content: center;
    grid-template-areas:
      "recipe related ad"
      "recipe newsletter ad"
      "recipe .  ad";
    grid-template-rows: auto auto 1fr;
  }
  .ad > .ad-slot { position: sticky; inset-block-start: 1rem; }
}
```

Markup order is `recipe`, `newsletter`, `related`, `ad`. That is also the right reading and screen-reader order.

## Checks

- **320px:** one column, no sideways scroll. The related grid drops to 1 or 2 across because the minimum is capped at `min(10rem, 100%)`.
- **~700px:** two columns would not fit well, so it stays single-column. The related grid shows 3 or 4 across.
- **1024px:** two columns, with the ad under the newsletter in the sidebar. The three-column layout would leave the recipe too narrow.
- **1280px:** three columns, with the recipe at about 46rem.
- **2560px and 3440px:** the layout caps at 100rem and centers, and the recipe text never exceeds 65ch. If you'd rather use the empty space, the usual move is a larger sidebar or a bigger photo, not a wider text column. I'd leave it as margin.
- **Long strings:** `minmax(0, …)`, `min-inline-size: 0` and `overflow-wrap: anywhere` cover long ingredient names and URLs.
- **Text zoom to 200%:** the container queries use `rem`, so the layout drops to fewer columns instead of cramming.

I kept two queries, and both are container queries because the layout reacts to its own width. If the page shell is simply the viewport, plain media queries at the same `48rem` and `75rem` also work.

## Assumptions

1. The ads are standard 300px-wide units. If your ad network serves 160px skyscrapers or wider 336px units, change the `19rem` column and the 75rem breakpoint.
2. Evergreen browsers only (container queries need roughly 2023 or newer).
3. Left-to-right only. The rules use logical properties, so right-to-left will mostly work, but I haven't checked it.
