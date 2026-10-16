I couldn't save the page as a file because the Write tool is disabled in this session. The full page is below as a single self-contained HTML file. Save it as `index.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nook Air – Preorder a pocket-sized air quality monitor</title>
<meta name="description" content="Nook Air is a pocket-sized air quality monitor for renters. It reads fine particles and CO2 and shows a green, yellow or red light. No app. Preorder for a $10 refundable deposit.">
<style>
  :root { --ink:#1d2421; --muted:#5b6761; --bg:#fbfaf7; --card:#fff; --line:#e4e1d8; --accent:#1f5f4a; --green:#2e9e5b; --yellow:#e5b823; --red:#d64545; }
  * { box-sizing: border-box; }
  body { margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; color:var(--ink); background:var(--bg); line-height:1.6; }
  .wrap { max-width:720px; margin:0 auto; padding:0 20px; }
  header.top { padding:20px 0; }
  .brand { font-weight:700; letter-spacing:.02em; }
  .hero { padding:40px 0 32px; }
  h1 { font-size:clamp(2rem,6vw,3rem); line-height:1.15; margin:0 0 16px; }
  h2 { font-size:1.4rem; margin:0 0 12px; }
  p { margin:0 0 14px; }
  .lede { font-size:1.2rem; color:var(--muted); }
  .lights { display:flex; gap:10px; margin:24px 0; }
  .lights span { width:22px; height:22px; border-radius:50%; display:inline-block; }
  .g{background:var(--green)} .y{background:var(--yellow)} .r{background:var(--red)}
  .btn { display:inline-block; background:var(--accent); color:#fff; text-decoration:none; padding:14px 26px; border-radius:10px; font-weight:600; font-size:1.05rem; }
  .btn:hover,.btn:focus { background:#174a39; }
  .fine { font-size:.92rem; color:var(--muted); margin-top:12px; }
  section { padding:28px 0; border-top:1px solid var(--line); }
  .card { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:20px 22px; }
  ul.plain { padding-left:20px; margin:0 0 14px; }
  ul.plain li { margin-bottom:8px; }
  table { width:100%; border-collapse:collapse; }
  td { padding:10px 0; border-bottom:1px solid var(--line); vertical-align:top; }
  td:first-child { width:42%; font-weight:600; }
  tr:last-child td { border-bottom:0; }
  details { border-bottom:1px solid var(--line); padding:12px 0; }
  details:last-child { border-bottom:0; }
  summary { cursor:pointer; font-weight:600; }
  details p { margin:10px 0 0; color:var(--muted); }
  footer { padding:32px 0 48px; color:var(--muted); font-size:.9rem; border-top:1px solid var(--line); }
  a { color:var(--accent); }
</style>
</head>
<body>

<header class="top"><div class="wrap"><span class="brand">Nook Air</span></div></header>

<main>
<div class="wrap">

  <div class="hero">
    <h1>Know if the air in your place is okay. At a glance.</h1>
    <p class="lede">Nook Air is a pocket-sized air quality monitor made for renters. It measures fine particles and CO2 and shows the result as a green, yellow or red light on the front. No app, no account, no drilling into walls.</p>
    <div class="lights" aria-label="Green, yellow and red status lights"><span class="g"></span><span class="y"></span><span class="r"></span></div>
    <a class="btn" href="#CHECKOUT_LINK">Preorder for a $10 refundable deposit</a>
    <p class="fine">Planned price $79. Pay $10 now, the rest only when it ships.</p>
  </div>

  <section>
    <h2>How it works</h2>
    <ul class="plain">
      <li><strong>It measures two things:</strong> fine particles (the tiny stuff from cooking, candles, traffic and smoke) and CO2 (a sign a room needs fresh air).</li>
      <li><strong>It shows one light.</strong> Green, yellow or red on the front. Glance at it and you know.</li>
      <li><strong>It goes where you do.</strong> Set it on a shelf or clip it to a bag.</li>
      <li><strong>No app needed.</strong> Turn it on and read the light.</li>
    </ul>
  </section>

  <section>
    <h2>Where we are, honestly</h2>
    <div class="card">
      <p>Nook Air is not in production yet and nothing has shipped. So far, working prototypes have been used in my own apartment and a few friends' homes. That's the whole track record, and I'd rather you know it before you put money down.</p>
      <p>I'm building this because I rent, and I wanted a simple way to tell when my place needed airing out, without a dashboard or a subscription.</p>
      <p style="margin-bottom:0">Details may change between prototype and final product. I'll tell you if they do.</p>
    </div>
  </section>

  <section>
    <h2>What preordering means</h2>
    <table>
      <tr><td>Today</td><td>You pay a <strong>$10 deposit</strong>. It's refundable.</td></tr>
      <tr><td>When it ships</td><td>The remaining balance (planned $79 total, so $69) is charged, and Nook Air is sent to you.</td></tr>
      <tr><td>Timing</td><td>We're aiming for <strong>spring 2027</strong>. That's a target, not a promise. I'll email you with real updates, including if it slips.</td></tr>
      <tr><td>Changed your mind?</td><td>Ask for your deposit back and you'll get it. See the refund details below.</td></tr>
    </table>
  </section>

  <section>
    <h2>Questions</h2>
    <details>
      <summary>Is the deposit really refundable?</summary>
      <p>Yes. If you change your mind before your order ships, email <a href="mailto:EMAIL_PLACEHOLDER">EMAIL_PLACEHOLDER</a> and your $10 goes back to you. [CONFIRM: refund window and how long it takes to reach your card.]</p>
    </details>
    <details>
      <summary>When will I be charged the rest?</summary>
      <p>Only when your Nook Air is ready to ship. You'll get an email before that happens. [CONFIRM: how much notice.]</p>
    </details>
    <details>
      <summary>Will it really ship in spring?</summary>
      <p>That's the goal, but I can't promise a date. Small hardware projects run into delays. If the timeline changes you'll hear it from me directly, and you can take your deposit back at any point before shipping.</p>
    </details>
    <details>
      <summary>Do I need an app or Wi-Fi?</summary>
      <p>No. The light on the front is the whole interface.</p>
    </details>
    <details>
      <summary>Is it a medical or safety device?</summary>
      <p>No. Nook Air is a simple indicator to help you decide when to open a window or run a fan. It is not a medical device, and it is not a smoke or carbon monoxide alarm. Keep your existing alarms.</p>
    </details>
    <details>
      <summary>Will the price change?</summary>
      <p>$79 is the planned price. If it has to change, I'll tell you before charging the balance, and you can cancel for a full deposit refund.</p>
    </details>
  </section>

  <section style="text-align:center">
    <h2>Want one?</h2>
    <p>$10 now. Refundable. The rest only when it ships.</p>
    <a class="btn" href="#CHECKOUT_LINK">Preorder Nook Air</a>
  </section>

</div>
</main>

<footer>
  <div class="wrap">Questions? <a href="mailto:EMAIL_PLACEHOLDER">EMAIL_PLACEHOLDER</a> &middot; Nook Air is an early-stage product.</div>
</footer>

</body>
</html>
```

**To fill in before publishing**
- Replace `#CHECKOUT_LINK` with your payment link and `EMAIL_PLACEHOLDER` with a real contact address.
- Two `[CONFIRM: …]` notes mark things I don't know. They are the refund window and how much notice you'll give before charging the balance. Replace them with real answers, because they matter most for trust.

**Choices I made that you should check**
- **Spring date:** I wrote "spring 2027" and labeled it a target, not a promise. Change it if you meant something else.
- **Refund promises:** The page says people can get the deposit back any time before it ships, including if the date or price changes. That's more generous than "refundable" alone, and I thought it would help people feel safe. Only keep it if you'll honor it.
- **Prototype history:** I described it as only your apartment and friends' homes, with no reviews, accuracy numbers or testing claims. I invented no specs, sensor names or light thresholds. If you have real ones, add them.
- **Safety disclaimer:** The FAQ says it isn't a medical device or a smoke or CO alarm. I added that because the light could be mistaken for a safety signal. Keep it.
- **Wi-Fi:** The "no Wi-Fi" answer assumes the device works fully on its own. Correct it if it doesn't.
