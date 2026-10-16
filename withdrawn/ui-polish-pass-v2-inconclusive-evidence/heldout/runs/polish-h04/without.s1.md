I haven't run this in a browser. Here's the tidied version:

```html
<div class="overlay" id="ov">
  <div class="dialog" role="alertdialog" aria-modal="true" aria-labelledby="dt" aria-describedby="dd">
    <div class="title" id="dt">Delete project?</div>
    <p id="dd">This removes "Harvest Planner" and its 14 tasks.</p>
    <button type="button" class="btn cancel" onclick="closeD()" autofocus>Cancel</button>
    <button type="button" class="btn del" onclick="del()">Delete</button>
  </div>
</div>
<style>
:root{--bg:#16181d;--text:#9aa0a6;--panel:#1f2229;--title:#e8eaed;--border:#3c4048}
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);display:grid;place-items:center}
.dialog{background:var(--panel);color:var(--text);padding:24px;border-radius:10px;width:420px;max-width:calc(100vw - 32px);border:1px solid var(--border);animation:pop .15s ease-out}
.title{font-size:18px;color:var(--title)}
.btn{display:inline-block;padding:8px 14px;margin-right:8px;cursor:pointer;font:inherit;border-radius:6px;border:1px solid transparent;background:none}
.btn:focus-visible{outline:2px solid #8ab4f8;outline-offset:2px}
.cancel{color:var(--title);border-color:#5f6368}
.del{background:#b3261e;color:#fff}
@keyframes pop{from{transform:scale(.96);opacity:0}to{transform:scale(1);opacity:1}}
@media (prefers-reduced-motion:reduce){.dialog{animation:none}}
</style>
```

**What I changed**

- **Contrast (the likely source of the complaints):**
  - The title was `#555` on `#1f2229`, about 2:1. It's now `#e8eaed`.
  - Cancel was `#444`, which is nearly invisible. It's now `#e8eaed` with a visible border.
  - Delete was `#8c3b3b` text on a `#7a1f1f` background, which is close to unreadable. It's now white on `#b3261e`, about 6:1.
  - The body text color `#9aa0a6` already passes, so I left it.
- **Separation from the page:** The overlay was only 30% black, so the dark dialog blended into the dark app. I raised it to 60% and added a 1px border to the dialog.
- **Keyboard and screen readers:**
  - The buttons were `<span>`s, so they couldn't be tabbed to or activated with the keyboard. They're now real `<button>`s, restyled to look the same.
  - I added a visible focus ring.
  - I added dialog roles and labels.
  - Cancel gets initial focus, so Enter or Space doesn't delete by accident.
- **Animation:** The pop-in took 0.6s and started at half size, which is slow and jarring. It's now 0.15s from 96% scale, and it's turned off for users with reduced-motion set.
- **Small screens:** The dialog now has `max-width: calc(100vw - 32px)`, so the fixed 420px width can't overflow narrow screens.

I didn't change the layout, copy, or `closeD()`/`del()`. Two things are left for you. Escape-to-close and a focus trap aren't in this markup, so check whether your JS handles them. `--bg` is unused in this snippet, so I left it alone.
