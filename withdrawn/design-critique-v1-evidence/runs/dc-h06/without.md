```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Request a Quote | Duran &amp; Sons Plumbing</title>
<style>
  :root {
    --navy: #12355b;
    --navy-dark: #0c2542;
    --text: #1e2a38;
    --muted: #5d6b7a;
    --border: #cbd5e0;
    --bg: #eef2f6;
    --focus: #2f80ed;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    min-height: 100vh;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding: 40px 16px;
    background: var(--bg);
    color: var(--text);
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    line-height: 1.5;
  }
  .card {
    width: 100%;
    max-width: 520px;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(16, 24, 40, .08), 0 8px 24px rgba(16, 24, 40, .06);
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
    letter-spacing: .06em;
    text-transform: uppercase;
  }
  header p {
    margin: 4px 0 0;
    font-size: .9rem;
    opacity: .8;
  }
  form { padding: 28px 32px 32px; }
  .field { margin-bottom: 20px; }
  label {
    display: block;
    margin-bottom: 6px;
    font-size: .875rem;
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
    transition: border-color .15s, box-shadow .15s;
  }
  textarea { resize: vertical; min-height: 110px; }
  input:focus, select:focus, textarea:focus {
    outline: none;
    border-color: var(--focus);
    box-shadow: 0 0 0 3px rgba(47, 128, 237, .25);
  }
  button {
    width: 100%;
    padding: 13px;
    font: inherit;
    font-weight: 600;
    letter-spacing: .04em;
    color: #fff;
    background: var(--navy);
    border: 0;
    border-radius: 8px;
    cursor: pointer;
    transition: background .15s;
  }
  button:hover { background: var(--navy-dark); }
  button:focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; }
  @media (max-width: 480px) {
    body { padding: 0; }
    .card { border-radius: 0; box-shadow: none; }
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

    <form method="post">
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
    </form>
  </main>
</body>
</html>
```

What changed:
- **Layout:** It's now a centered card with a navy header. It's responsive and goes full-width on phones.
- **Form:** I replaced the table layout with proper labels tied to their inputs. The fields are full-width with focus rings, and the button has hover and keyboard focus states.
- **Fonts:** System fonts only, as you asked.
- **Behavior:** Name, phone and address are required. The phone field uses `type="tel"`, so phones show the number pad. Autofill hints are set.

Your original form had no `action`, so as before it doesn't send anywhere yet. Add `action="..."` to the `<form>` tag with your form handler or service URL. I also gave each field a `name` attribute, which a form needs to submit its data.
