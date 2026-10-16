# Stakeholders and experiments

Load for mapping stakeholders, a success-and-scope note, split tests or analytics interpretation. Starting values; change them when the situation says otherwise.

## Map who can help or stop the work

Do this before design work when budgets, approvals, politics or unclear success could sink the project. Talk to people one at a time, privately, half an hour is usually enough; a short written exchange beats skipping them. Explain how their input is used and that it is not attributed.

| Person | What they need | What they can block | Open conflict |
|---|---|---|---|
| Name or role, listed by influence rather than title | Their goal, in their words | Budget, approval, access, launch | Who they disagree with, and about what |

- Include people close to users (support, sales), whoever maintains the result afterwards, and doubters; do not wait to be told whom to ask.
- Useful prompts: how they would know it worked, what worries them, what changes for them, who else to ask. With someone wary, restate the goal, ask one broad question and let them steer.

## Agree success before design

Write a short note, shared and confirmed by the decision-maker: the problem; what success looks like and how it will be measured; what is in scope, what is out, and who owns each part; known risks; how decisions get made. Leave solutions out. Where people want different things, propose something that serves both or mark the conflict for the decision-maker. Unsupplied facts become `[to confirm]`.

## Experiments and analytics

- Define the one goal metric and the current rate before the test, plus the smallest change worth acting on. A test with no stated metric proves nothing.
- Traffic: a small difference needs a large sample. If the page cannot produce it in a reasonable time, do not test; use qualitative checks or ship the change on judgment and measure.
- Duration: run whole weeks, about two with no holidays or unusual traffic spikes, even if the numbers look decided early. Peeking and stopping on a good day produces false winners.
- Confidence figures are only valid when the plan was fixed in advance. A relative lift ("a tenth more signups") on a small base can be noise; ask for the counts, not the percentage.
- Test where variation is harmless: one clear behavior on a page that tolerates variants. Leave out navigation, trust-critical or legal pages, and anything where inconsistency itself hurts.
- Tests polish what exists; they do not choose a direction. Settle the direction with people first.
- Winners are often surprising; treat results as learning and follow up with a conversation about why.
- Analytics numbers need a goal to be read against. More page views can be engagement or lost people; high bounce can be unmet expectation or a perfect answer.
- If asked "ship it?" on thin data: say what the data does and does not show, the next cheapest step, and what you would watch after shipping. Give a recommendation, not a survey of options.
