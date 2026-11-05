Your team is right: the deck reads like a document. It has an agenda slide, label titles ("Velocity", "Quality"), and slides with 6 to 10 lines each. I'm assuming a 15-minute slot, which fits about 6 content slides. Tell me if the slot is different.

**Takeaway:** Harbor shipped about 15% more per sprint and made fewer mistakes, and the one big incident came from the notification rewrite, with fixes already in place.

**What I'd change**
- **Cut slide 2 (Overview) and slide 8 (Thank You).** Preview the structure out loud in the first 30 seconds. Put the closing content on the last slide and leave it up during questions.
- **Rewrite every title as a claim.** The titles alone should tell the story.
- **Keep to one idea per slide, under about 30 words.** Body text should be 32 px or larger, since the screen is big but 40 people are reading from a distance.
- **Move detail to the appendix.** That means the individual sprint numbers, test coverage, and the flaky-suite swap. Say the main point aloud and leave the rest in the appendix.

**Proposed deck**

1. **"Q3: We shipped more, with fewer defects, and learned from one outage"**
   - Add "Team Harbor, sprints 14–19, Imani Okafor" as a small subtitle.
   - Open here with the takeaway rather than a separate title slide.

2. **"We delivered 15% more per sprint and hit our commitments"**
   - Show one big number: 84% commitment accuracy, up from 71%.
   - Add a small bar chart of points per sprint, with the Sprint 17 dip labeled "2 out, holiday week".
   - Say aloud: average 41.8 vs 36.5. Carry-over fell from 9 to 4.

3. **"Seven features shipped, most of them to speed up dispatchers"**
   - Group them into three lines:
     - Dispatcher speed: saved filters, bulk edit, assignment modal, dark mode.
     - Scale and access: 50k-row CSV export, subcontractor roles.
     - Platform: notification rewrite.

4. **"Escaped defects nearly halved, and P2 fixes take half as long"**
   - Show two numbers: 31 → 17 and 6.2 → 3.5 days.
   - Move coverage and the flaky-suite swap to the appendix.

5. **"The notification rewrite caused a 3-hour alert backup on Aug 29"**
   - Show three facts:
     - 1,140 delayed driver alerts.
     - Cause: queue prefetch limit set too low.
     - Fixed the same day, with a queue-depth alert added the next week.
   - This is the slide product people will ask about, so don't shrink it. Being upfront about it builds trust.

6. **"Q4: finish permissions, close two test gaps, and hire"**
   - Show three or four items:
     - Subcontractor permissions, phase 2.
     - Load test the queue before further changes.
     - Add the missing CSV export test.
     - Hire one senior engineer.
   - Tech debt, the route-optimization spike, and the monthly-release investigation can go in the appendix or be said aloud, unless you want feedback on any of them.
   - Keep this slide up during Q&A.

**Two things to check**
- The queue load test is a follow-up on your incident slide but isn't in your Q4 plan. I added it so the two slides agree.
- If you want something from the room, such as input on the monthly cadence or help with the hire, say so on slide 6 with an owner and a date. I left that out because I don't know your ask.

**Likely hard questions:** "Why did the rewrite ship without a load test?" and "Is the CSV export safe at 50k rows with no automated check?" Park a backup slide for each after the end. I can draft the slide text, the appendix, or short speaker notes if you want them.
