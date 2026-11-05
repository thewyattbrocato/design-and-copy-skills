Here's the polished version. The layout, field order and labels are unchanged.

```html
<form id="vol" novalidate>
 <label for="vname">Name</label>
 <input id="vname" name="name" autocomplete="name">
 <label for="vemail">Email</label>
 <input id="vemail" name="email" type="email" autocomplete="email"
        aria-describedby="emsg" required>
 <p id="emsg" class="err" hidden></p>
 <button id="send" type="submit">Sign me up</button>
 <p id="msg" role="status" aria-live="polite"></p>
</form>
<div class="dots" aria-hidden="true"></div>
<script>
 const f = document.getElementById('vol');
 const email = document.getElementById('vemail');
 const emsg = document.getElementById('emsg');
 const msg = document.getElementById('msg');
 const send = document.getElementById('send');
 const dots = document.querySelector('.dots');

 function setEmailError(text) {
  emsg.textContent = text || '';
  emsg.hidden = !text;
  email.toggleAttribute('aria-invalid', !!text);
  if (text) email.setAttribute('aria-invalid', 'true');
 }
 email.addEventListener('input', () => setEmailError(''));

 f.addEventListener('submit', async e => {
  e.preventDefault();
  if (send.disabled) return;
  msg.textContent = '';
  const v = email.value.trim();
  if (!v) {
   setEmailError('Enter your email so we can reach you.');
   email.focus();
   return;
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) {
   setEmailError('That email looks incomplete. It should look like name@example.org.');
   email.focus();
   return;
  }
  setEmailError('');

  send.disabled = true;
  send.textContent = 'Signing you up…';
  f.setAttribute('aria-busy', 'true');
  dots.classList.add('spin');
  let ok = false;
  try {
   const r = await fetch('/api/volunteers', {method: 'POST', body: new FormData(f)});
   ok = r.ok;
  } catch (_) {}
  dots.classList.remove('spin');
  f.removeAttribute('aria-busy');
  send.disabled = false;
  send.textContent = 'Sign me up';

  if (ok) {
   msg.textContent = 'Thank you, you’re signed up as a volunteer.';
   msg.className = 'ok';
   f.reset();
  } else {
   msg.textContent = 'We couldn’t send your sign-up. Your details are still here, so please press “Sign me up” to try again.';
   msg.className = 'bad';
  }
 });
</script>
<style>
 .spin{width:24px;height:24px;border:3px solid #ccc;border-top-color:#333;border-radius:50%;animation:turn 1s linear infinite}
 @keyframes turn{to{transform:rotate(360deg)}}
 #msg{margin-top:12px}
 #msg.ok{color:#1a6b2a}
 #msg.bad{color:#b00020}
 .err{color:#b00020;margin:4px 0 0}
 input[aria-invalid]{border:2px solid #b00020}
 button:disabled{cursor:progress;opacity:.7}
 :focus-visible{outline:2px solid #1a4fd6;outline-offset:2px}
 @media (prefers-reduced-motion:reduce){.spin{animation:none;border-top-color:#ccc}}
</style>
```

**What changed**
- **Email errors:** the red border alone is now an inline message that says what to fix. It's linked to the field, flags it as invalid for screen readers, and moves focus there. It clears when the person types. Empty and malformed emails get separate messages, and the check is stricter than `includes('@')`.
- **Submit:** the button disables and reads "Signing you up…" while the request runs, so a second click can't double-submit.
- **Network failure:** a dropped connection used to leave the page stuck. It now shows the failure message.
- **Result messages:** the status area is announced to screen readers. "Done" became a clear thank-you, and the failure message says what to do next. The form keeps what was typed on failure and clears only on success.
- **Contrast:** the plain `red` text failed contrast, so I swapped it for a darker red and a slightly darker green. Both messages now say what happened in words, not just color.
- **Focus and motion:** there's a visible focus ring. With reduced motion the spinner stops, and the button text still shows the busy state.

**Notes**
- I kept the name field optional, since the original didn't require it. Tell me if you want it required.
- I haven't run this in a browser or with a screen reader, and I haven't tried your real `/api/volunteers` endpoint. Before the meeting, try one successful sign-up, one blocked request (offline in DevTools) and a bad email.
- The 24px spinner still appears below the form only while it spins, as before. The button text carries the busy state, so a small layout shift there is the only side effect.
