I couldn't save the file because the Write tool is disabled in this session. The full single-file HTML is below, so you can save it as `pricing.html`. I haven't opened it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ledgerly pricing</title>
<style>
  :root {
    --ink: #14211c;
    --muted: #4a5a53;
    --line: #d8dfdb;
    --bg: #f6f8f7;
    --card: #ffffff;
    --accent: #0b5d47;
    --accent-ink: #ffffff;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: var(--ink);
    background: var(--bg);
    line-height: 1.5;
  }
  .pricing { max-width: 1040px; margin: 0 auto; padding: 80px 24px; }
  .pricing h2 {
    margin: 0 0 8px;
    font-size: 2.25rem;
    line-height: 1.15;
    font-weight: 700;
    letter-spacing: -0.02em;
  }
  .pricing .lede { margin: 0 0 56px; font-size: 1.0625rem; color: var(--muted); }
  .tiers {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    align-items: stretch;
  }
  .tier {
    display: flex;
    flex-direction: column;
    padding: 32px 28px;
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 12px;
  }
  .tier.featured {
    border: 2px solid var(--accent);
    padding: 48px 28px 32px;
    box-shadow: 0 12px 32px rgba(11, 93, 71, 0.14);
    position: relative;
  }
  .badge {
    position: absolute;
    top: 16px;
    left: 28px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--accent);
  }
  .tier h3 { margin: 0; font-size: 1rem; font-weight: 600; color: var(--muted); }
  .featured h3 { color: var(--ink); }
  .price {
    margin: 12px 0 4px;
    font-size: 2.5rem;
    line-height: 1;
    font-weight: 700;
    letter-spacing: -0.02em;
  }
  .featured .price { font-size: 3.5rem; }
  .price span { font-size: 1rem; font-weight: 400; color: var(--muted); letter-spacing: 0; }
  .for { margin: 0 0 24px; font-size: 0.9375rem; color: var(--muted); }
  ul {
    list-style: none;
    margin: 0 0 32px;
    padding: 24px 0 0;
    border-top: 1px solid var(--line);
    flex: 1;
  }
  li { position: relative; padding-left: 24px; margin-bottom: 12px; font-size: 0.9375rem; }
  li::before {
    content: "";
    position: absolute;
    left: 3px;
    top: 0.35em;
    width: 6px;
    height: 11px;
    border: solid var(--accent);
    border-width: 0 2px 2px 0;
    transform: rotate(45deg);
  }
  .btn {
    display: block;
    padding: 12px 16px;
    text-align: center;
    font: inherit;
    font-weight: 600;
    text-decoration: none;
    border-radius: 8px;
    border: 1.5px solid var(--ink);
    color: var(--ink);
    background: transparent;
  }
  .btn:hover { background: var(--bg); }
  .featured .btn {
    background: var(--accent);
    border-color: var(--accent);
    color: var(--accent-ink);
    padding: 14px 16px;
  }
  .featured .btn:hover { background: #084836; }
  .btn:focus-visible { outline: 3px solid #7bb8a6; outline-offset: 2px; }
  @media (max-width: 860px) {
    .tiers { grid-template-columns: 1fr; max-width: 440px; }
    .tier.featured { order: -1; }
    .pricing { padding: 56px 20px; }
  }
</style>
</head>
<body>
<section class="pricing" aria-labelledby="pricing-title">
  <h2 id="pricing-title">Simple pricing for freelancers</h2>
  <p class="lede">Pick a plan, change it any time. Billed monthly.</p>

  <div class="tiers">
    <article class="tier">
      <h3>Solo</h3>
      <p class="price">$9<span>/mo</span></p>
      <p class="for">For one person getting started.</p>
      <ul>
        <li>1 user</li>
        <li>50 invoices</li>
      </ul>
      <a class="btn" href="#solo">Choose Solo</a>
    </article>

    <article class="tier featured">
      <span class="badge">Most popular</span>
      <h3>Studio</h3>
      <p class="price">$24<span>/mo</span></p>
      <p class="for">For a growing practice.</p>
      <ul>
        <li>5 users</li>
        <li>Unlimited invoices</li>
        <li>Receipt scanning</li>
      </ul>
      <a class="btn" href="#studio">Choose Studio</a>
    </article>

    <article class="tier">
      <h3>Agency</h3>
      <p class="price">$59<span>/mo</span></p>
      <p class="for">For teams that need more.</p>
      <ul>
        <li>Unlimited users</li>
        <li>API access</li>
        <li>Priority support</li>
      </ul>
      <a class="btn" href="#agency">Choose Agency</a>
    </article>
  </div>
</section>
</body>
</html>
```

**How Studio stands out:**
- **Size and weight:** Its price is the largest thing in the section (3.5rem against 2.5rem for the others).
- **Structure:** Its card has a green border, a soft shadow and extra top padding, and it carries a "Most popular" label. The label is text, so the emphasis doesn't depend on color alone.
- **Action:** Its button is the only solid one. Solo and Agency get outline buttons.

**Other layout choices:**
- Everything else is quiet. The tier names and "/mo" are muted, and the bullets use plain ticks with no icons or gradients.
- The page uses system fonts only, with no external assets.
- On narrow screens the cards stack, and Studio moves to the top.

I added a short tagline under each price and a "Billed monthly" line under the heading. Delete them if you'd rather not have them.
