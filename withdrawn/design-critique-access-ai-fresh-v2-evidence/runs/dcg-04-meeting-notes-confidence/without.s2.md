# Critique: meeting-notes screen

The main problem is that the screen asks users to trust AI output, gives them almost no way to fix it, and then makes sending the output to everyone the biggest thing on the page.

## Most serious

**1. The send button is high-stakes and unguarded.**
- It sends to every attendee, which is outward-facing and can't be undone.
- Nothing lets the user preview what goes out, choose recipients, or confirm.
- The 41% and 62% items would go out unreviewed.
- A wrong task assigned to a named colleague in front of the whole group is a real social cost.
- **Fix:** Put the recipient count in the label ("Send to 7 attendees"). Add a preview or confirm step. Allow a "send to me first" option. Consider a short undo window.

**2. The uncertainty signal is unlabeled, small and grey.**
- The percentages are the most decision-relevant data on the screen, and they're styled as the least important.
- Nobody can tell what they measure. It could be extraction confidence, owner-match confidence, or completion likelihood.
- The 41% row looks identical to the 94% row at a glance.
- **Fix:** Name the metric ("AI confidence" or similar) in a column header or tooltip. Treat low values visibly, for example with a "Needs review" tag below a threshold. Don't rely on grey versus slightly darker grey. Don't show raw numbers unless they're calibrated. Two or three bands ("Check this") are often more honest and easier to act on.

**3. Users can see a problem but can't fix it here.**
- The task text is read-only, and owners need a separate page.
- The screen surfaces doubt and then makes correction costly.
- Pre-filled owner chips look authoritative even when the model guessed.
- **Fix:** Edit task text inline. Make the owner chip a dropdown. Let users delete a row and add one. Hallucinated or duplicated items are common in this kind of tool, and right now the only recourse is not to send.

## Significant

**4. The checkbox is ambiguous.** It could mean "done" or "include in the send". If it means "include", it's your best safety valve, so make that explicit and consider unchecking low-confidence rows by default. If it means "done", it conflicts with a screen whose purpose is to distribute a fresh list.

**5. Verification is too far away.**
- "View transcript" sits beside the send button and takes the user away from the screen.
- Checking a doubtful item means finding the right passage in a full transcript.
- **Fix:** Add a per-row "source" affordance that expands the supporting quote or timestamp. Keep the transcript link, but it shouldn't be the only evidence path.

**6. The summary is unmarked and probably uneditable.**
- It's four AI-written sentences with no indication they're AI-written.
- If it goes out in the send, it needs the same review and edit treatment as the tasks.
- **Fix:** Label it as AI-generated and make it editable.

## Smaller points

- **Visual hierarchy:** The large blue button dominates, while the review work that should come first looks secondary. Consider disabling or de-emphasizing it until flagged items are reviewed or dismissed.
- **Accessibility:** Small grey text will likely fail contrast. Don't encode confidence by color alone. Make sure the chips and checkboxes have adequate hit targets and text labels.
- **Missing task fields:** There are no due dates, and no way to see unassigned tasks. A task with no clear owner should show as "Unassigned", not get a best-guess name.
- **Ordering:** Consider grouping or sorting by "needs review" so the 41% item isn't hidden at the bottom of the list.

## Suggested flow

Show the AI draft with flagged rows at the top. Let users edit inline, then confirm with a preview that says exactly who receives what. That keeps the speed of automation while putting the user's review where the risk is.

I can sketch a revised layout if you'd like. A few questions would help me tailor it:
- What does the percentage actually represent?
- Does the checkbox mean "done" or "include"?
- Is the summary part of the send?
