I'm working from your description, not the code. Ranked by user impact:

**1. Add: save confirmation on the contact-details form.**
This is your worst gap. Saving, then nothing, then a page reload looks like a failure, and people resubmit or wonder whether their phone number changed.
- Disable the button and show "Saving…" while the request runs.
- Afterwards, show an inline "Contact details saved" message. Put it in an `aria-live="polite"` region so screen readers announce it.
- If the reload has to stay, persist the message across it as a banner. Better still, drop the reload and update in place.
- This needs no flashy animation. A short fade-in of the message is enough.

**2. Cut: the 80ms row stagger on appointments.**
With 30 to 40 rows, the last row appears after 2.4 to 3.2 seconds. That's on a screen people open to find one date.
- Render the list at once.
- If you want some polish, fade the whole list in over about 150ms.

**3. Cut and replace: the 600ms full-page sideways slide on tab switches.**
- Sliding the whole page, including the header and tabs, is slow and disorienting. It's also a motion-sickness trigger for some users.
- Keep the tab bar and header fixed. Swap only the panel content, either instantly or with a crossfade of 150ms or less.

**4. Add: a visible cue for new lab results.**
Results appearing silently is a real problem, because these are the items people most need to notice.
- Add a "New" badge, or a highlight that fades over a couple of seconds.
- Announce the arrival through an `aria-live="polite"` region.
- Don't shove rows down while someone is reading or about to click. If they've scrolled or are interacting, show a "1 new result" banner instead of inserting.

**5. Change: the bad-password feedback.**
Three shakes plus a red flash is too much, and a flash conveys nothing to colorblind users.
- Make an inline text error the primary signal, e.g. "That password isn't right," tied to the field. Move focus back to the field.
- If you keep the shake, make it one nudge of about 200ms. Drop the flash and use a steady red border plus the text.

**6. Cut: the logo bounce on load.**
It carries no information, repeats on every load, and delays nothing useful. Remove it, or at most use a plain fade.

**7. Leave alone: the Refill request button's checkmark.**
It confirms a discrete action, it's quick, and it sits where the user's attention already is. Two checks:
- Make sure it has a pending state and an error state.
- Make sure the confirmed state also changes the label, e.g. "Requested," so it isn't an icon only.

**Across the board:** honor `prefers-reduced-motion`. When it's set, turn the slide, shake and highlight fades into instant changes or plain opacity fades. Your users skew older, so this matters more than usual.

**Net effect:** you'd remove about three seconds of dead time and a lot of decoration. You'd add the two things that matter for trust in a health portal: confirmation that a save worked, and notice that new results arrived.
