I'm working from your description only, not the code. Ranked by impact:

1. **Contact-details save: add feedback (biggest gap).**
   - Right now the user gets silence, then a reload. For a form holding personal health information, they can't tell whether it worked.
   - Disable the button on submit, and show a spinner only if the save takes longer than about 200ms.
   - After the save, show a persistent "Contact details saved" message in an `aria-live` region. If you keep the reload, show the message after it, because a toast would vanish with the page. Better, update in place and drop the reload.
   - Motion matters little here. The missing status is the real problem.

2. **New lab results: add a visible, non-disruptive arrival.**
   - Silent insertion causes layout shift. Someone could click the wrong row, and a screen reader user never learns anything changed.
   - Don't push content down under the user's cursor. Either show a "1 new result" banner they can click, or insert the row with a short highlight that fades over 1 to 2 seconds.
   - Add a "New" badge that stays until the result is viewed. Motion alone is transient and easy to miss.
   - Announce it with `aria-live="polite"`.

3. **Tab slide: cut it and replace it with something smaller.**
   - A 600ms full-page sideways slide is too slow for something people do repeatedly. Large lateral motion is also a vestibular trigger.
   - The tabs are peers, not spatial navigation, so the slide implies a spatial model that doesn't exist.
   - Swap the content instantly, or crossfade just the panel in 100 to 150ms. If you want some motion, slide only the active-tab underline.

4. **Row-by-row list fade: cut it.**
   - At 80ms per row, 40 rows take about 3.2 seconds to finish. People looking for an appointment wait on decoration.
   - Render the list immediately. If you want something, fade the whole list in once, in 150ms or less.

5. **Bad-password shake: keep it, but tone it down.**
   - Three shakes plus a red flash is punishing, and a flash shouldn't be the only error signal.
   - Use one short shake (about 250ms) and no flash. Add an inline text error ("Incorrect email or password"), tie it to the field, and move focus there.
   - The text carries the message, and the shake just reinforces it.

6. **Logo bounce on load: cut it.**
   - It plays on every page load, adds no information, and delays nothing useful. It also reads as playful on a screen people open about their health or bills.
   - If branding matters, a single quiet fade is enough.

7. **Refill button checkmark: leave it alone, with a check.**
   - It's a good pattern: it gives immediate, local confirmation.
   - Verify that it shows a pending state before the checkmark, so it doesn't confirm before the server does.
   - Verify that it ends on a state with text ("Requested") and stays disabled, so the user can't submit twice.
   - Verify that the change is announced to assistive tech.

**Across everything you keep:** wrap the motion in `prefers-reduced-motion`. Under that setting, drop the shake, highlight and crossfade to instant changes, and keep the text and badge signals.

**The pattern:** your decorative motion (slide, stagger, bounce) is slow and gets in the way, while your meaningful state changes (save, new results) have none. The redesign should move that motion budget from the first group to the second.
