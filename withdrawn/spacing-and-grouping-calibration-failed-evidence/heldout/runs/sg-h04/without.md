Your last bar probably looked small because the type was around 13–14px and the bar was under 56px tall. Next to a full-bleed photo, that reads as cramped. These numbers fix it by making the bar 72px tall with 16px links and a 44px button.

```html
<header class="topbar">
  <div class="topbar__inner">
    <a class="logo" href="/">Switchback</a>
    <nav class="nav" aria-label="Primary">
      <a href="/runs">Runs</a>
      <a href="/routes">Routes</a>
      <a href="/gear">Gear</a>
    </nav>
    <a class="btn" href="/runs/new">Log a run</a>
  </div>
</header>
```

```css
.topbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: #fff;
  border-bottom: 1px solid #e5e7e3;
}

.topbar__inner {
  max-width: 1280px;
  height: 72px;
  margin: 0 auto;
  padding: 0 32px;
  display: flex;
  align-items: center;
}

.logo {
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: #14281d;
  text-decoration: none;
}

.nav {
  display: flex;
  gap: 8px;
  margin-left: 48px;   /* space between logo and links */
  margin-right: auto;  /* pushes the button to the far right */
}

.nav a {
  padding: 10px 14px;  /* ~40px tall hit area */
  font-size: 16px;
  font-weight: 500;
  line-height: 20px;
  color: #3b4a41;
  text-decoration: none;
  border-radius: 6px;
}

.nav a:hover { color: #14281d; background: #f1f4f0; }

.btn {
  display: inline-flex;
  align-items: center;
  height: 44px;
  padding: 0 22px;
  font-size: 16px;
  font-weight: 600;
  color: #fff;
  background: #1f6b45;  /* white text on this is ~6.3:1 */
  border-radius: 8px;
  text-decoration: none;
}

.btn:hover { background: #185537; }
.btn:focus-visible,
.nav a:focus-visible { outline: 3px solid #7cc4a0; outline-offset: 2px; }

@media (max-width: 720px) {
  .topbar__inner { height: 64px; padding: 0 16px; }
  .logo { font-size: 20px; }
  .nav { margin-left: 20px; }
  .nav a { padding: 10px; font-size: 15px; }
  .btn { height: 40px; padding: 0 16px; font-size: 15px; }
}
```

Why these numbers:
- **72px bar:** with a large hero underneath, anything under 64px looks like a thin strip. 72px gives the bar enough weight to hold its own against the photo.
- **24px logo and 16px links:** the logo reads as the anchor, and the links stay readable. 14px nav text is the usual cause of the "tiny" feel.
- **44px button:** this is the standard minimum touch target. It's also taller than the 40px link hit areas, so it reads as the primary action.
- **48px gap after the logo, 8px between link boxes:** each link has 14px of padding, so the visible gap between words is about 36px. That's enough to keep them from looking cramped.

If the hero photo is dark and you want the bar to sit on top of it, change `.topbar` to `position: absolute; background: transparent; border: 0`. Then switch the logo and link colors to white, and add a subtle top gradient on the photo so the text stays legible.
