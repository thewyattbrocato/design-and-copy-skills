I couldn't save the file because the Write tool is disabled in this session. The full single-page HTML is below, so you can save it as `claim-step-2-incident.html` and open it in a browser. I haven't opened or tested it in a browser.

**Layout decisions**
- **Progress:** a four-segment named bar (Policy details, Incident, Documents upload, Review and submit) with `aria-current="step"`. Text such as "Step 2 · Current" means state isn't shown by colour alone. The heading area also says "Step 2 of 4". On phones, only the current step's label shows.
- **Required fields:** all three fields are required, so a single line says "All questions are required". There are no asterisks.
- **Date:** a visible label with a hint, a native date input at a short width, and a `max` of today.
- **Type:** three radios in a fieldset, each with a one-line description so people can compare them. Each option is a full-width tap target of at least 44px.
- **Description:** a visible label with a hint saying what to include, and a resizable textarea.
- **Buttons:** "Continue to documents" is the primary action. "Back to policy details" is a quieter text-style button. On mobile they stack with Continue on top.
- **Validation:** nothing shows an error until the first submit. After that, each error clears as the field is fixed. Continue stays pressable. Errors appear inline with a ⚠ cue, and an error summary links to each field.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Incident, step 2 of 4 – Make a claim</title>
<style>
  :root {
    --ink: #1f2933; --muted: #52606d; --line: #9aa5b1; --soft: #e4e7eb;
    --bg: #f5f7fa; --brand: #0b5cad; --brand-dark: #084680;
    --error: #b42318; --error-bg: #fef3f2;
  }
  * { box-sizing: border-box; }
  body { margin: 0; font: 16px/1.5 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; color: var(--ink); background: var(--bg); }
  main { max-width: 640px; margin: 0 auto; padding: 24px 16px 48px; }
  .brand { font-weight: 700; color: var(--brand); margin: 0 0 16px; }

  .steps { display: flex; list-style: none; margin: 0 0 24px; padding: 0; gap: 8px; }
  .steps li { flex: 1; border-top: 4px solid var(--soft); padding-top: 8px; font-size: 14px; color: var(--muted); }
  .steps li.done { border-top-color: var(--brand); }
  .steps li.current { border-top-color: var(--brand); color: var(--ink); font-weight: 700; }
  .steps .n { display: block; font-size: 12px; font-weight: 400; color: var(--muted); }
  @media (max-width: 480px) {
    .steps li .label { display: none; }
    .steps li.current .label { display: inline; }
    .steps li.current { flex: 3; }
  }

  h1 { font-size: 1.75rem; line-height: 1.2; margin: 0 0 4px; }
  .step-count { color: var(--muted); margin: 0 0 24px; }
  .card { background: #fff; border: 1px solid var(--soft); border-radius: 8px; padding: 24px; }

  .field { margin: 0 0 32px; padding: 0; border: 0; min-width: 0; }
  label, legend { display: block; font-weight: 600; padding: 0; margin-bottom: 4px; }
  .hint { color: var(--muted); font-size: 14px; margin: 0 0 8px; }
  input[type="date"], textarea {
    font: inherit; color: inherit; border: 1px solid var(--line);
    border-radius: 6px; background: #fff; padding: 10px 12px;
  }
  input[type="date"] { min-height: 44px; width: 12rem; }
  textarea { width: 100%; min-height: 9rem; resize: vertical; }
  :focus-visible { outline: 3px solid #f7b500; outline-offset: 2px; }

  .options { display: grid; gap: 8px; }
  .option {
    display: flex; align-items: flex-start; gap: 12px; min-height: 44px;
    padding: 10px 12px; border: 1px solid var(--line); border-radius: 6px;
    font-weight: 400; margin: 0; cursor: pointer;
  }
  .option input { width: 20px; height: 20px; margin: 2px 0 0; flex: none; accent-color: var(--brand); }
  .option:has(input:checked) { border-color: var(--brand); box-shadow: inset 0 0 0 1px var(--brand); background: #f0f7ff; }
  .option b { display: block; font-weight: 600; }
  .option span { display: block; color: var(--muted); font-size: 14px; }

  .error { display: none; color: var(--error); font-size: 14px; margin: 6px 0 0; font-weight: 600; }
  .error::before { content: "\26A0\FE0E  "; }
  .has-error .error { display: block; }
  .has-error input[type="date"], .has-error textarea { border-color: var(--error); border-width: 2px; }
  .summary { display: none; background: var(--error-bg); border: 2px solid var(--error); border-radius: 6px; padding: 12px 16px; margin-bottom: 24px; }
  .summary.show { display: block; }
  .summary h2 { font-size: 1rem; margin: 0 0 4px; color: var(--error); }
  .summary ul { margin: 0; padding-left: 20px; }
  .summary a { color: var(--error); }

  .actions { display: flex; gap: 12px; align-items: center; }
  .btn { font: inherit; font-weight: 600; min-height: 44px; padding: 10px 20px; border-radius: 6px; cursor: pointer; border: 2px solid var(--brand); }
  .btn.primary { background: var(--brand); color: #fff; }
  .btn.primary:hover { background: var(--brand-dark); border-color: var(--brand-dark); }
  .btn.secondary { background: #fff; color: var(--brand); border-color: transparent; }
  .btn.secondary:hover { text-decoration: underline; }
  .saved { color: var(--muted); font-size: 14px; margin: 16px 0 0; }
  @media (max-width: 480px) {
    .card { padding: 16px; }
    .actions { flex-direction: column-reverse; align-items: stretch; }
  }
</style>
</head>
<body>
<main>
  <p class="brand">Pawsure Pet Insurance</p>

  <nav aria-label="Claim progress">
    <ol class="steps">
      <li class="done"><span class="n">Step 1 · Complete</span><span class="label">Policy details</span></li>
      <li class="current" aria-current="step"><span class="n">Step 2 · Current</span><span class="label">Incident</span></li>
      <li><span class="n">Step 3</span><span class="label">Documents upload</span></li>
      <li><span class="n">Step 4</span><span class="label">Review and submit</span></li>
    </ol>
  </nav>

  <h1>Incident</h1>
  <p class="step-count">Step 2 of 4. All questions are required.</p>

  <form class="card" id="incident-form" novalidate>
    <div class="summary" id="summary" role="alert" tabindex="-1">
      <h2>There is a problem</h2>
      <ul id="summary-list"></ul>
    </div>

    <div class="field" id="f-date">
      <label for="date">Date of incident</label>
      <p class="hint" id="date-hint">The day your pet was hurt or first showed symptoms. Best guess is fine.</p>
      <input type="date" id="date" name="incident_date" aria-describedby="date-hint date-error">
      <p class="error" id="date-error"></p>
    </div>

    <fieldset class="field" id="f-type" aria-describedby="type-error">
      <legend>Type of incident</legend>
      <div class="options">
        <label class="option">
          <input type="radio" name="incident_type" value="accident">
          <div><b>Accident</b><span>An injury, such as a broken leg or swallowing something harmful</span></div>
        </label>
        <label class="option">
          <input type="radio" name="incident_type" value="illness">
          <div><b>Illness</b><span>A condition, infection or disease</span></div>
        </label>
        <label class="option">
          <input type="radio" name="incident_type" value="other">
          <div><b>Other</b><span>Something that doesn’t fit the above</span></div>
        </label>
      </div>
      <p class="error" id="type-error"></p>
    </fieldset>

    <div class="field" id="f-desc">
      <label for="desc">What happened?</label>
      <p class="hint" id="desc-hint">Describe the symptoms or injury, when you noticed them, and any treatment so far.</p>
      <textarea id="desc" name="description" rows="6" aria-describedby="desc-hint desc-error"></textarea>
      <p class="error" id="desc-error"></p>
    </div>

    <div class="actions">
      <button type="button" class="btn secondary" id="back">Back to policy details</button>
      <button type="submit" class="btn primary">Continue to documents</button>
    </div>
    <p class="saved">Your answers are saved if you go back.</p>
  </form>
</main>

<script>
  const form = document.getElementById('incident-form');
  const summary = document.getElementById('summary');
  const list = document.getElementById('summary-list');
  const date = document.getElementById('date');
  const desc = document.getElementById('desc');
  const today = new Date().toISOString().slice(0, 10);
  date.max = today;

  const checks = {
    date: () => !date.value ? 'Enter the date of the incident, like 14/03/2026.'
      : date.value > today ? 'Enter a date that is today or earlier.' : '',
    type: () => form.incident_type.value ? '' : 'Select the type of incident: accident, illness or other.',
    desc: () => desc.value.trim() ? '' : 'Describe what happened, even briefly.'
  };
  let submitted = false;

  function show(key) {
    const msg = checks[key]();
    document.getElementById(key + '-error').textContent = msg;
    document.getElementById('f-' + key).classList.toggle('has-error', !!msg);
    const input = document.getElementById(key);
    if (input) input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    return msg;
  }

  function run() {
    const errors = [];
    for (const key of Object.keys(checks)) {
      const msg = show(key);
      if (msg) errors.push([key, msg]);
    }
    list.innerHTML = '';
    errors.forEach(([key, msg]) => {
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = '#f-' + key;
      a.textContent = msg;
      a.addEventListener('click', e => {
        e.preventDefault();
        (key === 'type' ? form.querySelector('input[name="incident_type"]') : document.getElementById(key)).focus();
      });
      li.appendChild(a);
      list.appendChild(li);
    });
    summary.classList.toggle('show', errors.length > 0);
    return errors;
  }

  form.addEventListener('submit', e => {
    e.preventDefault();
    submitted = true;
    const errors = run();
    document.title = (errors.length ? errors.length + ' error' + (errors.length > 1 ? 's' : '') + ' – ' : '')
      + 'Incident, step 2 of 4 – Make a claim';
    if (errors.length) summary.focus();
    else alert('Demo: this would go to step 3, Documents upload.');
  });

  // After a first submit, messages clear as soon as a field is fixed.
  form.addEventListener('input', () => { if (submitted) run(); });
  document.getElementById('back').addEventListener('click', () => {
    alert('Demo: this would return to step 1, keeping your answers.');
  });
</script>
</body>
</html>
```

If you enable Write, I can save it to the working directory.
