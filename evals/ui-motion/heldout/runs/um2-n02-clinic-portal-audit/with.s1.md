Anchor: quiet and crisp, like a tool people use to get something done. This is based on your descriptions, not the code. I assumed a web portal with CSS transitions.

## Ranked

| # | Action | Item |
|---|---|---|
| 1 | **Add** | Contact-details save feedback |
| 2 | **Add** | Lab result arrival cue |
| 3 | **Cut** | 600ms sideways tab slide |
| 4 | **Cut** | Row-by-row appointment fade |
| 5 | **Trim** | Bad-password shake |
| 6 | **Cut** | Logo bounce |
| 7 | **Leave** | Refill checkmark |

**1. Add: contact-details save feedback.**
- **Problem:** "Nothing, then a reload" reads as a hang. Patients will double-submit or wonder whether their phone number changed.
- **Fix:** The button shows "Saving…" in the same footprint, and the wait only gets an indicator past about 300ms. On success it shows "Saved" with a check. Don't disable the other fields.
- **If the reload stays:** motion can't carry the confirmation, because the page is gone. Show a persistent "Contact details saved" message at the top of the reloaded page, and put focus on it.
- **Better:** Submit without a reload and update in place.
- **Spec:** 150ms label and icon swap, ease-out. Keep the message visible 4–8s, announced to screen readers.

**2. Add: new lab results arriving silently.**
- **Problem:** This is the one change outside the user's focus, and the content matters.
- **Fix:** Fade and settle the new row in over 200ms with ease-out and about 8px of travel. Give it a highlight that starts strong and fades over about 1s. Add a text "New" tag that persists until seen.
- **Batching:** If several results land together, use one pulse for the batch.
- **Accessibility:** Announce it in an `aria-live="polite"` region.
- **Layout:** Don't push rows out from under someone who is reading or about to click. Insert above the viewport, or show a "2 new results" pill instead.
- **Reduced motion:** Keep the highlight and the tag, and drop the travel.

**3. Cut: 600ms sideways page slide between tabs.**
- **Problem:** It's the most frequent action in the portal, and it's slow, large and spatially false. Billing isn't "to the right of" Appointments.
- **Fix:** Swap the content instantly, or use a 120–150ms opacity crossfade. Optionally slide the active-tab underline for 200ms.
- **Interruption:** Clicking another tab mid-change must retarget immediately.

**4. Cut: 80ms-per-row stagger.**
- **Problem:** With 30–40 rows, the last row lands 2.4–3.2s late. Patients are often there to find one appointment, so this makes them wait for content that was already ready.
- **Fix:** Render the list at once. At most, fade the whole list in over 150ms.

**5. Trim: bad-password shake.**
- **Problem:** Three shakes plus a red flash is long and strobe-like, and the shake is the only error signal.
- **Fix:** Keep one small shake of about 6px for 300ms.
  - Make the red a steady border, not a flash.
  - Add text such as "That password isn't right" with an icon.
  - Move focus to the field.
  - Reserve the message's space so the layout doesn't jump.
- **Reduced motion:** Drop the shake and keep the border and text.

**6. Cut: logo bounce on load.**
- **Problem:** It has no job, bounce is wrong for a healthcare tone, and it replays on every visit. If the practice's brand brief explicitly wants it, limit it to once per session and under 400ms.

**7. Leave: Refill request checkmark.**
- **Why:** It's a cause-to-result confirmation in the control that was pressed. That's the right pattern.
- **Check only:**
  - The button keeps its width.
  - The check appears after the server confirms, not before.
  - There's a text state such as "Requested" for screen readers.
  - The swap takes 250ms or less.
  - Don't retune it otherwise.

## Not adding
- Page-load fades on content already in view.
- Scroll reveals.
- Row hover lifts.
- Count-ups on balances.
- Anything on the Billing totals.

These are decoration on pages people visit to get something done.

## Before shipping
Add a `prefers-reduced-motion` block that removes movement (slide, shake, travel) but keeps opacity, color, highlights and focus rings. Don't blanket-delete transitions.

If you share the CSS or components, I can turn this into exact changes.
