# One-off long jobs, many agents, eagerness and permission scopes

Load this for a single job that runs for hours, a run made of phases, one person supervising several agents at once, or a question of how readily an agent acts versus asks. A small ask (one alert, one undo, one message) does not need it. Numbers are starting points to test.

## How eager it should be

Default: treat eagerness as a design choice made from error costs, not a property of the model.

1. For the action, write what a wrong act costs and who pays, and what a miss costs and who pays.
2. Estimate how many flagged items the person can really check in a day or a shift. Name the number, or label a placeholder.
3. Set the lean so the expected flags fit that number. If checking costs more than the errors it prevents, the agent should act more and report afterwards. If a wrong act is expensive or cannot be reversed, it should flag more, even when that means more reviewing.
4. Test the choice: would it flip if either cost doubled or halved? If so, say so and put the setting where the owner can change it.
5. Never show an accuracy figure without both error counts behind it. "95% right" hides which way the 5% fails.

## A one-off long job

A standing agent is judged over weeks; a one-off job is judged once, at the end, so a wrong turn early compounds unseen. Default: add the points below only for a job that is long, costly or hard to reverse, and for the first runs of any new agent. A cheap, reversible job gets a start button and a result.

- **Plan before it starts.** Show the steps as something the person can edit, reorder or cut, with the points where it will stop and ask marked. Skip the plan when the job is short and every step can be undone.
- **One place to watch.** Current step, steps done, what it has found so far, and a detailed log that opens on demand but is not in the way. Acknowledge each new instruction at once, even if it will apply later.
- **Stop is not pause.** Stop ends work now, keeps what is finished, says what was left half-done, and never restarts without a clear new start. Pause keeps the working state and accepts new direction before resuming. Offer both, one step from the watching view.
- **Check in at the seams.** Between phases, a two-line statement: the goal as it now reads it, what it is assuming, what it will do next. The person can correct it, and a phase can be rerun without the bad assumption carried forward. Skip it inside a phase.
- **Costly exploration still asks.** Inside an approved plan, a step that spends money, contacts people or touches a live system needs its own approval or a hard cap. "Approved the job" is not "approved this".
- **Review the output as a change set.** Show what it produced as parts the person can accept or reject singly, the parts it was unsure of first, a one-step refine instead of a full rerun, and a kept record of what was accepted. A total ("done, 412 changes") is not a review.

## Permissions at commit points

Default: ask when the job reaches a point that sends, spends, deletes or commits the person, not at setup and not at every step. Access requested at setup is covered in [setup and limits](setup-and-limits.md#permissions).

- The request names the action, the target and the consequence in plain words.
- The grant has a scope: this once, this job, or always for this kind of action. Offer the narrowest as the default and the others one tap away.
- Route by how often the agent's guess is wrong times what a wrong act costs. Rarely wrong and cheap: act and report. Often wrong or costly: ask.
- A prompt on every step is a defect: people approve without reading, and the one that mattered gets the same tap. Batch low-risk approvals with a reason shown, and keep the full-attention prompt for the few that matter.

## One person, many agents

The supervisor's job is knowing where to look, not watching each agent.

- Counts by state at the top: running, waiting on the person, stuck, done. Waiting and stuck come first.
- A list the person can filter by state, then open any one agent to see its status view, plan and log.
- Pause or stop by group, with the count shown before it applies.
- One queue of the items that need the person, across all agents, each with its reason; approve similar ones together only when the reason is the same.
- Do not offer a draggable board of phases unless moving a card really changes the work. A read-only board that looks editable teaches people to distrust it.
- Each agent's own message still follows the five kinds in the main skill; the fleet view adds a layer, it does not replace them.

## Which version ran

Where a standing instruction gets corrected, the activity record says under which version of the instruction each action ran, so an old action is not judged by the new rule.
