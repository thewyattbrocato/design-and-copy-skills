The layout, labels, dark mode, focus rings and the party-size error all work, and I'd leave them alone. Two things should stop you from sending it as is.

## Fix before sending

**1. The form doesn't save anything.** The submit handler only prints "You are on the list…" on the page. Nobody on the organising side receives the sign-up, so every member would see a false confirmation. Send the data somewhere (a form service, a Google Sheet endpoint, your own server) and only show success once that succeeds. I don't know what you use, so the endpoint below is a placeholder:

```js
f.addEventListener('submit',async ev=>{ev.preventDefault();
  const v=+n.value,badN=!Number.isInteger(v)||v<1||v>8,badName=!f.name.value.trim();
  e.hidden=!badN;n.setAttribute('aria-invalid',badN);
  ne.hidden=!badName;f.name.setAttribute('aria-invalid',badName);
  s.textContent='';
  if(badName){f.name.focus();return} if(badN){n.focus();return}
  b.disabled=true;b.textContent='Saving…';
  try{
    const r=await fetch('[your sign-up endpoint]',{method:'POST',body:new FormData(f)});
    if(!r.ok)throw 0;
    s.style.color='';s.textContent='You are on the list: '+f.name.value.trim()+', party of '+v+'. See you under the stars.';
    b.textContent='Saved';
  }catch{
    s.style.color='var(--bad)';s.textContent='We could not save your place, and your answers are still here. Please try again.';
    b.disabled=false;b.textContent='Save my place';
  }});
```

You'd also need `const b=f.querySelector('button'),ne=document.getElementById('name-err');`. Add this after the name input, and add `aria-describedby="name-err"` to the input:

```html
<p class="err" id="name-err" hidden>Enter your name so we know who is coming.</p>
```

**2. The page doesn't say when or where.** Members will open it and not know the date, start time, meeting place or what happens if clouds roll in. Add a line under the lead, for example:

```html
<p class="lead">[Date] from [start time] at [location]. If the sky is clouded out, we will [how you will tell people].</p>
```

I left those as placeholders because I don't have the facts.

## Smaller gaps

- **Empty name:** with `novalidate` and no name check, a blank name gives "You are on the list: , party of 2". The patch above fixes this.
- **Decimals:** `2.5` currently passes the party-size check. The patch above uses `Number.isInteger`.
- **Contact for cancellations:** if you may cancel for weather, consider an optional email or phone field. That's your call, so I haven't added it.
- **Changing a sign-up:** once someone submits, they have no way to edit or cancel. Even a line like "Need to change this? Reply to [contact]" would help.

I only read the code. I haven't run the page, tested it on a phone, or checked it with a screen reader.
