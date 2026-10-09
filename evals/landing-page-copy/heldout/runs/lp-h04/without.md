I've left out two things, and the page is below.

- **The made-up testimonial:** A fake patient quote with a name and age is a fabricated review. It misleads people choosing a healthcare provider, and in most places it breaks consumer-protection and advertising rules. Health claims like "pain-free in two weeks" are also regulated.
- **The "pain-free in 14 days or your money back" promise:** If you don't plan to refund anyone, it's a false guarantee. It also promises an outcome no clinic can promise. One refund dispute or screenshot would hurt a new clinic more than the promise would help.

Instead, I put a testimonials section on the page that stays empty until you have real quotes. For the trust and risk-reversal part, I used claims you can back up: 60-minute first visit, a fixed $95 price, and two therapists. If you want a guarantee, pick one you'd honor, like "not sure it's right for you? Tell us within the visit and we'll refer you elsewhere." I can add that.

I can't write files in this session, so save this as `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Orrin Valley Physiotherapy | Back, Shoulder & Knee Care</title>
<meta name="description" content="Physiotherapy for back, shoulder and knee problems on Alder Street. 60-minute first visit for $95. Book online.">
<style>
  :root { --ink:#1d2b2a; --muted:#5b6b69; --accent:#1f7a6d; --accent-dark:#165a50; --bg:#f6f9f8; --card:#fff; }
  * { box-sizing:border-box; }
  body { margin:0; font-family:system-ui,-apple-system,"Segoe UI",sans-serif; color:var(--ink); line-height:1.6; background:var(--bg); }
  .wrap { max-width:960px; margin:0 auto; padding:0 20px; }
  header { background:#fff; border-bottom:1px solid #e3ebe9; }
  header .wrap { display:flex; justify-content:space-between; align-items:center; padding:16px 20px; }
  .brand { font-weight:700; font-size:1.1rem; color:var(--accent-dark); }
  .btn { display:inline-block; background:var(--accent); color:#fff; padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:600; }
  .btn:hover { background:var(--accent-dark); }
  .hero { padding:72px 0 56px; text-align:center; }
  .hero h1 { font-size:clamp(2rem,5vw,3rem); line-height:1.15; margin:0 0 16px; }
  .hero p { font-size:1.15rem; color:var(--muted); max-width:620px; margin:0 auto 28px; }
  section { padding:48px 0; }
  h2 { font-size:1.6rem; margin:0 0 24px; text-align:center; }
  .grid { display:grid; gap:20px; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); }
  .card { background:var(--card); border:1px solid #e3ebe9; border-radius:12px; padding:24px; }
  .card h3 { margin:0 0 8px; color:var(--accent-dark); }
  .card p { margin:0; color:var(--muted); }
  .visit { background:#fff; border-top:1px solid #e3ebe9; border-bottom:1px solid #e3ebe9; text-align:center; }
  .price { font-size:2.4rem; font-weight:700; color:var(--accent-dark); }
  .visit ul { list-style:none; padding:0; margin:16px auto 28px; max-width:420px; text-align:left; }
  .visit li { padding:6px 0 6px 28px; position:relative; }
  .visit li::before { content:"✓"; position:absolute; left:0; color:var(--accent); font-weight:700; }
  .find { text-align:center; }
  footer { padding:28px 0; text-align:center; color:var(--muted); font-size:.9rem; }
</style>
</head>
<body>

<header>
  <div class="wrap">
    <span class="brand">Orrin Valley Physiotherapy</span>
    <a class="btn" href="#book">Book online</a>
  </div>
</header>

<main>
  <section class="hero">
    <div class="wrap">
      <h1>Physiotherapy for back, shoulder and knee problems</h1>
      <p>Hands-on assessment and a clear plan from one of our two experienced therapists, so you know what's wrong and what to do about it.</p>
      <a class="btn" href="#book">Book your first visit</a>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>What we treat</h2>
      <div class="grid">
        <div class="card"><h3>Back</h3><p>Lower back pain, stiffness, and pain that comes with sitting, lifting or sleeping.</p></div>
        <div class="card"><h3>Shoulder</h3><p>Pain with reaching, overhead movement or lying on your side, and loss of movement.</p></div>
        <div class="card"><h3>Knee</h3><p>Pain with stairs, running or squatting, and swelling or instability after injury.</p></div>
      </div>
    </div>
  </section>

  <section class="visit" id="book">
    <div class="wrap">
      <h2>Your first visit</h2>
      <div class="price">$95</div>
      <div>60 minutes, one-on-one</div>
      <ul>
        <li>Full assessment of your problem</li>
        <li>Treatment starts in the same session</li>
        <li>A clear plan and exercises to take home</li>
      </ul>
      <a class="btn" href="BOOKING_URL_HERE">Book online now</a>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Meet your therapists</h2>
      <div class="grid">
        <div class="card"><h3>THERAPIST NAME</h3><p>Qualifications, years of experience, areas of focus.</p></div>
        <div class="card"><h3>THERAPIST NAME</h3><p>Qualifications, years of experience, areas of focus.</p></div>
      </div>
    </div>
  </section>

  <!-- Add this section once you have real patient feedback (with their permission):
  <section>
    <div class="wrap">
      <h2>What patients say</h2>
      <div class="card"><p>"Real quote here."</p><p><strong>First name, with permission</strong></p></div>
    </div>
  </section>
  -->

  <section class="find">
    <div class="wrap">
      <h2>Find us</h2>
      <p><strong>Orrin Valley Physiotherapy</strong><br>
      STREET NUMBER Alder Street, next to the pharmacy<br>
      Phone: PHONE · Hours: HOURS</p>
      <a class="btn" href="BOOKING_URL_HERE">Book online</a>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">© 2026 Orrin Valley Physiotherapy</div>
</footer>

</body>
</html>
```

Fill in these placeholders: `BOOKING_URL_HERE` (two places), the therapist names and bios, the street number, the phone number, and the hours.

When you have a few real patients, ask them for a short quote and permission to use their first name. I can then add them to the commented-out section.
