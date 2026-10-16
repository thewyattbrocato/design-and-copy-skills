**Anchor:** quiet and crisp, like a scoreboard that taps you on the shoulder. This is a web page, and the values below are starting points to tune.

## The approach: highlight the changed value, don't animate it

Nobody is looking at the number when it changes, so the cue has to be strong the instant it lands and then fade. Don't use bounces, count-ups, sliding digits or flashing. Those are what annoy people on a page that updates every 20 seconds, all day.

**Score change (runs or total)**
- Swap the number instantly. It must be readable the moment it changes.
- Put a background highlight on that value, such as a soft amber tint. It starts at full strength immediately and fades out over about 1.2 s with ease-out.
- Don't move the number or the layout. Use tabular numerals so the digits don't shift width.

**Wicket**
- It matters more than runs, so give it a second cue that doesn't rely on motion. Use a different color (red tint instead of amber) and a small "W" or "WICKET" tag next to the score. The tag stays for about 60 s, or until the next ball or update.
- The highlight timing is the same as for runs. The extra weight comes from the color and the tag, not from more movement.

**Match-level state**
- If a match finishes or an innings ends, show it as a persistent status label ("Innings break", "Result"), not as an animation.
- If a match is off-screen, the same highlight still runs. People who scroll back will see the "last changed" tag instead.

## Handling "away on another task" and "scrolling"

- **Don't re-run the highlight for stale changes.** If the tab was hidden or the tablet was asleep, don't replay a pile of animations when it wakes. Apply the latest values quietly and show a small "Updated 14:32" stamp or a "changed" tag. Check `document.visibilityState` before animating.
- **Rate-limit.** If several things change in one refresh, pulse each changed value once together. Don't stagger them, and don't go louder each time.
- **Keep the tag as a second channel.** A small dot or "NEW" marker beside a changed match, fading after about 60 s, helps people who were scrolled elsewhere and missed the 1.2 s pulse. A pulse alone can't reach someone who isn't looking.
- **Don't reorder or move cards on update.** Nobody should lose the match they were reading. If you want a "live matches first" order, do it only on page load or on a manual action.
- **Don't scroll or steal focus.** Never auto-scroll to the changed match.
- **Optional:** a quiet counter in the page title or tab ("● 2 updates") helps the clubhouse tablet case. Skip sound unless there's an opt-in toggle. A chime every 20 s in a clubhouse would be a nuisance.

## Accessibility

- With `prefers-reduced-motion`, the highlight is only a color fade, so it already qualifies. Shorten it or make it a static tint that clears after a moment. Keep the tag.
- Don't use color alone. The "W" tag and the text carry the meaning.
- Make sure the highlight never flashes more than three times a second. Yours is one fade, so it's safe.
- For screen readers, put a short summary in a polite live region ("Marlow CC 142 for 4"). Announce only wickets and milestones, not every refresh.

## Spec

| Motion | Trigger | Properties | Duration | Easing | Interrupt | Reduced motion |
|---|---|---|---|---|---|---|
| Run change | Value differs after refresh | background-color on the value | 1200 ms fade from full tint | ease-out | A new change restarts from full tint | Tint holds about 1 s, then clears (no movement involved) |
| Wicket | Wickets count increases | red tint + "W" tag | 1200 ms fade; tag holds about 60 s | ease-out | Same as above | Same, tag unchanged |
| Changed marker | Any change on an off-screen match | dot/tag opacity | 200 ms in, 300 ms out after about 60 s | ease-out / ease-in | Resets on a new change | Same (opacity only) |
| Wake / hidden tab | `visibilitychange` to visible | none | n/a | n/a | n/a | Apply values silently and show "Updated" stamp |

## Sketch

```css
.score.changed { animation: settle 1200ms cubic-bezier(0.2, 0, 0, 1); }
.score.changed.wicket { --flash: var(--wicket-tint); }
@keyframes settle { from { background: var(--flash, var(--run-tint)); } to { background: transparent; } }
.score { font-variant-numeric: tabular-nums; }
@media (prefers-reduced-motion: reduce) {
  .score.changed { animation-duration: 1000ms; animation-timing-function: linear; }
}
```

In the script, compare old and new values per match, add `changed` only to cells that differ, remove the class on `animationend`, and skip the animation when `document.hidden` is true.

If you tell me how the page is built (plain HTML plus a fetch loop, a framework, or server-rendered), I can write this into the actual code.
