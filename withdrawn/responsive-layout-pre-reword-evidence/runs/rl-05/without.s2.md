# Responsive layout spec: recipe page

## Guiding principles
- **Recipe first.** The recipe is the product. Everything else yields to it.
- **The reading column never gets too wide.** Cap it at about 65–75 characters per line (`max-width: ~720px` or `70ch` for body text). On a 34" screen, extra space becomes margin or side columns, never wider text.
- **Build mobile-first** with `min-width` breakpoints, and use a CSS Grid page shell.

## Breakpoints

| Tier | Width | Layout |
|---|---|---|
| **Phone** | < 640px | 1 column |
| **Tablet** | 640–1023px | 1 column, with related recipes in a grid below |
| **Laptop** | 1024–1439px | 2 columns: recipe + sidebar |
| **Desktop** | 1440–1919px | 3 columns: recipe + sidebar + ads |
| **Ultra-wide** | ≥ 1920px | 3 columns, centered, with a max total width |

## Behavior by tier

### Phone (< 640px)
Everything stacks in this order:
1. Title, hero image, meta (time, servings, rating)
2. **Jump to Recipe** button (anchors past any story or intro)
3. Ingredients, then Steps
4. Newsletter box, inline after the recipe
5. Related recipes, as a horizontal scroll row or a 1-column list
6. Ads, in designated inline slots (see below)

Details:
- Side padding is 16px. Tap targets are at least 44px.
- Ingredients come before steps, with checkboxes so people can tick items off while shopping or cooking.
- Don't put a sticky ad or a large newsletter popup over the content. Both hurt readers and search ranking.

### Tablet (640–1023px)
- Still 1 column, but the recipe column is centered at max ~720px.
- Related recipes become a 2–3 column card grid under the recipe.
- Newsletter becomes a full-width band between the recipe and related recipes.
- Ingredients and steps can sit side by side only if the width allows. Otherwise keep them stacked.

### Laptop (1024–1439px)
- Two columns: recipe (flexible, max ~720px) and sidebar (fixed ~300px), with a 32–40px gap.
- Sidebar holds the newsletter box and related recipes.
- Sidebar is `position: sticky; top: 16px` only if it's shorter than the viewport. Otherwise let it scroll normally.
- **Ads in this tier:** move them out of a dedicated column. Put one ad slot at the bottom of the sidebar and one or two inline slots in the recipe (between the intro and ingredients, or after the steps).

### Desktop (1440–1919px)
- Three columns: recipe (flexible, max ~720px), sidebar (~300px), ad column (~300px, the standard 300×600 unit).
- The ad column is sticky. Sidebar and ad column stay in the viewport while the recipe scrolls.
- Inline ad slots from the laptop tier are removed here, so readers don't see ads twice.

### Ultra-wide (≥ 1920px)
- Set `max-width: ~1600px` on the page shell and center it. Don't stretch the three columns to fill 34".
- Gutters on either side are plain background.
- Optional: scale the type up a step (for example, base 18px to 20px) so it doesn't look tiny at that distance. The line length cap still applies.
- Don't add a fourth column. Don't let the hero image go full-bleed at native size. Cap it at the recipe column width.

## Grid skeleton for your developer

```css
.page {
  display: grid;
  gap: 24px;
  padding-inline: 16px;
  max-width: 1600px;
  margin-inline: auto;
  grid-template-columns: minmax(0, 1fr);
}

@media (min-width: 1024px) {
  .page {
    grid-template-columns: minmax(0, 720px) 300px;
    justify-content: center;
    gap: 40px;
  }
}

@media (min-width: 1440px) {
  .page {
    grid-template-columns: minmax(0, 720px) 300px 300px;
  }
}

.recipe { max-width: 70ch; }
```

## Edge cases to hand over
- **Ad column missing or blocked:** the layout must not leave a hole. Collapse the column and let the other two stay centered.
- **Layout shift:** reserve fixed heights for ad slots (`min-height`) so the page doesn't jump as ads load.
- **Print:** hide the sidebar, ads, and newsletter. Print only the recipe, ingredients, and steps on one column.
- **Zoomed or large-text users:** breakpoints use `em`/`rem`, not `px`, in the real build, so a user who increases text size gets the simpler layout sooner.
- **Landscape phones:** treat as phone or tablet based on width, not device. Don't apply a sticky header taller than ~48px.
- **Images:** use `srcset` and `sizes` so phones don't download desktop-size heroes.

## Decisions to confirm with your team
1. Do you need the ad column on laptops for revenue? If so, an alternative is dropping the sidebar into the recipe flow rather than losing the ad column.
2. Is the newsletter box more valuable above or below the recipe on mobile? I'd put it after, because early interruptions raise bounce rate.
3. Is "Jump to Recipe" acceptable to your content and SEO team? Readers strongly prefer it, and it's now standard on recipe sites.

If you'd like, I can turn this into a working HTML/CSS prototype you can resize in a browser to check each tier.
