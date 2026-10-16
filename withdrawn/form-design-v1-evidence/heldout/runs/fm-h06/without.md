I don't have a file-writing tool in this session, so the full page is below. Save it as `claim-step-2.html` and open it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Submit a claim – Incident</title>
<style>
  :root {
    --bg: #f5f7f6;
    --card: #ffffff;
    --ink: #1c2b27;
    --muted: #5b6b66;
    --line: #d5dedb;
    --brand: #0f766e;
    --brand-dark: #0b5a54;
    --brand-tint: #e3f3f1;
    --focus: #1d4ed8;
    --radius: 10px;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font: 16px/1.5 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    color: var(--ink);
    background: var(--bg);
  }
  .wrap { max-width: 680px; margin: 0 auto; padding: 32px 16px 56px; }
  header.site { font-weight: 700; color: var(--brand); margin-bottom: 24px; }
  h1 { font-size: 1.6rem; margin: 0 0 4px; }
  .sub { color: var(--muted); margin: 0 0 28px; }

  /* Progress indicator */
  .steps {
    list-style: none; margin: 0 0 28px; padding: 0;
    display: flex; gap: 8px;
  }
  .steps li { flex: 1; position: relative; text-align: center; font-size: .85rem; color: var(--muted); }
  .steps li::before {            /* connector line */
    content: ""; position: absolute; top: 15px; left: -50%; width: 100%;
    height: 2px; background: var(--line); z-index: 0;
  }
  .steps li:first-child::before { display: none; }
  .steps .dot {
    position: relative; z-index: 1;
    display: grid; place-items: center;
    width: 32px; height: 32px; margin: 0 auto 6px;
    border-radius: 50%; border: 2px solid var(--line);
    background: var(--card); font-weight: 600;
  }
  .steps li.done::before, .steps li.current::before { background: var(--brand); }
  .steps li.done .dot { background: var(--brand); border-color: var(--brand); color: #fff; }
  .steps li.current .dot { border-color: var(--brand); color: var(--brand); box-shadow: 0 0 0 4px var(--brand-tint); }
  .steps li.current { color: var(--ink); font-weight: 600; }
  .step-count { display: none; }

  /* Card + form */
  .card {
    background: var(--card); border: 1px solid var(--line);
    border-radius: var(--radius); padding: 28px;
  }
  fieldset { border: 0; padding: 0; margin: 0 0 24px; min-width: 0; }
  legend, label.lbl { display: block; font-weight: 600; margin-bottom: 6px; padding: 0; }
  .hint { color: var(--muted); font-size: .875rem; margin: 0 0 8px; }
  .req { color: #b91c1c; }

  input[type="date"], textarea {
    width: 100%; font: inherit; color: inherit;
    padding: 10px 12px; border: 1px solid var(--line);
    border-radius: 8px; background: #fff;
  }
  input[type="date"] { max-width: 220px; }
  textarea { min-height: 140px; resize: vertical; }
  :is(input, textarea, button):focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; }

  /* Radio cards */
  .options { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
  .option input { position: absolute; opacity: 0; }
  .option span {
    display: block; padding: 12px; text-align: center; cursor: pointer;
    border: 1px solid var(--line); border-radius: 8px; font-weight: 500;
  }
  .option input:checked + span { border-color: var(--brand); background: var(--brand-tint); color: var(--brand-dark); font-weight: 600; }
  .option input:focus-visible + span { outline: 3px solid var(--focus); outline-offset: 2px; }
  .count { text-align: right; color: var(--muted); font-size: .8rem; margin-top: 4px; }

  /* Actions */
  .actions { display: flex; justify-content: space-between; gap: 12px; margin-top: 8px; }
  button {
    font: inherit; font-weight: 600; padding: 11px 24px;
    border-radius: 8px; cursor: pointer; border: 1px solid transparent;
  }
  .btn-back { background: #fff; color: var(--ink); border-color: var(--line); }
  .btn-back:hover { background: var(--bg); }
  .btn-next { background: var(--brand); color: #fff; }
  .btn-next:hover { background: var(--brand-dark); }

  @media (max-width: 520px) {
    .card { padding: 20px 16px; }
    .options { grid-template-columns: 1fr; }
    .steps li span.label { display: none; }
    .steps li.current span.label { display: block; position: absolute; left: 50%; transform: translateX(-50%); white-space: nowrap; }
    .steps { margin-bottom: 44px; }
    .actions { flex-direction: column-reverse; }
    button { width: 100%; }
  }
</style>
</head>
<body>
<div class="wrap">
  <header class="site">PawSure Pet Insurance</header>
  <h1>Submit a claim</h1>
  <p class="sub">Step 2 of 4 &middot; Tell us what happened.</p>

  <nav aria-label="Claim progress">
    <ol class="steps">
      <li class="done"><span class="dot" aria-hidden="true">&#10003;</span><span class="label">Policy details</span></li>
      <li class="current" aria-current="step"><span class="dot">2</span><span class="label">Incident</span></li>
      <li><span class="dot">3</span><span class="label">Documents</span></li>
      <li><span class="dot">4</span><span class="label">Review &amp; submit</span></li>
    </ol>
  </nav>

  <form class="card" action="#" method="post">
    <fieldset>
      <label class="lbl" for="incident-date">Date of incident <span class="req" aria-hidden="true">*</span></label>
      <p class="hint" id="date-hint">The day symptoms started or the accident occurred.</p>
      <input type="date" id="incident-date" name="incident_date" required aria-describedby="date-hint">
    </fieldset>

    <fieldset>
      <legend>Type of incident <span class="req" aria-hidden="true">*</span></legend>
      <div class="options">
        <label class="option"><input type="radio" name="type" value="accident" required><span>Accident</span></label>
        <label class="option"><input type="radio" name="type" value="illness"><span>Illness</span></label>
        <label class="option"><input type="radio" name="type" value="other"><span>Other</span></label>
      </div>
    </fieldset>

    <fieldset>
      <label class="lbl" for="description">Description <span class="req" aria-hidden="true">*</span></label>
      <p class="hint" id="desc-hint">Include symptoms, how it happened, and any treatment so far.</p>
      <textarea id="description" name="description" maxlength="1000" required aria-describedby="desc-hint"
        oninput="document.getElementById('c').textContent=this.value.length"></textarea>
      <div class="count"><span id="c">0</span> / 1000</div>
    </fieldset>

    <div class="actions">
      <button type="button" class="btn-back">Back</button>
      <button type="submit" class="btn-next">Continue</button>
    </div>
  </form>
</div>
</body>
</html>
```

**Layout decisions**
- **Progress indicator:** four numbered steps joined by a line. Completed steps show a checkmark, the current step has a ring, and it carries `aria-current="step"`. On narrow screens only the current step's label is shown.
- **Form card:** a single column in the order date, type, description, so the page reads top to bottom. Labels sit above the fields, with hint text for guidance.
- **Type radios:** styled as selectable cards for large tap targets. The native radio inputs stay in the DOM, so keyboard and screen-reader behavior is unchanged.
- **Actions:** Back is the secondary outline button on the left. Continue is the primary filled button on the right. On mobile they stack, with Continue on top.
- **Validation:** the fields use native `required`. Add inline error messages when you wire it up.

The company name "PawSure" is a placeholder.
