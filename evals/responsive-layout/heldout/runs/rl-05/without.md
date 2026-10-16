# Responsive layout spec: single recipe page

## Principles

1. **The recipe is the product.** It gets a readable line length at every size (about 60-75 characters, roughly 640-760px for body text). It never stretches to fill a wide screen.
2. **Extra width goes to margins and secondary columns, not to wider text.**
3. **Secondary content stacks below the recipe on small screens** and never pushes the ingredients or steps down.
4. **Ads get reserved space** so the page doesn't jump while they load.

## Breakpoints

| Range | Name | Columns | Layout |
|---|---|---|---|
| 0-599px | Phone | 1 | Everything stacked |
| 600-1023px | Tablet / small laptop | 1 (recipe) + inline extras | Recipe full width, extras in a row below |
| 1024-1439px | Laptop | 2: recipe + sidebar | Ad column hidden or moved into the sidebar |
| 1440-1919px | Desktop | 3: recipe + sidebar + ad | Your current design, with capped widths |
| 1920px+ | Ultra-wide | 3, centered | Same as desktop, with a max-width container and growing side margins |

The exact numbers matter less than the rules. Have the developer adjust the breakpoints to where the layout breaks, not to device names.

## Behavior by size

### Phone (under 600px)
- **One column, 16px side padding.**
- **Order:**
  1. Title, hero image, time/yield/rating summary
  2. A "Jump to recipe" button, for readers who scroll past the story
  3. Ingredients
  4. Steps
  5. Notes and nutrition
  6. Related recipes, as a horizontal scroll row of cards
  7. Newsletter box
- **Ads:** one in-content slot between sections (for example after the steps), plus an optional sticky banner at the bottom. Keep these to a minimum on phones. Never place an ad between an ingredient and its quantity, or in the middle of the steps.
- **Touch targets:** at least 44×44px for checkboxes, buttons, and links.
- **Type:** body at least 16px, and 17-18px for the steps. This also stops iOS from zooming into form fields. Steps get generous line height (about 1.6).
- **Newsletter:** a single email field and button, full width, not a modal on first load.

### Tablet (600-1023px)
- **The recipe is still one column**, with its container capped at about 720px and centered, or left-aligned with padding.
- **Ingredients and steps** can sit side by side only if the screen is 900px or wider. Otherwise keep them stacked. Side-by-side ingredients are a common source of cramped steps.
- **Related recipes** become a 2-3 column grid below the recipe.
- **Newsletter** sits full width below the related recipes.
- **Ads:** inline slots, plus one leaderboard-sized slot (728×90) at the bottom or between sections.

### Laptop (1024-1439px)
- **Two columns:** the recipe (fluid, capped around 720px) and a sidebar of about 300-340px.
- **The sidebar holds** related recipes and the newsletter box.
- **Do not show the third ad column here.** At 1280px, three columns leave the recipe under 600px. Move the ad into the sidebar (300×250 or 300×600) beneath the newsletter box.
- **Sticky sidebar:** make the newsletter box or ad `position: sticky` below the header. Don't stick the whole sidebar if it's taller than the viewport.

### Desktop (1440-1919px)
- **Three columns** with a fixed ad column: `sidebar 300px | recipe (fluid, max ~760px) | ad 300px`. Your current design maps to this size. The order depends on your current layout, so keep what you have.
- **Total container** is about 1400px max, centered.
- **The ad column** is sticky, with a reserved width, so a missing ad doesn't collapse the layout.

### Ultra-wide (1920px+, including the 34-inch monitor)
- **Cap the whole layout** at a max-width of about 1440-1600px and center it. Without the cap, the recipe stretches and the sidebars drift off to the edges.
- **Don't scale the text up forever.** Keep body text at 17-18px and let the margins grow.
- **Optional:** use the background color or a subtle pattern outside the container. A wallpaper-style ad skin is sometimes sold for this space. If you use one, it must not push the content off-center.
- **Hero image:** cap its height so it doesn't fill the whole viewport. A 16:9 or 3:2 crop at the container width works.

## Recipe-specific details

- **Ingredients and steps are the priority.** On any screen where they can't both be visible, put the ingredients first and the steps right after.
- **Cook mode (nice to have):** a toggle that enlarges the text and keeps the screen awake (the Wake Lock API). This helps on phones and tablets in the kitchen.
- **Print:** hide the sidebar, ads, and newsletter, and keep the recipe in a single column.
- **Sticky "Jump to recipe" and "Print"** buttons at the top of the recipe on phones and tablets.

## Implementation notes for the developer

- **CSS Grid** for the page shell, with `grid-template-columns` changing at each breakpoint. Use `minmax(0, 1fr)` for the recipe column so long words or images can't overflow it.
- **Use `ch` or `rem` for the recipe's max-width** (for example `max-width: 70ch`) instead of fixed pixels, so it adapts to font size.
- **Fluid type** with `clamp()`, for example `font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem)`.
- **Images:** `srcset` and `sizes`, with `aspect-ratio` set to avoid layout shift.
- **Ads:** reserve `min-height` for each slot to avoid layout shift. Lazy-load the ones below the fold, and don't let the ad container's size change the recipe column's width.
- **Order in the HTML** should match the reading order: recipe, then sidebar, then ads. Use grid placement to position the columns, so phones and screen readers get the right order.
- **Test widths:** 360, 390, 768, 1024, 1280, 1440, 1920, and 3440 (a 34-inch ultra-wide). Also test zoomed to 200%, which should behave like a narrower screen.
- **Test with real content:** a long ingredient list, a very long title, a recipe with no image, and an empty ad slot.

## Questions to settle before building

1. **Ad revenue:** how important is the ad column? If it's a major source of revenue, you may want a sticky ad in the sidebar on laptops instead of hiding it.
2. **Phone traffic share:** if most readers are on phones, design the phone layout first and build up from it.
3. **Cook mode:** is it worth building now, or later?

I can turn this into a wireframe sketch or a CSS grid skeleton if that would help your developer.
