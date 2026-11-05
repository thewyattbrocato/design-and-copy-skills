Here are the changes. The layout, field order and labels are untouched, and I added one empty line under the email field for its error message.

```html
<form id="vol" novalidate>
 <label for="vname">Name</label>
 <input id="vname" name="name" autocomplete="name">
 <label for="vemail">Email</label>
 <input id="vemail" name="email" type="email" autocomplete="email" aria-describedby="vemail-err">
 <p id="vemail-err" class="err"></p>
 <button id="send" type="submit">Sign me up</button>
 <p id="msg" role="status"></p>
</form>
<div class="dots" aria-hidden="true"></div>
<script>
 const f = document.getElementById('vol');
 const email = document.getElementById('vemail');
 const emailErr = document.getElementById('vemail-err');
 const send = document.getElementById('send');
 const msg = document.getElementById('msg');
 const dots = document.querySelector('.dots');

 function setEmailError(text) {
  emailErr.textContent = text;
  if (text) email.setAttribute('aria-invalid', 'true');
  else email.removeAttribute('aria-invalid');
 }
 function say(text, kind) {
  msg.textContent = text;
  msg.className = kind || '';
 }
 email.addEventListener('input', () => setEmailError(''));

 f.addEventListener('submit', async e => {
  e.preventDefault();
  if (send.getAttribute('aria-disabled') === 'true') return; // no double-submit
  say('');
  const value = email.value.trim();
  if (!value) {
   setEmailError('Enter your email so we can reach you.');
   email.focus();
   return;
  }
  if (!/^\S+@\S+\.\S+$/.test(value)) {
   setEmailError('That email looks incomplete. It should look like name@example.com.');
   email.focus();
   return;
  }
  setEmailError('');
  send.setAttribute('aria-disabled', 'true');
  send.textContent = 'Signing you up…';
  dots.classList.add('spin');
  say('Signing you up…');
  try {
   const r = await fetch('/api/volunteers', {method: 'POST', body: new FormData(f)});
   if (r.ok) {
    say('Thank you, you’re signed up.', 'ok');
    f.reset();
   } else {
    say('We couldn’t sign you up. Your details are still here, so please try again.', 'bad');
   }
  } catch {
   say('We couldn’t reach the server. Check your connection and try again. Your details are still here.', 'bad');
  } finally {
   dots.classList.remove('spin');
   send.removeAttribute('aria-disabled');
   send.textContent = 'Sign me up';
  }
 });
</script>
<style>
 .dots{min-height:24px}
 .spin{width:24px;height:24px;border:3px solid #ccc;border-top-color:#333;border-radius:50%;animation:turn 1s linear infinite}
 @keyframes turn{to{transform:rotate(360deg)}}
 @media (prefers-reduced-motion:reduce){.spin{animation:none;border-top-color:#ccc}}
 #msg{margin-top:12px}
 #msg.ok{color:#1a6b2a}
 #msg.bad{color:#b00020}
 .err{margin:4px 0 0;color:#b00020;min-height:0}
 #vol input[aria-invalid="true"]{border:2px solid #b00020}
 #vol :focus-visible{outline:2px solid #1a56db;outline-offset:2px}
 #send[aria-disabled="true"]{opacity:.7;cursor:progress}
</style>
```

**What changed, by importance**
- **Silent failure:** the old code threw an uncaught error if the network was down, and the spinner never cleared. It now catches that, shows a message, and keeps what the person typed.
- **Email error:** it was only a red border, with no words and no screen-reader announcement. There's now a message under the field, `aria-invalid`, and focus moves to the field. The message clears as they type. An empty email and a malformed one get different messages.
- **Double submit:** the button now shows "Signing you up…" and ignores repeat clicks. I used `aria-disabled` so keyboard focus isn't dropped.
- **Result messages:** "Something went wrong" now says what happened and what to do. "Done" now reads "Thank you, you're signed up." The form clears on success so a second click can't sign them up twice. The `#msg` element is a live region, so the result is announced.
- **Contrast and focus:** the pure `red` was about 4:1 on white, so it's now a darker red, and the green is a deeper one. Both messages are words, not just color. Keyboard focus is clearly visible.
- **Spinner:** I reserved its 24px so the page doesn't jump when it appears, and hid it from assistive tech. With reduced motion it stops spinning, and the "Signing you up…" text still shows progress.

**Notes**
- Name is still optional, as in your original. If the trustees expect it to be required, say so and I'll add the same inline check.
- I haven't run this in a browser or tested it with a screen reader. Before the meeting, try it once with the network off and once with the endpoint returning a 500.
