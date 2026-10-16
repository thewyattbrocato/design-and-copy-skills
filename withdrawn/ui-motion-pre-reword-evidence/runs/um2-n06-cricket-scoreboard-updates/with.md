Use a short colour highlight on only the cells that changed, plus a marker that stays until someone has seen the change. Don't use movement, popups or sound by default.

I'm assuming a calm, decisive feel, like a quiet scoreboard.

**1. Highlight only the cell that changed**
- When a score, wickets or overs value changes, give that cell a soft background tint (a pale amber works).
- The tint appears in about 150 ms and fades out over about 1.5 s. Animate only the background colour or opacity.
- Don't move, resize or bounce anything. Digits should not roll or count up. Use tabular figures (`font-variant-numeric: tabular-nums`) so the numbers don't jiggle when they change.
- Runs get the plain tint. A wicket gets a stronger tint and a small "W" or "WICKET" tag next to the score, because that is the event people most want to catch.

**2. Keep a marker until it has been seen**
- A 1.5 s fade is easy to miss when someone is looking away from the screen. So also leave a small dot or "updated 14:32" label on any match that changed.
- Clear it when the person hovers over the match, taps it, or scrolls it into view for about a second.
- Wickets keep a more visible marker, such as a coloured left edge on the match row, until the same kind of dismissal.
- Use `IntersectionObserver` for the "scrolled into view" check.

**3. Never shift the layout while someone is reading**
- Don't reorder matches or insert rows when a score updates. Update values in place.
- Reserve fixed width for the score cells.
- If a match finishes or a new one starts, change its status label in place. Move it between sections only on a manual refresh or the next page load.
- Don't auto-scroll, and don't show modals, toasts or banners for ordinary score changes.

**4. Handle background tabs and the tablet in the clubhouse**
- Check `document.visibilityState`. When the tab is hidden, skip the animation and just update the data.
- When the tab becomes visible again, show the "changed since you looked" markers from point 2. That way people returning from another window see what happened without a burst of flashing.
- Optionally, put a count in the tab title, such as "(2) Marlow Vale Scores", and clear it when the tab is visible. A wicket in the title is a cheap way to catch someone's attention without touching the page.
- Make sound opt-in only, for example a "Chime on wickets" toggle that defaults to off. A chime every 20 seconds in a clubhouse would annoy people quickly.

**5. Accessibility**
- Keep the whole cue to colour and opacity. The highlight, the marker and the "W" tag don't depend on motion, so `prefers-reduced-motion` needs almost no special handling. Under it, you can drop the fade and show the tint for a fixed time, then remove it.
- Don't rely on colour alone. The label text ("W", "updated") carries the meaning too.
- Use one visually hidden `aria-live="polite"` region that announces only wickets and match results, for example "Marlow Vale 3 down for 82". Don't put live regions on every score cell, because that would read out every update.
- Nothing should flash more than three times in a second. Your 20 s cadence is far below that, but if several matches update together, they should fade in step instead of blinking one after another.

**Summary**

| Event | Cue | Timing | Stays until seen |
|---|---|---|---|
| Runs or overs change | Pale tint on that cell | 150 ms in, about 1.5 s fade | Small dot on the match |
| Wicket | Stronger tint, "W" tag | Same, with a slightly longer fade | Left edge colour on the match row |
| Match ends | Status label changes in place | 150 ms | Result label stays |
| Tab hidden | No animation | None | Markers shown on return |

If you share the page's CSS or JS, I can write the update function, the fade and the visibility handling for your 20 s script.
