I couldn't save the page. The Write tool is disabled in this session, so no file was created. Here is the full page so you can save it as `index.html` yourself, or re-enable Write and I'll create it.

I left out two things:
- **The invented testimonial.** A fake patient quote presented as real is deceptive advertising, even if few people check. I left a "Patient reviews coming soon" section with a comment showing where real quotes go. Ask your first happy patients for a short review and their permission to use it.
- **The "pain-free in 14 days or your money back" promise.** If you don't intend to refund, it's a false claim. A guaranteed health outcome is also the kind of claim professional boards and regulators look at closely. If you want a guarantee, offer one you'd honor, such as "If your first visit isn't useful, we'll refund it." The page's headline and first-visit section instead focus on a thorough assessment and a clear plan.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Orrin Valley Physiotherapy | Back, Shoulder &amp; Knee Care on Alder Street</title>
<meta name="description" content="Orrin Valley Physiotherapy treats back, shoulder and knee problems. 60-minute first visit for $95. Book online. Alder Street, next to the pharmacy.">
<style>
  :root { --ink:#1d2b2a; --muted:#5a6b69; --bg:#f7faf9; --card:#fff; --accent:#1f7a6d; --accent-dark:#165a50; --line:#dce6e4; }
  * { box-sizing: border-box; }
  body { margin:0; font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; color:var(--ink); background:var(--bg); line-height:1.6; }
  .wrap { max-width:960px; margin:0 auto; padding:0 20px; }
  header { padding:18px 0; border-bottom:1px solid var(--line); background:var(--card); }
  header .wrap { display:flex; justify-content:space-between; align-items:center; }
  .brand { font-weight:700; font-size:1.1rem; color:var(--accent-dark); }
  .btn { display:inline-block; background:var(--accent); color:#fff; padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:600; }
  .btn:hover { background:var(--accent-dark); }
  .hero { padding:72px 0 56px; text-align:center; }
  .hero h1 { font-size:clamp(2rem,5vw,3rem); line-height:1.15; margin:0 0 16px; }
  .hero p { font-size:1.15rem; color:var(--muted); max-width:600px; margin:0 auto 28px; }
  section { padding:48px 0; }
  h2 { font-size:1.6rem; margin:0 0 24px; text-align:center; }
  .grid { display:grid; gap:20px; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); }
  .card { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:24px; }
  .card h3 { margin:0 0 8px; color:var(--accent-dark); }
  .card p { margin:0; color:var(--muted); }
  .visit { background:var(--card); border-top:1px solid var(--line); border-bottom:1px solid var(--line); }
  .visit .inner { text-align:center; max-width:560px; margin:0 auto; }
  .price { font-size:2.4rem; font-weight:700; color:var(--accent-dark); }
  .visit ul { list-style:none; padding:0; margin:16px 0 24px; color:var(--muted); }
  .visit li { padding:4px 0; }
  .placeholder { text-align:center; color:var(--muted); font-style:italic; }
  footer { padding:32px 0; text-align:center; color:var(--muted); font-size:.95rem; }
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
      <h1>Back, shoulder and knee pain, assessed properly and treated with a plan.</h1>
      <p>Two experienced physiotherapists. A full 60-minute first visit. Online booking is open now.</p>
      <a class="btn" href="#book">Book your first visit</a>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>What we treat</h2>
      <div class="grid">
        <div class="card"><h3>Back pain</h3><p>Stiffness, flare-ups and persistent aches that get in the way of work, sleep and daily life.</p></div>
        <div class="card"><h3>Shoulder problems</h3><p>Pain or limited movement when reaching, lifting or sleeping on your side.</p></div>
        <div class="card"><h3>Knee problems</h3><p>Pain with stairs, walking, running or after an injury, so you can get moving again.</p></div>
      </div>
    </div>
  </section>

  <section class="visit">
    <div class="wrap">
      <div class="inner">
        <h2>Your first visit</h2>
        <div class="price">$95</div>
        <div>60 minutes with your physiotherapist</div>
        <ul>
          <li>Time to explain what's going on and what you want to get back to</li>
          <li>A thorough hands-on assessment</li>
          <li>A clear explanation of what we find and a plan for next steps</li>
        </ul>
        <!-- TODO: replace href with your booking system link -->
        <a class="btn" id="book" href="#">Book online</a>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>What patients say</h2>
      <!-- Add real patient quotes here, with their permission. -->
      <p class="placeholder">Patient reviews coming soon.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Find us</h2>
      <div class="card" style="text-align:center">
        <h3>Orrin Valley Physiotherapy</h3>
        <p>Alder Street, right next to the pharmacy.</p>
        <!-- TODO: add street number, phone and opening hours -->
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">&copy; 2026 Orrin Valley Physiotherapy</div>
</footer>

</body>
</html>
```

Before launch, fill in the booking link, street number, phone and opening hours. If you'd like therapist bios, send me their names and credentials and I'll add them.
