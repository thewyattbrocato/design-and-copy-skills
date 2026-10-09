I couldn't save the file. The Write tool is disabled in this session, so `index.html` doesn't exist yet. The full page is below. Save it as `index.html` and open it in a browser.

I made two changes from my first draft. I removed the weekday, because you didn't give one. I also changed "Gates open" to "Festival opens", because I don't know that the park has gates.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lantern Night · Oct 18 · Wren Park</title>
<meta name="description" content="Lantern Night, a free neighborhood festival at Wren Park on Oct 18, 6–10pm. Lantern parade, food trucks, kids' craft tent, live drumming.">
<style>
  :root {
    --night: #12142b; --night-2: #1b1e3d;
    --glow: #ffb43c; --glow-soft: #ffd98a; --ember: #ff6a3d;
    --paper: #fff6e3; --muted: #b9bcd9;
    --edge: clamp(1.25rem, 6vw, 4rem);
    --measure: 36rem;
    --serif: Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
    --sans: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }
  * { box-sizing: border-box; }
  html { -webkit-text-size-adjust: 100%; }
  body { margin: 0; background: var(--night); color: var(--paper); font-family: var(--sans); font-size: 1.0625rem; line-height: 1.55; }
  .wrap { max-width: 72rem; margin: 0 auto; padding-inline: var(--edge); }

  /* Hero */
  .hero {
    position: relative; overflow: hidden;
    padding-block: clamp(2.5rem, 8vw, 6rem) clamp(2.5rem, 6vw, 4.5rem);
    background:
      radial-gradient(60rem 30rem at 85% 0%, rgba(255,180,60,.22), transparent 60%),
      radial-gradient(40rem 24rem at 0% 100%, rgba(255,106,61,.14), transparent 60%),
      var(--night);
  }
  .kicker { margin: 0 0 1rem; font-size: .8125rem; letter-spacing: .22em; text-transform: uppercase; color: var(--glow-soft); font-weight: 700; }
  h1 { margin: 0; font-family: var(--serif); font-weight: 700; font-size: clamp(3.5rem, 15vw, 10.5rem); line-height: .88; letter-spacing: -.02em; }
  h1 span { display: block; color: var(--glow); }
  .tagline { margin: 1.5rem 0 0; max-width: var(--measure); font-size: clamp(1.15rem, 2.6vw, 1.5rem); line-height: 1.4; }

  /* decorative CSS lanterns */
  .lanterns { position: absolute; inset: 0; pointer-events: none; }
  .lantern {
    position: absolute; top: 0; left: var(--x);
    width: var(--w); height: calc(var(--w) * 1.25); margin-top: var(--drop);
    border-radius: 45% 45% 40% 40% / 38% 38% 55% 55%;
    background: radial-gradient(circle at 50% 55%, #fff1c2 0%, var(--glow) 45%, var(--ember) 100%);
    box-shadow: 0 0 2.5rem .6rem rgba(255,180,60,.45);
    animation: sway 6s ease-in-out infinite alternate;
    transform-origin: 50% calc(-1 * var(--drop));
  }
  .lantern::before { content: ""; position: absolute; left: 50%; bottom: 100%; width: 1px; height: var(--drop); background: rgba(255,217,138,.5); }
  .lantern::after { content: ""; position: absolute; left: 20%; right: 20%; top: -4%; height: 8%; background: #5a3a1a; border-radius: 3px; }
  .l1 { --w: 3.2rem; --x: 62%; --drop: 1.5rem; animation-delay: -1s; }
  .l2 { --w: 2.2rem; --x: 76%; --drop: 5rem;   animation-delay: -3s; }
  .l3 { --w: 4rem;   --x: 88%; --drop: 2.5rem; animation-delay: -2s; }
  .l4 { --w: 1.7rem; --x: 52%; --drop: 7rem;   animation-delay: -4s; }
  @keyframes sway { from { transform: rotate(-4deg); } to { transform: rotate(4deg); } }
  @media (prefers-reduced-motion: reduce) { .lantern { animation: none; } }
  @media (max-width: 40rem) {
    .l4 { display: none; }
    .l1 { --x: 66%; } .l2 { --x: 80%; } .l3 { --x: 90%; --w: 3rem; }
    .lantern { opacity: .55; }
  }

  /* key facts */
  .facts { list-style: none; margin: clamp(2rem, 5vw, 3.5rem) 0 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(10.5rem, 1fr)); border-top: 2px solid var(--glow); }
  .facts li { padding: 1rem 1rem 0 0; }
  .facts .label { display: block; font-size: .75rem; letter-spacing: .18em; text-transform: uppercase; color: var(--muted); font-weight: 700; }
  .facts .value { display: block; margin-top: .2rem; font-family: var(--serif); font-size: clamp(1.6rem, 4vw, 2.25rem); line-height: 1.1; font-weight: 700; }
  .facts .free { color: var(--glow); }

  /* Schedule */
  .schedule { background: var(--paper); color: #1d1a2e; padding-block: clamp(2.5rem, 7vw, 5rem); }
  h2 { margin: 0 0 1.5rem; font-family: var(--serif); font-size: clamp(2rem, 6vw, 3.25rem); line-height: 1; letter-spacing: -.01em; }
  .timeline { list-style: none; margin: 0; padding: 0; }
  .timeline li { display: grid; grid-template-columns: minmax(5.5rem, 9rem) 1fr; column-gap: clamp(1rem, 4vw, 3rem); align-items: baseline; padding-block: 1.25rem; border-top: 1px solid rgba(29,26,46,.25); }
  .timeline li:last-child { border-bottom: 1px solid rgba(29,26,46,.25); }
  .time { font-family: var(--serif); font-weight: 700; font-size: clamp(1.6rem, 5vw, 2.75rem); line-height: 1; color: #b8400f; white-space: nowrap; }
  .time small { font-size: .5em; font-family: var(--sans); letter-spacing: .05em; margin-left: .1em; }
  .what h3 { margin: 0; font-size: clamp(1.25rem, 3vw, 1.6rem); line-height: 1.2; }
  .what p { margin: .3rem 0 0; max-width: var(--measure); color: #46435c; }
  /* the parade is the headline event */
  .timeline li.main { background: var(--night); color: var(--paper); margin-inline: calc(-1 * clamp(.75rem, 2vw, 1.5rem)); padding-inline: clamp(.75rem, 2vw, 1.5rem); border-radius: .5rem; border-top-color: transparent; }
  .timeline li.main + li { border-top-color: transparent; }
  .timeline li.main .time { color: var(--glow); }
  .timeline li.main .what p { color: var(--muted); }

  /* Around the park */
  .extras { padding-block: clamp(2.5rem, 7vw, 5rem); background: var(--night-2); }
  .extras-grid { display: grid; gap: clamp(1.5rem, 4vw, 3rem); grid-template-columns: 1fr; }
  @media (min-width: 46rem) { .extras-grid { grid-template-columns: 1fr 1fr; } }
  .extra { border-left: 4px solid var(--glow); padding-left: 1.25rem; }
  .extra h3 { margin: 0; font-family: var(--serif); font-size: clamp(1.6rem, 4vw, 2.1rem); line-height: 1.1; color: var(--glow-soft); }
  .extra p { margin: .6rem 0 0; max-width: 30rem; }

  /* Footer */
  footer { padding-block: clamp(2.5rem, 6vw, 4rem); }
  .big-line { margin: 0; font-family: var(--serif); font-size: clamp(1.75rem, 6vw, 3.5rem); line-height: 1.05; font-weight: 700; }
  .big-line em { color: var(--glow); font-style: normal; }
  .fine { margin: 1rem 0 0; color: var(--muted); font-size: .9375rem; }
  :focus-visible { outline: 3px solid var(--glow); outline-offset: 3px; }
</style>
</head>
<body>

<header class="hero">
  <div class="lanterns" aria-hidden="true">
    <span class="lantern l1"></span><span class="lantern l2"></span>
    <span class="lantern l3"></span><span class="lantern l4"></span>
  </div>
  <div class="wrap">
    <p class="kicker">A neighborhood festival</p>
    <h1>Lantern <span>Night</span></h1>
    <p class="tagline">One evening, one park, and a whole neighborhood walking by lantern light.</p>
    <ul class="facts">
      <li><span class="label">Date</span><span class="value">Oct 18</span></li>
      <li><span class="label">Time</span><span class="value">6 – 10 pm</span></li>
      <li><span class="label">Place</span><span class="value">Wren Park</span></li>
      <li><span class="label">Admission</span><span class="value free">Free</span></li>
    </ul>
  </div>
</header>

<main>
  <section class="schedule" aria-labelledby="sched-h">
    <div class="wrap">
      <h2 id="sched-h">The evening</h2>
      <ol class="timeline">
        <li>
          <span class="time">6:00<small>PM</small></span>
          <div class="what"><h3>Festival opens</h3>
            <p>Find a spot on the lawn, grab dinner from the food trucks, and settle in as the light fades.</p></div>
        </li>
        <li class="main">
          <span class="time">7:30<small>PM</small></span>
          <div class="what"><h3>Lantern parade</h3>
            <p>The whole crowd sets out together, lanterns lit.</p></div>
        </li>
        <li>
          <span class="time">9:00<small>PM</small></span>
          <div class="what"><h3>Live drumming</h3>
            <p>The night closes with rhythm you can feel in your chest.</p></div>
        </li>
        <li>
          <span class="time">10:00<small>PM</small></span>
          <div class="what"><h3>Good night</h3>
            <p>Walk home slowly.</p></div>
        </li>
      </ol>
    </div>
  </section>

  <section class="extras" aria-labelledby="extras-h">
    <div class="wrap">
      <h2 id="extras-h">Around the park</h2>
      <div class="extras-grid">
        <div class="extra"><h3>Food trucks</h3>
          <p>A lineup of local trucks parked at Wren Park, so dinner is sorted.</p></div>
        <div class="extra"><h3>Kids’ craft tent</h3>
          <p>A tent just for young makers, with plenty of room to get creative.</p></div>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <p class="big-line">Oct 18 &middot; 6–10 pm &middot; <em>Wren Park</em> &middot; Free</p>
    <p class="fine">Bring your neighbors.</p>
  </div>
</footer>

</body>
</html>
```

**Layout**
- **Hero:** a dark night-sky poster with a large two-line "Lantern / Night" title. A row of four facts (date, time, place, free) sits under it, so the basics show before any scrolling. Four CSS-only lanterns sway gently. They're hidden or dimmed on small screens, and the sway stops if the viewer has reduced motion turned on.
- **Schedule:** a light band with a time-and-event list for 6:00, 7:30, 9:00 and 10:00. The 7:30 parade is the one dark, highlighted row.
- **Around the park:** the food trucks and kids' craft tent, side by side on desktop and stacked on a phone.
- **Footer:** the key facts repeated in one line.
- **Fonts and sizing:** it uses system fonts only, with sizes that scale between phone and desktop. Body text is capped at a comfortable line length.

**Things to check**
- I wrote the descriptions for the 10:00 "Good night" row, the food trucks and the craft tent myself. Edit anything that doesn't match the real event.
- I didn't add a street address or a rain plan, because you didn't give them.
- I haven't viewed the page in a browser.

If you'd like the file written to disk, enable the Write tool or tell me where to save it, and I'll do it.
