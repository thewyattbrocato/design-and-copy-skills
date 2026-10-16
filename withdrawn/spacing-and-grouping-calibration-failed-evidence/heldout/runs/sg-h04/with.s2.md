```css
:root {
  /* spacing scale (4px base) */
  --s-1: 4px;
  --s-2: 8px;
  --s-3: 12px;
  --s-4: 16px;
  --s-5: 24px;
  --s-6: 32px;
  --s-8: 48px;

  --ink: #14211a;
  --accent: #1f6b4a;
  --accent-hover: #185a3d;
}

.topbar {
  display: flex;
  align-items: center;
  height: 72px;
  padding-inline: var(--s-6);          /* 32px page margin */
  background: #fff;
  border-bottom: 1px solid rgb(20 33 26 / 0.1);
}

.topbar__logo {
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--ink);
  text-decoration: none;
}

.topbar__nav {
  display: flex;
  gap: var(--s-2);                     /* 8px between links */
  margin-left: var(--s-8);             /* 48px: logo and nav are separate groups */
}

.topbar__nav a {
  display: inline-flex;
  align-items: center;
  height: 44px;                        /* full touch target */
  padding-inline: var(--s-3);          /* 12px, so text sits ~24px apart */
  font-size: 16px;
  font-weight: 500;
  color: var(--ink);
  text-decoration: none;
  border-radius: 8px;
}
.topbar__nav a:hover { background: rgb(20 33 26 / 0.06); }

.topbar__cta {
  margin-left: auto;                   /* pushes the button to the right edge */
  display: inline-flex;
  align-items: center;
  height: 44px;
  padding-inline: var(--s-5);          /* 24px, about 2x the 12px vertical */
  font-size: 16px;
  font-weight: 600;
  color: #fff;
  background: var(--accent);
  border: 0;
  border-radius: 8px;
  text-decoration: none;
  cursor: pointer;
}
.topbar__cta:hover { background: var(--accent-hover); }

@media (max-width: 720px) {
  .topbar { height: 64px; padding-inline: var(--s-4); }   /* 16px margin */
  .topbar__logo { font-size: 20px; }
  .topbar__nav { margin-left: var(--s-5); }               /* 24px */
  .topbar__nav a { padding-inline: var(--s-2); font-size: 15px; }
  .topbar__cta { padding-inline: var(--s-4); font-size: 15px; }
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
  <a class="topbar__cta" href="/runs/new">Log a run</a>
</header>
```

**Why these numbers fix the "tiny and cramped" look**
- **Height:** 72px on desktop gives the bar enough weight next to a large hero. Anything under about 60px reads as thin there.
- **Gaps:** the logo-to-nav gap is 48px, and the links sit about 24px apart (8px gap plus 12px padding on each side). Space within the nav group is about half the space between groups, so the bar reads as logo, links, and action.
- **Button:** it's 44px tall with 24px side padding, so the horizontal padding is twice the vertical. At 16px/600 it reads clearly as the primary action. A 4px by 8px button is what usually looks tiny.
- **Links:** each link is 44px tall, so the hover and tap areas are comfortable even though the text is only 16px.
- **Mobile:** at 720px and below it drops to 64px, with 16px margins and slightly smaller type. The ratios between gaps stay the same. If three links plus the button still don't fit at 360px, hide the nav behind a menu button rather than squeezing it.

I used a green accent and ink color as placeholders. Swap in your brand colors, since the spacing doesn't depend on them.
