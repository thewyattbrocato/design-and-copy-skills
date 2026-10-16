Make changes loud enough to catch a glance, but never move anything on the page.

**1. Highlight in place and let it fade slowly.**
- Someone on a second monitor will miss a 1-second flash. When a value changes, give that cell a soft background tint that holds for about 30–60 seconds and then fades out. Anyone who looks over late can still see what just changed.
- Update only the cells whose values actually changed. If you re-render everything every 20 seconds, the whole page flickers.

**2. Use two tiers.**
- **Runs:** a subtle tint plus a small delta, such as "+4" or "+6", next to the score.
- **Wickets:** a stronger accent color and a "W" badge that stays for 1–2 minutes. Wickets are the moments people care about most.

**3. Never shift the layout.**
- Don't re-sort matches, insert rows, or auto-scroll while someone is reading. Keep the scroll position and the order stable.
- If you want "live matches first", apply that ordering only on a manual refresh.

**4. Tell people about changes they can't see.**
- If a match is scrolled off-screen, show a small pinned pill at the top, like "2 matches updated ↑". Clicking it scrolls to the first one.
- For tabs in the background, put the count in the tab title, e.g. `(2) Marlow Vale Live`. You can do this with `document.title` and the `visibilitychange` event.
- When someone returns to the tab, highlight everything that changed while they were away.

**5. Make it accessible.**
- Don't rely on color alone. The "+4" and "W" text covers that.
- Respect `prefers-reduced-motion`. Use a static highlight with no animation.
- Avoid rapid flashing.
- For screen readers, use one `aria-live="polite"` region with a summary like "Wicket: Riverside 84/5". Don't put live regions on every number.

**6. Show that the page is live.**
- A small "Updated 12s ago" label tells people the page is working.
- If an update fails, change the label (e.g. "Connection lost, retrying"). Otherwise a stale page looks like a quiet match.

**What to skip:** sound, popups or toasts, count-up animations, and shaking or pulsing. Each of these gets annoying fast on a screen that stays open all day. If people ask for sound, make it an opt-in toggle for wickets only.

If you'd like, I can sketch the CSS and JS for the fading highlight and the "N updated" pill. If you share your page markup, I can write it to fit.
