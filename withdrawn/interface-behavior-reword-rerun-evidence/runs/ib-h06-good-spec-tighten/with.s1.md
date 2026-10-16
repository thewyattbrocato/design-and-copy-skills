Here's the tightened spec. I kept the content as you wrote it and only fixed wording and ordering. Where the original was ambiguous, I picked the most likely reading and listed it below so you can check it.

---

**Reschedule a class**

**Choosing a booking**
- The Reschedule button lists the student's next three booked classes. Past classes are under "Past".

**Choosing a session**
- Tapping Reschedule opens the open sessions for the same class level, nearest date first.
- The student's last-used studio is pre-selected.
- The list can be searched by weekday or teacher. The search choice is remembered for next time.

**Moving the booking**
- Picking a session moves the booking immediately, with no confirmation dialog.
- A banner at the top reads "Moved to Thu 14 Mar, 6 pm. Undo" and stays for 10 seconds.
- Undo returns the booking to its original session.
  - If the original seat is still free, it is restored.
  - If the seat is taken, the banner says so and offers the waitlist.

**Loading**
- While a new session list loads, the previous list stays on screen and a thin progress line shows at the top.
- After 5 seconds, a "Still loading" message appears with a retry link.

**Cancelling (separate flow)**
- Cancelling a booking less than 24 hours before class asks for confirmation first. The prompt states the fee that will be charged.
- This is the only flow that asks before acting.

---

**Questions to settle before handoff**

1. **"Next three" vs. "older".** Only three classes show by default, but the only other place named is "Past". Where do upcoming classes beyond the third go? As written, "older ones" can't mean those. I'd guess you mean "all other classes", but that needs a decision.
2. **What does search remember?** "The choice" could mean the last search term, the weekday or teacher filter, or the studio. Studio is already covered by the pre-selection line. If you mean the filter, say "the last weekday or teacher filter".
3. **Rescheduling inside 24 hours.** The cancellation fee applies inside 24 hours. Does rescheduling a class that soon also carry a fee? If it does, "no confirmation" conflicts with your own rule about charging without asking. If not, a line saying so would stop developers from guessing.
4. **Undo after 10 seconds.** Once the banner is gone, can the student still reverse the move, or do they have to reschedule again? I left it unstated, as in your draft.

I can fold in your answers once you have them.
