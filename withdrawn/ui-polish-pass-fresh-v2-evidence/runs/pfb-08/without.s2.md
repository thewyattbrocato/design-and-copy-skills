Here's a polished version. The markup and layout are the same, with the changes below.

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
 const nameEl = document.getElementById('vname');
 const email = document.getElementById('vemail');
 const send = document.getElementById('send');
 const msg = document.getElementById('msg');
 const dots = document.querySelector('.dots');

 function say(text, ok) {
  msg.textContent = text;
  msg.className = ok ? 'ok' : 'err';
 }

 function invalid(el, text) {
  el.setAttribute('aria-invalid', 'true');
  say(text, false);
  el.focus();
 }

 [nameEl, email].forEach(el => el.addEventListener('input', () => {
  el.removeAttribute('aria-invalid');
  if (msg.className === 'err') say('', true);
 }));

 f.addEventListener('submit', async e => {
  e.preventDefault();
  if (send.disabled) return;

  nameEl.value = nameEl.value.trim();
  email.value = email.value.trim();

  if (!nameEl.value) return invalid(nameEl, 'Please enter your name.');
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
   return invalid(email, 'Please enter a valid email address.');
  }

  send.disabled = true;
  say('', true);
  dots.classList.add('spin');
  try {
   const r = await fetch('/api/volunteers', {method: 'POST', body: new FormData(f)});
   if (r.ok) {
    say('Thank you! You\u2019re signed up. We\u2019ll be in touch soon.', true);
    f.reset();
   } else {
    say('Something went wrong. Please try again.', false);
   }
  } catch {
   say('Couldn\u2019t reach the server. Check your connection and try again.', false);
  } finally {
   dots.classList.remove('spin');
   send.disabled = false;
  }
 });
</script>
<style>
 input[aria-invalid="true"]{border:1px solid #b00020;outline-color:#b00020}
 button:disabled{opacity:.6;cursor:not-allowed}
 #msg{margin-top:12px;min-height:1.2em}
 #msg.ok{color:#146c2e}
 #msg.err{color:#b00020}
 .dots{width:24px;height:24px;border:3px solid transparent;border-radius:50%;visibility:hidden}
 .dots.spin{visibility:visible;border-color:#ccc;border-top-color:#333;animation:turn 1s linear infinite}
 @keyframes turn{to{transform:rotate(360deg)}}
 @media (prefers-reduced-motion:reduce){.dots.spin{animation-duration:3s}}
</style>
```

**What changed**
- **Validation:** Name is now required. Email is checked with a real pattern, not just "contains @". Input is trimmed. A bad field gets a plain-language message and focus. The error clears when the user types. Before, the border went red and never reset.
- **Network failures:** Before, if the request threw (for example, Wi-Fi dropped), the spinner spun forever. A `try/catch/finally` now handles that and always stops the spinner.
- **Double submits:** The button is disabled while sending.
- **Success:** The message is friendlier and the form clears. Before, it just said "Done" and left the old values in the fields.
- **Accessibility:** The message is announced by screen readers (`role="status"`). Invalid fields are flagged with `aria-invalid`. The green and red now have enough contrast. The spinner slows down for users who prefer reduced motion.
- **Layout:** The spinner and message areas now keep their space. Before, the page jumped when they appeared. This adds about 24px of blank space below the form when idle. If you don't want that, remove `visibility:hidden` and put the old sizing back.

Two things I couldn't check from here: how it looks with your page's CSS, and what `/api/volunteers` returns on failure. Before the meeting, submit once with the server working and once with it off, so you know both paths look right.
