The popup works for a mouse user and fails for almost everyone else. That's probably why it looks fine to you and feels broken to them.

**Likely causes of the "feels broken" reports**

1. **The Keep and Remove controls aren't buttons.** They're `<span onclick>`, so they can't be focused. Tab skips them, and Enter and Space do nothing. Keyboard, switch and screen-reader users can open the popup but can't answer it. Mobile users also get small, unlabelled tap targets, and the "Keep her" link has no button affordance.
2. **Escape and clicking outside don't close it.** People expect both from a modal. Without them the popup feels stuck.
3. **Focus isn't managed.**
   - Focus stays on the trash button when the popup opens, so Tab moves through the page behind the overlay.
   - Nothing moves focus into the popup.
   - When the popup closes, focus isn't returned to the trigger.
4. **There's no dialog semantics.** The popup has no `role="dialog"`, `aria-modal` or `aria-labelledby`, so screen readers don't announce it. The title is a plain `div`.
5. **The trigger has no accessible name.** It's an icon-only button with no `aria-label`, so a screen reader says just "button".
6. **Remove gives no feedback.** `doRemove()` closes the popup immediately, whether or not the server call succeeds. There's no loading state and no success or error message. Nothing visibly happens, and a failure is silent. It can also be double-clicked.

**A bug you may have missed**

`openConfirm()` takes no argument and the name "Dana Okafor" is hardcoded. If this button is repeated per row, every row asks about Dana, and a user could remove the wrong person. Pass the volunteer's name and ID in.

**Smaller points**

- "Keep her" assumes a pronoun. "Cancel" or "Keep on rota" is safer. The same goes for "She will be notified". Use the name or "They".
- The two choices look different (a plain link and a button), so the safe option reads as secondary text. That's fine for a destructive action, but make sure the link is a real button.

**A fix using native `<dialog>`**

This gives you the focus trap, Escape, `aria-modal` and focus return for free.

```html
<button class="icon-btn" aria-label="Remove Dana Okafor from rota"
        onclick="openConfirm('Dana Okafor', 123)">
  <svg aria-hidden="true" viewBox="0 0 20 20">…</svg>
</button>

<dialog id="confirm" aria-labelledby="confirm-title">
  <h2 id="confirm-title"></h2>
  <p id="confirm-note"></p>
  <div class="row">
    <button type="button" class="btn" onclick="confirm.close()" autofocus>Keep on rota</button>
    <button type="button" class="btn danger" id="remove-btn">Remove</button>
  </div>
</dialog>

<script>
  const dlg = document.getElementById('confirm');
  function openConfirm(name, id) {
    document.getElementById('confirm-title').textContent = `Remove ${name} from the Saturday rota?`;
    document.getElementById('confirm-note').textContent = `${name} will be notified by email.`;
    document.getElementById('remove-btn').onclick = () => doRemove(id);
    dlg.showModal();
  }
  dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close(); }); // backdrop click
  async function doRemove(id) {
    const btn = document.getElementById('remove-btn');
    btn.disabled = true; btn.textContent = 'Removing…';
    try {
      await fetch(`/rota/${id}`, { method: 'DELETE' }); // check res.ok in real code
      dlg.close(); /* update the list and show a "Dana removed" message */
    } catch {
      btn.disabled = false; btn.textContent = 'Remove';
      /* show an error inside the dialog */
    }
  }
</script>
```

To confirm this is the cause, try the popup yourself with only the keyboard: Tab, Enter, Esc. Then try it with VoiceOver or NVDA. You'll probably hit the problem within seconds.
