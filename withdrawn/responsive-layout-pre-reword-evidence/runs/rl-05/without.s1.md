# Responsive layout spec: single recipe page

## Guiding principle
Content-first. The recipe is the page. Sidebar and ads are secondary and must never squeeze the recipe below a comfortable reading width or push it below the fold on small screens.

**Reading width target:** the recipe column should stay between about 60 and 75 characters per line (roughly `max-width: 70ch`, or about 680–760px for body text).

## Breakpoints

| Tier | Viewport width | Columns | Layout |
|---|---|---|---|
| Phone | < 640px | 1 | Single stacked column |
| Large phone / small tablet | 640–1023px | 1 | Single column, wider margins, some modules go 2-up |
| Laptop / tablet landscape | 1024–1439px | 2 | Recipe + sidebar |
| Desktop | 1440–1919px | 3 | Recipe + sidebar + ad column |
| Ultrawide | ≥ 1920px | 3, capped | Same as desktop, centered in a max-width container |

Use `min-width` media queries (mobile-first) or container queries on the page shell.

## Tier behavior

### Phone (< 640px)
- **One column.** Side padding 16px.
- **Order (top to bottom):**
  1. Title, rating, byline, hero image
  2. Quick facts (time, servings) and "Jump to recipe" button
  3. Ingredients
  4. Method steps
  5. Notes and nutrition
  6. Newsletter box
  7. Related recipes (a horizontal scroll strip, or a 1-up list)
  8. Footer
- **Ads:** no ad column. Put in-content ad slots between sections, for example after the intro and after the method. Reserve their height (`min-height`) to prevent layout shift. Never place an ad between an ingredient and its quantity, or inside the numbered steps.
- Tap targets are at least 44×44px. Body text is at least 16px (smaller sizes make iOS zoom on form inputs).
- Ingredients and method stack vertically. Ingredients should not be a sticky element on a phone.

### Large phone / small tablet (640–1023px)
- Still one column, but content is centered with `max-width: 720px` and 24–32px side padding.
- Related recipes become a 2-up or 3-up card grid.
- Newsletter box can be full-width and horizontal (text left, input right).
- Ads stay in-content. A leaderboard (728×90) fits here, and the phone sizes still apply below it.

### Laptop (1024–1439px): two columns
- Grid: `minmax(0, 1fr) 300px`, with a 32–40px gap.
- Main column on the left (capped at about 760px of content). Sidebar on the right: newsletter, then related recipes.
- Sidebar is `position: sticky; top: <header height + 16px>` only if it fits within the viewport height. If it is taller than the viewport, don't make it sticky, or the bottom is unreachable.
- Ads: the 300px sidebar holds one 300×250 unit beneath the newsletter box. There is no separate ad column yet.
- Inside the main column, ingredients and method may sit side by side at the top of the 2-column range. This only works if the method keeps at least 55ch, so otherwise keep them stacked.

### Desktop (1440–1919px): three columns
- Grid: `minmax(0, 1fr) 300px 160px` or similar. Use the width of your actual ad units (160 or 300).
- Typical template: `[recipe: minmax(0, 760px)] [sidebar: 300px] [ads: 300px]`, with 32px gaps.
- The ad column is sticky, with a single unit or two. Don't stretch the ad column to fill leftover space.
- The recipe column keeps its max width. Extra space goes to the outer margins, not to the text.

### Ultrawide (≥ 1920px, including 34" at 3440×1440)
- Wrap the whole page in a container with `max-width: ~1600px; margin-inline: auto`. The content is centered, and the outer margins are empty (or carry a page background).
- Do not widen the recipe text, since line length is the main complaint on big screens.
- Optionally use the extra space to enlarge the hero image or make a full-bleed hero band that spans the viewport. The text stays in the capped container.
- For 3440px-wide screens, optional upgrades are a larger base font (18–19px) and a slightly wider recipe column (up to ~820px). Don't go further than that.
- Ads: stay in the capped ad column. Do not scale the ads up or add more columns of ads to fill space.

## Component rules
- **Recipe card (ingredients + method):** the priority element. It's always first in DOM order, and the sidebar and ads come after it. This gives the right order on phones with no reordering, and it's better for accessibility and SEO.
- **Hero image:** `width: 100%; height: auto; aspect-ratio: 3/2` (or 16/9 on wide screens). Use `srcset`/`sizes` so phones don't download desktop images.
- **Newsletter box:** on phones, don't put it above the recipe. On desktop, put it at the top of the sidebar.
- **Related recipes:** a vertical list in the sidebar. A card grid on tablets. A horizontal scroll strip on phones.
- **Ad slots:** always reserve their space (`min-height` or `aspect-ratio`), and don't let ads collapse the layout when they fail to load. Avoid sticky ads on mobile, which tend to annoy readers.
- **Print:** hide the sidebar, newsletter, and ads, and let the recipe use the full width. Many readers print recipes.

## CSS skeleton (for the developer)

```css
.page {
  max-width: 1600px;
  margin-inline: auto;
  padding-inline: 16px;
}

.layout {
  display: grid;
  gap: 32px;
  grid-template-columns: minmax(0, 1fr);   /* phone + small tablet */
}

@media (min-width: 640px)  { .page { padding-inline: 32px; } }

@media (min-width: 1024px) {
  .layout { grid-template-columns: minmax(0, 1fr) 300px; }
  .ads    { display: none; }               /* ads live in sidebar at this size */
}

@media (min-width: 1440px) {
  .layout { grid-template-columns: minmax(0, 760px) 300px 300px; justify-content: center; }
  .ads    { display: block; }
  .sidebar-ad { display: none; }           /* avoid duplicating the unit */
}

@media (min-width: 1920px) {
  html { font-size: 112.5%; }              /* 18px base */
}

.recipe { max-width: 70ch; }
.sidebar, .ads { align-self: start; }
```

## Things to confirm before building
1. **Which ad sizes does your network sell?** The column widths (160 vs 300) and the in-content slots depend on this.
2. **Is the sidebar content worth keeping on phones**, or should related recipes move to the end of the page only? I assumed the end.
3. **Do you want a sticky "Jump to recipe" button on phones?** It's popular on recipe sites, but it competes with the ads.
4. **Check the analytics split.** If most readers are on phones, design phone-first and treat the desktop tiers as enhancements.

Happy to turn this into a wireframe or a working HTML prototype if that would help.
