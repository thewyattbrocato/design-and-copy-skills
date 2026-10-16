Your last bar probably looked small because it was short and its type was small, so it lost to the hero photo. A site header usually runs 64–80px tall. I've used 72px on desktop, which is enough to hold its own over a big image.

```css
:root {
  /* 4px-base spacing scale */
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;

  --bar-height: 72px;
  --page-margin: clamp(16px, 4vw, 40px);
}

.topbar {
  height: var(--bar-height);
  padding-inline: var(--page-margin);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #fff;
  border-bottom: 1px solid rgb(0 0 0 / 0.08);
}

/* Logo */
.topbar__logo {
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -0.01em;
  line-height: 1;
}

/* Links sit next to the logo, not floating in the middle */
.topbar__nav {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-left: var(--space-10);   /* logo -> links: bigger than link gap */
  margin-right: auto;             /* pushes the button to the far right */
}

.topbar__nav a {
  display: inline-flex;
  align-items: center;
  height: 44px;                   /* touch-sized hit area */
  padding-inline: var(--space-4);
  font-size: 16px;
  font-weight: 500;
  line-height: 1;
  border-radius: 8px;
  color: #3a3f45;
  text-decoration: none;
}
.topbar__nav a:hover { background: rgb(0 0 0 / 0.05); color: #111; }

/* Log a run button */
.btn-primary {
  display: inline-flex;
  align-items: center;
  height: 44px;
  padding-inline: var(--space-6);  /* 24px: ~2x the 12px of vertical room */
  font-size: 16px;
  font-weight: 600;
  line-height: 1;
  white-space: nowrap;
  color: #fff;
  background: #1f6f4a;             /* swap for your brand green */
  border: 0;
  border-radius: 8px;
  cursor: pointer;
}
.btn-primary:hover { background: #185a3c; }

@media (max-width: 640px) {
  :root { --bar-height: 64px; }
  .topbar__logo { font-size: 20px; }
  .topbar__nav { margin-left: var(--space-4); }
  .topbar__nav a { padding-inline: var(--space-3); font-size: 15px; }
  .btn-primary { padding-inline: var(--space-4); }
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
  <button class="btn-primary">Log a run</button>
</header>
```

The numbers and why I picked them:
- **Bar height:** 72px on desktop and 64px at 640px and below. The height is the same at every width within a breakpoint, so the bar doesn't jump around.
- **Link and button height:** both are 44px, which leaves 14px above and below inside the 72px bar. They're also a comfortable touch size.
- **Link text:** 16px/500. Anything under 15px next to a big photo reads as tiny.
- **Button padding:** 24px sides on a 44px height. That's about twice the vertical room, so it reads as a button and not a cramped link.
- **Link spacing:** links are 8px apart, and each has 16px of its own side padding. That puts about 32px between the words, so they read as one group.
- **Logo to links:** 40px, bigger than the gap between links, so the logo reads as a separate group.
- **Side margins:** 16–40px, scaling with the viewport. This stays larger than the gaps inside the bar.
- **Bar edge:** a 1px hairline at 8% black. If the bar sits on top of the photo, drop the border and use a transparent background with white text instead. In that case, add a dark gradient scrim on the photo so the links stay readable.
