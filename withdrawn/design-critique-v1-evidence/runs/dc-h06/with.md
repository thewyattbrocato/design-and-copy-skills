```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Request a Quote | Duran & Sons Plumbing</title>
<style>
  :root {
    --navy: #12324a;
    --blue: #1f6f9f;
    --blue-dark: #165579;
    --bg: #eef2f5;
    --border: #c9d3db;
    --text: #1c2630;
    --muted: #5b6b78;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 24px 16px;
    background: var(--bg);
    color: var(--text);
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.5;
  }
  .card {
    width: 100%;
    max-width: 520px;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 4px 24px rgba(18, 50, 74, 0.12);
    overflow: hidden;
  }
  header {
    background: var(--navy);
    color: #fff;
    padding: 28px 32px;
  }
  header h1 {
    margin: 0;
    font-size: 1.35rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }
  header p {
    margin: 4px 0 0;
    font-size: 0.95rem;
    color: #b9d3e6;
  }
  form { padding: 28px 32px 32px; }
  .field { margin-bottom: 18px; }
  label {
    display: block;
    margin-bottom: 6px;
    font-size: 0.9rem;
    font-weight: 600;
  }
  input, select, textarea {
    width: 100%;
    padding: 11px 12px;
    font: inherit;
    color: inherit;
    background: #fff;
    border: 1px solid var(--border);
    border-radius: 8px;
    transition: border-color 0.15s, box-shadow 0.15s;
  }
  textarea { resize: vertical; min-height: 110px; }
  input:focus, select:focus, textarea:focus {
    outline: none;
    border-color: var(--blue);
    box-shadow: 0 0 0 3px rgba(31, 111, 159, 0.25);
  }
  button {
    width: 100%;
    padding: 14px;
    font: inherit;
    font-weight: 700;
    letter-spacing: 0.04em;
    color: #fff;
    background: var(--blue);
    border: 0;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.15s;
  }
  button:hover { background: var(--blue-dark); }
  button:focus-visible { outline: 3px solid rgba(31, 111, 159, 0.4); outline-offset: 2px; }
  .note {
    margin: 14px 0 0;
    text-align: center;
    font-size: 0.82rem;
    color: var(--muted);
  }
  @media (max-width: 480px) {
    header, form { padding-left: 20px; padding-right: 20px; }
  }
</style>
</head>
<body>
  <main class="card">
    <header>
      <h1>Duran &amp; Sons Plumbing</h1>
      <p>Request a quote</p>
    </header>

    <form method="post" action="#">
      <div class="field">
        <label for="name">Name</label>
        <input id="name" name="name" type="text" autocomplete="name" required>
      </div>

      <div class="field">
        <label for="phone">Phone</label>
        <input id="phone" name="phone" type="tel" autocomplete="tel" required>
      </div>

      <div class="field">
        <label for="address">Address</label>
        <input id="address" name="address" type="text" autocomplete="street-address" required>
      </div>

      <div class="field">
        <label for="job">Job type</label>
        <select id="job" name="job_type">
          <option>Leak</option>
          <option>Blocked drain</option>
          <option>Water heater</option>
          <option>Other</option>
        </select>
      </div>

      <div class="field">
        <label for="details">Describe the problem</label>
        <textarea id="details" name="details" rows="4"></textarea>
      </div>

      <button type="submit">Send request</button>
      <p class="note">We'll get back to you with a quote as soon as possible.</p>
    </form>
  </main>
</body>
</html>
```

Two things to know:

- **Form action:** Your original had no `<form>` tag, so SEND didn't submit anywhere. I wrapped the fields in one with `action="#"`. Replace that with your real endpoint (a Formspree URL, your server script, or a `mailto:`), or the button still won't send anything.
- **Additions you didn't ask for:** Name, phone and address are now required. I also added `name` attributes, which a form needs in order to send data. The footer line under the button ("We'll get back to you with a quote as soon as possible.") is placeholder wording, so edit or delete it.
