Your markup and styling work. The red danger button, the "48 photos" consequence line and the Cancel option are all right. What's missing is mostly accessibility and the failure path. In order of harm:

1. **Keyboard and screen-reader users can't use it.**
   - The Delete, Cancel and × controls are `div`/`span` elements, so Tab skips them and Enter/Space do nothing.
   - The × is announced as the letter "x".
   - The overlay has no `role="dialog"` or label.
   - Focus never moves into the dialog and doesn't return to "Delete album" on close.
   - Escape doesn't close it, and Tab reaches the page behind it.
   - Fix: use a native `<dialog>` with `showModal()`, which handles the focus trap, Escape, background inertness and focus return. Use real `<button>`s, with `aria-label="Close"` on the ×.

2. **A failed delete looks like a successful one.** `fetch` doesn't reject on a 404 or 500, so `.then(closeDlg)` closes the dialog whatever happened. The person is left on a page that still shows the album. There's also no busy state, so a double-click sends two DELETEs, and no confirmation on success. On a network failure there's an unhandled rejection and the dialog stays open with no explanation.

3. **The default focus is risky.** For an irreversible action, focus should start on the safe choice (Cancel).

4. **The wording is weak.** The bare "Delete" and "Cancel" buttons would be clearer as "Delete album" and "Keep album". The body should also say that the deletion can't be undone.

5. **Smaller things.**
   - `/albums/12` and "48" are hardcoded.
   - `max-width:360px` has no margin on a 320px screen.
   - `.btn` has no `:focus-visible` style, which the native buttons below get by default.

Changed pieces:

```html
<dialog id="dlg" class="dialog" aria-labelledby="dlg-title" aria-describedby="dlg-desc">
 <button type="button" class="x" aria-label="Close" onclick="closeDlg()">×</button>
 <h3 id="dlg-title">Delete this album?</h3>
 <p id="dlg-desc">The 48 photos in it will be removed for good. This can't be undone.</p>
 <p id="dlg-err" role="alert" hidden></p>
 <button type="button" class="btn danger" id="confirm" onclick="reallyDelete()">Delete album</button>
 <button type="button" class="btn" autofocus onclick="closeDlg()">Keep album</button>
</dialog>

<script>
 const dlg = document.getElementById('dlg'),
       err = document.getElementById('dlg-err'),
       confirmBtn = document.getElementById('confirm');

 document.getElementById('del').onclick = () => { err.hidden = true; dlg.showModal(); };
 function closeDlg(){ dlg.close(); }   // focus returns to #del

 async function reallyDelete(){
  confirmBtn.disabled = true;
  confirmBtn.textContent = 'Deleting…';
  try {
   const r = await fetch('/albums/12', {method: 'DELETE'});
   if (!r.ok) throw new Error(r.status);
   location.href = '/albums';          // [where to go after delete]
  } catch (e) {
   err.textContent = "Couldn't delete the album. Check your connection and try again.";
   err.hidden = false;
   confirmBtn.disabled = false;
   confirmBtn.textContent = 'Try again';
   confirmBtn.focus();
  }
 }
</script>

<style>
 .dialog{background:#fff;padding:24px;border-radius:8px;border:0;max-width:min(360px,calc(100vw - 32px))}
 .dialog::backdrop{background:rgba(0,0,0,.5)}
 .x{position:absolute;top:8px;right:8px;background:none;border:0;font-size:20px;cursor:pointer}
 .btn{display:inline-block;padding:8px 14px;border:1px solid #888;background:#fff;font:inherit;cursor:pointer}
 .danger{background:#c62828;color:#fff}
 #dlg-err{color:#b00020}
</style>
```

I removed the `.overlay` rules and the `#overlay` wrapper because `<dialog>` replaces them.

- **Open decisions:** where to go after a successful delete (I left a placeholder URL), and whether the ID and photo count should come from the page. I'd also consider a "Deleted" message on the destination page.
- **Not checked:** I haven't run this in a browser or with a screen reader. I also haven't checked your server's auth or CSRF handling for the DELETE.
