Here's a tidied version. It keeps the same behavior (POST `{delay: boolean}` to `/api/prefs`) and fixes the rough edges.

```html
<form class="setting-card" id="prefs">
  <div class="setting">
    <label id="delay-label" for="delay">Email me when a ferry is delayed</label>
    <button type="button" id="delay" class="switch" role="switch"
            aria-checked="false" aria-labelledby="delay-label"></button>
  </div>

  <div class="actions">
    <button type="submit" id="save" class="btn">Save</button>
    <span id="status" role="status" aria-live="polite"></span>
  </div>
</form>

<style>
  .setting-card {
    width: 320px;
    padding: 16px;
    font: 15px/1.4 system-ui, sans-serif;
    color: #1a1a1a;
    border: 1px solid #e2e2e2;
    border-radius: 8px;
  }

  .setting {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
  }

  .switch {
    flex: none;
    position: relative;
    width: 40px;
    height: 22px;
    padding: 0;
    border: 0;
    border-radius: 11px;
    background: #767676;
    cursor: pointer;
    transition: background-color .15s;
  }
  .switch::after {
    content: '';
    position: absolute;
    top: 2px;
    left: 2px;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #fff;
    transition: transform .15s;
  }
  .switch[aria-checked="true"] { background: #1f7a5c; }
  .switch[aria-checked="true"]::after { transform: translateX(18px); }
  .switch:focus-visible,
  .btn:focus-visible { outline: 2px solid #1f5fbf; outline-offset: 2px; }

  .actions {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 16px;
  }
  .btn {
    padding: 6px 16px;
    border: 0;
    border-radius: 6px;
    background: #1f5fbf;
    color: #fff;
    font: inherit;
    cursor: pointer;
  }
  .btn:disabled { opacity: .6; cursor: default; }

  #status { font-size: 13px; color: #555; }
  #status.error { color: #b3261e; }

  @media (prefers-reduced-motion: reduce) {
    .switch, .switch::after { transition: none; }
  }
</style>

<script>
  const form = document.getElementById('prefs');
  const toggle = document.getElementById('delay');
  const saveBtn = document.getElementById('save');
  const status = document.getElementById('status');

  function setStatus(text, isError = false) {
    status.textContent = text;
    status.classList.toggle('error', isError);
  }

  toggle.addEventListener('click', () => {
    const on = toggle.getAttribute('aria-checked') !== 'true';
    toggle.setAttribute('aria-checked', String(on));
    setStatus('');
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    saveBtn.disabled = true;
    setStatus('Saving…');
    try {
      const res = await fetch('/api/prefs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ delay: toggle.getAttribute('aria-checked') === 'true' }),
      });
      if (!res.ok) throw new Error(res.status);
      setStatus('Saved');
    } catch {
      setStatus('Couldn’t save. Please try again.', true);
    } finally {
      saveBtn.disabled = false;
    }
  });
</script>
```

**What changed**
- **Switch:** it's now a real `<button role="switch">` with `aria-checked`, so it works with the keyboard (Tab, Space, Enter) and screen readers. Before, it was a bare `<div>`. The visible text labels it.
- **Visuals:**
  - The knob slides with a transition, which is turned off for reduced-motion users.
  - There's a visible focus ring.
  - The off-state gray is darker so it's easier to see.
  - The row is vertically centered, with a gap between the text and the switch.
  - The group sits in a bordered card with a styled Save button.
- **Save feedback:** before, a click on Save did nothing visible. Now the button disables while saving, and the page shows "Saved" or an error message. Failures used to be silent.
- **Code:** it uses `addEventListener` instead of `onclick`, and the state lives in `aria-checked` instead of a CSS class.

**Things to check**
- I added a `Content-Type: application/json` header to the request. If your server only accepts the old header-less request, remove that line.
- The toggle always starts off. If the user's saved preference should load first, you'll need a GET on `/api/prefs` to set the initial state. I didn't add that because I can't see your API.
