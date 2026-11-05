# Brindlemoor install guide: review rule

**Why this exists.** Reviewers didn't respond, we published anyway, and step 6 was wrong. A customer lost a day. Waiting was never the fix. Nobody was assigned to answer, and nothing said what a missing answer meant.

## Rule

1. **One named owner.** Owner: `[name]`. They decide when a change is ready. If they're out, `[backup]` covers.
2. **One named reviewer per change.** The owner assigns a single person, not a group. That person has to have **run the steps on the current Brindlemoor version**. Reading them doesn't count.
3. **Time limit: `[N working days]`.** The owner pings the reviewer at the halfway point. If there's still no answer at the limit, the owner reassigns to the backup reviewer `[name]`. **Silence never counts as approval for steps.**
4. **Steps need a run-through.** Any change to a numbered step, command, setting, or version number needs a reviewer to confirm they ran it. Record who, which version, and the date in the page history. Wording, typo and formatting fixes need only the owner's okay.
5. **No run-through, no publish.** If no one can run the steps in time, the owner has two options:
   - Publish the unchanged steps and hold the changed ones.
   - Publish with a visible banner: "Steps not yet verified on version X."

   The owner never ships unverified steps as if they were checked.
6. **Urgent fixes.** For a customer-blocking error, the owner or `[backup]` may publish a correction right away, as long as they ran the corrected step themselves. A reviewer checks it within `[1 working day]` afterward.
7. **When a step turns out wrong.** Fix it, note it in the page history, and tell support `[channel]` so they can contact affected customers. Add one line to the page history on how it got through.

## Release checklist (owner)

- [ ] Every changed step has a run-through recorded (who, version, date)
- [ ] Nothing waiting on a reviewer who hasn't answered
- [ ] Any unverified section is held or bannered

**Notes**
- I left the names, the review time limit, and the support channel as placeholders because I don't know them. Your team has to fill those in. The rule only works once each has a real name or number.
- To size the time limit, check how long a reviewer actually needs to run the install on your side. Set the limit from that.
