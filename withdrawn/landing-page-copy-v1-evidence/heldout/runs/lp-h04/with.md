I couldn't save the page to a file because the Write tool is disabled in this session. Below is the full page as one HTML file. Copy it into `index.html` and it will work as is.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Orrin Valley Physiotherapy | Back, shoulder and knee care on Alder Street</title>
<meta name="description" content="Physiotherapy for back, shoulder and knee problems. 60-minute first visit, $95. Book online. Alder Street, next to the pharmacy.">
<style>
  :root { --ink:#1d2b2a; --muted:#52615f; --accent:#1f6f66; --bg:#f6f9f8; --line:#d9e4e2; }
  * { box-sizing: border-box; }
  body { margin:0; font:18px/1.6 system-ui, -apple-system, "Segoe UI", sans-serif; color:var(--ink); background:#fff; }
  .wrap { max-width:720px; margin:0 auto; padding:0 24px; }
  section { padding:56px 0; border-bottom:1px solid var(--line); }
  section.alt { background:var(--bg); }
  h1 { font-size:2.4rem; line-height:1.15; margin:0 0 16px; }
  h2 { font-size:1.6rem; line-height:1.25; margin:0 0 16px; }
  h3 { font-size:1.1rem; margin:24px 0 4px; }
  p { margin:0 0 16px; }
  .brand { font-weight:700; letter-spacing:.02em; color:var(--accent); padding:20px 0; }
  .sub { font-size:1.2rem; color:var(--muted); }
  .btn { display:inline-block; background:var(--accent); color:#fff; text-decoration:none; font-weight:600; padding:14px 28px; border-radius:6px; }
  .btn:hover { background:#17564f; }
  .note { font-size:.9rem; color:var(--muted); margin-top:12px; }
  ul { padding-left:20px; margin:0 0 16px; }
  li { margin-bottom:8px; }
  .price { font-size:2.2rem; font-weight:700; color:var(--accent); margin:0; }
  .placeholder { border:2px dashed var(--line); padding:16px; color:var(--muted); border-radius:6px; }
  footer { padding:32px 0; color:var(--muted); font-size:.95rem; }
</style>
</head>
<body>

<header class="wrap">
  <div class="brand">Orrin Valley Physiotherapy</div>
</header>

<section>
  <div class="wrap">
    <h1>Physiotherapy for back, shoulder and knee pain, with an hour to work out what's going on.</h1>
    <p class="sub">Your first visit with one of our two physiotherapists is 60 minutes and $95. Book online, and we're on Alder Street next to the pharmacy.</p>
    <a class="btn" href="#book">Book your first visit</a>
    <p class="note">60 minutes · $95 · Online booking open</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2>We focus on three areas: back, shoulder and knee.</h2>
    <h3>Back pain</h3>
    <p>Pain that comes on when you sit, lift, bend or sleep, whether it started suddenly or has been building for a while.</p>
    <h3>Shoulder problems</h3>
    <p>Pain or stiffness when you reach, carry or lift your arm, or when you lie on that side at night.</p>
    <h3>Knee problems</h3>
    <p>Pain on stairs, when you walk, run or squat, or after an injury that hasn't settled.</p>
    <p class="note">Not sure yours fits? Book a visit and we'll tell you honestly whether we can help or whether you should see someone else.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>The first visit is 60 minutes, so nobody rushes your story.</h2>
    <p>You get a full hour with your physiotherapist. We use it to:</p>
    <ul>
      <li>Listen to what's wrong, when it started and what makes it better or worse.</li>
      <li>Examine the area and how you move.</li>
      <li>Explain what we think is going on, in plain language.</li>
      <li>Agree a plan with you for what to do next.</li>
    </ul>
    <p>Two therapists means you deal with a small team who know your case.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2>What patients say</h2>
    <div class="placeholder">[Add a real patient quote here once you have one, with their permission. Use their own words, and name and age only if they agree.]</div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>First visit: $95 for a full 60 minutes.</h2>
    <p class="price">$95</p>
    <p>One 60-minute first appointment. [Add what follow-up visits cost, and whether insurance can be billed, so people know before they book.]</p>
    <h3>Find us</h3>
    <p>Alder Street, next to the pharmacy. [Add street number, parking info and opening hours.]</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2>Common questions</h2>
    <h3>What should I bring or wear?</h3>
    <p>[Confirm: e.g. comfortable clothes that let us see and move the sore area.]</p>
    <h3>Do I need a referral?</h3>
    <p>[Add your policy.]</p>
    <h3>How many visits will I need?</h3>
    <p>It depends on the problem and the person. After your first visit we'll give you our honest estimate and the reasoning behind it.</p>
    <h3>What if you can't help me?</h3>
    <p>We'll say so and point you to who can.</p>
  </div>
</section>

<section id="book">
  <div class="wrap">
    <h2>Book a 60-minute first visit for $95.</h2>
    <p>Pick a time that suits you. Booking takes a couple of minutes.</p>
    <a class="btn" href="#">Book your first visit</a>
    <p class="note">[Replace the # with your online booking link.]</p>
  </div>
</section>

<footer class="wrap">
  Orrin Valley Physiotherapy · Alder Street, next to the pharmacy · [phone / email]
</footer>

</body>
</html>
```

**Fill these in before launch:**
- The booking link.
- The street number and opening hours.
- Follow-up visit pricing.
- A phone number or email.
- The answers on referrals and what to wear.

**On the two things I left out:**
- **Testimonial:** Ask your first few patients for a short quote and their permission to use it. A real quote from the first month is worth more than an invented one, and it's legal.
- **Guarantee:** If you want a risk-reducer that you will honor, you could offer a first-visit promise such as "If we can't help with your problem, we'll tell you and refer you on." The FAQ already says something like this. Don't promise a pain-free outcome in any form, because physio results vary and you can't control them.
