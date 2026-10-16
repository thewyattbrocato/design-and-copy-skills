```html
<header class="topbar">
  <div class="topbar__inner">
    <a class="logo" href="/">Switchback</a>
    <nav class="nav" aria-label="Primary">
      <a href="/runs">Runs</a>
      <a href="/routes">Routes</a>
      <a href="/gear">Gear</a>
    </nav>
    <a class="btn" href="/log">Log a run</a>
  </div>
</header>
```

```css
:root {
  --ink: #1b2a22;
  --bg: #ffffff;
  --line: #e4e7e3;
  --accent: #c2410c;       /* white text on this is ~5.2:1 */
  --accent-hover: #9a3412;
}

.topbar {
  position: sticky;
  top: 0;
  z-index: 50;
  background: var(--bg);
  border-bottom: 1px solid var(--line);
}

.topbar__inner {
  display: flex;
  align-items: center;
  height: 76px;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 40px;
}

.logo {
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--ink);
  text-decoration: none;
}

.nav {
  display: flex;
  gap: 36px;
  margin-left: 56px;      /* space between logo and first link */
}

.nav a {
  font-size: 17px;
  font-weight: 500;
  color: var(--ink);
  text-decoration: none;
  padding: 12px 2px;      /* ~44px tall tap target */
}

.nav a:hover { text-decoration: underline; text-underline-offset: 6px; text-decoration-thickness: 2px; }

.btn {
  margin-left: auto;      /* pushes it to the right edge */
  display: inline-flex;
  align-items: center;
  height: 48px;
  padding: 0 26px;
  font-size: 16px;
  font-weight: 600;
  color: #fff;
  background: var(--accent);
  border-radius: 10px;
  text-decoration: none;
  transition: background 0.15s;
}

.btn:hover { background: var(--accent-hover); }
.btn:focus-visible,
.nav a:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }

@media (max-width: 720px) {
  .topbar__inner { height: 64px; padding: 0 16px; }
  .logo { font-size: 22px; }
  .nav { gap: 20px; margin-left: 24px; }
  .nav a { font-size: 16px; }
  .btn { height: 44px; padding: 0 18px; font-size: 15px; }
}
```

**Why these numbers fix the "tiny" look:**
- **Bar height:** 76px on desktop. A full-bleed hero photo needs a bar of at least ~72px to feel proportionate, and 48–56px reads as a thin strip beside it.
- **Type:** the logo at 26px, links at 17px and the button at 16px give three clear levels. Links under 15px are what usually make a bar feel cramped.
- **Spacing:** a 36px gap between links and 56px between logo and nav keeps the groups distinct. The 40px side padding stops the logo and button from touching the viewport edge.
- **Button:** 48px tall with 26px horizontal padding is a generous, obviously clickable target. The solid orange also stands out against the green and neutral photo and text.

**Mobile:** if three links plus the button don't fit below ~420px, hide the nav behind a menu button. Don't shrink the type below 15px to squeeze them in.
