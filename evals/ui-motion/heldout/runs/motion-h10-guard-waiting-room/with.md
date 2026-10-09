Here's the full updated file. I couldn't see your script, so it works without changes. A `MutationObserver` watches the text and plays the animation whenever the script updates the number, room or next-up tickets.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Queue</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {
    --ease-out: cubic-bezier(.16, 1, .3, 1);
    --accent: #7fd6a8;
  }
  * { box-sizing: border-box; }
  html, body { height: 100%; }
  body {
    margin:0; color:#fff; font-family: system-ui, sans-serif;
    font-variant-numeric: tabular-nums;
    background: radial-gradient(120% 90% at 50% 0%, #1a3260 0%, #0f1b2d 60%) #0f1b2d;
    display:flex; flex-direction:column; overflow:hidden;
  }

  /* Now serving */
  .now {
    flex: 1; display:flex; flex-direction:column; justify-content:center; align-items:center;
    margin: 32px 48px 0; padding: 32px;
    text-align:center; border-radius: 28px;
    background: linear-gradient(180deg, #1a3157, #16294a);
    border: 1px solid rgba(155,179,214,.18);
    box-shadow: 0 20px 60px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.06);
    position: relative; overflow:hidden;
  }
  /* Highlight wash that plays when a new patient is called */
  .now::after {
    content:""; position:absolute; inset:0; border-radius:inherit; pointer-events:none;
    background: radial-gradient(70% 70% at 50% 50%, rgba(127,214,168,.35), rgba(127,214,168,0) 70%);
    opacity:0;
  }
  .now small { font-size:clamp(24px, 2.4vw, 36px); letter-spacing:.18em; color:#9bb3d6; font-weight:600; }
  .now .num {
    font-size:clamp(120px, 17vw, 280px); font-weight:800; line-height:1.05; letter-spacing:-.02em;
    background: linear-gradient(180deg, #fff 30%, #cfe0ff);
    -webkit-background-clip:text; background-clip:text; color:transparent;
  }
  .now .room {
    font-size:clamp(36px, 3.6vw, 60px); font-weight:600; color:var(--accent);
    padding: 8px 28px; border-radius: 999px; background: rgba(127,214,168,.12);
  }

  /* Up next */
  .next { display:flex; gap:24px; padding:32px 48px 40px; }
  .next > div {
    flex:1; text-align:center; padding:24px; border-radius:20px;
    background: #1b2f55; border: 1px solid rgba(155,179,214,.14);
  }
  .next .n { font-size:clamp(48px, 5vw, 80px); font-weight:700; }
  .next .l { font-size:clamp(20px, 1.8vw, 28px); color:#9bb3d6; }

  /* Change animation (triggered by script below) */
  .now.changed::after { animation: wash 1400ms ease-out; }
  .now.changed .num   { animation: num-in 450ms var(--ease-out); }
  .now.changed .room  { animation: num-in 450ms var(--ease-out) 90ms backwards; }
  .next.changed > div { animation: card-in 350ms var(--ease-out) backwards; }
  .next.changed > div:nth-child(2) { animation-delay: 40ms; }
  .next.changed > div:nth-child(3) { animation-delay: 80ms; }

  @keyframes num-in  { from { opacity:0; transform: translateY(28px); } to { opacity:1; transform:none; } }
  @keyframes card-in { from { opacity:0; transform: translateY(16px); } to { opacity:1; transform:none; } }
  @keyframes wash    { 0% { opacity:1; } 100% { opacity:0; } }

  /* Reduced motion: drop movement, keep the fade and highlight so the change is still noticeable */
  @media (prefers-reduced-motion: reduce) {
    .now.changed .num, .now.changed .room { animation-name: fade-in; }
    .next.changed > div { animation-name: fade-in; }
    @keyframes fade-in { from { opacity:0; } to { opacity:1; } }
  }
</style></head>
<body>
  <div class="now"><small>NOW SERVING</small><div class="num" id="num">A-117</div><div class="room" id="room">Go to Room 3</div></div>
  <div class="next">
    <div><div class="n">A-118</div><div class="l">Next</div></div>
    <div><div class="n">A-119</div><div class="l">Then</div></div>
    <div><div class="n">A-120</div><div class="l">Then</div></div>
  </div>

<script>
  // Replays a CSS animation on `el` each time the watched content changes.
  // Works with whatever script updates the text; no changes to it are needed.
  function animateOnChange(el, watch) {
    var timer;
    new MutationObserver(function () {
      el.classList.remove('changed');
      void el.offsetWidth; // restart the animation if it was mid-play
      el.classList.add('changed');
      clearTimeout(timer);
      timer = setTimeout(function () { el.classList.remove('changed'); }, 1600);
    }).observe(watch, { childList: true, characterData: true, subtree: true });
  }
  animateOnChange(document.querySelector('.now'), document.querySelector('.now'));
  animateOnChange(document.querySelector('.next'), document.querySelector('.next'));
</script>
</body></html>
```

**What changed**
- **Look:** The page now has a soft gradient background, rounded cards with subtle borders, and a pill behind the room line. The text scales with the screen (`clamp`), so it fills a TV and stays readable from across the room. Digits use `tabular-nums`, so numbers don't jitter in width.
- **Motion:** The only motion plays when a patient is called. The number and room slide up and fade in over 450 ms. A soft green glow fades out over 1.4 s, which is long enough to catch someone's eye in a waiting room. The next-up cards fade in with a 40 ms stagger. Nothing loops or pulses, so the screen stays calm the rest of the time.
- **Reduced motion:** Users with `prefers-reduced-motion` get fades and the glow, with no sliding.

**What to check**
- If your script rebuilds the `.now` or `.next` elements instead of changing their text, the observer will be lost. Tell me if it does that and I'll adjust it.
- I didn't add a chime. It would help people who aren't looking at the screen, but it needs a one-time click to enable audio in browsers, and I didn't want to add that without asking.
