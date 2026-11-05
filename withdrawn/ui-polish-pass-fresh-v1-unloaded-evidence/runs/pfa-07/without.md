The popup works with a mouse, which is probably why it looks fine to you. I only have the markup, not your CSS or the live page. From the markup, it falls apart for keyboard, screen-reader, and slow-network users.

**Most likely causes of "feels broken"**

1. **The Keep and Remove controls are `<span>`s with `onclick`.** They can't be tabbed to, and Enter and Space do nothing on them. A keyboard user can open the popup but can't confirm or cancel it. They're also invisible to screen readers as buttons. Use real `<button type="button">` elements.

2. **Focus isn't managed.**
   - When the popup opens, focus stays on the trigger behind the overlay. Tab then moves through the page underneath.
   - Escape doesn't close the popup, and neither does clicking the backdrop.
   - When it closes, focus is lost rather than returned to the trigger.

3. **There's no feedback after Remove.** `doRemove()` closes the popup immediately and posts in the background. There's no loading state, no success message, and no error handling. If the request is slow or fails, the user sees the popup vanish and nothing else. That feels broken, and it's a likely cause for mouse users too. Wait for the response, then update the rota and show a confirmation or an error.

**Also worth fixing**

4. **The trigger button has no accessible name.** It's an icon-only SVG, so screen readers announce just "button". Add `aria-label="Remove Dana Okafor from the Saturday rota"`, plus `aria-hidden="true"` on the SVG. The SVG path also has no stroke or fill in the markup, so check that your CSS actually draws it.

5. **The popup isn't marked up as a dialog.** It needs `role="dialog"`, `aria-modal="true"`, and `aria-labelledby` pointing at the title. For a destructive confirmation, `role="alertdialog"` is more appropriate.

6. **The copy is hardcoded.** "She will be notified" and "Keep her" are baked in. If this is a template reused for other volunteers, it will be wrong for some of them. Use neutral wording such as "Keep on rota" and "They'll be notified".

**Minimal fix**

```html
<button class="icon-btn" id="trigger" aria-label="Remove Dana Okafor from the Saturday rota">
  <svg aria-hidden="true" viewBox="0 0 20 20">…</svg>
</button>

<div id="confirm" class="overlay" style="display:none">
  <div class="box" role="alertdialog" aria-modal="true" aria-labelledby="c-title">
    <div class="title" id="c-title">Remove Dana Okafor from the Saturday rota?</div>
    <p>They will be notified by email.</p>
    <div class="row">
      <button type="button" class="btn" id="keep">Keep on rota</button>
      <button type="button" class="btn danger" id="remove">Remove</button>
    </div>
  </div>
</div>

<script>
  const dlg = document.getElementById('confirm');
  const trigger = document.getElementById('trigger');
  const keep = document.getElementById('keep');
  const remove = document.getElementById('remove');

  function openConfirm() { dlg.style.display = 'flex'; keep.focus(); }
  function closeConfirm() { dlg.style.display = 'none'; trigger.focus(); }

  trigger.addEventListener('click', openConfirm);
  keep.addEventListener('click', closeConfirm);
  dlg.addEventListener('click', e => { if (e.target === dlg) closeConfirm(); });
  dlg.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeConfirm();
    if (e.key === 'Tab') { // simple focus trap between the two buttons
      const first = keep, last = remove;
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  remove.addEventListener('click', async () => {
    remove.disabled = true; remove.textContent = 'Removing…';
    try {
      await fetch(/* … */);
      closeConfirm(); /* update the rota and show "Dana removed" */
    } catch {
      /* show an inline error and keep the dialog open */
    } finally {
      remove.disabled = false; remove.textContent = 'Remove';
    }
  });
</script>
</parameter>
```

Focus on **Keep on rota** when the popup opens. That makes the safe action the default, so an accidental Enter doesn't remove someone.

You could also use a native `<dialog>` with `showModal()`. It gives you the focus trap, Escape handling, and backdrop for free.

To confirm the diagnosis, try the popup yourself with only the keyboard (Tab, Enter, Esc). Then throttle the network in dev tools and click Remove.
