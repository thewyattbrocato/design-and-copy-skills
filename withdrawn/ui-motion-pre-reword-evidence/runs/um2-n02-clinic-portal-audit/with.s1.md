**Anchor:** calm and decisive, like a quiet clinical tool. Patients come here to check something and leave. I'm assuming a web app, with these screens used often. I haven't seen your code, so the specs below are targets.

## Ranked

**1. Cut: the row-by-row fade on appointments.**
- 40 rows at 80ms each means the last row arrives at about 3.2s, so people wait to read their own appointments.
- Render the list immediately. If you want one cue, fade the whole list in over 150ms ease-out with no stagger.
- A stagger is only acceptable for about 8 items, 20–40ms apart, capped near 250ms total. This list is far past that.

**2. Cut and replace: the 600ms full-page sideways slide between tabs.**
- This is your most frequent interaction, and it pays the most for its cost. Sliding the whole page is also a common cause of motion discomfort.
- Swap only the panel content, using a 120ms fade-out then a 160ms fade-in (ease-out, opacity only, no travel). Slide a tab underline between tabs over 200ms ease-in-out, so people can see where they are.
- Make it interruptible. A second click mid-transition retargets from the current state, and tabs are never disabled while it plays.

**3. Add: feedback when the contact-details form saves.**
- Right now there's nothing, then a reload. People can't tell whether it worked, and they'll double-submit.
- Within 100ms, put the button into a pending state ("Saving…"). Don't show a spinner unless the wait passes about 1s.
- After success, show persistent "Details saved" text next to the form, and move focus to it. If the page must reload, show that message after the reload, because a toast would be wiped by it.
- On failure, show text near the field. Motion is optional here.
- Better still, submit without reloading so the message can appear in place.

**4. Add: a visible, announced arrival for new lab results.**
- This is a change outside the person's focus, and it matters. Silent inserts shift rows under their cursor or finger.
- Fade the new row in over 200ms and mark it "New" until it's viewed. Don't add a highlight that flashes.
- If the user is scrolled down or mid-interaction, don't insert it live. Show a "1 new result" banner they can click.
- Announce it through a polite live region for screen-reader users. This is the one item where accessibility matters more than animation.

**5. Reduce: the bad-password shake.**
- Three shakes plus a red flash is too much for a rare event. A flash repeated three times is also close to the flashing-safety limit.
- Keep persistent error text next to the field ("Incorrect password"), move focus to it, and leave the field contents alone.
- Optionally add one small horizontal nudge of about 6px over 250ms, with no color flash. Under reduced motion, drop the nudge and keep the text.

**6. Cut: the logo bounce on load.**
- It has no job and it plays on every load. Bounce is also a poor fit for a dental portal's calm tone. Show the logo static.

## Leave alone

**The Refill request button turning into a checkmark.**
- It confirms an action in place, on the control the person just pressed. That is the job.
- One check: the checkmark should appear only after the server confirms, and the button should keep a text or accessible label such as "Requested". If that's already true, don't touch it.

## Across all of it

- Under `prefers-reduced-motion`, remove movement (the slide, the nudge, the underline travel). Keep opacity changes, the persistent messages and focus styles. Don't strip every transition.
- Standardize on three durations (120, 200, 300ms), ease-out for things arriving and fast fades for things leaving, so the redesign has one vocabulary.

The cuts (1, 2, 6) are mostly deletions, so they're the cheapest and ship first. Item 3 is the best-value addition. Item 4 is the one that needs design and accessibility work, so start it early.
