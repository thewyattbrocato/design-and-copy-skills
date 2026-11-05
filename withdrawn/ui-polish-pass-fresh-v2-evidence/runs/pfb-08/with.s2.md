Here are the changed pieces. The layout, field order and labels are the same.

```html
<form id="vol" novalidate>
 <label for="vname">Name</label>
 <input id="vname" name="name" autocomplete="name">
 <label for="vemail">Email</label>
 <input id="vemail" name="email" type="email" autocomplete="email"
        aria-describedby="msg" inputmode="email" autocapitalize="off" spellcheck="false">
 <button id="send" type="submit">Sign me up</button>
 <p id="msg" role="status" aria-live="polite"></p>
</form>
<div class="dots" aria-hidden="true"></div>
<script>
 const f = document.getElementById('vol');
 const email = document.getElementById('vemail');
 const send = document.getElementById('send');
 const msg = document.getElementById('msg');
 const dots = document.querySelector('.dots');

 function say(text, kind) {
  msg.textContent = text;
  msg.className = kind || '';
 }

 email.addEventListener('input', () => {
  if (email.getAttribute('aria-invalid')) {
   email.removeAttribute('aria-invalid');
   say('');
  }
 });

 f.addEventListener('submit', async e => {
  e.preventDefault();
  if (send.disabled) return;

  if (!email.value.trim() || !email.validity.valid) {
   email.setAttribute('aria-invalid', 'true');
   say(email.value.trim()
     ? 'That email doesn’t look right. Check it for typos, like name@example.com.'
     : 'Enter your email so we can reach you.', 'error');
   email.focus();
   return;
  }

  send.disabled = true;
  send.textContent = 'Signing you up…';
  f.setAttribute('aria-busy', 'true');
  say('');
  dots.classList.add('spin');
  try {
   const r = await fetch('/api/volunteers', {method: 'POST', body: new FormData(f)});
   if (r.ok) {
    f.reset();
    say('Thanks, you’re signed up.', 'ok');
   } else {
    say('We couldn’t sign you up. What you typed is still here, so please try again.', 'error');
   }
  } catch (err) {
   say('We couldn’t reach the server. Check your connection and try again. What you typed is still here.', 'error');
  } finally {
   dots.classList.remove('spin');
   f.removeAttribute('aria-busy');
   send.disabled = false;
   send.textContent = 'Sign me up';
  }
 });
</script>
<style>
 .dots{min-height:24px}
 .spin{width:24px;height:24px;border:3px solid #ccc;border-top-color:#333;border-radius:50%;animation:turn 1s linear infinite}
 @keyframes turn{to{transform:rotate(360deg)}}
 @media (prefers-reduced-motion:reduce){.spin{animation-duration:3s}}
 #msg{margin-top:12px}
 #msg.ok{color:#1a6b2f}
 #msg.error{color:#b00020}
 input[aria-invalid="true"]{border:2px solid #b00020}
 button:disabled{cursor:progress}
</style>
```

**What changed, in order of importance**
- **Network failure:** before, a dropped connection threw an error, left the spinner running and gave no message. Now `try/catch/finally` always stops the spinner, re-enables the button and shows a message.
- **Double submit:** the button disables while sending and reads "Signing you up…".
- **Bad email:** before, the only sign was a red border, which relies on color alone and never cleared. Now there's a message in words, `aria-invalid`, and focus moves to the field. The error clears when they start typing. The check uses the browser's email validation instead of `includes('@')`.
- **Result message:** "Done" and "Something went wrong" are now plain sentences that say what to do next. They're announced to screen readers via `role="status"`. The form clears on success so a second click can't sign them up twice. On failure it keeps what they typed.
- **Contrast:** pure `red` on white is too faint for text, so I swapped it for a darker red and green.
- **Spinner space:** `.dots` reserves its height so the page doesn't jump when the spinner appears.
- **Reduced motion:** the spinner slows down, but it still shows.

**Notes**
- Name is still optional, as in your original. If volunteers must give one, say so and I'll add the same check.
- I haven't run this in a browser or with a screen reader. Before the meeting, try it once with the network off (DevTools → Offline) to see the failure message.
