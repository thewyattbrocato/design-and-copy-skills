Partly. Enforcing harder as the first move is the wrong call, but your manager is right that the forks are a problem.

**Why enforcement alone fails**

Two teams forked Button and DatePicker because forking was cheaper than waiting on you. Your 6-month-old requests show that. If you add mandates on top of a 40-item backlog, you make the system a bottleneck with authority. Teams will route around it more quietly, or they'll comply and resent it. Enforcement works when the official path is faster than the unofficial one, and right now it isn't.

**What I'd do, in order**

1. **Talk to the two forking teams (a week or two).** Find out what they changed and why. Those forks are free research. If they fixed real gaps, such as scheduling-specific date ranges or button states, fold the changes back into the system. That turns a compliance problem into a win for both sides. If they diverged for taste, that's a different conversation.

2. **Triage the backlog honestly.** With two people part-time, you can't clear 40 items. Sort them into:
   - Ship soon, which includes anything the forks revealed.
   - Decline, with a reason.
   - Park, with a stated revisit date.

   Closing a 6-month-old request with an honest "no" builds more trust than leaving it open. Then set a visible cadence, such as a weekly triage and a response within 5 business days, even if the response is "not now."

3. **Make contributing cheaper.** A short contribution guide, a PR template, and a rule that teams can build the thing and you review it. This is the main way a two-person team scales.

4. **Then add light enforcement on the things that matter.** I'd pick a few:
   - Lint or CI checks for token use and for hardcoded colors or spacing.
   - Accessibility requirements on form controls. In a clinical setting, a DatePicker that breaks for screen readers or mishandles dates is a real patient-safety and compliance risk. That's your strongest argument for consistency.
   - A drift report showing which repos have forked components.

   Don't try to enforce visual sameness everywhere.

5. **Decide what happens to the existing forks.** For each one, either migrate it back, formally adopt it as a variant, or accept it as a known exception with an owner. Don't demand immediate removal.

**How to put it to your manager**

"Enforcement needs capacity to back it up. Right now the system is slower than the alternative, so mandates would create friction without fixing the cause. I'll fix responsiveness and reabsorb the forks first, then add automated guardrails on accessibility and tokens. Here's what that looks like in 60 days." Also ask for something concrete: more of the designer's time, or one engineer lent from a consuming team. If leadership wants the system enforced, they should staff it.

One caveat: I'm going on what you've told me. If the forks were mandated by a team lead who deliberately chose to opt out, that's an organizational problem, and your manager's escalation path matters more.

I can draft the triage rubric, the contribution guide, or the 60-day plan for your manager if that would help.
