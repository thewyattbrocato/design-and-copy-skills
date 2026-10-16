I'd make the change visible in place, make it last long enough to catch a glance, and never move anything. I'm assuming a calm, decisive tone and a plain web page with CSS.

**1. Highlight only the values that changed.**
- Compare each poll with the previous one and touch only the cells that differ. Unchanged matches do nothing every 20 seconds.
- Swap the number instantly so the information is never delayed.
- Add a background tint behind it. It starts at full strength and fades out over about 2.5 s with `ease-out`. This animates only `background-color` or `opacity`.
- Don't use count-ups, rolling digits, or slides.

**2. Make the cue last longer than the flash.**
Someone looking at another monitor will miss a 2.5 s fade. So after the fade, leave a quiet "recently updated" marker on that match row, such as a small dot or a slightly bolder score. Clear it after about 60 s, or sooner if they hover or click the row.

**3. Treat a wicket as a bigger event than runs.**
- Runs get the tint only.
- A wicket gets a stronger tint, a "W" chip next to the score, and a marker that lasts longer, about 2 minutes.
- Don't add shake, pulse, or looping animation. Wickets come often enough that anything loud gets old by the third one.

**4. Don't shift the layout.**
- Never reorder matches, insert rows, or auto-scroll when data changes. Someone mid-read must not have the page jump.
- Use `font-variant-numeric: tabular-nums` and reserve space for the "W" chip so digits don't resize anything.
- If a match needs to move, such as when it finishes, leave it where it is until the next manual refresh or page load.

**5. Handle matches that are off-screen.**
For people who scroll, show a small sticky pill at the top, like "2 matches updated ↓". Clicking it scrolls to the first changed match. Fade it in over about 200 ms and update its count in place. It shouldn't steal focus.

**6. Handle people who aren't looking at the tab.**
- Update `document.title`, for example `(1 wicket) Marlow Vale Live`. Clear it when the tab becomes visible.
- Skip sound by default. In a clubhouse it would be annoying. If you add it, make it an opt-in toggle.

**7. Batch simultaneous changes.**
If several things change in one poll, they all tint at once with no stagger. Twenty-second updates are frequent enough that choreography would just be delay.

**8. Handle accessibility.**
- Under `prefers-reduced-motion`, keep the tint and markers. They're color and opacity, not movement. Only remove any slide on the pill.
- Don't make the whole table `aria-live`. Use one visually hidden `aria-live="polite"` region with a short summary like "Wicket: Riverside 112 for 6".
- Don't rely on color alone. The dot, chip, and bold text carry the meaning too.

| Cue | Trigger | Timing |
|---|---|---|
| Tint on changed value | Any score change | Instant on, 2.5 s fade, ease-out |
| Wicket tint and W chip | Wicket | Stronger tint, same fade, chip stays about 2 min |
| "Updated" dot | Any change | Stays about 60 s, cleared on interaction |
| Sticky pill | Changes off-screen | 200 ms fade in, count updates in place |
| Tab title | Hidden tab | Until the tab is visible |

If you share the markup or the polling script, I can wire this up. It's about 30 lines of diffing JS and a few CSS rules.
