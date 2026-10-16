I fixed the dialog below. I haven't rendered it, and I worked out the contrast ratios by hand, so check it in the browser.

```html
<div class="overlay" id="ov">
  <div class="dialog" role="alertdialog" aria-modal="true" aria-labelledby="dlg-title" aria-describedby="dlg-desc">
    <div class="title" id="dlg-title">Delete project?</div>
    <p id="dlg-desc">This removes "Harvest Planner" and its 14 tasks.</p>
    <button type="button" class="btn cancel" onclick="closeD()">Cancel</button>
    <button type="button" class="btn del" onclick="del()">Delete</button>
  </div>
</div>
<style>
:root{--bg:#16181d;--text:#b4bac1;--panel:#1f2229;--title:#e8eaed}
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);display:grid;place-items:center}
.dialog{background:var(--panel);color:var(--text);padding:24px;border-radius:10px;width:420px;border:1px solid #2f343d;animation:pop .15s ease-out}
.title{font-size:18px;color:var(--title)}
.btn{display:inline-block;padding:8px 14px;margin-right:8px;cursor:pointer;font:inherit;border-radius:6px}
.btn:focus-visible{outline:2px solid #8ab4f8;outline-offset:2px}
.cancel{background:transparent;color:var(--title);border:1px solid #4a505a}
.del{background:#a32a2a;color:#fff;border:1px solid transparent}
@keyframes pop{from{transform:scale(.96);opacity:0}to{transform:scale(1);opacity:1}}
@media (prefers-reduced-motion:reduce){.dialog{animation:none}}
</style>
```

**What I changed**
- **Title:** `#555` on the dark panel was about 2:1 contrast. It's now `#e8eaed`, which is well above the 4.5:1 target.
- **Cancel:** `#444` text was nearly invisible. It's now light text with a visible border, so it reads as a button.
- **Delete:** `#8c3b3b` text on a `#7a1f1f` background was about 1.3:1. It's now white on `#a32a2a`, about 7:1. It's still the same red family and still looks like the destructive action.
- **Body text:** I lightened it slightly from `#9aa0a6` to `#b4bac1`. The old value passed, but only just.
- **Backdrop:** the scrim was 30% black, which barely separated the dialog from a dark page. It's now 60%. I also added a 1px border to the dialog so its edge is clear.
- **Animation:** the 0.6s pop from half size felt sluggish and jarring. It's now 0.15s from 96% size. It's turned off for users with `prefers-reduced-motion`.
- **Buttons:** the `<span>` buttons are now real `<button>` elements. They can be reached with Tab and activated with Enter or Space, and they have a focus ring. I added border radius to match the dialog.
- **Dialog semantics:** I added `role="alertdialog"`, `aria-modal` and labelling, so screen readers announce the title and message.

I kept the layout, copy, sizes and handlers (`closeD()`, `del()`) as they were.

I didn't add focus trapping, auto-focus on open, or Escape to close. Those are worth doing, but they're JS behavior changes beyond tidying, so I left them out. I can add them if you want.
