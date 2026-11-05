**Verdict: this screen asks people to trust the model and then makes that trust irreversible.** The wrong-owner rate is a symptom. Ticked checkboxes, no source, a primary button that sends to everyone, and a hidden confidence signal combine so that about 1 in 5 wrong assignments goes out to the whole call. I'm assuming the reader is the organizer or note-taker, right after the call, and that this is a high-fidelity shipped screen.

## What I'd change, in order

**1. The send button is a blocker, so fix it first. (Blocker)**
- "Send to everyone on the call" is the only large, blue, obvious action. It sits under 6 items where your own testing says roughly 1 in 5 owners is wrong. With 6 items, you'd expect on average more than one wrong owner per send.
- A wrong owner is not a cosmetic error. It tells a colleague, in front of others, that they own something they never agreed to. Or it leaves the real owner thinking someone else has it.
- Change: make the send step a review step.
  - Label it with what it does ("Review and send"). Show the count of unconfirmed items.
  - Show who will receive what. Let people send each person only their own items.
  - Keep sending available, but not as a single tap past unreviewed content.

**2. Items start ticked, so the default is "approved". (Blocker)**
- A ticked checkbox usually means "done". Here it means "include" or "accepted", and nobody accepted anything. Skimming and tapping send reads as consent to all six.
- Change: start unticked, or replace the checkbox with a clear "Confirmed" state that the organizer sets per item. Low-confidence items should need an explicit confirmation.
- The checkbox's meaning is also unclear. Is it "done", "send", or "correct"? Pick one and label it.

**3. There is no way to check an item against the call. (Major)**
- With no source, the organizer must recall one hour of conversation to judge six items. The summary has no sources either, so the same problem applies to the paragraph at the top.
- Change: attach a timestamped transcript snippet to each item, with a play button, and show 1 to 2 lines inline. For the summary, link each sentence to its source.
- This fixes the cause of the owner errors, not just their detection. Seeing "Sam said 'I can't take that'" makes a wrong owner obvious in 2 seconds.

**4. Owner assignment is a guess presented as a fact. (Major)**
- The owner is "who spoke nearest the topic", which is a proxy. Someone who raised a problem often isn't the one who volunteered for it. The screen shows that guess in the same way as a confirmed assignment.
- Change:
  - Mark owner as suggested ("Suggested: Priya") until it is confirmed.
  - Make the owner the main editable field, with a tap-to-change picker of attendees. Right now it is buried behind a tiny "Edit" link.
  - Where the transcript has no explicit commitment ("I'll do it"), leave the owner blank rather than guessing. A blank owner is visible and easy to fix. A wrong owner is not.

**5. The confidence pill is weak and doesn't say what it's about. (Major)**
- "87% sure" is small and grey. It doesn't say sure of what: the task, the owner, or both? Your problem is specifically the owner, so a single score probably hides it.
- Percentages also imply a precision that probably isn't there. I haven't seen how they're calibrated, so I can't say whether 54% is truly worse than 87% in practice. Check this against your test data before relying on it.
- Change: show confidence on the owner only, in plain words ("Owner unclear"), and only where it is low. Sort or flag low-confidence rows at the top. Use a visible color plus text, not grey alone.

**6. "Edit" is too small and too uniform. (Moderate)**
- Six identical small links at the right edge are easy to miss and are probably small touch targets. I haven't measured them, so this is not checked. If it is a touch screen, check against a 44 px minimum.
- Editing is the main task on this screen given the error rate, so it shouldn't be the least visible control. Make owner, text, and delete directly tappable per row.
- There's also no way to remove an item, or to add one the model missed. I'd confirm that's true; if so, add both.

**7. The summary paragraph. (Moderate)**
- Five lines of unsourced prose at the top gets read first, and errors in it spread unnoticed. Add sources (see 3), and consider shortening it. Five lines is also a lot to read before the thing the person must act on.

## What to keep
- **Action items as a list with owner next to task.** It's the right structure for the job, and what people scan for.
- **Showing confidence at all.** Being honest about uncertainty is the right instinct. It just needs to be about the right thing and visible.
- **Edit available per row, inline.** Keep it, but promote it.
- **A single clear end action.** One primary button is good. It just shouldn't be this one at this moment.

## Fastest way to verify
Watch 3 to 5 organizers go through this right after a real call, without help. Count how many wrong owners they catch before sending. My expectation, which is a guess, is that they'll catch few with the current screen. Re-run the same test after fixes 1 to 3.

Not checked: contrast, touch-target sizes, and the real visual layout. I worked from your description only.
