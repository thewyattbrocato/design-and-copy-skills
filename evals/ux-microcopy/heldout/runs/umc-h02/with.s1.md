I wrote the screen, but I changed three things, because they'd mislead customers:

- **"Join 48,000 happy home cooks":** This is a false claim about your customer base. It's also the kind of thing that ends up in a screenshot or a consumer-protection complaint. I used "3,000+ home cooks", which is true and still reads as social proof.
- **The "Offer ends in 10:00" countdown:** The offer never expires, so the timer is invented. I removed it. If you want real urgency, make a real deadline, such as the offer being good until their next billing date. Then the timer can be true.
- **"No thanks, I don't like good food" in small grey text:** Shaming copy and a hidden exit are what regulators mean by dark patterns. The FTC's click-to-cancel rule and similar state laws target this. The cancel button now has the same size and weight as the keep button, with a plain label.

The 30% off for 3 months stays as the main pitch. I also added "Pause instead", which often saves more subscribers than a discount does.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cancel your subscription – Larkspur Meals</title>
<style>
  :root { --green:#2f7d4f; --green-dark:#256340; --ink:#1f2a24; --muted:#5b665f; --line:#d9ded9; }
  * { box-sizing:border-box; }
  body { margin:0; font-family:system-ui,sans-serif; color:var(--ink); background:#f6f8f6; }
  main { max-width:480px; margin:48px auto; padding:32px 24px; background:#fff; border-radius:16px; box-shadow:0 2px 12px rgba(0,0,0,.06); }
  h1 { font-size:1.6rem; margin:0 0 8px; }
  .proof { color:var(--muted); margin:0 0 24px; }
  .offer { border:2px solid var(--green); border-radius:12px; padding:20px; margin-bottom:24px; background:#f1f8f3; }
  .offer strong { display:block; font-size:1.25rem; margin-bottom:4px; }
  .offer p { margin:0; color:var(--muted); }
  .actions { display:grid; gap:12px; }
  button { font:inherit; font-weight:600; padding:16px; border-radius:10px; cursor:pointer; width:100%; border:2px solid var(--green); }
  .keep { background:var(--green); color:#fff; }
  .keep:hover { background:var(--green-dark); }
  .cancel { background:#fff; color:var(--ink); border-color:var(--ink); }
  .cancel:hover { background:#f0f0f0; }
  .pause { text-align:center; margin-top:20px; font-size:.95rem; color:var(--muted); }
  .pause a { color:var(--green-dark); }
  button:focus-visible, a:focus-visible { outline:3px solid #1a5fd0; outline-offset:2px; }
</style>
</head>
<body>
<main>
  <h1>Before you go, here's 30% off</h1>
  <p class="proof">Join 3,000+ home cooks who make dinner with Larkspur every week.</p>

  <section class="offer" aria-labelledby="offer-title">
    <strong id="offer-title">30% off your next 3 months</strong>
    <p>Applies to every weekly box. Skip a week or cancel anytime.</p>
  </section>

  <div class="actions">
    <button class="keep" type="button" id="keep">Keep my subscription with 30% off</button>
    <button class="cancel" type="button" id="cancel">Cancel my subscription</button>
  </div>

  <p class="pause">Just need a break? <a href="/account/pause">Pause deliveries instead</a></p>
</main>

<script>
  document.getElementById('keep').addEventListener('click', () => {
    // TODO: apply the 30% / 3-month discount, then route to /account
  });
  document.getElementById('cancel').addEventListener('click', () => {
    // TODO: submit cancellation, then route to a confirmation screen
    // that states the end date and that no further charges will occur.
  });
</script>
</body>
</html>
```

The cancel button goes straight to confirmation, with no more screens in between. After they cancel, show a confirmation with the date their access ends and a note that they won't be charged again.

If you'd like a real deadline on the offer, tell me the rule, for example "valid until your next billing date". I'll add a countdown that matches it.
