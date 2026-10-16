I can't write files in this session, so the full page is below. You can save it as `index.html`.

I kept all three claims in, as you asked. Each one has a `TODO` comment in the code so you can check it before publishing. Two of them need a closer look:
- **"Voted Best… 2021"** is five years old now. It may read as stale even if it's accurate.
- **"Over 3,000 patients treated"** is probably higher by now. If you have a current number, use that.

I didn't invent any insurance names, hours, address or phone number. Those are bracketed placeholders.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Fernwood Physical Therapy | Marlow Heights</title>
  <meta name="description" content="Fernwood Physical Therapy in Marlow Heights. Sports injury care, post-surgery rehab and back pain treatment. Open Monday to Saturday.">
  <style>
    :root { --green: #2f5d50; --light: #eef4f1; --text: #222; }
    * { box-sizing: border-box; }
    body { margin: 0; font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; color: var(--text); line-height: 1.6; }
    .wrap { max-width: 960px; margin: 0 auto; padding: 0 20px; }
    header { background: var(--green); color: #fff; padding: 14px 0; }
    header .wrap { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; }
    header strong { font-size: 1.25rem; }
    .hero { background: var(--light); padding: 64px 0; text-align: center; }
    .hero h1 { font-size: 2.4rem; margin: 0 0 12px; line-height: 1.2; }
    .hero p { font-size: 1.15rem; max-width: 620px; margin: 0 auto 24px; }
    .btn { display: inline-block; background: var(--green); color: #fff; padding: 14px 28px; border-radius: 6px; text-decoration: none; font-weight: 600; }
    .badges { display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; margin-top: 28px; }
    .badge { background: #fff; border: 1px solid #cfdcd6; border-radius: 999px; padding: 8px 18px; font-size: .95rem; }
    section { padding: 52px 0; }
    h2 { font-size: 1.7rem; margin-top: 0; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; }
    .card { border: 1px solid #dde5e1; border-radius: 8px; padding: 22px; }
    .card h3 { margin-top: 0; color: var(--green); }
    .alt { background: var(--light); }
    footer { background: #1d2b26; color: #dfe8e4; padding: 32px 0; font-size: .95rem; }
  </style>
</head>
<body>

<header>
  <div class="wrap">
    <strong>Fernwood Physical Therapy</strong>
    <span>Marlow Heights</span>
  </div>
</header>

<main>
  <div class="hero">
    <div class="wrap">
      <h1>Move better. Hurt less. Get back to what you love.</h1>
      <p>Hands-on, one-on-one physical therapy for sports injuries, post-surgery recovery and back pain, right here in Marlow Heights.</p>
      <a class="btn" href="#contact">Book your first visit</a>

      <div class="badges">
        <!-- TODO: confirm each claim below is still accurate before publishing. -->
        <!-- TODO: confirm the 2021 award is still worth featuring and the wording is correct. -->
        <span class="badge">Voted Best Physical Therapist in Marlow County 2021</span>
        <!-- TODO: confirm the current patient count. -->
        <span class="badge">Over 3,000 patients treated</span>
        <!-- TODO: confirm we are still accepting new patients; remove if not. -->
        <span class="badge">Now accepting new patients</span>
      </div>
    </div>
  </div>

  <section>
    <div class="wrap">
      <h2>What we treat</h2>
      <div class="grid">
        <div class="card">
          <h3>Sports injuries</h3>
          <p>From sprains and strains to overuse injuries, we help athletes of every level recover and return to play with a plan built around their sport.</p>
        </div>
        <div class="card">
          <h3>Post-surgery rehab</h3>
          <p>Recovering from surgery takes more than time. We guide you through each stage of healing to restore strength, motion and confidence.</p>
        </div>
        <div class="card">
          <h3>Back pain</h3>
          <p>We look for the cause of your pain, not just the symptoms, and give you the tools to feel better and stay that way.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="alt">
    <div class="wrap">
      <h2>Your first visit</h2>
      <p>Your first appointment is a full 60 minutes. We'll talk through your history and goals, assess how you move, and explain what we find in plain language. You'll leave with a clear plan for your recovery.</p>
      <p>Our two therapists work with you directly, so you get consistent, personal care from start to finish.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Insurance</h2>
      <!-- TODO: list the specific plans we accept once confirmed. -->
      <p>We take most major insurance plans. Contact us and we'll help you check your coverage before your first visit.</p>
    </div>
  </section>

  <section class="alt" id="contact">
    <div class="wrap">
      <h2>Visit us</h2>
      <p><strong>Fernwood Physical Therapy</strong><br>
        Marlow Heights<br>
        [Street address]</p>
      <p><strong>Hours:</strong> Monday to Saturday<br>
        [Add opening and closing times]</p>
      <p><strong>Phone:</strong> [Phone number]<br>
        <strong>Email:</strong> [Email address]</p>
      <a class="btn" href="tel:">Call to book</a>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    &copy; 2026 Fernwood Physical Therapy &middot; Marlow Heights
  </div>
</footer>

</body>
</html>
```

**Before you publish:**
1. Confirm you're still accepting new patients. If not, delete that badge.
2. Check the award and patient-count wording.
3. Fill in the address, hours, phone and email. The "Call to book" button needs a real `tel:` number.
4. Add the specific insurance plans once you've looked them up. Until then the page says "most major insurance plans," which matches what you told me.

I also wrote the descriptive copy, like "hands-on, one-on-one" and "plain language." Change anything that doesn't match how you work.
