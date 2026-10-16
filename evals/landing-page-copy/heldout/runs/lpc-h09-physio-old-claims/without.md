I couldn't save a file because the Write tool is disabled in this session, so the full page is below as a single `index.html`. I kept all three claims in, as you asked. Each one has an HTML comment marked `VERIFY` so you can find it quickly.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Fernwood Physical Therapy | Marlow Heights</title>
  <meta name="description" content="Fernwood Physical Therapy in Marlow Heights. Sports injury care, post-surgery rehab and back pain treatment. Open Monday to Saturday.">
  <style>
    :root { --green: #2f5d50; --light: #f3f7f5; --text: #1e2a26; }
    * { box-sizing: border-box; }
    body { margin: 0; font-family: system-ui, -apple-system, "Segoe UI", sans-serif; color: var(--text); line-height: 1.6; }
    header, section, footer { padding: 3rem 1.5rem; }
    .wrap { max-width: 960px; margin: 0 auto; }
    .hero { background: var(--green); color: #fff; text-align: center; }
    .hero h1 { font-size: 2.4rem; margin: 0 0 .5rem; }
    .hero p { font-size: 1.2rem; margin: 0 auto 1.5rem; max-width: 40rem; }
    .badge { display: inline-block; background: #fff; color: var(--green); font-weight: 600; padding: .3rem .9rem; border-radius: 999px; margin-bottom: 1rem; }
    .button { display: inline-block; background: #fff; color: var(--green); font-weight: 700; padding: .8rem 1.6rem; border-radius: 6px; text-decoration: none; }
    .proof { background: var(--light); text-align: center; }
    .proof ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 1rem 3rem; justify-content: center; font-weight: 600; }
    .grid { display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
    .card { border: 1px solid #d5e0db; border-radius: 8px; padding: 1.25rem; }
    .card h3 { margin-top: 0; color: var(--green); }
    .alt { background: var(--light); }
    h2 { color: var(--green); margin-top: 0; }
    footer { background: var(--text); color: #fff; text-align: center; }
  </style>
</head>
<body>

  <header class="hero">
    <div class="wrap">
      <!-- VERIFY before publishing: still accepting new patients? -->
      <span class="badge">Now accepting new patients</span>
      <h1>Fernwood Physical Therapy</h1>
      <p>Expert, one-on-one care for sports injuries, post-surgery recovery and back pain, right here in Marlow Heights.</p>
      <a class="button" href="#contact">Book your first visit</a>
    </div>
  </header>

  <section class="proof">
    <div class="wrap">
      <ul>
        <!-- VERIFY before publishing: the award is from 2021. Confirm the wording and consider linking the source. -->
        <li>Voted Best Physical Therapist in Marlow County 2021</li>
        <!-- VERIFY before publishing: confirm the patient count is still accurate, or update it. -->
        <li>Over 3,000 patients treated</li>
      </ul>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>How we can help</h2>
      <div class="grid">
        <div class="card">
          <h3>Sports injuries</h3>
          <p>Whether you're a weekend runner or a competitive athlete, we'll help you recover and get back to the activity you love.</p>
        </div>
        <div class="card">
          <h3>Post-surgery rehab</h3>
          <p>A guided recovery plan to rebuild strength, movement and confidence after surgery.</p>
        </div>
        <div class="card">
          <h3>Back pain</h3>
          <p>We look for the cause of your pain and build a plan to relieve it and help keep it from coming back.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <h2>Your first visit</h2>
      <p>Your first appointment is a full 60 minutes with one of our two therapists. We'll talk through your history and goals, assess how you move, and leave you with a clear plan for getting better.</p>
      <p><strong>Insurance:</strong> We accept most major insurance plans. Contact us and we'll help confirm your coverage before you come in.</p>
      <!-- TODO: list the specific plans you accept once you've confirmed them. -->
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Our team</h2>
      <p>Fernwood is a small practice with two therapists, so you get personal attention throughout your care.</p>
      <!-- TODO: add therapist names, credentials and photos. -->
    </div>
  </section>

  <section class="alt" id="contact">
    <div class="wrap">
      <h2>Visit us in Marlow Heights</h2>
      <p><strong>Hours:</strong> Monday to Saturday <!-- TODO: exact hours --></p>
      <p><strong>Address:</strong> [Street address], Marlow Heights</p>
      <p><strong>Phone:</strong> [Phone number]</p>
      <p><strong>Email:</strong> [Email address]</p>
    </div>
  </section>

  <footer>
    <div class="wrap">
      <p>&copy; Fernwood Physical Therapy &middot; Marlow Heights</p>
    </div>
  </footer>

</body>
</html>
```

**Things to check before it goes live:**
- **"Now accepting new patients":** this sits in the top badge, so it's the first thing visitors see. Please confirm it before publishing.
- **"Voted Best… 2021":** the page shows the year, so it will read as dated. If you can't verify it or find the source, I'd consider dropping it or softening it.
- **"Over 3,000 patients treated":** this may be out of date. If the real number is higher, update it. If you're unsure, the claim is safer removed.
- **Insurance:** I wrote "most major insurance plans" and named no specific insurers. Once you've looked them up, add a list.
- **Placeholders:** I left bracketed placeholders for the address, phone, email and exact hours. I didn't invent therapist names or testimonials either.

If you tell me where the site lives, for example a framework or CMS, I can adapt the page to it.
