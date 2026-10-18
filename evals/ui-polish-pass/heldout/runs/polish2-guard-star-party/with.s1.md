**The sign-up doesn't save anything.** Pressing "Save my place" only prints "You are on the list" in the visitor's own browser. No one is added to a list and you won't receive anything. Members will think they're signed up when they aren't, so fix this before you send the link.

The rest of the page is in good shape: labels, keyboard focus, dark mode, the count error message and the status announcement all work.

Findings, most serious first:

1. **Nothing is sent anywhere.** Point the form at wherever you collect responses: a Google Form or Sheet, a form service, or a small endpoint. I don't know which you use, so I haven't invented one. Once it submits for real, it also needs:
   - a "Saving…" state with the button disabled, so people can't double-submit;
   - a failure message that keeps what they typed and offers a retry. The success line should only appear after the save succeeds.

2. **Event details are missing.** The page never says which Saturday, the start time, the location, what to bring (warm clothes, a red torch), or what happens if it's cloudy. Add a line under the heading, for example: `Saturday [date], [time] at [location]. If it's cloudy: [rain plan].` I left the details as placeholders because I don't have them.

3. **The name field isn't validated.** An empty name gives "You are on the list: , party of 2." The count field also accepts 1.5. Suggested fix:

```html
<input id="name" name="name" autocomplete="name" required aria-describedby="name-err">
<p class="err" id="name-err" hidden>Enter your name so we know who to expect.</p>
```
```js
const nm=document.getElementById('name'),ne=document.getElementById('name-err');
// inside the submit handler, replacing the existing validity check:
const badN=!nm.value.trim(), bad=!(Number.isInteger(v)&&v>=1&&v<=8);
ne.hidden=!badN; nm.setAttribute('aria-invalid',badN);
e.hidden=!bad; n.setAttribute('aria-invalid',bad); s.textContent='';
if(badN||bad){(badN?nm:n).focus();return}
```

4. **The field borders are faint.** `--line` is about 1.5:1 against the background in light mode, and the dark value is similarly low. Input borders should reach about 3:1. Darkening `--line` to roughly `#8a91a0` in light mode and `#6b7280` in dark mode would do it, but it also changes the card look, so it's your call.

5. **There's no way to change or cancel.** Someone who can't come, or who got the count wrong, has nowhere to go. Add a line like "Plans changed? Contact [organiser email]" under the form.

I only read the code. I haven't run it in a browser or tested it with a screen reader.
