I couldn't save the file because the Write tool is disabled in this session. The full single-file HTML is below, so you can save it as `pricing.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ledgerly Pricing</title>
<style>
  :root {
    --bg: #f6f7f9;
    --card: #ffffff;
    --ink: #14181f;
    --muted: #566070;
    --line: #dde1e8;
    --accent: #0b6b5c;
    --accent-dark: #084f44;
    --accent-tint: #e6f3f0;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.5;
  }
  .pricing {
    max-width: 1040px;
    margin: 0 auto;
    padding: 72px 24px 88px;
  }
  .pricing-head { text-align: center; max-width: 560px; margin: 0 auto 56px; }
  .pricing-head h2 {
    font-size: clamp(28px, 4vw, 40px);
    line-height: 1.15;
    letter-spacing: -0.02em;
    margin: 0 0 12px;
  }
  .pricing-head p { margin: 0; color: var(--muted); font-size: 18px; }

  .tiers {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    align-items: center;
  }
  .tier {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 32px 28px;
    display: flex;
    flex-direction: column;
    position: relative;
  }
  .tier.featured {
    border: 2px solid var(--accent);
    padding: 44px 28px 36px;
    box-shadow: 0 18px 40px -16px rgba(11, 107, 92, 0.35);
  }
  .badge {
    position: absolute;
    top: -14px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--accent);
    color: #fff;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.02em;
    padding: 4px 14px;
    border-radius: 999px;
    white-space: nowrap;
  }
  .tier h3 { margin: 0; font-size: 20px; }
  .tagline { margin: 4px 0 20px; color: var(--muted); font-size: 15px; }
  .price { display: flex; align-items: baseline; gap: 4px; margin-bottom: 24px; }
  .price .amount { font-size: 48px; font-weight: 700; letter-spacing: -0.03em; line-height: 1; }
  .featured .price .amount { font-size: 56px; }
  .price .per { color: var(--muted); font-size: 16px; }

  .cta {
    display: block;
    text-align: center;
    text-decoration: none;
    font-weight: 600;
    font-size: 16px;
    padding: 12px 16px;
    border-radius: 10px;
    border: 1.5px solid var(--ink);
    color: var(--ink);
    background: transparent;
    transition: background 0.15s, color 0.15s;
  }
  .cta:hover { background: var(--ink); color: #fff; }
  .featured .cta {
    background: var(--accent);
    border-color: var(--accent);
    color: #fff;
    padding: 14px 16px;
  }
  .featured .cta:hover { background: var(--accent-dark); border-color: var(--accent-dark); }
  .cta:focus-visible { outline: 3px solid #f2b705; outline-offset: 2px; }

  .features {
    list-style: none;
    margin: 28px 0 0;
    padding: 24px 0 0;
    border-top: 1px solid var(--line);
    display: grid;
    gap: 12px;
    font-size: 15px;
  }
  .features li { display: flex; gap: 10px; align-items: flex-start; }
  .features li::before {
    content: "";
    flex: none;
    width: 18px; height: 18px;
    margin-top: 2px;
    border-radius: 50%;
    background: var(--accent-tint)
      url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 18 18'%3E%3Cpath d='M5 9.5l2.6 2.6L13 6.8' fill='none' stroke='%230b6b5c' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")
      center / 18px no-repeat;
  }

  @media (max-width: 860px) {
    .tiers { grid-template-columns: 1fr; max-width: 420px; margin: 0 auto; gap: 28px; }
    .featured { order: -1; }
  }
</style>
</head>
<body>
<section class="pricing" aria-labelledby="pricing-title">
  <div class="pricing-head">
    <h2 id="pricing-title">Simple pricing for independent work</h2>
    <p>Pick the plan that fits how you work. Change or cancel anytime.</p>
  </div>

  <div class="tiers">
    <article class="tier">
      <h3>Solo</h3>
      <p class="tagline">For getting started on your own.</p>
      <div class="price"><span class="amount">$9</span><span class="per">/mo</span></div>
      <a class="cta" href="#solo" aria-label="Choose the Solo plan">Choose Solo</a>
      <ul class="features">
        <li>1 user</li>
        <li>50 invoices</li>
      </ul>
    </article>

    <article class="tier featured">
      <span class="badge">Most popular</span>
      <h3>Studio</h3>
      <p class="tagline">For growing freelance businesses.</p>
      <div class="price"><span class="amount">$24</span><span class="per">/mo</span></div>
      <a class="cta" href="#studio" aria-label="Choose the Studio plan">Choose Studio</a>
      <ul class="features">
        <li>5 users</li>
        <li>Unlimited invoices</li>
        <li>Receipt scanning</li>
      </ul>
    </article>

    <article class="tier">
      <h3>Agency</h3>
      <p class="tagline">For teams that need more reach.</p>
      <div class="price"><span class="amount">$59</span><span class="per">/mo</span></div>
      <a class="cta" href="#agency" aria-label="Choose the Agency plan">Choose Agency</a>
      <ul class="features">
        <li>Unlimited users</li>
        <li>API access</li>
        <li>Priority support</li>
      </ul>
    </article>
  </div>
</section>
</body>
</html>
```

**How Studio stands out**
- **Emphasis:** It sits in the middle and is taller than the other two. It has a green border, a soft shadow, a "Most popular" badge, a larger price, and a filled button. Solo and Agency get outline buttons.
- **Mobile:** Below 860px the tiers stack, and Studio moves to the top.

**Other details**
- **No external assets:** It uses system fonts only, and the checkmark icons are inline SVG data URIs.
- **Accessibility:** The text contrast is high, the buttons have a visible focus ring, and each button has an `aria-label`.
- **Placeholder copy:** I wrote the headline, the taglines, and the "Change or cancel anytime" line. Edit them if they don't match your terms.
- **Placeholder links:** The button links (`#solo`, `#studio`, `#agency`) need to point to your signup URLs.
