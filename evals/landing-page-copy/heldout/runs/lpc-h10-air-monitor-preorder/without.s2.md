I couldn't save the file because the Write tool is disabled in this session. The full page is below as a single self-contained HTML file, so you can save it as `index.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nook Air: preorder a pocket-sized air quality monitor</title>
<meta name="description" content="Nook Air is a pocket-sized air quality monitor for renters. It reads fine particles and CO2 and shows a green, yellow or red light. No app. Preorder with a refundable $10 deposit.">
<style>
  :root { --ink:#1d2421; --muted:#5b6761; --bg:#fbfaf7; --card:#fff; --line:#e4e1d9;
          --green:#2e9e5b; --yellow:#e8b020; --red:#d9483b; --accent:#1f5f4a; }
  * { box-sizing: border-box; }
  body { margin:0; font:17px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif; color:var(--ink); background:var(--bg); }
  .wrap { max-width:720px; margin:0 auto; padding:0 22px; }
  header { padding:22px 0; } .brand { font-weight:700; }
  .hero { padding:40px 0 28px; }
  h1 { font-size:clamp(2rem,6vw,3rem); line-height:1.12; margin:0 0 16px; }
  h2 { font-size:1.4rem; margin:0 0 12px; }
  p { margin:0 0 14px; }
  .lede { font-size:1.15rem; color:var(--muted); }
  .lights { display:flex; gap:10px; margin:24px 0; }
  .lights span { width:22px; height:22px; border-radius:50%; }
  .g { background:var(--green); } .y { background:var(--yellow); } .r { background:var(--red); }
  .btn { display:inline-block; background:var(--accent); color:#fff; text-decoration:none;
         padding:14px 26px; border-radius:10px; font-weight:600; font-size:1.05rem; }
  .btn:hover, .btn:focus-visible { background:#17493a; }
  .small { font-size:.92rem; color:var(--muted); }
  section { padding:28px 0; border-top:1px solid var(--line); }
  .card { background:var(--card); border:1px solid var(--line); border-radius:14px; padding:22px; }
  .steps, ul.plain { padding-left:1.2em; margin:0; }
  .steps li, ul.plain li { margin-bottom:10px; }
  .legend { list-style:none; padding:0; margin:0; }
  .legend li { display:flex; gap:12px; align-items:flex-start; margin-bottom:10px; }
  .legend .dot { flex:none; width:16px; height:16px; border-radius:50%; margin-top:7px; }
  details { border-bottom:1px solid var(--line); padding:14px 0; }
  summary { cursor:pointer; font-weight:600; }
  details p { margin:10px 0 0; color:var(--muted); }
  footer { padding:28px 0 56px; color:var(--muted); font-size:.9rem; }
</style>
</head>
<body>
<header><div class="wrap"><div class="brand">Nook Air</div></div></header>

<main><div class="wrap">

  <div class="hero">
    <h1>Know what you're breathing, at a glance.</h1>
    <p class="lede">Nook Air is a pocket-sized air quality monitor made for renters. It checks fine particles and CO2 and shows the result as one light: green, yellow or red. No app, no account, no drilling into walls.</p>
    <div class="lights" aria-hidden="true"><span class="g"></span><span class="y"></span><span class="r"></span></div>
    <p><a class="btn" href="#preorder">Preorder for a $10 deposit</a></p>
    <p class="small">Planned price $79. Deposit is refundable. Not shipping yet. Read the honest status below.</p>
  </div>

  <section>
    <h2>What it does</h2>
    <ul class="plain">
      <li><strong>Reads fine particles and CO2.</strong> Two things that are hard to notice without a sensor: smoke and dust on one side, stale, stuffy air on the other.</li>
      <li><strong>Shows one light on the front.</strong> You don't need to interpret numbers.</li>
      <li><strong>Sits on a shelf or clips to a bag.</strong> Leave it in the bedroom, or bring it to a coworking space or a friend's place.</li>
      <li><strong>Works without an app.</strong> Turn it on and look at it.</li>
    </ul>
  </section>

  <section>
    <h2>What the light means</h2>
    <ul class="legend">
      <li><span class="dot g"></span><span><strong>Green:</strong> air looks fine.</span></li>
      <li><span class="dot y"></span><span><strong>Yellow:</strong> worth paying attention. Maybe open a window or turn on a fan.</span></li>
      <li><span class="dot r"></span><span><strong>Red:</strong> air is poor. Time to act.</span></li>
    </ul>
  </section>

  <section id="status">
    <h2>Where things really stand</h2>
    <div class="card">
      <p>We'd rather you know this before you put money down:</p>
      <ul class="plain">
        <li><strong>Nook Air has not shipped to anyone yet.</strong> There are no customers and no reviews, because there is nothing to review yet.</li>
        <li><strong>It's been tested in a small number of homes.</strong> Prototypes have been used in the founder's apartment and a few friends' places. That's all the real-world testing so far.</li>
        <li><strong>We're aiming for spring 2027, but we can't promise a date.</strong> If that changes, we'll email you and tell you why.</li>
        <li><strong>It's a consumer indicator, not a medical or safety device.</strong> It helps you notice when the air in a room is off. It doesn't replace a smoke alarm, a carbon monoxide alarm, or professional testing.</li>
      </ul>
    </div>
  </section>

  <section id="preorder">
    <h2>How preordering works</h2>
    <ol class="steps">
      <li><strong>Today: $10 deposit.</strong> That holds your place in line.</li>
      <li><strong>The deposit is refundable.</strong> If you change your mind, ask and you get your $10 back.</li>
      <li><strong>When it ships: the rest.</strong> We charge the remaining balance (planned price $79 total, so $69) only when your Nook Air is ready to ship.</li>
      <li><strong>We keep you posted.</strong> Expect honest progress updates by email, including delays.</li>
    </ol>
    <p style="margin-top:22px"><a class="btn" href="#CHECKOUT_URL">Put down a $10 deposit</a></p>
    <p class="small">You won't be charged the balance until it ships. The planned price may change before launch. If it does, you can take your refund instead of paying it.</p>
  </section>

  <section>
    <h2>Questions</h2>
    <details><summary>Do I need an app or Wi-Fi?</summary>
      <p>No. The light on the front is the whole interface.</p></details>
    <details><summary>Is it safe to preorder something that hasn't shipped?</summary>
      <p>That's why the deposit is only $10 and refundable. You're not paying the full price up front, and the balance is charged only at shipping.</p></details>
    <details><summary>When will it ship?</summary>
      <p>We're aiming for spring 2027. It's a target, not a promise. We'll email you if the timeline moves.</p></details>
    <details><summary>How do I get my deposit back?</summary>
      <p>Email <a href="mailto:hello@example.com">hello@example.com</a> and ask. Your $10 comes back to you.</p></details>
    <details><summary>Can I rely on it as a safety alarm?</summary>
      <p>No. It's an everyday indicator. Keep working smoke and carbon monoxide alarms in your home.</p></details>
  </section>

</div></main>

<footer><div class="wrap">Nook Air is in development. Specs, design and price may change before launch.</div></footer>
</body>
</html>
```

**Approach:** The page tells people plainly that nothing has shipped, that testing so far is your apartment and a few friends' places, and that spring is a target. The reassurance comes from the small refundable deposit and the "balance only at shipping" promise, so there's no hype or invented social proof.

**Fill in or confirm before launch:**
- **Checkout link:** The buttons point to `#CHECKOUT_URL`. Replace it with your Stripe, Shopify or other payment link.
- **Refund contact:** `hello@example.com` is a placeholder. The "ask and you get your $10 back" wording also assumes you'll refund any time before shipping, so adjust it if your terms differ.
- **Price-change clause:** I added "if the price changes, you can take your refund." Delete it if you don't want to commit to that.
- **Updates promise:** The "we'll email you if the timeline moves" line is a commitment, so only keep it if you'll follow through.
- **Light thresholds:** I kept the green, yellow and red descriptions generic. If you have actual cutoffs, such as a CO2 ppm number, adding them would build more trust.
- **Safety disclaimer:** I added a "not a safety alarm" note. Keep it unless you've tested and validated the sensors for that.
