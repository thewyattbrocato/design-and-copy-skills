I couldn't save this to a file because the Write tool is disabled in this session. The complete file is below, so you can save it as `contact.html`. I haven't opened it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Contact us</title>
<style>
  :root {
    --text: #1d1d1f;
    --muted: #55595f;
    --border: #8a8f98;
    --accent: #0b5fd3;
    --error: #b3261e;
    --error-bg: #fdecea;
    --ok-bg: #e9f6ee;
    --ok: #17613a;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 24px 16px;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: var(--text);
    background: #f6f7f9;
    line-height: 1.5;
  }
  main {
    max-width: 480px;
    margin: 0 auto;
    padding: 24px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, .12);
  }
  h1 { margin: 0 0 4px; font-size: 1.5rem; }
  .intro { margin: 0 0 24px; color: var(--muted); }
  .field { margin-bottom: 20px; }
  label { display: block; margin-bottom: 4px; font-weight: 600; }
  .hint { margin: 0 0 6px; font-size: .875rem; color: var(--muted); }
  input, textarea {
    display: block;
    width: 100%;
    min-height: 44px;
    padding: 10px 12px;
    font: inherit;
    font-size: 1rem;
    color: inherit;
    background: #fff;
    border: 1px solid var(--border);
    border-radius: 6px;
  }
  textarea { min-height: 140px; resize: vertical; }
  input:focus, textarea:focus, button:focus-visible, .summary:focus {
    outline: 3px solid var(--accent);
    outline-offset: 2px;
  }
  [aria-invalid="true"] { border: 2px solid var(--error); padding: 9px 11px; }
  .error {
    display: none;
    margin: 6px 0 0;
    font-size: .875rem;
    color: var(--error);
    font-weight: 600;
  }
  .error::before { content: "\26A0\FE0E  "; }
  .field.has-error .error { display: block; }
  .summary {
    display: none;
    margin-bottom: 20px;
    padding: 12px 16px;
    background: var(--error-bg);
    border-left: 4px solid var(--error);
    border-radius: 4px;
  }
  .summary.show { display: block; }
  .summary h2 { margin: 0 0 6px; font-size: 1rem; color: var(--error); }
  .summary ul { margin: 0; padding-left: 20px; }
  .summary a { color: var(--error); }
  button {
    min-height: 44px;
    padding: 10px 24px;
    font: inherit;
    font-weight: 600;
    color: #fff;
    background: var(--accent);
    border: 0;
    border-radius: 6px;
    cursor: pointer;
  }
  button:hover { background: #094ca8; }
  .confirmation {
    padding: 16px;
    background: var(--ok-bg);
    color: var(--ok);
    border-radius: 6px;
  }
  .confirmation:focus { outline: 3px solid var(--accent); outline-offset: 2px; }
  .confirmation h2 { margin: 0 0 4px; font-size: 1.125rem; }
  .confirmation p { margin: 0; }
  [hidden] { display: none !important; }
</style>
</head>
<body>
<main>
  <h1>Contact us</h1>
  <p class="intro">All fields are required. We reply by email.</p>

  <div id="summary" class="summary" tabindex="-1" role="group" aria-labelledby="summary-title">
    <h2 id="summary-title"></h2>
    <ul id="summary-list"></ul>
  </div>

  <form id="contact" novalidate>
    <div class="field" data-field="name">
      <label for="name">Your name</label>
      <input id="name" name="name" type="text" autocomplete="name" aria-describedby="name-error" required>
      <p class="error" id="name-error"></p>
    </div>

    <div class="field" data-field="email">
      <label for="email">Email</label>
      <p class="hint" id="email-hint">For example, name@example.com</p>
      <input id="email" name="email" type="email" inputmode="email" autocomplete="email"
             autocapitalize="off" autocorrect="off" spellcheck="false"
             aria-describedby="email-hint email-error" required>
      <p class="error" id="email-error"></p>
    </div>

    <div class="field" data-field="message">
      <label for="message">Message</label>
      <textarea id="message" name="message" aria-describedby="message-error" required></textarea>
      <p class="error" id="message-error"></p>
    </div>

    <button type="submit" id="send">Send message</button>
  </form>

  <div id="confirmation" class="confirmation" tabindex="-1" hidden>
    <h2>Message sent</h2>
    <p>Thanks. We'll reply to <strong id="sent-to"></strong>, usually within two working days.</p>
  </div>
</main>

<script>
(function () {
  var form = document.getElementById('contact');
  var summary = document.getElementById('summary');
  var summaryTitle = document.getElementById('summary-title');
  var summaryList = document.getElementById('summary-list');
  var baseTitle = document.title;
  var submitted = false;

  var rules = {
    name: function (v) {
      return v.trim() ? '' : 'Enter your name.';
    },
    email: function (v) {
      v = v.trim();
      if (!v) return 'Enter your email address, like name@example.com.';
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)
        ? ''
        : 'Enter an email address with an @ and a domain, like name@example.com.';
    },
    message: function (v) {
      return v.trim() ? '' : 'Enter a message.';
    }
  };
  var labels = { name: 'Your name', email: 'Email', message: 'Message' };

  function setError(id, msg) {
    var input = document.getElementById(id);
    var wrap = input.closest('.field');
    document.getElementById(id + '-error').textContent = msg;
    wrap.classList.toggle('has-error', !!msg);
    if (msg) input.setAttribute('aria-invalid', 'true');
    else input.removeAttribute('aria-invalid');
  }

  function check(id) {
    var msg = rules[id](document.getElementById(id).value);
    setError(id, msg);
    return msg;
  }

  function renderSummary(errors) {
    summaryList.textContent = '';
    if (errors.length < 2) {
      summary.classList.remove('show');
      document.title = baseTitle;
      return;
    }
    summaryTitle.textContent = errors.length + ' problems to fix';
    errors.forEach(function (e) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = '#' + e.id;
      a.textContent = labels[e.id] + ': ' + e.msg;
      a.addEventListener('click', function (ev) {
        ev.preventDefault();
        document.getElementById(e.id).focus();
      });
      li.appendChild(a);
      summaryList.appendChild(li);
    });
    summary.classList.add('show');
    document.title = errors.length + ' problems - ' + baseTitle;
  }

  function collect() {
    return Object.keys(rules).map(function (id) {
      return { id: id, msg: check(id) };
    }).filter(function (e) { return e.msg; });
  }

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    submitted = true;
    var errors = collect();
    renderSummary(errors);
    if (errors.length > 1) {
      summary.focus();
      return;
    }
    if (errors.length === 1) {
      document.getElementById(errors[0].id).focus();
      return;
    }
    // Replace with a real request (fetch to your endpoint) and keep values if it fails.
    document.getElementById('sent-to').textContent = document.getElementById('email').value.trim();
    form.hidden = true;
    var c = document.getElementById('confirmation');
    c.hidden = false;
    c.focus();
  });

  // After a first submit, re-check as the person edits so messages clear once fixed.
  form.addEventListener('input', function (ev) {
    var id = ev.target.id;
    if (!submitted || !rules[id]) return;
    if (!ev.target.closest('.field').classList.contains('has-error')) return;
    check(id);
    var remaining = Object.keys(rules).filter(function (k) {
      return rules[k](document.getElementById(k).value);
    }).map(function (k) {
      return { id: k, msg: rules[k](document.getElementById(k).value) };
    });
    renderSummary(remaining);
  });
})();
</script>
</body>
</html>
```

**What I fixed**
- **Labels:** each field now has a visible `<label>` linked to it. Before, the placeholders were the only names, and they vanish once you type. The email field also gets a hint showing an example address.
- **Email input:** it is now `type="email"` with `inputmode="email"` and `autocomplete="email"`. Autocapitalize and spellcheck are off. The original was `type='text'`.
- **Autofill:** the name field has `autocomplete="name"`.
- **Send button:** it is no longer `disabled`. A button that is disabled until the form is valid doesn't tell people why. It now reads "Send message" and is always pressable.
- **Required fields:** the intro says all fields are required, so there are no unexplained asterisks.
- **Sizing:** input text is 16px, and fields and the button are at least 44px tall. This stops iOS zooming on focus and makes them easy to tap.
- **Focus:** focus outlines are visible.

**Error states**
- **Invalid email:** for something like `foo@bar`, the message under the field reads "Enter an email address with an @ and a domain, like name@example.com." It has a ⚠ icon, bold text and a thicker red border, so it doesn't rely on color alone. The input gets `aria-invalid`, and the message is tied to it with `aria-describedby`.
- **Timing:** nothing is checked until the first submit. After that, a field's message clears as soon as that field is fixed.
- **Several problems at once:** an error summary appears at the top with links to each field, focus moves to it, and the page title shows the count. With one problem, you get only the inline message and focus goes to that field.
- **Confirmation:** a successful submit shows a "Message sent" confirmation.

**Still to do:** the form has no `action` and doesn't send anything. The submit handler shows the confirmation, with a comment marking where to add your real request. Whatever receives the message should validate it again on the server.
