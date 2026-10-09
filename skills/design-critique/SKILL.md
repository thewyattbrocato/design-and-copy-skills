---
name: design-critique
description: Use whenever someone wants a design judged, in any words, any length or language: "what do you think", "is this good", "why does it feel off", "make it feel more professional", "tear this apart", "will people get it", "which one is better", "give me feedback"; critique, review, audit, score or compare a screenshot, mockup, wireframe, HTML page, live site, flow, dashboard, chart, form or a described design; findings with severity, anchored scores, a fix order, what to keep; not for building or applying fixes (including the last small polish pass on a nearly finished screen), logo or identity critique (brand-identity) or code review.
---

# Design critique

Judge a design like a careful colleague: what it is for, what works, what fails and for whom, how bad each problem is, what to change first. The default failure is vague advice (make it pop, add whitespace) and long unranked lists. The fix is evidence, severity, an order of attack, and honesty about what could not be seen.

## Do not produce

- A finding with no element, number or reason behind it.
- A flat list mixing taste, function and polish; a critique with nothing kept.
- Color and type nitpicks on a sketch or gray wireframe.
- Conventional polish demanded of a deliberate style (brutalist, dense, playful) instead of judging it by its own intent.
- A redesign or rewrite when a critique was asked for, or a critique when something was asked to be built.
- A survey or opinion poll where watching a few people would answer the question.
- Manipulative patterns recommended as conversion tactics.
- Invented evidence: a contrast ratio, size, count, analytics figure, user quote or test result that was not supplied or computed from what was supplied.

## When not to use

- Building, fixing or restyling: do the work (applying fixes includes the last small polish pass on a nearly finished screen); give a critique only if one was asked for, never in its place.
- Logos, wordmarks, identity systems (brand-identity, if installed); code correctness, security or performance review.
- Research programs (surveys, statistical tests): give a short recommendation only.

## When facts are missing

- Infer purpose, audience, main task and fidelity from the material first. Ask once only if the chat is interactive, the question is cheap and the answer would change the verdict; give a default with it. Never reply with only questions.
- Otherwise deliver on stated assumptions, in one line ("assuming a first-time visitor deciding whether to sign up; high fidelity").
- Nothing to inspect (no markup, no description detail)? Say what cannot be judged, critique what is given, list what to send. Do not invent the design.
- A number you cannot compute is "not checked: contrast", never an estimate dressed as a measurement. Label a rough estimate as one.
- The user's brand, design system, platform conventions and stated constraints win over generic taste.

## Deliver

- Open with the verdict or the top finding. No preamble, no restating the design, no design theory.
- When a count is asked for (three fixes, two options, top five), give exactly that count. Honor any length cap by dropping the lowest-value points, and count rather than assert.
- Scale to the ask: a one-line question gets a verdict plus the few findings that matter; an audit gets the report in [report format](references/report-format.md). Short is not small: keep evidence.
- Notes beyond what was asked: at most two short lines (assumptions, what was not checked).
- Compute instead of asserting: contrast ratios, target sizes, line lengths, counts of font sizes, colors and button styles, clicks to the goal, from the supplied code or description.
- Each finding: what is on screen, who is affected and how, a concrete change. Mark taste as taste.
- Severity on every finding; blockers first. Weigh reach: a minor problem on every screen can outrank a major one on a rare path.
- Group repeats into one finding with a count. Report patterns, not every instance.
- Name two to four things that work and should stay, with a reason each.

## Judgment calls

**What the design is for comes first.** Check the first screen before details: could a stranger say what this is, what they can do, and why here? Failing that is usually the top finding. For a deep page: which site, which page, where am I, how do I get back.

**Match depth to fidelity.** Sketches and wireframes: purpose, structure, flow, content priority, task fit. High fidelity adds type, color, spacing, states, copy. Shipped adds accessibility, consistency, perceived speed. Polish notes on a rough piece only if asked, labeled premature.

**Taste or function.** Lead with function (the task, errors, legibility, access). A preference ("I don't like the blue") becomes a question about the goal it should serve, plus contrast and brand fit; keep it labeled as preference. When a team is arguing over taste, recommend settling the criteria before looking at options, one named decision-maker, and a presenter who recommends one option with reasons rather than asking "which do you like?".

**Deliberate style.** Judge against its own intent; flag only what harms use (contrast, legibility, navigation, focus, labels). If intent is unstated and the style hurts the goal, ask about intent rather than rule.

**Cognition over theory.** Tie a finding to what a person must notice, read or remember, and to a measurable fact (distance, contrast, seconds, clicks), not to a named law or a rule of thumb about reading.

**Comparing variants.** Decide for the stated audience and task, cite the specific differences, say how sure you are. Say "close call, test it" only when the evidence is really balanced, and name the cheapest test.

**Does it already work?** Say so plainly and list only real issues. Do not invent problems to look thorough.

**Comprehension questions.** If a finding hinges on whether people understand something, recommend three to five people doing real tasks without help and a same-day debrief; fixes should remove things before adding explanations. Use analytics or a larger study only when the question is volume.

**Audits at scale.** Inventory the screens, sample key flows and one screen per pattern, check consistency (duplicate components, one-off values, mismatched labels), report patterns with counts, give a deliverable shape. For a huge set, deliver the first slice in full, then continue.

**Vague feedback.** Rewrite each phrase as an observable issue, the reason, and a fix ("too busy" becomes "six type sizes and four accents compete in the first viewport; keep one accent, cut to three sizes"). If it is pure preference, say so and ask what it should achieve.

**Manipulation.** Hidden or late costs, forced accounts, pre-checked consent, decline buttons worded to shame, false urgency or scarcity, cancel harder than sign-up, defaults that work against the person: report as findings with an honest alternative. If asked for them, decline that part in one sentence and offer two or three honest routes. Describe what is on screen; do not label on a hunch.

**Scores.** Only for audits or when asked: 0 to 4 per applicable dimension with a one-line reason, whole numbers, anchors in [report format](references/report-format.md). A blocker caps the overall; two 4s do not offset a 0. Mark dimensions that cannot be assessed.

## Checks

[checks](references/checks.md) holds short passes for interaction, state and errors, accessibility, content, data displays and manipulative patterns. Load it when the design contains those parts. For full procedures use visual-hierarchy, spacing-and-grouping, layout-structure, typesetting, color-palette, form-design, ui-motion, chart-design and data-tables, each if installed; otherwise use ordinary judgment. Detailed component accessibility semantics and multi-chart dashboard layout are outside these skills: use ordinary judgment.

## Before sending

- First line is the verdict or the top finding.
- Every number shown was computed from what was supplied; estimates are labeled.
- Findings are ranked, each with severity and a fix; taste is labeled.
- The count and length match the ask; at most two notes.
- Nothing was built or redesigned that was not asked for.
- What was not checked is stated.

## References

- [references/report-format.md](references/report-format.md): load for a full review, audit or scored review; order, finding template, severity labels, score anchors, compact template.
- [references/checks.md](references/checks.md): load when judging flows, forms, states, errors, accessibility, content, charts, tables, dashboards, or pricing, consent and cancellation.
