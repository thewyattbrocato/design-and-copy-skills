Make the loudness proportional to how much the change matters. Keep the layout completely still, and let people who weren't looking catch up afterward.

**1. Three tiers of change**
- **Runs and overs (routine):** Update the number in place. Give it a soft background tint that fades over 1–2 seconds, and show the delta briefly, like "+4". This should be easy to ignore.
- **Wicket:** Treat it as a bigger event. Give the card a stronger highlight and a "W" badge or the dismissed batter's name. It should stay visible for 60–90 seconds, because a 2-second flash on a second monitor is easy to miss.
- **Milestones (50, 100, innings end, result):** Use the same treatment as a wicket, or a slightly longer one.

**2. Fade, then leave a quiet trace**
After the animation ends, keep a small "updated 0:40 ago" label or a thin accent edge on the card that fades over a minute or two. Someone who glances over 30 seconds later can still see what changed.

**3. Never move things around**
- Update only the text nodes that changed, and don't re-render the whole list. This keeps scroll position, text selection and hover state.
- Don't reorder matches, auto-scroll, or open modals or toasts over the content.
- Reserve space for badges so nothing shifts.

**4. Changes that happen off-screen**
For people who've scrolled to read another match, show a small pill pinned to an edge, such as "● Wicket – Marlow v Vale". Clicking it scrolls to that card. Combine several changes into one pill ("3 updates"), and don't stack a notification for each.

**5. Changes while the tab is hidden or the tablet is asleep**
- Browsers throttle timers in background tabs. When the page becomes visible again, listen for `visibilitychange`, refresh straight away, and show a "Since you last looked" summary. Don't replay every animation you missed.
- Put a marker in the tab title, like "(W) Marlow v Vale", so the change shows up in the tab bar.
- Skip animations on the first page load.

**6. Sound and system notifications are opt-in**
They're off by default. If you add them, offer a toggle, and consider limiting them to wickets and match results, and to matches the user has starred. In a clubhouse, unprompted sound will annoy people quickly.

**7. Accessibility**
- Don't rely on color alone. Pair it with the badge, the "+4", or an icon.
- Under `prefers-reduced-motion`, replace the fade with a static highlight.
- Put wickets and results in an `aria-live="polite"` region. Leave routine runs out of it, or screen readers will announce every refresh.

**8. Refresh behavior**
Compare the new data against the previous data and only animate real differences. Merge multiple changes from one refresh into a single animation per card. If cricket-specific events like boundaries matter to people, a small "4" or "6" tag works well as a middle tier.

Optional: let people star their teams or matches. Then those cards get the full treatment, and others get only the subtle one. That does more to reduce annoyance than any animation tweak.

I can sketch the CSS and JS for the diff-and-highlight logic if you'd like. What are you building it with: plain JS, React, or something else?
