I couldn't save this as a file because the Write tool is disabled in this session. The full page is below as a single HTML file. Copy it into `index.html`.

I left out two lines I'd drafted because your facts don't support them. One said you don't ask people to move out. The other said you'd flag bad boxes "before a deposit." The form's `action="#"` is a placeholder, so you'll need to point it at your form handler.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cabinet Refacing in Calder Ridge, from $4,800 | Marrow Creek Cabinet Refacing</title>
<meta name="description" content="Keep your cabinet boxes, replace the doors and drawer fronts. Kitchens from $4,800, typically done in 5 to 7 working days. Free in-home measure in Calder Ridge.">
<style>
  :root { --ink:#25211c; --muted:#5c554b; --bg:#faf7f2; --card:#fff; --accent:#8a3b1f; --accent-dark:#6b2c15; --line:#e2dbcf; }
  * { box-sizing:border-box; }
  body { margin:0; font:18px/1.6 Georgia, "Times New Roman", serif; color:var(--ink); background:var(--bg); }
  h1,h2,h3,.btn,label,button,input { font-family:-apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }
  .wrap { max-width:960px; margin:0 auto; padding:0 20px; }
  header.top { border-bottom:1px solid var(--line); background:var(--card); }
  header.top .wrap { display:flex; justify-content:space-between; align-items:center; padding:14px 20px; gap:12px; flex-wrap:wrap; }
  .brand { font-family:-apple-system,"Segoe UI",Arial,sans-serif; font-weight:700; }
  .phone { font-family:-apple-system,"Segoe UI",Arial,sans-serif; font-weight:600; color:var(--accent); text-decoration:none; }
  .hero { padding:56px 0 40px; }
  h1 { font-size:2.3rem; line-height:1.15; margin:0 0 16px; }
  .lead { font-size:1.2rem; max-width:40em; }
  .btn { display:inline-block; background:var(--accent); color:#fff; padding:14px 24px; border-radius:6px; text-decoration:none; font-weight:600; font-size:1rem; border:0; cursor:pointer; }
  .btn:hover { background:var(--accent-dark); }
  .hero .note { color:var(--muted); font-size:.95rem; margin-top:12px; }
  section { padding:36px 0; border-top:1px solid var(--line); }
  h2 { font-size:1.6rem; margin:0 0 14px; }
  h3 { font-size:1.1rem; margin:0 0 6px; }
  .grid { display:grid; gap:20px; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); }
  .card { background:var(--card); border:1px solid var(--line); border-radius:8px; padding:20px; }
  .card p { margin:0; }
  blockquote { margin:0; }
  blockquote p { font-size:1.15rem; margin:0 0 8px; }
  cite { font-style:normal; color:var(--muted); font-size:.95rem; }
  .callout { background:#fff3e6; border:1px solid #ecd2b3; border-radius:8px; padding:18px 20px; }
  form { background:var(--card); border:1px solid var(--line); border-radius:8px; padding:24px; max-width:520px; }
  label { display:block; font-weight:600; font-size:.95rem; margin-bottom:14px; }
  input { display:block; width:100%; margin-top:6px; padding:11px 12px; font-size:1rem; border:1px solid #b9b0a1; border-radius:6px; }
  footer { border-top:1px solid var(--line); padding:28px 0 40px; color:var(--muted); font-size:.95rem; }
  @media (max-width:600px){ h1{font-size:1.8rem;} body{font-size:17px;} }
</style>
</head>
<body>

<header class="top">
  <div class="wrap">
    <span class="brand">Marrow Creek Cabinet Refacing</span>
    <a class="phone" href="tel:5550143">Call 555-0143</a>
  </div>
</header>

<main>
<div class="wrap">

  <div class="hero">
    <h1>A new-looking kitchen from $4,800, without tearing out your cabinets.</h1>
    <p class="lead">We keep your existing cabinet boxes, replace the doors and drawer fronts, and cover the visible frames with matching veneer. New hinges and pulls are included. The work typically takes 5 to 7 working days.</p>
    <p><a class="btn" href="#book">Book your free in-home measure</a></p>
    <p class="note">Or call 555-0143. Serving homeowners in and around Calder Ridge for 14 years.</p>
  </div>

  <section id="price">
    <h2>What it costs</h2>
    <div class="grid">
      <div class="card">
        <h3>From $4,800</h3>
        <p>That's the starting price for a standard 10 by 10 kitchen.</p>
      </div>
      <div class="card">
        <h3>Final price is set at the measure</h3>
        <p>The in-home measure is free.</p>
      </div>
      <div class="card">
        <h3>Simple payment</h3>
        <p>30% deposit to book. The rest is due at the final walkthrough.</p>
      </div>
    </div>
  </section>

  <section id="what">
    <h2>What refacing includes</h2>
    <div class="grid">
      <div class="card"><h3>Your boxes stay</h3><p>We keep your existing cabinet boxes, so your layout stays as it is.</p></div>
      <div class="card"><h3>New doors and drawer fronts</h3><p>We replace them all.</p></div>
      <div class="card"><h3>Matching veneer</h3><p>The visible frames are covered to match.</p></div>
      <div class="card"><h3>Hinges and pulls</h3><p>New hinges and pulls are included.</p></div>
    </div>
  </section>

  <section id="timeline">
    <h2>Living without a kitchen: what to expect</h2>
    <p>The job typically takes 5 to 7 working days. Here is the part to plan for:</p>
    <div class="callout">
      <p style="margin:0"><strong>During days 3 to 5, the cabinet doors are off the boxes, and the kitchen is usable for the sink and the fridge only.</strong></p>
    </div>
  </section>

  <section id="reviews">
    <h2>What homeowners say</h2>
    <div class="grid">
      <div class="card">
        <blockquote>
          <p>“They were out of my kitchen faster than the tile guy.”</p>
          <cite>Rosalind, Calder Ridge</cite>
        </blockquote>
      </div>
      <div class="card">
        <blockquote>
          <p>“It looks like we replaced everything. We kept our layout and saved a lot.”</p>
          <cite>Anil, Eastbrook</cite>
        </blockquote>
      </div>
    </div>
  </section>

  <section id="fine-print">
    <h2>The warranty, and when refacing isn't the right fit</h2>
    <div class="grid">
      <div class="card">
        <h3>5-year warranty</h3>
        <p>Covers doors, finish and hardware. It does not cover the existing cabinet boxes underneath.</p>
      </div>
      <div class="card">
        <h3>Water-damaged or sagging boxes</h3>
        <p>We can't reface these. They need replacing, and we'll tell you at the measure.</p>
      </div>
    </div>
  </section>

  <section id="book">
    <h2>Book your free in-home measure</h2>
    <p>Call <a class="phone" href="tel:5550143">555-0143</a> or use the form.</p>
    <form action="#" method="post">
      <label>Your name
        <input type="text" name="name" autocomplete="name" required>
      </label>
      <label>Phone number
        <input type="tel" name="phone" autocomplete="tel" required>
      </label>
      <label>Email
        <input type="email" name="email" autocomplete="email">
      </label>
      <button class="btn" type="submit">Request my free measure</button>
    </form>
  </section>

</div>
</main>

<footer>
  <div class="wrap">
    Marrow Creek Cabinet Refacing &middot; 14 years serving homeowners in and around Calder Ridge &middot; 555-0143
  </div>
</footer>

</body>
</html>
```

The page puts price and timeline in their own sections near the top, since those are the two worries. It states the days 3 to 5 limit and the warranty exclusion plainly rather than burying them.
