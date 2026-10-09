Your palette has three problems, and they compound each other.

**1. Everything has the same hue and the same mid-tone lightness.**
Four of your six colors sit at about 43-47° on the hue wheel (khaki and olive). All of them have low saturation, roughly 15-27%. Except for the background, they're all mid-lightness (45-57%). Nothing is bright, dark, or colorful enough to stand out, so the whole thing reads as one beige-gray wash. That's the "muddy and tired" feeling.

**2. Contrast is very low, which is also an accessibility problem.**
These are approximate WCAG contrast ratios against your `#cfc8b0` background. Body text needs 4.5:1.

| Element | Ratio |
|---|---|
| Body text `#a39b82` | about 1.7:1 |
| Links `#9c8b5e` | about 2.0:1 |
| Primary button `#8a7f5c` | about 2.4:1 |
| Error `#b5654a` | about 2.5:1 |

Body text is the worst offender, because it's nearly the same color as the page. Your errors are also easy to miss, and a telehealth app can't afford that.

**3. The roles aren't distinguishable.**
Primary button, link color, and secondary button are nearly the same color. Users can't tell what's the main action, what's clickable, and what's decoration. The only distinct color is the error terracotta, but it's too dusty to read as an alert.

**Fix**
Keep the warm, earthy personality, but add real range:
- **Light background, dark text.** Use a cream background and a deep warm-brown text color.
- **One confident, saturated primary.** The primary button should be the most colorful thing on screen.
- **Quiet secondary.** Make it a tint or an outline, not a second mid-tone.
- **Clear error red.** It should look different from your link color.

Here's a starting point to test. I estimated the contrast ratios by hand, so check them in a contrast checker before shipping:

| Role | Color | Notes |
|---|---|---|
| Page background | `#FAF5E9` | warm cream |
| Body text | `#2F2A22` | very high contrast, about 13:1 |
| Primary button | `#2F7D5B` | friendly green, white text about 5:1 |
| Secondary button | `#E3EBD9` fill with `#1F5A40` text | soft sage tint |
| Links | `#1F6B4A`, underlined | clearly different from body text |
| Highlight / badges | `#F2A33A` | warm amber, for non-text accents only |
| Error | `#B3261E` | unmistakably red, about 6:1 |

This keeps the natural sage, olive, and cream feel, but the green primary and amber accent bring in the warmth and energy a pet app needs.

I can mock this up as CSS variables or a quick HTML preview so you can compare the old and new palettes side by side. I'd need to know if you want that, or whether you have a codebase I should apply it to.
