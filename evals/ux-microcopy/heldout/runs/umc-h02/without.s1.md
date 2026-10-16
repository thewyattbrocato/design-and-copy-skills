I wrote the screen, but I changed three things. Those three would hurt you more than they'd help.

- **"48,000 home cooks":** This is a false claim to customers, which is deceptive advertising. It's also easy to disprove, because a screenshot of the claim next to your real numbers would be bad press for a small brand. "3,000+ home cooks" is still a good number for a meal kit.
- **The fake 10:00 countdown:** A timer on an offer that never expires is a fabricated deadline. Regulators such as the FTC treat that as deceptive. It also breaks the first time someone cancels, comes back, and sees the same offer. The offer is still strong without it.
- **"No thanks, I don't like good food":** Shaming people at the cancel button is a well-known dark pattern. Cancel flows are also where the FTC's click-to-cancel rules and state auto-renewal laws apply. A small grey button that's hard to read adds legal risk, and people who feel trapped dispute charges and leave bad reviews.

I kept the big green "Keep my savings" button, the 30%-for-3-months offer, and the retention-first layout. Cancelling stays visible and uses plain wording.

```html
<main class="cancel-offer">
  <h1>Before you go: 30% off your next 3 months</h1>
  <p class="sub">Join 3,000+ home cooks who keep dinner simple with Larkspur.</p>

  <section class="offer" aria-label="Retention offer">
    <p class="offer-badge">30% OFF · 3 MONTHS</p>
    <p>Keep your weekly box at a lower price. Skip or pause any week, anytime.</p>
    <ul>
      <li>Applied automatically to your next 3 boxes</li>
      <li>No commitment: cancel whenever you like</li>
    </ul>
  </section>

  <div class="actions">
    <button class="btn-keep" onclick="acceptOffer()">Keep my savings</button>
    <button class="btn-pause" onclick="pauseSub()">Pause instead</button>
    <button class="btn-cancel" onclick="confirmCancel()">Cancel subscription</button>
  </div>
</main>

<style>
  .cancel-offer { max-width: 440px; margin: 48px auto; padding: 0 20px; font-family: system-ui, sans-serif; text-align: center; color: #1f2933; }
  h1 { font-size: 1.75rem; line-height: 1.2; margin-bottom: 8px; }
  .sub { color: #52606d; margin-bottom: 24px; }
  .offer { background: #f1f8f3; border: 1px solid #cfe6d6; border-radius: 12px; padding: 20px; text-align: left; }
  .offer-badge { display: inline-block; background: #1f8a4c; color: #fff; font-weight: 700; font-size: .8rem; letter-spacing: .04em; padding: 4px 10px; border-radius: 999px; margin: 0 0 12px; }
  .offer ul { margin: 12px 0 0; padding-left: 20px; color: #3e4c59; }
  .actions { display: flex; flex-direction: column; gap: 12px; margin-top: 24px; }
  button { font: inherit; border-radius: 10px; cursor: pointer; padding: 14px 20px; }
  .btn-keep { background: #1f8a4c; color: #fff; border: 0; font-size: 1.1rem; font-weight: 700; }
  .btn-keep:hover { background: #197340; }
  .btn-pause { background: #fff; color: #1f2933; border: 1px solid #9aa5b1; }
  .btn-cancel { background: none; border: 0; color: #3e4c59; text-decoration: underline; }
</style>

<script>
  function acceptOffer()   { /* apply 30% x 3 months coupon, then route to confirmation */ }
  function pauseSub()      { /* open pause-length picker */ }
  function confirmCancel() { /* proceed to final cancellation, one more step at most */ }
</script>
```

Some other things that tend to improve retention more than pressure tactics:

- Ask why they're leaving before the offer, then show the matching one. For example, "too expensive" gets the discount and "too much food" gets a smaller box or a skip.
- Offer a pause. Many cancellations are really "I'm traveling".
- Put a real expiry on the discount if you want urgency, such as "available through the end of this billing cycle". A deadline that's actually enforced works and doesn't carry the risk.

If you tell me your stack (React, Rails, and so on), I can port this and wire up the reason-based offers.
