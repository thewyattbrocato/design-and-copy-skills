```css
.topbar {
  position: sticky;
  top: 0;
  z-index: 50;
  background: #fff;
  border-bottom: 1px solid #e4e7e3;
}

.topbar__inner {
  display: flex;
  align-items: center;
  height: 72px;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 40px;
}

.topbar__logo {
  display: flex;
  align-items: center;
  height: 32px;            /* logo mark/wordmark; scale the SVG to this */
  font-size: 24px;         /* if the logo is text */
  font-weight: 700;
  letter-spacing: -0.02em;
  color: #14201a;
  text-decoration: none;
}

.topbar__nav {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: 48px;
}

.topbar__nav a {
  padding: 10px 14px;      /* 44px+ tall hit area */
  font-size: 16px;
  font-weight: 500;
  line-height: 24px;
  color: #3b4640;
  text-decoration: none;
  border-radius: 6px;
}

.topbar__nav a:hover      { color: #14201a; background: #f1f3f0; }
.topbar__nav a[aria-current="page"] { color: #14201a; font-weight: 600; }

.topbar__cta {
  margin-left: auto;
  display: inline-flex;
  align-items: center;
  height: 44px;
  padding: 0 22px;
  font-size: 16px;
  font-weight: 600;
  line-height: 1;
  color: #fff;
  background: #1f5c3a;
  border-radius: 8px;
  text-decoration: none;
  transition: background 0.15s;
}

.topbar__cta:hover        { background: #17482e; }
.topbar__cta:focus-visible,
.topbar__nav a:focus-visible {
  outline: 2px solid #1f5c3a;
  outline-offset: 2px;
}

@media (max-width: 720px) {
  .topbar__inner { height: 60px; padding: 0 16px; }
  .topbar__logo  { font-size: 20px; }
  .topbar__nav   { margin-left: 16px; gap: 0; }
  .topbar__nav a { padding: 10px 8px; font-size: 15px; }
  .topbar__cta   { height: 40px; padding: 0 16px; font-size: 15px; }
}
```

```html
<header class="topbar">
  <div class="topbar__inner">
    <a class="topbar__logo" href="/">Switchback</a>
    <nav class="topbar__nav">
      <a href="/runs">Runs</a>
      <a href="/routes">Routes</a>
      <a href="/gear">Gear</a>
    </nav>
    <a class="topbar__cta" href="/log">Log a run</a>
  </div>
</header>
```

Why these numbers fix the "tiny and cramped" feel:

- **72px bar height.** Under a large hero, 56px reads as a thin strip. 72px gives the bar enough presence to hold its own.
- **16px links with 14px side padding.** The visible gap between links is about 36px (14 + 8 + 14), so they don't crowd. The hit areas are 44px tall.
- **48px between logo and nav.** This separates the logo from the links so they don't read as one cluster.
- **44px button, 16px/600 text.** The button is the tallest element in the bar. It's the primary action, so it should carry the most weight.
- **40px side padding in a 1280px container.** The content lines up with the hero's content edge. If your hero's text container uses different values, match those.

On mobile the bar drops to 60px and the button to 40px. Three links plus the button fit at 360px wide. If your logo is wider than about 110px at that size, collapse the nav into a menu below 720px.

If the bar sits on top of the photo instead of above it, swap the background for `transparent`, make the text white, and add a `linear-gradient(rgba(0,0,0,.45), transparent)` behind it. Otherwise the links will be hard to read on bright areas of the photo.
