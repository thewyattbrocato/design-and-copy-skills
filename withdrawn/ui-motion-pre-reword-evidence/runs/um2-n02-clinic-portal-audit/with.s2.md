Assumptions: web app, calm and decisive tone, CSS transitions, and system reduced-motion honored. Say if any of that is wrong.

## Add

**1. Saving the contact-details form (cause to result, highest value).**
- **Problem:** The user gets no feedback, then the page reloads. For contact details, they can't tell whether it worked.
- **Fix:** Save in place and drop the reload.
  - The button acknowledges the press within 100 ms.
  - Show a spinner inside the button only if the save takes longer than about 1 s.
  - On success, show persistent "Saved" text next to the button. Fade it in over 150 ms with ease-out.
  - On failure, show the error next to the field. Don't clear the form.
  - Keep the button live. Don't disable the whole form while saving.
- **Effort:** Medium, because the reload has to go.

**2. New lab results appearing silently (change outside focus).**
- **Problem:** Lab results are the item patients care most about, and the list changes without telling them.
- **Fix:**
  - Fade the new row in over 200 ms with ease-out.
  - Tint its background and fade the tint out over about 2 s, so the user can find it.
  - Don't shove rows down under someone who is reading or about to click. If they're scrolled away from the top, show a "1 new result" pill instead of inserting.
  - Announce the arrival through a polite live region, so screen-reader users also get it.
- **Effort:** Small to medium.

## Cut

**3. Tab slide over 600 ms.**
- **Problem:** Appointments, Billing and Messages are peers, not places in a row. The slide implies a spatial order that doesn't exist. It also costs 600 ms on every switch of a frequent action, and it moves the whole page.
- **Fix:** Swap instantly, or use a 120 to 150 ms opacity crossfade of the content area only. Keep the active-tab indicator change at about 150 ms.

**4. Row-by-row fade, 80 ms each.**
- **Problem:** At 30 to 40 rows, the last row lands at 2.4 to 3.2 s. The list is the content, and users are waiting for it to finish.
- **Fix:** Render it immediately. At most, fade the whole list in over 150 ms.

**5. Logo bounce on load.**
- **Problem:** It has no job, it recurs on every load, and bounce is the wrong register for a healthcare portal.
- **Fix:** Cut it.

## Trim

**6. Bad-password shake (3 shakes plus red flash).**
- **Problem:** It's too much for a mistake users make often, and three shakes plus a flash gets close to the flashing-safety limit.
- **Fix:**
  - Make persistent text under the field the primary cue ("That password isn't right"), and move focus to the field.
  - Keep a red border.
  - Optionally add one 250 ms shake of about 6 px as a secondary cue.
  - Under reduced motion, drop the shake and keep the text and border.
- **Check:** I don't know whether the message text exists today. If it doesn't, add it before touching the shake.

## Leave alone

- **Refill button turning into a checkmark.** It confirms an action in the control the user just pressed, which is the right place. I'm not retuning it. Check three things, none of them a redesign:
  - It should flip only after the server confirms.
  - A text label such as "Requested" should persist, so the checkmark isn't the only signal.
  - It should respect reduced motion by swapping with no movement.

## Across the board

Add a `prefers-reduced-motion` block. It should remove movement (slides, shakes, travel) and keep opacity, color and focus feedback. Don't delete all transitions. Keep to one set of values: 150 ms for small changes, 200 ms for insertions, and ease-out for anything arriving.

**Net effect:** The redesign adds two things, which are save feedback and a visible new-result cue. It cuts three, which are the slide, the stagger and the bounce. It trims one, the shake. It leaves one alone, the refill checkmark.
