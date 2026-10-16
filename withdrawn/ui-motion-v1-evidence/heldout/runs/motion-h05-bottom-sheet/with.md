Defaults I assumed: a web product UI, a frequently used path, a calm and decisive feel, CSS transitions, and system reduced-motion honored.

```html
<div class="backdrop" id="backdrop"></div>
<div class="sheet" id="sheet" role="dialog" aria-modal="true" aria-labelledby="sheet-title" aria-hidden="true">
  <h3 id="sheet-title">Choose your cabin</h3>
  <button class="cabin">Economy &middot; $212</button>
  <button class="cabin">Premium Economy &middot; $388</button>
  <button class="cabin">Business &middot; $946</button>
</div>
```

```css
:root {
  --ease-out: cubic-bezier(.22, 1, .36, 1);
  --ease-in: cubic-bezier(.4, 0, 1, 1);
}

.backdrop {
  position: fixed; inset: 0; background: rgba(0,0,0,.5);
  opacity: 0; visibility: hidden;
  /* exit: fade, then hide */
  transition: opacity 200ms linear, visibility 0s linear 200ms;
}
.backdrop.open {
  opacity: 1; visibility: visible;
  transition: opacity 280ms linear, visibility 0s;
}

.sheet {
  position: fixed; left: 0; right: 0; bottom: 0; height: 320px;
  background: #fff; border-radius: 16px 16px 0 0;
  padding: 24px 24px calc(24px + env(safe-area-inset-bottom));
  transform: translateY(100%);
  visibility: hidden;
  will-change: transform;
  /* exit: shorter, accelerates away */
  transition: transform 200ms var(--ease-in), visibility 0s linear 200ms;
}
.sheet.open {
  transform: translateY(0);
  visibility: visible;
  /* enter: decelerates into place */
  transition: transform 280ms var(--ease-out), visibility 0s;
}

.cabin {
  display: block; width: 100%; padding: 14px; margin-bottom: 10px;
  transition: background-color 120ms ease-out, transform 120ms ease-out;
}
.cabin:hover { background-color: #f3f4f6; }
.cabin:active { transform: scale(.98); }

@media (prefers-reduced-motion: reduce) {
  /* remove travel, keep the fade so the change is still visible */
  .sheet, .sheet.open { transform: none; opacity: 0; transition: opacity 150ms linear, visibility 0s linear 150ms; }
  .sheet.open { opacity: 1; transition: opacity 150ms linear, visibility 0s; }
  .cabin:active { transform: none; }
}
```

```js
const sheet = document.getElementById('sheet');
const backdrop = document.getElementById('backdrop');
const openBtn = document.getElementById('openBtn');

function setOpen(open) {
  sheet.classList.toggle('open', open);
  backdrop.classList.toggle('open', open);
  sheet.setAttribute('aria-hidden', String(!open));
  if (open) sheet.querySelector('.cabin').focus({ preventScroll: true });
  else openBtn.focus();
}

openBtn.addEventListener('click', () => setOpen(true));
backdrop.addEventListener('click', () => setOpen(false));
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && sheet.classList.contains('open')) setOpen(false);
});
```

**What changed and why**

| Before | After |
|---|---|
| `transition: all 0.8s ease-in-out` animated `bottom`, which triggers layout and causes the jank. | The sheet animates only `transform`, which runs on the GPU. |
| 800 ms in both directions | Enter takes 280 ms with ease-out, so it lands decisively. Exit takes 200 ms with ease-in, so it gets out of the way. |
| The backdrop popped in with `display: none`, so it appeared instantly. | It fades (280 ms in, 200 ms out). `visibility` is delayed on exit so the fade finishes first. |
| Hover animated `padding` and `margin` over 0.6 s, so the buttons moved under the cursor and shifted the layout. | Hover is a 120 ms background tint. Press is a `scale(.98)` for tactile feedback. Nothing reflows. |
| Nothing handled reduced motion. | Reduced motion removes the slide and keeps a 150 ms fade. |

Interruption works because these are plain transitions. If someone taps the backdrop mid-open, the sheet reverses from its current position, and nothing is disabled while it moves.

I also made a few small fixes while I was in there:
- The closed sheet is now `visibility: hidden`, so keyboard users can't tab into offscreen buttons.
- Focus moves into the sheet on open and returns to the trigger on close.
- Escape closes the sheet.
- The sheet is marked as a dialog, and the bottom padding respects the iOS safe area.

Your snippet used `openBtn` as an implicit global. I switched to `getElementById`, so make sure the trigger has `id="openBtn"`.

I didn't add drag-to-dismiss. It would feel great on mobile, but it needs pointer handling and a spring release. I can add it if you want it.
