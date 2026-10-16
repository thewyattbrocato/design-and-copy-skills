**No, not as the first move.** Enforcing harder would make the problem worse. The two forks and the 40 stale requests are probably the same problem seen from two sides.

**Why enforcement is the wrong first move**

- Teams forked Button and DatePicker for a reason. Most likely the system couldn't do something they needed, and the board couldn't deliver it in a reasonable time. A 6-month-old request is effectively a "no" that nobody had to say out loud.
- If you mandate compliance while the board is backed up, teams will route around you more quietly. Or they'll resent you, and you'll lose the goodwill you need.
- Two people can't police 40 clinics' worth of apps anyway. Enforcement that only works if you have capacity doesn't scale.

**What I'd do, in order**

1. **Triage the board this week.** I'd sort every request into one of four buckets and reply to each:
   - Accept, with a rough quarter.
   - Decline, with the reason.
   - Merge into another request.
   - Close as stale, and ask the requester to reopen it if it still matters.

   Expect many to collapse into a handful of themes. An honest "no" is better than silence. After this, set a response SLA for new requests, something like a first reply within 5 business days. A reply is a commitment to respond, not to build.

2. **Treat the two forks as free research.** Diff each fork against the original and ask what each team needed that you didn't offer.
   - If a change is a real gap, such as a variant, a date-range mode, or a different validation state, bring it back into the system. Credit the team. That is your best proof that contributing works.
   - If a change is a one-off preference, give the team a clear, documented path to override it or leave it as a marked exception.
   - Then ask them to migrate back, with your help. This is a conversation, not a mandate.

3. **Make contributing cheaper than forking.** The system needs a small, written admission rule. I'd use "a second real use earns promotion", plus a lightweight way for teams to contribute a component or variant themselves, with you reviewing instead of building. If every request depends on your two people, you're the bottleneck.

4. **Add a few light guardrails, not a crackdown.**
   - Publish the components as a versioned package, so teams get fixes by upgrading instead of copying.
   - Add a lint rule or CI check that flags local copies of components that exist in the system. Have it warn first, not block.
   - Require new exceptions to be tagged with an owner and a review date.

5. **Then bring your manager a metric.** Present the plan as "enforcement that works", and include numbers: median request age, share of requests answered within the SLA, number of forked components, and adoption by app. I don't have your current numbers, so you'd pull those from the board and the repos. After the triage, you can say "we've cleared the backlog and fixed the gaps, so now we can hold teams to the system". That's a much stronger case for enforcement.

**What to say to your manager**

"I agree we need more consistency. If we enforce before we fix the backlog, we penalize teams for our slowness. I'll clear the board and pull the useful fork changes back in over the next few weeks, then we'll tighten expectations with data."

**Two notes**

- I'm assuming a web-based system with a shared package or repo that both apps can consume. If either app is native, the mechanics change a bit.
- Whether the backlog is realistically clearable by two people, one of them part-time, is the real constraint. If it isn't, the case to make to your manager is for capacity, such as a rotating engineer from the consuming teams, not for a stricter policy.

If it would help, I can draft the triage template, the admission rule, or the note to the two forking teams.
