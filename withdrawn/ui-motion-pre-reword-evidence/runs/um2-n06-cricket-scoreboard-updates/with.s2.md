Use a short, quiet motion to catch the eye, and a persistent marker that stays after the motion ends. A 300 ms flash is gone before someone glances back from another monitor, so the marker is what carries the message.

Feel: calm and decisive, like a scoreboard that updates in place.

## 1. When a score or wicket changes (the match is on screen)

- **Highlight the changed number only.** Not the whole card.
  - Animate the background of that cell from a soft accent tint to transparent.
  - Use 1.5 s with ease-out, so it appears instantly and fades slowly.
  - Animate only `background-color` or `opacity`.
- **Don't move or resize anything.** Swap the digits in place with no count-up and no sliding. Give the numerals a fixed width with `font-variant-numeric: tabular-nums` so nothing shifts. Layout shift is the most annoying thing while someone is reading.
- **Make wickets stronger than runs.** A wicket is rarer and matters more, so it gets a second cue. Use a different tint, and a small "W" or "WICKET" tag next to the score. Keep runs to the tint alone.
- **Leave a marker that outlasts the motion.** Keep a small dot, or a "+4" or "Wicket" tag, beside the changed value for about 60 s, then fade it out over 300 ms. Someone returning to the tablet can then see which matches moved while they were away. A pulse that happened five seconds ago can't tell them that.

## 2. When the change is off-screen (they've scrolled)

- **Don't scroll them or reorder the list.** Rows must never jump under a reader.
- **Mark the match's own card** with the same dot or tag, so the change is there when they scroll past.
- **Add a small sticky pill at the top**, such as "2 matches updated". Fade it in over about 200 ms with a few pixels of travel, and keep it still afterwards. Tapping it scrolls to the first changed match. Update the count in place rather than stacking toasts.

## 3. When the tab is in the background

- Update the tab title, for example `(2) Marlow Vale Live`, and clear it when the tab gets focus.
- Don't use sound or vibration by default. In a clubhouse it would fire constantly. If you want it, make it an opt-in toggle for wickets only.

## 4. Things to avoid

- **Re-rendering the whole list every 20 s.** Update only the changed text nodes. Replacing the DOM loses scroll position and text selection, and flickers every card, which is the biggest annoyance risk here.
- **Looping pulses or glows.** Anything that keeps moving on a second monitor becomes irritating very quickly.
- **Flashing.** One slow fade is fine. Never blink or flash the same element repeatedly.
- **Animating on first load.** Only animate changes after the initial render.
- **Several things at once.** If many matches change in the same refresh, apply the same highlight to each with no stagger, so they all appear together.

## 5. Spec

| Cue | Trigger | Motion | Duration / easing | Persists |
|---|---|---|---|---|
| Score changed | Value differs from last poll | Background tint fades to transparent | 1.5 s, ease-out | Dot or "+n" for 60 s |
| Wicket | Wicket count increases | Stronger tint, plus "W" tag | 2 s, ease-out | Tag for 60 s |
| Off-screen change | Changed card outside viewport | Sticky pill fades in with 4 px travel | 200 ms ease-out in, 150 ms out | Until tapped or scrolled to |
| Tab title | Changes while hidden | None | n/a | Until tab is focused |

**Interruption:** a new update during a fade restarts the fade from the full tint. Never queue animations.

**Reduced motion** (`prefers-reduced-motion: reduce`): remove the fade and the pill's travel. Show the tint as a static highlight that disappears after the same 1.5 s. Keep the dots, tags and pill, because they are information rather than motion.

**Accessibility:** don't put `aria-live` on the whole page, because a screen reader would announce every refresh. Put `aria-live="polite"` only on the "N matches updated" pill. Optionally add a visually hidden announcement for wickets in the match the user is following.

If you share the markup or the script that does the refresh, I can write the CSS and the diffing code that updates only the changed cells.
