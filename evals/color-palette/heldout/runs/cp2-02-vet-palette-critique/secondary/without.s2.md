The palette is muddy because nearly every color sits in the same narrow band: similar lightness, low saturation, and the same olive-khaki hue. Nothing has enough contrast to stand out, so the page reads as one tone with little hierarchy.

**What's going wrong**

1. **Body text is nearly unreadable.** `#a39b82` on `#cfc8b0` is about 1.7:1. WCAG asks for 4.5:1 for body text. The text is darker than the background, but barely.
2. **The background is too dark for a friendly app.** `#cfc8b0` is a mid-tone sand. Warm apps usually use a light cream so the content feels airy.
3. **The accents don't separate from each other.** Primary, secondary, and link are all mid-dark olive-gray. The link (`#9c8b5e`) is only about 2:1 against the background, and it's close in value to the primary button, so users can't tell what's clickable.
4. **Secondary is the wrong kind of color.** `#7d8a6b` is a grayed green with the same weight as the primary. It reads as another neutral, not a supporting accent.
5. **Error is the only real hue, and it's also muddy.** `#b5654a` is a terracotta that's close to the sand palette. It doesn't read as an alarm, and it's about 2.5:1 on the background.
6. **Low saturation everywhere.** Warm and friendly usually needs at least one clear, saturated color. Here every color is desaturated, so the whole thing looks tired.

**A direction that keeps it warm**

Keep the warmth in the neutrals, and add one clean accent for clarity.

- **Background:** `#FAF6EE` (light cream)
- **Body text:** `#3B3328` (dark warm brown), about 11:1 on the background
- **Primary buttons:** `#1E6F68` (deep teal) with white text, about 6:1. Teal feels calm and clinical without being cold, and it stands apart from the neutrals.
- **Links:** a darker teal such as `#17615B` on cream, so links read as links without competing with buttons.
- **Secondary buttons:** a pale sage fill (for example `#E4EBDC`) with dark teal text, or a teal outline on cream. This makes secondary feel quieter than primary.
- **Error:** `#B42318` (clear red), about 6:1 on cream. It's a true alert color and won't blend into the brand.

If you want to keep the olive family, the minimum fix is to lighten the background to a cream, darken body text to a warm brown, and raise primary saturation so it's clearly the strongest color on the page. Teal is my recommendation because it adds the freshness the current palette lacks.

I calculated these contrast ratios by hand from the sRGB values, so check the final pairs with a contrast checker before shipping. I assumed white text on the buttons, since you didn't list a button text color. If the text is dark, the current primary is even weaker than I've shown.
