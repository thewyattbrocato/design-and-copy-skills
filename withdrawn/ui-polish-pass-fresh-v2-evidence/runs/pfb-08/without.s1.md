Here's a polished version. The markup order is unchanged, so the layout is the same.

```html
<form id="vol" novalidate>
 <label for="vname">Name</label>
 <input id="vname" name="name" autocomplete="name" required aria-describedby="msg">
 <label for="vemail">Email</label>
 <input id="vemail" name="email" type="email" autocomplete="email" required aria-describedby="msg">
 <button id="send" type="submit">Sign me up</button>
 <p id="msg" role="status" aria-live="polite"></p>
</form>
<div class="dots" aria-hidden="true"></div>
<script>
 const f = document.getElementById('vol');
 const nameIn = document.getElementById('vname');
 const email = document.getElementById('vemail');
 const send = document.getElementById('send');
 const msg = document.getElementById('msg');
 const dots = document.querySelector('.dots');

 function show(text, ok) {
  msg.textContent = text;
  msg.className = ok ? 'ok' : 'err';
 }

 // Clear the error styling as soon as the user starts fixing a field
 [nameIn, email].forEach(el => el.addEventListener('input', () => {
  el.removeAttribute('aria-invalid');
  if (msg.className === 'err') show('', true);
 }));

 f.addEventListener('submit', async e => {
  e.preventDefault();
  if (send.disabled) return;

  [nameIn, email].forEach(el => el.removeAttribute('aria-invalid'));

  if (!nameIn.value.trim()) {
   nameIn.setAttribute('aria-invalid', 'true');
   show('Please enter your name.', false);
   nameIn.focus();
   return;
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) {
   email.setAttribute('aria-invalid', 'true');
   show('Please enter a valid email address.', false);
   email.focus();
   return;
  }

  send.disabled = true;
  send.textContent = 'Signing up…';
  show('', true);
  dots.classList.add('spin');

  try {
   const r = await fetch('/api/volunteers', {method: 'POST', body: new FormData(f)});
   if (r.ok) {
    show('Thank you! You’re signed up. We’ll be in touch soon.', true);
    f.reset();
   } else {
    show('Something went wrong. Please try again.', false);
   }
  } catch (err) {
   show('Couldn’t reach the server. Check your connection and try again.', false);
  } finally {
   dots.classList.remove('spin');
   send.disabled = false;
   send.textContent = 'Sign me up';
  }
 });
</script>
<style>
 .dots{min-height:30px}
 .spin{width:24px;height:24px;border:3px solid #ccc;border-top-color:#333;border-radius:50%;animation:turn 1s linear infinite}
 @keyframes turn{to{transform:rotate(360deg)}}
 @media (prefers-reduced-motion:reduce){.spin{animation-duration:3s}}
 #msg{margin-top:12px;min-height:1.5em}
 #msg.ok{color:#1a7f37}
 #msg.err{color:#c62828}
 input[aria-invalid="true"]{border-color:#c62828;outline-color:#c62828}
 button:disabled{opacity:.6;cursor:not-allowed}
</style>
```

**What changed**
- **Validation:** the email check is stricter than `includes('@')`. Errors now show a message and move focus to the field, where before it was only a red border that never cleared. The error clears when the user starts typing.
- **Double submits:** the button is disabled and reads "Signing up…" while the request is in flight.
- **Network failures:** a failed fetch used to leave the spinner running forever. It's now caught, and a `finally` block always resets the UI.
- **Success state:** the message is friendlier than "Done", and the form clears afterward.
- **Accessibility:** the message is announced by screen readers (`aria-live`). Errors no longer depend on color alone, and the green and red are darker for contrast. Reduced-motion users get a slower spinner.
- **Layout shift:** `.dots` reserves its height, so the page doesn't jump when the spinner appears.

**Decision for you:** I made Name required, since a sign-up with no name isn't much use. If your backend accepts blank names and you want that to stay, delete the name check block.

I didn't run this against your `/api/volunteers` endpoint. Before the meeting, do one real submit, plus one with the network off to see the error path.
