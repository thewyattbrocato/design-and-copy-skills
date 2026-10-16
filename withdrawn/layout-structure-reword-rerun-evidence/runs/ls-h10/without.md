I couldn't save the file because the Write tool is disabled in this session. The full sketch is below, so you can save it as `pricing.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Plans & Pricing – Driving School</title>
<style>
  :root {
    --bg: #f6f7f9;
    --card: #fff;
    --text: #1b2430;
    --muted: #5b6675;
    --line: #dfe3e8;
    --accent: #0a6cff;
    --accent-ink: #fff;
    --tint: #e8f1ff;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--text);
    font: 16px/1.5 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }
  header, main, footer { max-width: 480px; margin: 0 auto; padding: 0 16px; }
  header { padding-top: 24px; padding-bottom: 8px; }
  h1 { font-size: 1.6rem; line-height: 1.2; margin: 0 0 8px; }
  h2 { font-size: 1.2rem; margin: 32px 0 12px; }
  .lead { color: var(--muted); margin: 0; }

  .plan {
    position: relative;
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 14px;
    padding: 20px 16px;
    margin-bottom: 16px;
  }
  .plan.featured { border: 2px solid var(--accent); }
  .badge {
    position: absolute; top: -12px; left: 16px;
    background: var(--accent); color: var(--accent-ink);
    font-size: .75rem; font-weight: 700; letter-spacing: .04em;
    text-transform: uppercase; padding: 3px 10px; border-radius: 999px;
  }
  .plan h3 { margin: 0 0 4px; font-size: 1.15rem; }
  .hours {
    display: inline-block; background: var(--tint); color: var(--accent);
    font-size: .85rem; font-weight: 600; padding: 2px 10px; border-radius: 999px;
  }
  .price { margin: 12px 0 4px; font-size: 2rem; font-weight: 800; line-height: 1; }
  .price small { font-size: .9rem; font-weight: 500; color: var(--muted); }
  .plan p { margin: 8px 0 16px; color: var(--muted); }

  .btn {
    display: block; width: 100%; min-height: 48px; padding: 12px;
    text-align: center; text-decoration: none; font: inherit; font-weight: 700;
    border-radius: 10px; border: 2px solid var(--accent);
    color: var(--accent); background: transparent;
  }
  .featured .btn { background: var(--accent); color: var(--accent-ink); }

  .faq details {
    background: var(--card); border: 1px solid var(--line);
    border-radius: 10px; margin-bottom: 8px;
  }
  .faq summary {
    cursor: pointer; list-style: none; min-height: 48px;
    padding: 12px 40px 12px 16px; font-weight: 600; position: relative;
  }
  .faq summary::-webkit-details-marker { display: none; }
  .faq summary::after {
    content: "+"; position: absolute; right: 16px; top: 10px;
    font-size: 1.4rem; color: var(--accent);
  }
  .faq details[open] summary::after { content: "\2212"; }
  .faq details p { margin: 0; padding: 0 16px 16px; color: var(--muted); }

  footer { padding-top: 24px; padding-bottom: 32px; text-align: center; color: var(--muted); font-size: .85rem; }
</style>
</head>
<body>

<header>
  <h1>Choose your driving plan</h1>
  <p class="lead">Simple pricing. Book online in minutes.</p>
</header>

<main>
  <section aria-label="Course options" style="margin-top:24px">
    <article class="plan">
      <h3>Starter</h3>
      <span class="hours">6 hours</span>
      <div class="price">$299 <small>one-time</small></div>
      <p>Build confidence behind the wheel. Ideal for first-time drivers learning the basics.</p>
      <a class="btn" href="#book-starter">Book Starter</a>
    </article>

    <article class="plan featured">
      <span class="badge">Most popular</span>
      <h3>Standard</h3>
      <span class="hours">15 hours</span>
      <div class="price">$649 <small>one-time</small></div>
      <p>Complete lessons covering city driving, parking and road rules, with test preparation.</p>
      <a class="btn" href="#book-standard">Book Standard</a>
    </article>

    <article class="plan">
      <h3>Complete</h3>
      <span class="hours">30 hours</span>
      <div class="price">$1,199 <small>one-time</small></div>
      <p>Full program with highway and night driving, mock test and a test-day car included.</p>
      <a class="btn" href="#book-complete">Book Complete</a>
    </article>
  </section>

  <section class="faq" aria-labelledby="faq-h">
    <h2 id="faq-h">Frequently asked questions</h2>
    <details>
      <summary>Can I reschedule a lesson?</summary>
      <p>Yes. Reschedule free of charge up to 24 hours before your lesson.</p>
    </details>
    <details>
      <summary>Do I need a learner's permit first?</summary>
      <p>Yes for Standard and Complete. Starter students can get help with the permit at their first lesson.</p>
    </details>
    <details>
      <summary>Which payment methods do you accept?</summary>
      <p>Major credit and debit cards, plus split payments on Standard and Complete.</p>
    </details>
    <details>
      <summary>What if I need extra hours?</summary>
      <p>Add single hours to any plan at $55 per hour, booked right from your account.</p>
    </details>
  </section>
</main>

<footer>Prices in USD. Placeholder content.</footer>

</body>
</html>
```

**Layout**
- **Header:** a title and a one-line subtitle.
- **Plans:** three cards stacked in a single column. Each has the title, an hours pill, the price, a short description and a full-width "Book" button. The middle card (Standard) is highlighted with an accent border, a "Most popular" badge and a filled button.
- **FAQ:** four collapsible questions built on `<details>`, so they work without JavaScript. Each tap target is at least 48px tall.
- **Constraints:** the content is capped at 480px wide, uses system fonts and has no external assets. The plan names, prices, hours and FAQ answers are placeholders I made up.

If you give me write access, I'll save it to the working directory.
