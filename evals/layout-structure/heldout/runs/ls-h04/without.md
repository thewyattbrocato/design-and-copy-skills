I couldn't save the file because the Write tool is disabled in this session. The full page is below, so you can save it as `lantern-night.html`. It's a single file with inline CSS and system fonts, and it has no external assets. The layout is fluid, so it works on a phone and a desktop.

I left the weekday off the page because you didn't give one.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lantern Night · Oct 18 · Wren Park</title>
<style>
  :root {
    --night: #14122b;
    --night-2: #221c45;
    --glow: #ffb938;
    --ember: #ff7a3d;
    --paper: #fff6e3;
    --muted: #cfc6e8;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: var(--paper);
    background: var(--night);
    line-height: 1.5;
    -webkit-text-size-adjust: 100%;
  }
  .poster {
    max-width: 880px;
    margin: 0 auto;
    min-height: 100vh;
    padding: clamp(24px, 6vw, 64px) clamp(20px, 5vw, 56px);
    background:
      radial-gradient(ellipse at 50% 18%, rgba(255,185,56,.28), transparent 55%),
      linear-gradient(180deg, var(--night-2), var(--night) 70%);
    text-align: center;
  }
  .kicker {
    letter-spacing: .3em;
    text-transform: uppercase;
    font-size: clamp(.75rem, 2.4vw, .95rem);
    color: var(--glow);
    font-weight: 700;
  }
  .lanterns {
    display: flex;
    justify-content: center;
    gap: clamp(12px, 4vw, 32px);
    margin: 28px 0 8px;
    align-items: flex-start;
  }
  .lantern {
    width: clamp(36px, 10vw, 64px);
    aspect-ratio: 3 / 4;
    border-radius: 40% 40% 45% 45%;
    background: radial-gradient(circle at 50% 55%, #fff1b8, var(--glow) 45%, var(--ember));
    box-shadow: 0 0 28px 6px rgba(255,160,50,.55);
    position: relative;
  }
  .lantern::before {
    content: "";
    position: absolute;
    left: 50%; top: -22px;
    width: 2px; height: 22px;
    background: var(--muted);
    opacity: .6;
  }
  .lantern:nth-child(2n) { margin-top: 22px; background: radial-gradient(circle at 50% 55%, #ffe3d0, #ff9a6b 45%, #e5484d); box-shadow: 0 0 28px 6px rgba(255,100,80,.5); }
  .lantern:nth-child(3n) { margin-top: 8px; }
  h1 {
    font-size: clamp(3rem, 14vw, 7.5rem);
    line-height: .95;
    text-transform: uppercase;
    letter-spacing: -.02em;
    font-weight: 900;
    margin: 20px 0 12px;
    color: var(--paper);
    text-shadow: 0 0 30px rgba(255,185,56,.6);
  }
  h1 span { display: block; color: var(--glow); }
  .tagline {
    font-size: clamp(1rem, 3vw, 1.3rem);
    color: var(--muted);
    max-width: 32em;
    margin: 0 auto;
  }
  .when {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin: 40px 0;
  }
  .when div {
    border: 2px solid var(--glow);
    border-radius: 14px;
    padding: 16px 8px;
    background: rgba(255,185,56,.08);
  }
  .when b {
    display: block;
    font-size: clamp(1.2rem, 4.5vw, 2rem);
    color: var(--glow);
    line-height: 1.15;
  }
  .when small {
    font-size: .75rem;
    letter-spacing: .15em;
    text-transform: uppercase;
    color: var(--muted);
  }
  h2 {
    font-size: .85rem;
    letter-spacing: .3em;
    text-transform: uppercase;
    color: var(--glow);
    margin-bottom: 16px;
  }
  .schedule {
    list-style: none;
    text-align: left;
    max-width: 560px;
    margin: 0 auto 40px;
  }
  .schedule li {
    display: flex;
    gap: 18px;
    align-items: baseline;
    padding: 14px 0;
    border-bottom: 1px dashed rgba(207,198,232,.35);
    font-size: clamp(1.05rem, 3.5vw, 1.35rem);
  }
  .schedule time {
    flex: 0 0 5.2em;
    font-weight: 800;
    color: var(--glow);
    font-variant-numeric: tabular-nums;
  }
  .schedule em { display: block; font-style: normal; font-size: .8em; color: var(--muted); }
  .all-night {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 14px;
    margin-bottom: 40px;
    text-align: left;
  }
  .card {
    background: rgba(255,246,227,.07);
    border-radius: 14px;
    padding: 18px 20px;
  }
  .card h3 { font-size: 1.1rem; color: var(--paper); }
  .card p { color: var(--muted); font-size: .95rem; }
  .free {
    display: inline-block;
    background: var(--glow);
    color: var(--night);
    font-weight: 900;
    letter-spacing: .12em;
    text-transform: uppercase;
    padding: 12px 28px;
    border-radius: 999px;
    font-size: clamp(1rem, 3.5vw, 1.3rem);
  }
  footer { margin-top: 20px; color: var(--muted); font-size: .9rem; }
  @media (max-width: 420px) {
    .schedule li { gap: 12px; }
    .schedule time { flex-basis: 4.6em; }
  }
  @media (prefers-reduced-motion: no-preference) {
    .lantern { animation: bob 4s ease-in-out infinite; }
    .lantern:nth-child(2n) { animation-delay: -1.3s; }
    .lantern:nth-child(3n) { animation-delay: -2.6s; }
    @keyframes bob { 50% { transform: translateY(8px); } }
  }
</style>
</head>
<body>
<main class="poster">
  <p class="kicker">A neighborhood festival</p>

  <div class="lanterns" aria-hidden="true">
    <div class="lantern"></div><div class="lantern"></div><div class="lantern"></div>
    <div class="lantern"></div><div class="lantern"></div>
  </div>

  <h1>Lantern <span>Night</span></h1>
  <p class="tagline">An evening of light, music, and good food. Bring your neighbors and carry a light.</p>

  <section class="when" aria-label="Date, time and place">
    <div><b>Oct 18</b><small>Date</small></div>
    <div><b>6–10 pm</b><small>Time</small></div>
    <div><b>Wren Park</b><small>Place</small></div>
  </section>

  <section>
    <h2>The Evening</h2>
    <ul class="schedule">
      <li><time>6:00 pm</time><span>Doors open<em>Food trucks and craft tent are ready</em></span></li>
      <li><time>7:30 pm</time><span>Lantern parade<em>Lights up, we walk together</em></span></li>
      <li><time>9:00 pm</time><span>Live drumming<em>Close out the night with rhythm</em></span></li>
      <li><time>10:00 pm</time><span>Goodnight<em>Walk home safe</em></span></li>
    </ul>
  </section>

  <section>
    <h2>All Evening</h2>
    <div class="all-night">
      <div class="card"><h3>Food trucks</h3><p>Dinner and treats, right on the lawn.</p></div>
      <div class="card"><h3>Kids' craft tent</h3><p>Make a lantern to carry in the parade.</p></div>
    </div>
  </section>

  <p class="free">Free for everyone</p>
  <footer>Wren Park · October 18</footer>
</main>
</body>
</html>
```

I haven't opened it in a browser, so I haven't checked how it renders.

I added a few details you didn't give me, so check them:
- The "Doors open" line at 6:00 and "Goodnight" at 10:00 come from your 6–10pm window.
- The craft tent blurb says kids can make a lantern to carry in the parade. That's my guess, so change it if the tent does something else.
- The taglines and the "Walk home safe" line are placeholder copy.

If you enable Write, I can save the file directly.
