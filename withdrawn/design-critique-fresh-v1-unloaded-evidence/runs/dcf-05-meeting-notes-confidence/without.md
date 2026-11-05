The send button is the most dangerous part of this screen, so I'd fix it first. The owner guessing is the next problem. Most of the rest is there to help people check the output.

## The core problem
About 20% of items have the wrong owner. The screen pre-approves everything (ticked boxes), hides the evidence (no source), and then sends to the whole call with one big button. Errors will go out to everyone, and the screen gives the user little chance to catch them. A wrong owner is more than a typo. It tells a colleague they own work they never agreed to, in front of the whole team.

## What I'd change, in order

**1. Make sending safe (do this first, it's cheap).**
- Don't send straight from this screen. Make it "Review & send", with a preview of exactly what recipients will see.
- Default the audience to the person who ran the meeting, or send each person only their own items. "Everyone on the call" should be a deliberate choice.
- Make the button's weight match the risk. A huge blue primary button invites a tap by someone tired at the end of a call.
- Block or warn on sending items that are unassigned or low-confidence.

**2. Stop guessing owners.**
- "Who spoke nearest the topic" is a weak signal. It will often pick the person who raised a problem or asked a question, not the person who took it on.
- Assign an owner only when there's an explicit commitment ("I'll do that") or an explicit assignment ("Sam, can you…"). Otherwise show "Unassigned – pick owner" as a visibly empty state.
- Make the owner an inline tappable field with a picker of attendees. Right now fixing the most error-prone field takes a tiny "Edit" link and a full edit flow.
- Showing blank for 20% of owners is better than showing wrong ones. Blanks are visible, and wrong owners look like facts.

**3. Add provenance.**
- Give each item a timestamp and a one- or two-line transcript snippet, with a play-from-here control. This is the biggest trust and verification gain, and it makes the other fixes much easier to act on.
- Add the same to the summary: cite each sentence or claim to a moment in the call. A 5-line unsourced summary of an hour-long call can't be checked, so people will either trust it blindly or ignore it.

**4. Fix the confidence pills.**
- Ask what "87% sure" refers to: the task, the owner, or both? Split them, or show confidence only on the field that's uncertain.
- Check calibration. If the owner is wrong 1 time in 5 and items still show 87%, the numbers are misleading. Calibrate them against your test set or drop them.
- Don't keep them as small grey decoration. Use them to drive behavior. Items below a threshold should be unticked, flagged, or sorted to the top for review, and high-confidence items should stay quiet.
- Even well-calibrated percentages are hard for people to read. "Check owner" works better than "54% sure".

**5. Fix the checkbox semantics.**
- A pre-ticked checkbox on a task list reads as "done". Here it presumably means "include in the send". Those are different things, and users will misread it.
- Default to "needs review" rather than "approved". Use a different control for "include", or a clear confirm-per-item state. Even a "Confirmed 4 of 6" counter would help.

**6. Smaller things.**
- Let users add or remove items. The current screen only supports editing.
- Add due dates if the model can extract them. Action items without them are weak.
- Tell users what happens after they send (where the items live, who is notified).

## How to measure it
Track the owner-correction rate, the share of items edited before send, and how often people send without opening any item. If most users hit send untouched while 1 in 5 owners is wrong, the current design is shipping errors at scale. After the changes, the aim is to cut wrong-owner sends, not to raise the model's accuracy.

I'm working from your description rather than the screen itself, so I may have missed things like spacing or how the pills actually look.
