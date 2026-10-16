Make a changed score or wicket show up with a strong cue that settles, and don't let the number itself move. Anchor on quiet and crisp, like a scoreboard that stays readable.

## The core pattern: highlight the cell that changed, and let it fade

The change usually happens away from where people are looking, so it needs a stronger cue than a hover would. A flash or bounce is the wrong cue.

- **Score changes** (runs, overs, run rate): the new value appears instantly and stays fully readable. Put a soft background tint behind just that value. The tint starts at full strength and fades over about 1 s.
- **Wicket changes**: use the same mechanism with a different color, such as red or amber. Add a short text tag ("W", or "Wicket: Smith c Jones b Patel") that stays on the match row for 30–60 s or until the next ball. A wicket is rare and matters more than a run, so it can have a stronger and longer cue than the score tint.
- **Don't animate the digits.** No count-ups, rolling odometers or sliding numbers. They make the number harder to read at the moment it matters most.
- **Don't move the layout.** Reserve space for the wicket tag so rows don't jump. People who are scrolling or aiming at something would otherwise get the page shifting under them.

```css
.cell.changed { animation: settle 1000ms ease-out; }
@keyframes settle { from { background-color: var(--highlight); } to { background-color: transparent; } }
.cell.wicket.changed { --highlight: var(--wicket-color); animation-duration: 1600ms; }

@media (prefers-reduced-motion: reduce) {
  /* the tint is a color change, not movement, so it can stay */
  .cell.changed { animation-duration: 600ms; }
}
```

## Making it not annoying

1. **Only highlight what changed.** Compare each new value to the old one in your refresh script. Don't re-render or re-highlight every row every 20 s. If everything flashes on a timer, people learn to ignore it.
2. **Rate-limit the cue.** If a match changes several fields in one refresh (runs, overs and strike rate), tint them together as one batch. Don't highlight the secondary stats (run rate, extras) at all, or use a much fainter tint.
3. **Don't get louder over time.** Use the same intensity every time. Reserve the stronger treatment for wickets, milestones (50, 100) and match results.
4. **Don't flash.** A single fade is fine. Never pulse repeatedly, and never exceed three flashes per second.
5. **Use no sound or vibration by default.** A clubhouse is a shared space. If you add sound, make it an opt-in setting.

## Handling the two ways people use the page

**People who leave it open on a second monitor** won't see a 1 s fade, so the page needs a persistent cue as well:
- Show a small "updated 12:04:20" stamp or a "last changed" marker on each match row, such as a dot that stays until the person interacts with the page or a minute passes.
- Update the tab title when something changes, for example "(1) Marlow v Vale – W". Only use this for wickets and results so it doesn't nag.

**People who scroll to read other matches** will miss changes in rows that are off-screen:
- Never reflow the list or scroll the page when data refreshes. Keep scroll position and row order fixed.
- If a match moves out of view and changes, show a small "2 matches updated" pill at the top of the viewport. Tapping it scrolls to the first change. Don't auto-scroll.
- When a row scrolls into view, play its highlight if it changed within the last minute. Otherwise people never see what changed.
- Don't re-sort rows on update. If you must support "live first" ordering, re-sort only on a user action.

## Accessibility

- Put the change in text as well as color. The "W" tag and the "updated" stamp do this, and color-blind people need it too.
- Announce only important changes (wickets, results) in a polite `aria-live` region. Announcing every score refresh every 20 s makes the page unusable with a screen reader.
- Because the page updates automatically, offer a "Pause updates" control.
- Under `prefers-reduced-motion`, keep the tint. It's a color change, not movement. Shorten it and drop anything that slides or pulses.

## Spec

| Motion | Trigger | Property | Duration | Easing | Interrupt | Reduced motion |
|---|---|---|---|---|---|---|
| Score tint | Value differs from last refresh | background-color | 1000 ms | ease-out | A new change restarts the tint | 600 ms, same |
| Wicket tint | Wicket count increases | background-color | 1600 ms | ease-out | Restarts | 600 ms, same |
| Wicket tag | Wicket count increases | opacity only | 200 ms in; stays 30–60 s | ease-out | Replaced by the next wicket | Instant |
| "N updated" pill | Off-screen change | opacity | 200 ms in, 150 ms out | ease-out / ease-in | Updates its count | Instant |

I assumed a web page using plain CSS. If you tell me your stack, such as React re-rendering or a plain DOM update, I can show how to detect "this value changed" and restart the animation reliably. That is the part that usually goes wrong.
