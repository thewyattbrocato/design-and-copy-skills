I wrote the screen, but I changed three things. Those three are deceptive to customers, and they're also legal risks. The FTC treats false claims and manipulative cancel flows as violations, and several states' auto-renewal laws and the EU's rules on dark patterns do too.

- **"48,000 happy home cooks":** This is a made-up number. I used the real figure, and the copy still works.
- **The "Offer ends in 10:00" countdown:** The deal never expires, so the timer is fake urgency. I replaced it with a true statement about the offer.
- **"No thanks, I don't like good food":** This is confirmshaming. I made the cancel button clearly visible and neutral.

The offer stays prominent, and "Keep my savings" is still the big green button.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Before you go – Larkspur Meals</title>
<style>
  body { margin: 0; font-family: system-ui, sans-serif; background: #f7f5f0; color: #1f2a24; }
  .card { max-width: 480px; margin: 48px auto; padding: 32px; background: #fff;
          border-radius: 16px; box-shadow: 0 4px 24px rgba(0,0,0,.08); text-align: center; }
  h1 { font-size: 28px; margin: 0 0 8px; }
  .sub { color: #5b665f; margin: 0 0 24px; }
  .offer { border: 2px solid #2e9e5b; background: #f0faf4; border-radius: 12px; padding: 20px; margin-bottom: 24px; }
  .offer .big { font-size: 40px; font-weight: 800; color: #1f7a45; line-height: 1; }
  .offer .detail { margin-top: 8px; font-size: 15px; }
  .fine { font-size: 13px; color: #5b665f; margin-top: 8px; }
  .btn { display: block; width: 100%; box-sizing: border-box; padding: 16px; border-radius: 10px;
         font-size: 17px; font-weight: 600; cursor: pointer; text-decoration: none; }
  .keep { background: #2e9e5b; color: #fff; border: 0; font-size: 19px; padding: 18px; }
  .keep:hover { background: #268a4e; }
  .cancel { background: #fff; color: #1f2a24; border: 1px solid #b9c0bb; margin-top: 12px; }
  .cancel:hover { background: #f2f4f2; }
  .proof { margin-top: 24px; font-size: 14px; color: #5b665f; }
</style>
</head>
<body>
  <main class="card">
    <h1>Before you go, how about a break from full price?</h1>
    <p class="sub">Join 3,000 home cooks who make dinner easier with Larkspur.</p>

    <section class="offer" aria-label="Retention offer">
      <div class="big">30% off</div>
      <div class="detail">your next 3 months of deliveries</div>
      <div class="fine">Applies automatically. After 3 months your plan returns to its regular price. Cancel anytime.</div>
    </section>

    <form method="post" action="/subscription/keep-offer">
      <button class="btn keep" type="submit">Keep my savings</button>
    </form>

    <a class="btn cancel" href="/subscription/cancel/confirm">Continue to cancel</a>

    <p class="proof">Prefer to pause instead? <a href="/subscription/pause">Skip up to 8 weeks</a>.</p>
  </main>
</body>
</html>
```

Some notes on the design:

- **Real urgency:** If you want a deadline, make the offer actually expire, for example "Available until you leave this page" or a real 7-day window enforced server-side. Then a countdown is honest and will probably convert better, because customers learn the offer is real.
- **Pause link:** A pause option often saves more cancellations than a discount, and it's cheap to add.
- **Equal weight on cancel:** Keep "Continue to cancel" as easy to find as the keep button. Most click-to-cancel rules require that, and it reduces angry chargebacks and bad reviews.

I can port this to React, SwiftUI, or whatever stack Larkspur uses. I can also add a "why are you leaving?" step that changes the offer, such as a pause for travel or a cheaper plan for price complaints.
