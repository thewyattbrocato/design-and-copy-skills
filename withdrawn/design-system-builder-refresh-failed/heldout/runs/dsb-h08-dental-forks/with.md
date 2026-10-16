**Not as a first move.** Enforcing harder aims at the symptom. Two teams forking Button and DatePicker and a backlog of 40+ requests, some six months old, are the same problem seen from two sides. The system can't respond to teams fast enough, so they route around it. Mandates on top of that backlog will make teams resent you and fork more quietly. I'm assuming a web stack and that you don't have a lot of engineering capacity. I'm also working from your description, not from the forks or the board.

**What I'd do, in order**

1. **Triage the board in one sitting (this week).**
   - Sort every request into one of four buckets: *do*, *merge into another request*, *decline with a reason*, *not a system concern*.
   - Close or answer everything older than ~90 days. A clear "no, because X" beats six months of silence.
   - Aim to cut the list roughly in half without writing any code. I'd expect many requests to be duplicates or one-offs, but check that against the board itself.

2. **Read the two forks as requests.**
   - Diff each against your Button and DatePicker and write down what changed. `[diff from your repos]`
   - Each change is a missing variant or prop, a bug, or a real product need, such as scheduling-specific date behavior. The first two are fixes you should ship. The third may be a legitimate new component.
   - Then talk to those two teams. They have already built what you owe them, so ask what pushed them to fork.

3. **Take the forks back by promotion.**
   - Fold their changes into the shared components and publish a migration. Ask each team to delete its copy by an agreed date.
   - That gives you a concrete win: two teams back on the system because it now does what they needed.

4. **Add a lightweight contribution path.**
   - A team can contribute if it follows a short template: the need, the states, and keyboard and focus behavior.
   - Give requests a response SLA, such as a first reply within a week, and a weekly triage slot. With a part-time designer, treat this slot as protected time.
   - Also decide what counts as an acceptable local exception, and tag exceptions with an owner and a review date.

5. **Then enforce, narrowly.** Once the system is responsive, mandates become fair and cheap to apply.
   - Add a lint rule or CI check that flags copied or duplicated core components.
   - Require accessibility behavior (focus, keyboard, target size) in anything patient-facing. This matters most because the patient portal carries real risk if forks drift.
   - Deprecate with notice and a migration path. Don't just remove things.

**What to tell your manager**

Enforcement works when compliance is cheap. Right now compliance costs a six-month wait, so enforcement would punish teams for the system's slowness. Propose a 6–8 week plan: clear the backlog, absorb the two forks, set the SLA, then turn on the checks. Track a few numbers: median request age, forks remaining, and the share of screens using the shared components. I can't give you baselines for those, so pull them from your board and repos.

**One trade-off to expect:** being more responsive means saying "no" more often and faster. That's a feature, but you need your manager to back those decisions when a team escalates.

If you'd like, I can draft the triage rubric, the contribution template, or the fork-diff checklist. Or paste in the board list and I'll help sort it.
