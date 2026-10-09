Here's the full updated file. I kept the `#num` and `#room` IDs, and your update script doesn't need any changes. A `MutationObserver` watches those two elements and plays a short "new call" animation whenever their text changes.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Queue</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {
    --bg: #0b1424;
    --panel: #16294a;
    --card: #1b2f55;
    --muted: #a9bee0;
    --accent: #7fd6a8;
  }
  * { box-sizing: border-box; }
  html, body { height: 100%; }
  body {
    margin: 0; color: #fff; font-family: system-ui, sans-serif;
    display: flex; flex-direction: column; overflow: hidden;
    background: radial-gradient(1200px 700px at 50% 0%, #1a3260 0%, var(--bg) 70%);
  }

  /* top bar */
  .top {
    display: flex; justify-content: space-between; align-items: center;
    padding: 2vh 4vw 0; color: var(--muted); font-size: clamp(18px, 2.2vw, 36px);
  }
  .top .clock { font-variant-numeric: tabular-nums; font-weight: 600; }

  /* now serving */
  .now {
    flex: 1; display: flex; flex-direction: column; justify-content: center; align-items: center;
    margin: 2vh 4vw; border-radius: 28px; text-align: center; position: relative; overflow: hidden;
    background: linear-gradient(160deg, #1b3563, var(--panel));
    box-shadow: 0 20px 60px rgba(0,0,0,.4), inset 0 0 0 1px rgba(255,255,255,.07);
  }
  .now small {
    display: inline-flex; align-items: center; gap: .6em;
    font-size: clamp(22px, 2.6vw, 44px); letter-spacing: .14em; color: var(--muted);
  }
  .dot {
    width: .5em; height: .5em; border-radius: 50%; background: var(--accent);
    animation: pulse 2s ease-out infinite;
  }
  .now .num {
    font-size: clamp(100px, 20vw, 340px); font-weight: 800; line-height: 1; margin: .05em 0;
    font-variant-numeric: tabular-nums; letter-spacing: .02em;
    text-shadow: 0 0 40px rgba(127,214,168,.25);
  }
  .now .room {
    font-size: clamp(36px, 5vw, 88px); font-weight: 600; color: var(--accent);
  }

  /* highlight sweep + pop when a new patient is called */
  .now::after {
    content: ""; position: absolute; inset: 0; pointer-events: none; opacity: 0;
    background: linear-gradient(105deg, transparent 35%, rgba(127,214,168,.28) 50%, transparent 65%);
    transform: translateX(-100%);
  }
  .now.called::after { animation: sweep 1.4s ease-out; }
  .now.called .num, .now.called .room { animation: pop .8s cubic-bezier(.2,1.4,.4,1); }

  /* upcoming */
  .next { display: flex; gap: 2vw; padding: 0 4vw 3vh; }
  .next > div {
    flex: 1; background: var(--card); border-radius: 20px; padding: 2.2vh 1vw; text-align: center;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,.06);
    animation: rise .7s ease-out both;
  }
  .next > div:nth-child(2) { animation-delay: .12s; }
  .next > div:nth-child(3) { animation-delay: .24s; }
  .next .n { font-size: clamp(40px, 5.5vw, 96px); font-weight: 700; font-variant-numeric: tabular-nums; }
  .next .l { font-size: clamp(18px, 2vw, 32px); color: var(--muted); text-transform: uppercase; letter-spacing: .08em; }

  @keyframes pulse {
    0%   { box-shadow: 0 0 0 0 rgba(127,214,168,.6); }
    100% { box-shadow: 0 0 0 .6em rgba(127,214,168,0); }
  }
  @keyframes sweep {
    0%   { transform: translateX(-100%); opacity: 1; }
    100% { transform: translateX(100%);  opacity: 1; }
  }
  @keyframes pop {
    0%   { transform: scale(.85); opacity: 0; filter: brightness(2); }
    100% { transform: scale(1);   opacity: 1; filter: brightness(1); }
  }
  @keyframes rise {
    from { transform: translateY(24px); opacity: 0; }
    to   { transform: none; opacity: 1; }
  }
  @media (prefers-reduced-motion: reduce) {
    *, *::after { animation: none !important; }
  }
</style></head>
<body>
  <div class="top"><span>Please watch for your ticket number</span><span class="clock" id="clock"></span></div>
  <div class="now" id="now">
    <small><span class="dot"></span>NOW SERVING</small>
    <div class="num" id="num">A-117</div>
    <div class="room" id="room">Go to Room 3</div>
  </div>
  <div class="next">
    <div><div class="n">A-118</div><div class="l">Next</div></div>
    <div><div class="n">A-119</div><div class="l">Then</div></div>
    <div><div class="n">A-120</div><div class="l">Then</div></div>
  </div>

<script>
  // Clock
  const clock = document.getElementById('clock');
  const tick = () => clock.textContent =
    new Date().toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
  tick(); setInterval(tick, 5000);

  // Animate whenever the existing script changes the number or room
  const now = document.getElementById('now');
  const replay = () => {
    now.classList.remove('called');
    void now.offsetWidth; // restart animation
    now.classList.add('called');
  };
  const obs = new MutationObserver(replay);
  ['num', 'room'].forEach(id => obs.observe(document.getElementById(id),
    { childList: true, characterData: true, subtree: true }));
</script>
</body></html>
```

What changed, and why:

- **Sizes:** Text and layout scale with the screen (`clamp()` and `vw`), so it fills any TV. The ticket number is now up to about 340px, which helps people reading from across the room.
- **Look:** There's a soft gradient background, a rounded "now serving" panel with depth, and a faint glow on the number. The upcoming cards fade in one after another when the page loads.
- **Alive:** A pulsing green dot sits next to "NOW SERVING". A clock shows in the corner, which also makes it obvious the screen hasn't frozen.
- **New call:** The number and room pop in and a light sweep crosses the panel. That catches people's eye when the call changes. It plays only on a change, so nothing is moving constantly while people read.
- **Readability:** I didn't use any cycling or scrolling text, and the contrast is the same or slightly higher than before. Numbers use tabular figures so digits don't shift width. Animations switch off if the TV or browser has "reduce motion" enabled.

The "Next / Then" cards are still hardcoded in the HTML, as in your original. If your script updates them, give them IDs or classes and the same animation can be applied there.
