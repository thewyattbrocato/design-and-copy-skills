I couldn't save a file because the Write tool is disabled in this session. The full page is below, so you can paste it into `index.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Fernwood Physical Therapy | Marlow Heights</title>
  <meta name="description" content="Fernwood Physical Therapy in Marlow Heights. Sports injury care, post-surgery rehab and back pain treatment. Open Monday to Saturday.">
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; font-family: system-ui, -apple-system, "Segoe UI", sans-serif; color: #1f2d2a; line-height: 1.6; }
    .wrap { max-width: 960px; margin: 0 auto; padding: 0 1.25rem; }
    header { background: #2f5d50; color: #fff; padding: 4rem 0 3rem; text-align: center; }
    header h1 { margin: 0 0 .5rem; font-size: 2.4rem; }
    header p { margin: 0 auto 1.5rem; max-width: 36rem; font-size: 1.15rem; }
    .badge { display: inline-block; background: #e8f3ee; color: #1f4a3d; padding: .35rem .9rem; border-radius: 999px; font-weight: 600; margin-bottom: 1.25rem; }
    .btn { display: inline-block; background: #fff; color: #2f5d50; padding: .8rem 1.6rem; border-radius: 6px; font-weight: 700; text-decoration: none; }
    section { padding: 3rem 0; }
    section:nth-of-type(even) { background: #f4f8f6; }
    h2 { margin-top: 0; font-size: 1.7rem; color: #2f5d50; }
    .grid, .proof { display: grid; gap: 1.25rem; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
    .card { background: #fff; border: 1px solid #d8e4df; border-radius: 8px; padding: 1.25rem; }
    .card h3 { margin-top: 0; }
    .proof { text-align: center; font-weight: 600; font-size: 1.1rem; }
    footer { background: #1f2d2a; color: #cfdcd7; padding: 2rem 0; text-align: center; font-size: .95rem; }
  </style>
</head>
<body>

<header>
  <div class="wrap">
    <!-- VERIFY: confirm we're still accepting new patients. Remove badge if not. -->
    <span class="badge">Now accepting new patients</span>
    <h1>Fernwood Physical Therapy</h1>
    <p>Hands-on, personal physical therapy in Marlow Heights. Get moving, get stronger, and get back to what you love.</p>
    <a class="btn" href="#contact">Book Your First Visit</a>
  </div>
</header>

<section>
  <div class="wrap proof">
    <!-- VERIFY: award wording and year against the original source -->
    <div>Voted Best Physical Therapist in Marlow County 2021</div>
    <!-- VERIFY: confirm "over 3,000" still holds (or update the number) -->
    <div>Over 3,000 patients treated</div>
  </div>
</section>

<section id="services">
  <div class="wrap">
    <h2>What We Treat</h2>
    <div class="grid">
      <div class="card"><h3>Sports Injuries</h3>
        <p>Sprains, strains and overuse injuries. We help athletes of every level recover and return to play.</p></div>
      <div class="card"><h3>Post-Surgery Rehab</h3>
        <p>A structured recovery plan to restore strength, movement and confidence at the right pace.</p></div>
      <div class="card"><h3>Back Pain</h3>
        <p>Targeted treatment and exercise to relieve back pain and help keep it from coming back.</p></div>
    </div>
  </div>
</section>

<section id="about">
  <div class="wrap">
    <h2>Care That's Personal</h2>
    <p>Fernwood is a small clinic with two therapists, so you'll know who is treating you every time you come in. Your plan is built around your goals.</p>
    <h2>Your First Visit</h2>
    <p>Your first appointment is 60 minutes. We'll talk through your history and goals, assess how you move, and start on a plan right away.</p>
  </div>
</section>

<section id="insurance">
  <div class="wrap">
    <h2>Insurance</h2>
    <!-- TODO: list specific accepted plans once confirmed -->
    <p>We accept most insurance plans. Contact us and we'll help confirm your coverage before your first visit.</p>
  </div>
</section>

<section id="contact">
  <div class="wrap">
    <h2>Visit Us</h2>
    <p><strong>Fernwood Physical Therapy</strong><br>Marlow Heights<br>
    <!-- TODO: fill in address, phone, email, daily hours, booking link -->
    [Street address] &middot; [Phone] &middot; [Email]</p>
    <p><strong>Open Monday to Saturday</strong></p>
    <a class="btn" style="background:#2f5d50;color:#fff" href="#">Request an Appointment</a>
  </div>
</section>

<footer>
  <div class="wrap">&copy; 2026 Fernwood Physical Therapy &middot; Marlow Heights</div>
</footer>

</body>
</html>
```

**Claims to check before publishing:**
- **"Now accepting new patients":** This sits in a badge at the top of the page. Remove it if that's no longer true.
- **"Voted Best… 2021":** The year is in the text, so it reads as a past award and won't mislead anyone. A 2021 award on a 2026 page may look stale, so you could replace it with something more recent.
- **"Over 3,000 patients":** The count only goes up, so this is probably still true. Update it if you have a current figure.

**Left as placeholders:**
- The street address, phone number, email, booking link and daily hours.
- The list of insurance plans. The page says "most insurance plans" for now.

I also added a few short descriptions of each service and a line about your small two-therapist team. Edit those if they don't sound like you.
