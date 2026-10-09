I couldn't save the file because the Write tool is disabled in this session. The full page is below, so you can save it as `pricing.html`. I haven't opened it in a browser.

**Layout, top to bottom (single column, capped at 30rem):**
1. **Top bar.** The brand sits on the left edge and a "Questions?" link on the right, both on the same margin as the content.
2. **Intro.** A headline and one sentence say what this is, so the first plan appears without much scrolling.
3. **Three plan cards.** Each has a title, then hours and price on one row, then a short description and a full-width button. Starter, Full Licence and Test Ready are stacked, and Full Licence is the only dark, loud card.
4. **FAQ.** Four tap-to-open questions in a plain ruled list rather than cards, so it reads calmer than the plans.
5. **Closing prompt.** A "Talk to an instructor" button for anyone who can't pick a course.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Plans and pricing · Roadwise Driving School</title>
<style>
  :root {
    --ink: #17202a;
    --muted: #5a6672;
    --paper: #fbfaf7;
    --card: #ffffff;
    --line: #e2dfd7;
    --accent: #0b5fff;
    --accent-ink: #ffffff;
    --dark: #14213d;
    --margin: 1.25rem;
  }
  * { box-sizing: border-box; }
  html { -webkit-text-size-adjust: 100%; }
  body {
    margin: 0;
    background: var(--paper);
    color: var(--ink);
    font: 1rem/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }
  .wrap { max-width: 30rem; margin: 0 auto; padding: 0 var(--margin); }

  /* Top bar: brand on the shared left edge, one action on the right */
  .bar { border-bottom: 1px solid var(--line); }
  .bar .wrap { display: flex; align-items: center; justify-content: space-between; min-height: 3.5rem; }
  .brand { font-weight: 700; letter-spacing: -0.01em; }
  .bar a { color: var(--accent); font-weight: 600; text-decoration: none; padding: 0.75rem 0; }

  /* First screen: what this is, what to do */
  .intro { padding: 2rem 0 1.5rem; }
  .intro h1 { font-size: 2rem; line-height: 1.15; letter-spacing: -0.02em; margin: 0 0 0.75rem; }
  .intro p { margin: 0; color: var(--muted); }

  /* Plans */
  .plans { display: grid; gap: 1rem; padding-bottom: 2.5rem; }
  .plan {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 0.75rem;
    padding: 1.25rem;
  }
  .plan h2 { font-size: 1.25rem; margin: 0; letter-spacing: -0.01em; }
  .plan .meta { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; margin: 0.75rem 0; }
  .plan .meta div { margin: 0; }
  .plan dt { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); }
  .plan dd { margin: 0; }
  .hours { font-size: 1rem; font-weight: 600; }
  .price { font-size: 2rem; font-weight: 700; letter-spacing: -0.02em; line-height: 1; }
  .plan p { margin: 0 0 1.25rem; color: var(--muted); }
  .btn {
    display: flex; align-items: center; justify-content: center;
    min-height: 3rem; border-radius: 0.5rem;
    font-weight: 600; text-decoration: none;
    border: 1.5px solid var(--accent); color: var(--accent);
  }

  /* The one loud plan */
  .plan.featured { background: var(--dark); border-color: var(--dark); color: #fff; }
  .plan.featured p, .plan.featured dt { color: #c3cadb; }
  .plan.featured .btn { background: var(--accent); border-color: var(--accent); color: var(--accent-ink); }
  .tag {
    display: inline-block; margin-bottom: 0.5rem;
    font-size: 0.75rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;
    background: #ffd166; color: #3a2b00; padding: 0.15rem 0.5rem; border-radius: 99rem;
  }

  /* FAQ: calm, flat list on a ruled edge, no cards */
  .faq { border-top: 1px solid var(--line); padding: 2rem 0 1rem; }
  .faq h2 { font-size: 1.5rem; letter-spacing: -0.01em; margin: 0 0 0.5rem; }
  details { border-bottom: 1px solid var(--line); }
  summary {
    list-style: none; cursor: pointer;
    display: flex; justify-content: space-between; align-items: center; gap: 1rem;
    min-height: 3.5rem; padding: 0.75rem 0; font-weight: 600;
  }
  summary::-webkit-details-marker { display: none; }
  summary::after { content: "+"; font-size: 1.5rem; font-weight: 400; color: var(--accent); }
  details[open] summary::after { content: "\2212"; }
  details p { margin: 0 0 1rem; color: var(--muted); }

  /* Closing prompt */
  .close { padding: 1.5rem 0 3rem; }
  .close p { margin: 0 0 1rem; font-weight: 600; font-size: 1.125rem; }
  .close .btn { background: var(--accent); color: var(--accent-ink); }

  :focus-visible { outline: 3px solid #ffb703; outline-offset: 2px; }
</style>
</head>
<body>

<header class="bar">
  <div class="wrap">
    <span class="brand">Roadwise</span>
    <a href="#faq">Questions?</a>
  </div>
</header>

<main class="wrap">

  <section class="intro">
    <h1>Pick a course, book your first lesson.</h1>
    <p>Lessons with a licensed instructor in a dual-control car. Pay per course, reschedule free up to 24 hours before.</p>
  </section>

  <section class="plans" aria-label="Courses">

    <article class="plan">
      <h2>Starter</h2>
      <dl class="meta">
        <div><dt>Time</dt><dd class="hours">5 hours</dd></div>
        <div><dt>Price</dt><dd class="price">$275</dd></div>
      </dl>
      <p>For first-timers. Car controls, moving off, steering and quiet-street practice.</p>
      <a class="btn" href="#book-starter">Book Starter</a>
    </article>

    <article class="plan featured">
      <span class="tag">Most popular</span>
      <h2>Full Licence</h2>
      <dl class="meta">
        <div><dt>Time</dt><dd class="hours">20 hours</dd></div>
        <div><dt>Price</dt><dd class="price">$890</dd></div>
      </dl>
      <p>Everything from first lesson to test day, including junctions, roundabouts, parking and a mock test.</p>
      <a class="btn" href="#book-full">Book Full Licence</a>
    </article>

    <article class="plan">
      <h2>Test Ready</h2>
      <dl class="meta">
        <div><dt>Time</dt><dd class="hours">8 hours</dd></div>
        <div><dt>Price</dt><dd class="price">$420</dd></div>
      </dl>
      <p>Already driving? Sharpen weak spots on real test routes and take the test in our car.</p>
      <a class="btn" href="#book-test">Book Test Ready</a>
    </article>

  </section>

  <section class="faq" id="faq">
    <h2>Common questions</h2>

    <details>
      <summary>Do I need a learner permit first?</summary>
      <p>Yes. Bring your permit to the first lesson. If you don't have one yet, we can point you to how to apply.</p>
    </details>

    <details>
      <summary>Can I change or cancel a lesson?</summary>
      <p>Free to reschedule or cancel up to 24 hours before. Later changes lose that lesson's hour.</p>
    </details>

    <details>
      <summary>Is the driving test fee included?</summary>
      <p>Only in Test Ready, which covers the car hire on test day. The official test fee is paid separately.</p>
    </details>

    <details>
      <summary>Can I pay in instalments?</summary>
      <p>Full Licence can be split into two or four payments at no extra cost. Pick it at checkout.</p>
    </details>
  </section>

  <section class="close">
    <p>Not sure which course fits?</p>
    <a class="btn" href="#contact">Talk to an instructor</a>
  </section>

</main>

</body>
</html>
```

**Design notes:**
- **Content is placeholder.** The prices, course names and FAQ answers are plausible stand-ins, so swap in your real ones.
- **Prices are the largest text on each card.** People compare courses by price and hours first, so those two sit on one row above the description.
- **Full Licence is the only emphasised plan.** It has a dark card, a "Most popular" tag and a filled button. The other two use outlined buttons.
- **Phone-friendly details.** Buttons and FAQ rows are at least 3rem tall for easy tapping. Text sizes use `rem`, so system font scaling works. Longer titles or translated text will wrap without breaking the cards.
- **The FAQ uses native `<details>`.** It needs no JavaScript and works with a keyboard.

If you'd like me to write it to disk, re-enable Write or tell me another place to put it.
