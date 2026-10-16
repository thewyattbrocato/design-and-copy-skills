**Short version:** use a quick, strong highlight on the value that changed. Fade it out over about a second. Keep the number itself readable and don't move anything. Add a quiet cue for people who have scrolled away. Keep the loudest cue for wickets.

I'm assuming a web page, CSS transitions, a quiet and crisp feel, and system reduced-motion respected. Tell me if any of that is wrong.

## Why this works for your setup

Your viewers are looking elsewhere when a number changes: another monitor, another match, or nothing. A change away from where someone is looking needs a stronger cue than one under their cursor. The cue also has to stay calm, because people learn to ignore anything that gets louder or repeats too often.

## What to do

| Event | Cue | Duration | Notes |
|---|---|---|---|
| Runs or overs change | Background highlight behind the changed value only (a soft amber tint), then fade to normal | Appears at once, fades over about 1000 ms, ease-out | No movement. No count-up, because the digits need to be readable immediately. |
| Wicket | Same highlight, stronger color, plus a short text tag in the row such as "WICKET" or "W" that stays | Highlight about 1200 ms. The tag stays until the next update. | The tag is the lasting record, so someone returning to the tablet still sees what happened. |
| Match ends or result posted | Persistent state change (bold result line) | Instant | This is content, not an effect. |
| Nothing changed | Nothing | n/a | Don't pulse on refresh. Only animate values that actually differ. |

Details that matter:

- **Diff the data.** Compare the new payload to the old one and highlight only what changed. Don't re-render whole rows, or everything will flash every 20 seconds.
- **Rate-limit.** If several values in one match change in a single refresh, give them one pulse together. Reserve the stronger wicket cue for wickets so it keeps its meaning.
- **Don't shift the layout.** Use tabular numerals (`font-variant-numeric: tabular-nums`) so "99" to "101" doesn't jiggle the row. Don't slide or reorder matches mid-read. If order changes, apply it on the next load or leave it fixed.
- **Don't flash.** A single fade is fine. Never blink or alternate colors.
- **Don't use sound by default.** Clubhouse speakers would annoy people. If you add it, make it an opt-in toggle, never autoplay, and never the only cue.

## For people who've scrolled away

A highlight on a row nobody can see is wasted. Two low-cost options:

1. **A small "updates" indicator in a sticky header.** For example "2 matches updated", with a link that jumps to them. It fades in over about 200 ms and clears when they scroll to the match or click it. This beats auto-scrolling, which you should never do.
2. **Update the tab title or favicon.** Something like "(1) Marlow Vale – Live" helps when the tab is in the background. It costs nothing and is the best option for people who left it open and wandered off.

## Accessibility

- Put the update in a polite live region (`aria-live="polite"`), such as "Oakfield 142/4, wicket". Keep it terse and batch it per refresh so screen readers aren't flooded.
- Under `prefers-reduced-motion`, keep the highlight, because it's an opacity/color change and not movement. Drop it only if you add any scale or slide. Keep the "WICKET" tag either way.
- The color shouldn't be the only signal. The tag and the changed text carry the meaning.

## Sketch

```css
.score-cell.changed {
  animation: settle 1000ms cubic-bezier(0.2, 0, 0, 1);
}
.score-cell.changed.wicket {
  animation-name: settle-wicket;
  animation-duration: 1200ms;
}
@keyframes settle        { from { background: rgb(255 193 7 / .55); } to { background: transparent; } }
@keyframes settle-wicket { from { background: rgb(220 53 69 / .55); } to { background: transparent; } }

@media (prefers-reduced-motion: reduce) {
  .score-cell.changed { animation-duration: 600ms; }
}
```

In the script, add `changed` only to cells whose value differs. Remove the class on `animationend`, so the next change can retrigger it. To restart a running animation, remove the class, force a reflow, then add it again.

If you share the page's HTML or the refresh script, I can wire in the diffing, the sticky "updated" indicator and the tab-title count.
