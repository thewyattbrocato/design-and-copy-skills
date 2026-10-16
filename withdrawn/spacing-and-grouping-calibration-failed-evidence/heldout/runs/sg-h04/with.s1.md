```css
:root {
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
}

.topbar {
  display: flex;
  align-items: center;
  height: 72px;
  padding-inline: clamp(20px, 4vw, 48px);
  background: #fff;
  border-bottom: 1px solid rgba(0, 0, 0, 0.08);
}

.topbar__logo {
  height: 28px;              /* wordmark/logo image height */
  margin-right: var(--space-12);  /* 48px: logo is a separate group from the nav */
  font-size: 22px;           /* if the logo is text */
  font-weight: 700;
  letter-spacing: -0.01em;
}

.topbar__nav {
  display: flex;
  gap: var(--space-8);       /* 32px between links, smaller than the 48px after the logo */
}

.topbar__nav a {
  display: inline-flex;
  align-items: center;
  min-height: 44px;          /* comfortable hit area; the bar's 72px leaves 14px above and below */
  font-size: 16px;
  font-weight: 500;
  line-height: 1.5;
  color: #1f2a24;
  text-decoration: none;
}

.topbar__nav a:hover { text-decoration: underline; text-underline-offset: 6px; }

.topbar__cta {
  margin-left: auto;         /* pushes the button to the right edge */
  display: inline-flex;
  align-items: center;
  height: 44px;
  padding: 0 var(--space-6); /* 24px sides; 12px of the height on each side is roughly 1:2 */
  font-size: 16px;
  font-weight: 600;
  line-height: 1;
  color: #fff;
  background: #1f5d3a;
  border: 0;
  border-radius: 8px;
  white-space: nowrap;
}

.topbar__cta:hover { background: #174a2e; }

@media (max-width: 720px) {
  .topbar { height: 64px; }
  .topbar__logo { margin-right: var(--space-6); }
  .topbar__nav { gap: var(--space-4); }
  .topbar__cta { padding: 0 var(--space-4); }
}
```

```html
<header class="topbar">
  <a class="topbar__logo" href="/">Switchback</a>
  <nav class="topbar__nav">
    <a href="/runs">Runs</a>
    <a href="/routes">Routes</a>
    <a href="/gear">Gear</a>
  </nav>
  <button class="topbar__cta">Log a run</button>
</header>
```

Here's why these numbers fix the cramped look:

- **72px bar height.** A tall hero photo needs a bar with some weight. The 44px button and links leave 14px above and below.
- **16px links and button text.** 14px text next to a big photo is probably what made your last attempt look tiny.
- **Spacing steps.** The gaps are 32px between links and 48px between the logo and the nav. Links are one group, and the logo is separate from them. The button sits alone on the right, so it reads as an action and not as a fourth link.
- **Button padding.** The 12px vertical and 24px horizontal padding is the roughly 1:2 ratio that reads as a comfortable button.
- **Side padding.** It scales from 20px to 48px (4vw in between), so the bar lines up with the hero's content margin. If your hero uses a different margin, set the same value here.
- **Border.** A 1px hairline at 8% black separates the bar from a busy photo. If the bar sits on top of the photo, drop the border and use a transparent background with white text.

On mobile, if three links plus the button don't fit, collapse the links into a menu below about 560px instead of shrinking them further.
