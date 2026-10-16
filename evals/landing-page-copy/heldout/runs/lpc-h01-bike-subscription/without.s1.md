I couldn't save a file because file writing is disabled in this session, so the whole page is below as a single HTML file. Save it as `index.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Commuter Care Plan – Tallow Lane Cycles, Dunmore</title>
<meta name="description" content="$19 a month: a safety check and tune-up every 3 months, free brake and gear adjustments, and bike pickup and drop-off within 3 miles of the shop.">
<style>
  :root { --ink:#1f2421; --muted:#5a635d; --accent:#b4531f; --bg:#faf8f4; --card:#fff; --line:#e3ded4; }
  * { box-sizing: border-box; }
  body { margin:0; font:17px/1.6 system-ui, -apple-system, "Segoe UI", sans-serif; color:var(--ink); background:var(--bg); }
  .wrap { max-width:680px; margin:0 auto; padding:0 20px; }
  header { padding:48px 0 24px; }
  .brand { font-size:.85rem; letter-spacing:.08em; text-transform:uppercase; color:var(--accent); font-weight:700; }
  h1 { font-size:2.2rem; line-height:1.15; margin:.4em 0 .3em; }
  h2 { font-size:1.35rem; margin:2em 0 .5em; }
  p { margin:.6em 0; }
  .price { display:inline-block; background:var(--ink); color:#fff; padding:.5em 1em; border-radius:6px; font-size:1.1rem; margin-top:.5em; }
  .price strong { font-size:1.6rem; }
  ul.inc { list-style:none; padding:0; margin:0; }
  ul.inc li { background:var(--card); border:1px solid var(--line); border-radius:8px; padding:14px 16px; margin:10px 0; }
  ul.inc strong { display:block; }
  form { background:var(--card); border:1px solid var(--line); border-radius:10px; padding:24px; margin:1em 0 3em; }
  label { display:block; font-weight:600; margin-top:1em; }
  input { width:100%; padding:11px 12px; font:inherit; border:1px solid #b9b3a6; border-radius:6px; margin-top:4px; }
  input:focus, button:focus { outline:3px solid #f0b48f; outline-offset:1px; }
  .hint { display:block; font-size:.9rem; color:var(--muted); font-weight:400; }
  button { margin-top:1.5em; width:100%; padding:14px; font:inherit; font-weight:700; color:#fff; background:var(--accent); border:0; border-radius:6px; cursor:pointer; }
  button:hover { background:#963f12; }
  footer { border-top:1px solid var(--line); padding:20px 0 40px; font-size:.9rem; color:var(--muted); }
</style>
</head>
<body>
<div class="wrap">

<header>
  <div class="brand">Tallow Lane Cycles · Dunmore</div>
  <h1>Keep your commute bike running for $19 a month.</h1>
  <p>If you ride to work, your bike has to start every morning. The Commuter Care Plan gets it checked and tuned on a regular schedule, fixes the small stuff at no charge, and can even come to you.</p>
  <div class="price"><strong>$19</strong> / month</div>
</header>

<main>

<h2>What you get</h2>
<ul class="inc">
  <li><strong>A safety check and tune-up every 3 months</strong>
    Four times a year we go over your bike and tune it up, so wear gets caught before it leaves you stranded.</li>
  <li><strong>Brake and gear adjustments, any time, no charge</strong>
    Rubbing brake? Skipping gears? Bring it in whenever it happens. You don't pay for the adjustment.</li>
  <li><strong>Pickup and drop-off within 3 miles of the shop</strong>
    If you live within 3 miles, we collect your bike from your home and bring it back when it's done.</li>
</ul>

<h2>What costs extra</h2>
<p>Parts. If a check or repair shows you need a new chain, tires, brake pads or anything else, you pay for the part at our normal shop prices. The $19 covers the labor and the service described above, not the parts.</p>

<h2>Who it's for</h2>
<p>People who commute by bike. If your bike is how you get to work, a squeaky drivetrain or soft brakes isn't a minor annoyance. It's a bad morning. The plan is built to keep that from happening and to make repairs easy to fit into a working week.</p>
<p>It's a good fit if you'd rather pay a flat monthly amount than remember to book a service, or if getting the bike to a shop is the part you keep putting off.</p>

<h2>About us</h2>
<p>Tallow Lane Cycles has been repairing bikes in Dunmore for six years. The Commuter Care Plan is brand new, so if you join now you're one of the first.</p>

<h2>Common questions</h2>
<p><strong>I live more than 3 miles away. Can I still join?</strong><br>
Pickup and drop-off only covers addresses within 3 miles of the shop. We use the home address you give below to check which side of that line you're on.</p>
<p><strong>Does the $19 cover parts?</strong><br>
No. Parts are charged separately at our normal shop prices.</p>
<p><strong>How many brake and gear adjustments do I get?</strong><br>
They're free any time you need them.</p>

<h2>Sign up</h2>
<p>Fill in the form below. It takes under a minute.</p>

<!-- TODO: set action to your form handler (Formspree, Netlify Forms, your own endpoint, etc.) -->
<form action="REPLACE_WITH_FORM_ENDPOINT" method="post">
  <label for="name">Full name
    <input id="name" name="name" type="text" autocomplete="name" required>
  </label>
  <label for="email">Email
    <input id="email" name="email" type="email" autocomplete="email" required>
  </label>
  <label for="address">Home address
    <span class="hint">Street, town and ZIP. We use it to check whether you're in our 3-mile pickup area.</span>
    <input id="address" name="address" type="text" autocomplete="street-address" required>
  </label>
  <button type="submit">Join for $19 a month</button>
</form>

</main>

<footer>Tallow Lane Cycles · Dunmore</footer>

</div>
</body>
</html>
```

The copy runs about 550 words. A few things need your input before it goes live:

- **Form endpoint:** `action="REPLACE_WITH_FORM_ENDPOINT"` needs a real handler, such as Formspree, Netlify Forms or your own backend. Until then the form won't submit anywhere.
- **Payment:** The form collects no payment details, and the page doesn't say how members pay. You'll need to decide that, whether it's a payment link after sign-up, an invoice or something else. Then add a line saying so, since people will wonder.
- **Cancellation and commitment:** I left these out because you didn't mention them. Add a line if there's a policy, such as "cancel any time" or a minimum term.
- **Contact details:** The page has no phone number, street address or hours. I didn't want to invent them, so add them to the footer.
- **Pickup details:** I didn't say how pickup gets scheduled or how long a tune-up takes. Both are common questions, so they'd work well as extra FAQ entries.

I kept the copy to what you told me. There are no testimonials or member counts, and the "brand new" status is stated plainly.
