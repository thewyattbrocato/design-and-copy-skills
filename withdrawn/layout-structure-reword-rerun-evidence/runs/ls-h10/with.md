I couldn't save the file because the Write tool is disabled in this session. The full page is below, so you can save it as `pricing.html`.

The layout is one column with a 30rem cap and 20px side margins. The three courses stack as equal cards with the same order in each: title, hours, price, description, button. Standard is outlined with a "Most popular" badge, as the one loud card. The FAQ sits on a white band below, with four questions that open and close using `<details>`, so it needs no JavaScript.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Course plans and pricing · Roadwise Driving School</title>
<style>
  :root {
    --ink: #1b2430;
    --muted: #55606e;
    --line: #d9dee5;
    --bg: #f6f7f9;
    --card: #fff;
    --accent: #0b5fff;
    --accent-ink: #fff;
    --pad: 20px;
  }
  * { box-sizing: border-box; }
  html { -webkit-text-size-adjust: 100%; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font: 16px/1.5 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  }
  .wrap { max-width: 30rem; margin: 0 auto; padding: 0 var(--pad); }

  header.top { background: var(--card); border-bottom: 1px solid var(--line); }
  header.top .wrap { display: flex; align-items: center; justify-content: space-between; height: 56px; }
  .brand { font-weight: 700; letter-spacing: .01em; }
  .link { color: var(--accent); font-weight: 600; text-decoration: none; font-size: .9375rem; }

  .intro { padding: 32px var(--pad) 20px; }
  h1 { margin: 0 0 8px; font-size: 1.75rem; line-height: 1.2; }
  .intro p { margin: 0; color: var(--muted); }

  .plans { display: grid; gap: 16px; padding-bottom: 40px; }
  .plan { background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: 20px; }
  .plan.featured { border: 2px solid var(--accent); padding: 19px; }
  .badge {
    display: inline-block; margin-bottom: 10px; padding: 2px 10px; border-radius: 99px;
    background: var(--accent); color: var(--accent-ink);
    font-size: .75rem; font-weight: 700; text-transform: uppercase; letter-spacing: .05em;
  }
  .plan h2 { margin: 0; font-size: 1.25rem; line-height: 1.25; }
  .hours { margin: 2px 0 0; color: var(--muted); font-size: .9375rem; }
  .price { margin: 16px 0 12px; font-size: 2.25rem; font-weight: 700; line-height: 1; }
  .price small { font-size: .875rem; font-weight: 400; color: var(--muted); }
  .plan p.desc { margin: 0 0 18px; }
  .btn {
    display: block; text-align: center; text-decoration: none;
    min-height: 48px; line-height: 48px; border-radius: 10px;
    font-weight: 600; border: 1px solid var(--ink); color: var(--ink);
  }
  .featured .btn { background: var(--accent); border-color: var(--accent); color: var(--accent-ink); }

  .faq { background: var(--card); border-top: 1px solid var(--line); padding: 32px 0 40px; }
  .faq h2 { margin: 0 0 8px; font-size: 1.375rem; }
  details { border-bottom: 1px solid var(--line); }
  summary {
    list-style: none; cursor: pointer;
    display: flex; justify-content: space-between; gap: 16px; align-items: center;
    min-height: 56px; padding: 12px 0; font-weight: 600;
  }
  summary::-webkit-details-marker { display: none; }
  summary::after { content: "+"; font-size: 1.5rem; font-weight: 400; color: var(--muted); }
  details[open] summary::after { content: "\2212"; }
  details p { margin: 0 0 16px; color: var(--muted); }

  footer { padding: 24px 0 40px; text-align: center; color: var(--muted); font-size: .875rem; }
</style>
</head>
<body>

<header class="top">
  <div class="wrap">
    <span class="brand">Roadwise</span>
    <a class="link" href="#">Log in</a>
  </div>
</header>

<main>
  <section class="intro wrap">
    <h1>Pick a course, book your first lesson</h1>
    <p>Fixed prices, licensed instructors, and no booking fees. Choose the amount of driving time that fits you.</p>
  </section>

  <section class="plans wrap" aria-label="Courses">
    <article class="plan">
      <h2>Starter</h2>
      <p class="hours">10 hours behind the wheel</p>
      <p class="price">$449 <small>total</small></p>
      <p class="desc">Car controls, junctions and basic road rules. Best if you already have some practice with family or friends.</p>
      <a class="btn" href="#">Book Starter</a>
    </article>

    <article class="plan featured">
      <span class="badge">Most popular</span>
      <h2>Standard</h2>
      <p class="hours">20 hours behind the wheel</p>
      <p class="price">$849 <small>total</small></p>
      <p class="desc">Complete path from first lesson to test day, including roundabouts, parking, motorway driving and a mock test.</p>
      <a class="btn" href="#">Book Standard</a>
    </article>

    <article class="plan">
      <h2>Intensive</h2>
      <p class="hours">30 hours over 2 weeks</p>
      <p class="price">$1,249 <small>total</small></p>
      <p class="desc">Daily lessons for a fast track to your test. Includes the test booking and use of our car on the day.</p>
      <a class="btn" href="#">Book Intensive</a>
    </article>
  </section>

  <section class="faq">
    <div class="wrap">
      <h2>Questions</h2>
      <details>
        <summary>Which course should I choose?</summary>
        <p>New drivers usually pick Standard. Choose Starter if you have already practised, or Intensive if you need your licence quickly.</p>
      </details>
      <details>
        <summary>Can I reschedule a lesson?</summary>
        <p>Yes, free of charge up to 24 hours before the lesson. Later changes may cost half the lesson fee.</p>
      </details>
      <details>
        <summary>Is the test fee included?</summary>
        <p>Only in Intensive. For Starter and Standard, you pay the test fee directly to the licensing authority.</p>
      </details>
      <details>
        <summary>Can I pay in instalments?</summary>
        <p>Yes. Split any course into three equal monthly payments at checkout, with no extra interest.</p>
      </details>
    </div>
  </section>
</main>

<footer>© Roadwise Driving School</footer>

</body>
</html>
```

I haven't opened it in a browser, so the layout is untested. The school name, prices, hours and FAQ answers are placeholders I made up, so swap in your real ones.
