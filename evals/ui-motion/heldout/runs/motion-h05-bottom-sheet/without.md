Here's the improved version. The main fixes are listed after the code.

```html
<button id="openBtn">Choose cabin</button>

<div class="backdrop" id="backdrop"></div>
<div class="sheet" id="sheet" role="dialog" aria-modal="true"
     aria-labelledby="sheetTitle" tabindex="-1" aria-hidden="true">
  <div class="grabber" id="grabber" aria-hidden="true"></div>
  <h3 id="sheetTitle">Choose your cabin</h3>
  <button class="cabin">Economy &middot; $212</button>
  <button class="cabin">Premium Economy &middot; $388</button>
  <button class="cabin">Business &middot; $946</button>
</div>
```

```css
:root {
  --ease-out: cubic-bezier(.32, .72, 0, 1);   /* fast start, soft landing */
  --ease-in:  cubic-bezier(.4, 0, 1, 1);
}

.backdrop {
  position: fixed; inset: 0;
  background: rgba(0, 0, 0, .5);
  opacity: 0; visibility: hidden;
  transition: opacity .25s ease, visibility 0s .25s;
}
.backdrop.open {
  opacity: 1; visibility: visible;
  transition: opacity .3s ease, visibility 0s;
}

.sheet {
  position: fixed; left: 0; right: 0; bottom: 0;
  max-height: 85dvh; overflow-y: auto; overscroll-behavior: contain;
  padding: 12px 24px calc(24px + env(safe-area-inset-bottom));
  background: #fff; border-radius: 20px 20px 0 0;
  box-shadow: 0 -8px 32px rgba(0, 0, 0, .16);
  transform: translateY(100%);
  visibility: hidden;
  will-change: transform;
  outline: none;
  transition: transform .25s var(--ease-in), visibility 0s .25s;
}
.sheet.open {
  transform: translateY(0);
  visibility: visible;
  transition: transform .45s var(--ease-out), visibility 0s;
}
.sheet.dragging { transition: none; }

.grabber {
  width: 36px; height: 5px; margin: 0 auto 16px;
  border-radius: 3px; background: #d0d0d5;
  touch-action: none; cursor: grab;
}

.cabin {
  display: block; width: 100%; padding: 14px; margin-bottom: 10px;
  border: 1px solid #e3e3e8; border-radius: 12px; background: #fff;
  font: inherit; text-align: left; cursor: pointer;
  transition: transform .15s ease, background-color .15s ease, box-shadow .15s ease;
}
.cabin:hover { background: #f6f7fb; box-shadow: 0 2px 8px rgba(0, 0, 0, .08); }
.cabin:active { transform: scale(.98); }
.cabin:focus-visible { outline: 2px solid #2563eb; outline-offset: 2px; }

@media (prefers-reduced-motion: reduce) {
  .sheet, .sheet.open, .backdrop, .backdrop.open, .cabin { transition-duration: .01s; }
}
```

```js
const openBtn  = document.getElementById('openBtn');
const sheet    = document.getElementById('sheet');
const backdrop = document.getElementById('backdrop');
const grabber  = document.getElementById('grabber');

function openSheet() {
  sheet.classList.add('open');
  backdrop.classList.add('open');
  sheet.setAttribute('aria-hidden', 'false');
  sheet.focus({ preventScroll: true });
}

function closeSheet() {
  sheet.style.transform = '';
  sheet.classList.remove('open', 'dragging');
  backdrop.classList.remove('open');
  backdrop.style.opacity = '';
  sheet.setAttribute('aria-hidden', 'true');
  openBtn.focus({ preventScroll: true });
}

openBtn.addEventListener('click', openSheet);
backdrop.addEventListener('click', closeSheet);
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && sheet.classList.contains('open')) closeSheet();
});

// Drag-to-dismiss on the grabber
let startY = 0, dy = 0, startT = 0;

grabber.addEventListener('pointerdown', e => {
  startY = e.clientY; dy = 0; startT = performance.now();
  grabber.setPointerCapture(e.pointerId);
  sheet.classList.add('dragging');
});

grabber.addEventListener('pointermove', e => {
  if (!grabber.hasPointerCapture(e.pointerId)) return;
  dy = Math.max(0, e.clientY - startY);          // no dragging upward
  sheet.style.transform = `translateY(${dy}px)`;
  backdrop.style.opacity = String(1 - Math.min(dy / sheet.offsetHeight, 1));
});

function endDrag(e) {
  if (!grabber.hasPointerCapture(e.pointerId)) return;
  grabber.releasePointerCapture(e.pointerId);
  const velocity = dy / (performance.now() - startT);   // px per ms
  sheet.classList.remove('dragging');
  if (dy > sheet.offsetHeight * 0.3 || velocity > 0.5) {
    closeSheet();
  } else {
    sheet.style.transform = '';                  // spring back
    backdrop.style.opacity = '';
  }
}
grabber.addEventListener('pointerup', endDrag);
grabber.addEventListener('pointercancel', endDrag);
```

**What was causing the jank and cheap feel**

- **Animating `bottom` with `transition: all`:** this triggers layout every frame, and `all` animates properties you never meant to. The sheet now uses `transform: translateY()`, which runs on the GPU, and each transition names its property.
- **Timing:** 0.8s `ease-in-out` feels sluggish. Opening is now 450ms with a decelerating curve, so it starts fast and settles softly. Closing is a quicker 250ms, because exits should feel snappier than entrances.
- **Backdrop:** `display: none` to `block` can't animate, so it popped in. It now fades with `opacity` and `visibility`.
- **Hover on the cabin buttons:** animating `padding` and `margin` over 0.6s resized each button and shoved its neighbours around. Hover now changes only background and shadow. A press gives a subtle `scale(.98)`.
- **Hardcoded 320px height:** it's now content-sized with a `max-height`, so it won't clip on small screens.

**Polish I added**

- A grabber handle with drag-to-dismiss. The backdrop fades as you drag, and the sheet springs back if you let go early.
- Safe-area padding for phones with a home indicator.
- Escape to close.
- Focus moves into the sheet on open and back to the trigger on close.
- `role="dialog"` and `aria-modal` for screen readers.
- A `prefers-reduced-motion` fallback.

I assumed `openBtn` is the trigger, since your snippet used it without defining it. I gave the buttons light border and radius styling to match the rounded sheet, so adjust those to your design tokens. I haven't run this in a browser. It's worth testing the drag on a real touch device.
