**Don't send it yet.** The page looks good and reads well, in light and dark. But it doesn't save anything, and it's missing the basic details a member needs.

**1. Sign-ups aren't recorded (blocks the purpose).**
- The submit handler only prints "You are on the list…" in the browser. No `fetch`, no `action` and no form service is involved.
- Every member would see a confirmation, and you'd receive nothing.
- The fix is to point the form at wherever you collect responses. I don't know that, so I haven't invented one.
- Once it's wired up, show "Saving…" and disable the button while it sends.
- If the save fails, keep what they typed and say so with a retry. For example: "We couldn't save your place. Try again, or [contact link]."
- Only show "You are on the list" after the save succeeds.

**2. Event details are missing (misleads).**
- "Saturday" has no date, start time, location, or arrival and parking info.
- There's also no word on what to bring or wear, or the cloud-out or cancellation plan.
- Add these under the lead paragraph, for example "[date], [time] at [location]. If it's cloudy: [plan]."

**3. No way to change or cancel, and no contact.** Add a line like "Plans changed? [contact link]". Leaving should be as easy as joining.

**4. Small bugs in the form.** This patch fixes them without changing the look:
- A blank name is accepted, which gives "You are on the list: , party of 2".
- 2.5 people passes validation.
- The telescope choice is collected but never shown back.

```html
<input id="name" name="name" autocomplete="name" required aria-describedby="name-err">
<p class="err" id="name-err" hidden>Enter your name so we know who to look for.</p>
```
```js
const f=document.getElementById('f'),nm=document.getElementById('name'),ne=document.getElementById('name-err'),
n=document.getElementById('n'),e=document.getElementById('n-err'),s=document.getElementById('status');
f.addEventListener('submit',ev=>{ev.preventDefault();
const v=+n.value,badName=!nm.value.trim(),bad=!(Number.isInteger(v)&&v>=1&&v<=8);
ne.hidden=!badName;nm.setAttribute('aria-invalid',badName);
e.hidden=!bad;n.setAttribute('aria-invalid',bad);s.textContent='';
if(badName||bad){(badName?nm:n).focus();return}
// TODO: save here; show the message below only after it succeeds
s.textContent='You are on the list: '+nm.value.trim()+', party of '+v+' ('+f.scope.value+'). See you under the stars.'});
```

**What already works:**
- Labels are tied to their fields.
- Focus rings are visible, and the error moves focus to the field.
- The status message is announced to screen readers.
- Contrast holds in both themes.
- The "sign up in two parts" guidance is helpful.

I haven't run this in a browser or with a screen reader. The main thing left is to choose where responses go and fill in the event details.
