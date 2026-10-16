Make the change visible where people are already looking, and leave a quiet trace for anyone who looked away.

**1. Update in place, and never move things**
- Don't reorder cards, auto-scroll, or open modals or toasts over the content. Anyone reading a match further down the page will lose their place.
- Use `font-variant-numeric: tabular-nums` and fixed-width score cells so a change from 99 to 100 doesn't shift the layout.

**2. Give a score change a short highlight**
- Flash the changed number with a soft background tint that fades over about 2–3 seconds. Run it once, not as a loop.
- A 20-second cycle means a fade is easy to miss if someone glanced away, so add the next point.

**3. Leave a faint "recently changed" marker**
- Put a small dot or a "NEW" tag on the match card for about 60–90 seconds. It should clear on its own, or when the user hovers or clicks.
- Show "Updated 12s ago" per match, or once globally. This also tells people the page is still live.

**4. Treat wickets as stronger than runs**
- Runs get only the subtle highlight.
- A wicket gets a short event line on the card, such as "WICKET – Smith b Jones 34", with a distinct accent and an icon. The line stays until the next event.
- Don't rely on color alone. Use text or an icon too.

**5. Handle changes off-screen**
- If an update happens in a match that isn't in view, show a small, non-blocking pill such as "2 updates below". Clicking it scrolls to the match.
- Update the tab title, for example "(2) Marlow Vale Live", for people on another tab or monitor.
- Let people star or follow their own team's match. Only followed matches get stronger cues, so everyone else isn't pulled around by every game.

**6. Handle edge cases**
- On first load, and when a hidden tab becomes visible again, don't animate every difference. Show one "Since you left: 3 updates" summary or just the markers. A refresh after a long gap shouldn't turn into a flashing wall.
- If several things change in one refresh, batch them so they appear together instead of one after another.
- Respect `prefers-reduced-motion`. Replace the fade with a static highlight that clears after a few seconds.
- Use `aria-live="polite"` only for followed matches, so screen readers don't announce every update.

**7. Keep sound and notifications opt-in**
- A clubhouse tablet shouldn't make noise by default. If you add sound or browser notifications, make them an explicit toggle for wickets in followed matches only.

If you want, I can build this as a small CSS and JS example that fits your 20-second refresh script. Tell me how the page is structured (plain HTML, a framework, or server-rendered).
