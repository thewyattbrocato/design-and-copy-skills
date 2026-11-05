The dialog works with a mouse on the happy path. Here's what's missing, most serious first.

## Bugs

1. **Failed deletes look like successes.** `fetch` only rejects on network errors, so a 403, 404, or 500 still runs `.then(closeDlg)`. The dialog closes, the user thinks the album is gone, and it isn't. Check `res.ok` and show an error.
2. **A network failure leaves an unhandled rejection.** The dialog stays open and shows nothing.
3. **Nothing happens after a successful delete.** The album is still on the page. You need a redirect, a removed list item, or a toast.
4. **No pending state.** Double-clicking Delete sends two DELETEs, and the second likely returns a 404. Disable the button and show "Deleting…" while the request runs.
5. **The album ID and the "48" are hardcoded.** I assume that's just for the example, but both need to come from data.
6. **There's no CSRF token or credentials handling.** If you use cookie auth, the request needs one.

## Accessibility

This is the biggest gap.

- **The buttons are `<div>`s and a `<span>`.** Keyboard users can't tab to Delete, Cancel, or the ×, and screen readers don't announce them as buttons. Use `<button type="button">`.
- **There's no dialog semantics.** It needs `role="dialog"` (or `alertdialog` for a destructive confirm), `aria-modal="true"`, and `aria-labelledby`/`aria-describedby`.
- **There's no focus management.** Focus should move into the dialog when it opens, and Cancel is the safest default for a destructive action. Focus should be trapped there and restored to the trigger on close.
- **Escape doesn't close it.**
- **The page behind it is still reachable.** Tab and screen-reader navigation go straight past the overlay. The background isn't inert and can still scroll.
- **The × has no accessible name.** Use `aria-label="Close"` and a bigger hit target.
- **There's no `:focus-visible` style.**

## Polish

- Add a `z-index` to `.overlay`. Without one, positioned elements elsewhere can paint over it.
- Make the dialog fit narrow screens, for example `width: calc(100% - 32px)`.
- Consider whether clicking the backdrop should close it. If so, make sure that doesn't happen mid-delete.
- Consider making the Delete button's label more specific ("Delete album"), and think about whether you need undo or a soft delete for 48 photos.

## Easiest fix

The native `<dialog>` element with `showModal()` gives you the focus trap, Escape handling, inert background, and top-layer stacking (so no z-index) for free:

```html
<button id="del">Delete album</button>

<dialog id="dlg" aria-labelledby="dlg-title" aria-describedby="dlg-desc" role="alertdialog">
  <h3 id="dlg-title">Delete this album?</h3>
  <p id="dlg-desc">The 48 photos in it will be removed for good.</p>
  <p id="dlg-err" role="alert" hidden>Couldn't delete the album. Please try again.</p>
  <button type="button" id="cancel" autofocus>Cancel</button>
  <button type="button" id="confirm" class="danger">Delete album</button>
</dialog>

<script>
  const dlg = document.getElementById('dlg');
  const confirmBtn = document.getElementById('confirm');
  const err = document.getElementById('dlg-err');

  document.getElementById('del').onclick = () => { err.hidden = true; dlg.showModal(); };
  document.getElementById('cancel').onclick = () => dlg.close();

  confirmBtn.onclick = async () => {
    confirmBtn.disabled = true;
    confirmBtn.textContent = 'Deleting…';
    try {
      const res = await fetch('/albums/12', { method: 'DELETE', credentials: 'same-origin' });
      if (!res.ok) throw new Error(res.status);
      dlg.close();
      location.href = '/albums';   // or remove from the list
    } catch {
      err.hidden = false;
    } finally {
      confirmBtn.disabled = false;
      confirmBtn.textContent = 'Delete album';
    }
  };
</script>

<style>
  dialog { border: 0; border-radius: 8px; padding: 24px; max-width: min(360px, calc(100% - 32px)); }
  dialog::backdrop { background: rgba(0,0,0,.5); }
  button { padding: 8px 14px; border: 1px solid #888; background: #fff; cursor: pointer; }
  button:focus-visible { outline: 2px solid #1a73e8; outline-offset: 2px; }
  .danger { background: #c62828; color: #fff; border-color: #c62828; }
</style>
```

`<dialog>` also restores focus to the trigger on close. I haven't run this snippet, so test it in your target browsers. The server side matters too: confirm the DELETE endpoint checks authorization, since a client-side confirm protects nothing on its own.
