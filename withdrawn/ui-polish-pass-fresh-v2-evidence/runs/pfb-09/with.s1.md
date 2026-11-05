Your dialog looks fine on screen, but it fails for keyboard and screen-reader users. It also reports success when the delete fails. These are ranked by harm.

**1. A failed delete looks like a success.** `fetch` doesn't reject on a 404 or 500, so `.then(closeDlg)` closes the dialog whatever the server said. The person thinks the album is gone, and nothing on the page changes either way. There's also no busy state, so a double-click sends two DELETEs.

```js
async function reallyDelete(){
  const btn = document.getElementById('confirm');
  btn.disabled = true; btn.textContent = 'Deleting…';
  try {
    const r = await fetch('/albums/12', {method:'DELETE'});
    if (!r.ok) throw new Error();
    closeDlg();
    // then remove the album from the page or navigate away, and say so
  } catch {
    btn.disabled = false; btn.textContent = 'Delete album';
    const e = document.getElementById('err');
    e.textContent = "Couldn't delete the album. Nothing was removed. Try again.";
    e.hidden = false;
  }
}
```
```html
<p id="err" role="alert" hidden></p>
```
Add a visible success result, such as a message or a redirect. Right now nothing happens after a successful delete.

**2. The buttons can't be used from a keyboard.** The Delete, Cancel and × controls are `div`/`span` elements with `onclick`. They can't be tabbed to or activated with Enter or Space, and the × has no accessible name. Make them real buttons:
```html
<button class="x" aria-label="Close" onclick="closeDlg()">×</button>
<button id="confirm" class="btn danger" onclick="reallyDelete()">Delete album</button>
<button class="btn" onclick="closeDlg()">Keep album</button>
```
Add `font:inherit` and `background:#fff` to `.btn` (the `.danger` rule still overrides the background), and `.x{background:none;border:0}`. The labels now name the consequence ("Delete album" / "Keep album") instead of a bare "Delete".

**3. The dialog isn't really a dialog.**
- It has no `role="dialog"`, `aria-modal="true"` or `aria-labelledby`.
- Focus never moves into it, so keyboard users keep tabbing through the page behind the overlay.
- Escape doesn't close it.
- On close, focus is lost instead of returning to "Delete album".

Simplest fix: use `<dialog>` with `showModal()`. That gives you focus trapping, Escape, and the inert background. Otherwise, do it by hand:
```js
let opener;
del.onclick = () => { opener = del; overlay.style.display='flex'; cancelBtn.focus(); };
function closeDlg(){ overlay.style.display='none'; opener && opener.focus(); }
overlay.addEventListener('keydown', e => { if (e.key==='Escape') closeDlg(); });
```
You'd still need a Tab trap. Start focus on Keep (the safe choice), not Delete.

**4. Focus is invisible.** Nothing sets a focus style. Once these are real buttons, the browser default will show, but check it against the red button: `.btn:focus-visible{outline:2px solid #1a73e8;outline-offset:2px}`.

**5. Narrow screens.** `.dialog` has `max-width` but no width or margin, so at 320px it can touch the edges. Add `width:calc(100% - 32px)` and `max-height:90vh;overflow:auto`.

**6. Hardcoded content.**
- Album id `12` and "48 photos" are literals. Make sure they come from real data.
- Consider naming the album in the title ("Delete “[album name]”?"). I don't know where the name comes from, so I left it out.
- Check the singular case: "The 1 photos" would be wrong, and so would an empty album.

**What already works:** the copy states the consequence plainly, the red button marks the destructive action, and Cancel is as easy to reach as Delete. A confirm is the right call here because the delete is permanent.

I didn't run any of this, and I haven't tested it with a screen reader.
