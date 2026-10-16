I couldn't save the page to a file because the Write tool is disabled in this session. The full page is below as a single `index.html`. Copy it into a file, or re-enable Write and I'll save it.

I stuck to your facts. The form's `action="#"` is a placeholder, so it needs to be pointed at wherever submissions should go.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cabinet Refacing in Calder Ridge | Marrow Creek Cabinet Refacing</title>
<meta name="description" content="Cabinet refacing from $4,800 for a standard 10 by 10 kitchen. Typically 5 to 7 working days. 5-year warranty on doors, finish and hardware. Serving Calder Ridge.">
<style>
  :root { --ink:#26211c; --muted:#5e554c; --bg:#faf7f2; --card:#fff; --accent:#2f5d50; --accent-dark:#234539; --line:#e2dbd0; }
  * { box-sizing:border-box; }
  body { margin:0; font:17px/1.6 Georgia, "Times New Roman", serif; color:var(--ink); background:var(--bg); }
  h1,h2,h3,.btn,label,button,input,select,textarea { font-family:system-ui, -apple-system, "Segoe UI", sans-serif; }
  .wrap { max-width:960px; margin:0 auto; padding:0 20px; }
  header.top { border-bottom:1px solid var(--line); background:var(--card); }
  header.top .wrap { display:flex; justify-content:space-between; align-items:center; gap:16px; padding:14px 20px; flex-wrap:wrap; }
  .brand { font:700 18px system-ui, sans-serif; }
  .phone { font:600 18px system-ui, sans-serif; color:var(--accent); text-decoration:none; }
  .hero { padding:56px 0 40px; }
  h1 { font-size:clamp(30px,5vw,44px); line-height:1.15; margin:0 0 16px; }
  .lead { font-size:19px; color:var(--muted); max-width:640px; margin:0 0 24px; }
  .btn { display:inline-block; background:var(--accent); color:#fff; padding:14px 24px; border-radius:6px; text-decoration:none; font-weight:600; font-size:17px; border:0; cursor:pointer; }
  .btn:hover { background:var(--accent-dark); }
  .or { margin-left:14px; font-family:system-ui,sans-serif; }
  section { padding:40px 0; border-top:1px solid var(--line); }
  h2 { font-size:28px; margin:0 0 12px; line-height:1.2; }
  h3 { font-size:18px; margin:0 0 6px; }
  p { margin:0 0 14px; }
  .grid { display:grid; gap:18px; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); }
  .card { background:var(--card); border:1px solid var(--line); border-radius:8px; padding:20px; }
  .card p:last-child { margin-bottom:0; }
  .big { font:700 30px system-ui,sans-serif; color:var(--accent); margin:0 0 6px; }
  .note { background:#f1ece2; border-left:4px solid var(--accent); padding:14px 18px; border-radius:4px; }
  blockquote { margin:0; }
  blockquote p { font-size:19px; font-style:italic; }
  cite { font:600 15px system-ui,sans-serif; font-style:normal; color:var(--muted); }
  form { display:grid; gap:14px; max-width:480px; }
  label { font-weight:600; font-size:15px; display:grid; gap:4px; }
  input, textarea { font-size:16px; padding:11px; border:1px solid #b9b0a3; border-radius:6px; }
  footer { padding:28px 0 40px; border-top:1px solid var(--line); color:var(--muted); font:15px system-ui,sans-serif; }
</style>
</head>
<body>

<header class="top">
  <div class="wrap">
    <span class="brand">Marrow Creek Cabinet Refacing</span>
    <a class="phone" href="tel:555-0143">555-0143</a>
  </div>
</header>

<main>
  <div class="wrap">

    <div class="hero">
      <h1>A new-looking kitchen, without tearing out your cabinets.</h1>
      <p class="lead">We keep your existing cabinet boxes and replace the doors and drawer fronts. Refacing starts from $4,800 for a standard 10 by 10 kitchen, and the work typically takes 5 to 7 working days.</p>
      <a class="btn" href="#book">Book your free in-home measure</a>
      <span class="or">or call <a href="tel:555-0143">555-0143</a></span>
    </div>

    <section>
      <h2>What refacing means</h2>
      <p>Your cabinet boxes stay where they are. Here is what we change:</p>
      <div class="grid">
        <div class="card"><h3>New doors and drawer fronts</h3><p>We replace the doors and drawer fronts.</p></div>
        <div class="card"><h3>Matching veneer</h3><p>We cover the visible frames with matching veneer.</p></div>
        <div class="card"><h3>New hinges and pulls</h3><p>Included in the price.</p></div>
      </div>
    </section>

    <section>
      <h2>What it costs</h2>
      <div class="card">
        <p class="big">From $4,800</p>
        <p>That is for a standard 10 by 10 kitchen. Your final price is set at the free in-home measure.</p>
        <p><strong>How payment works:</strong> a 30% deposit books your job, and the rest is due at the final walkthrough.</p>
      </div>
    </section>

    <section>
      <h2>Living without your kitchen</h2>
      <p>The work typically takes 5 to 7 working days. Here is the stretch that is hardest to live with:</p>
      <div class="note">
        <p><strong>Days 3 to 5:</strong> the cabinet doors are off the boxes. During those days the kitchen is usable for the sink and fridge only.</p>
      </div>
      <blockquote class="card" style="margin-top:18px">
        <p>“They were out of my kitchen faster than the tile guy.”</p>
        <cite>Rosalind, Calder Ridge</cite>
      </blockquote>
    </section>

    <section>
      <h2>Warranty, and what it doesn't cover</h2>
      <p>Doors, finish and hardware are covered for 5 years. The warranty does not cover the existing cabinet boxes underneath.</p>
    </section>

    <section>
      <h2>When refacing won't work</h2>
      <p>We cannot reface boxes that are water-damaged or sagging. Those need replacing. If yours are in that shape, we will tell you at the measure.</p>
    </section>

    <section>
      <h2>What homeowners say</h2>
      <blockquote class="card">
        <p>“It looks like we replaced everything. We kept our layout and saved a lot.”</p>
        <cite>Anil, Eastbrook</cite>
      </blockquote>
    </section>

    <section id="book">
      <h2>Book your free in-home measure</h2>
      <p>Call <a href="tel:555-0143"><strong>555-0143</strong></a> or use the form below.</p>
      <form action="#" method="post">
        <label>Name <input type="text" name="name" required autocomplete="name"></label>
        <label>Phone <input type="tel" name="phone" required autocomplete="tel"></label>
        <label>Address <input type="text" name="address" autocomplete="street-address"></label>
        <label>Anything we should know? <textarea name="notes" rows="3"></textarea></label>
        <button class="btn" type="submit">Request my free measure</button>
      </form>
    </section>

  </div>
</main>

<footer>
  <div class="wrap">Marrow Creek Cabinet Refacing · 14 years in business · Serving homeowners in and around Calder Ridge · <a href="tel:555-0143">555-0143</a></div>
</footer>

</body>
</html>
```

**Design choices**
- **Order:** the page follows the two worries in the order a nervous homeowner would raise them. Price comes first, then the days without a kitchen.
- **Rosalind's quote:** it sits under the downtime section, because it speaks to that worry.
- **Anil's quote:** it comes after the limits and warranty, because it speaks to savings.
- **Limits stated plainly:** the warranty exclusion and the water-damaged or sagging boxes both get their own sections. People who find limits themselves tend to distrust the rest of a page.
- **Left out on purpose:** your facts don't cover licensing or insurance, financing, a callback time, or which rooms or materials you work with. The page says nothing about any of them.
- **Form fields:** the facts only name "the form on this page", so I picked name, phone, address and notes. Change them if your form differs.
