---
name: user-research-basics
description: Use whenever someone needs to find out what people do, need or struggle with, in any words, length or language - "should we research this", "we need to understand our users", "write a screener or interview guide", "is this survey okay", "make sense of these notes or support tickets", "what do these test results mean", "create personas", "can we ship this test result", "talk to stakeholders before we start". Covers scoping, cheapest method, small-study plans, neutral questions, bias and consent, synthesis, finding priority, personas from evidence, experiment hygiene. Not for judging a design (design-critique), form fields (form-design) or page copy.
---

# User research basics

Research here means a clear question tied to a decision, the right few people, neutral asking, honest counting and a short written trail. This skill plans studies and analyzes material the user supplies. It cannot recruit anyone or run a session, so it always says what a human must do. The default failures are a survey asking what people want, five hundred respondents instead of five conversations, invented personas, percentages from a handful of people, and findings that jump to features.

## Do not produce

- A participant, quote, count, percentage, persona detail or "users said" line that is not in the supplied material. Missing evidence becomes a labeled hypothesis or `[to collect]`.
- A survey or interview asking what people want, whether they like it, or whether they would use it.
- Personas, journey maps or segments with no source data. Offer labeled assumptions plus a plan to test them.
- Percentages or "significant" from fewer than about thirty people; say "3 of 7".
- Solutions inside findings, or findings that name no source.
- A long academic plan, or "research is needed" with no plan.
- Focus groups as a method; a friend, colleague or enthusiast as the whole sample.

## Missing facts

Deliver on stated assumptions, in one line ("assuming a consumer app and no existing interviews"). Ask once, with a default, only if interactive and cheap; never reply with only questions. Do not invent traffic, sample sizes, budgets, dates or who attended.

## First decision: is research warranted?

Name the decision, who will act on it and what a wrong guess costs in months of work. Then check what already exists: tickets, chat logs, sales notes, search queries, reviews, analytics, earlier studies. Default: use existing evidence first. Research only the expensive assumptions; skip it for a throwaway prototype or a choice that is cheap to reverse. If a person insists on a method that cannot answer the question, say what it can and cannot tell them and propose the cheaper fit.

## Pick the method from the question

Phrase the question so you can tell when it is answered: name the output (a list of X, a comparison of Y). Add the method and the result that would change the plan. Smallest versions to start from:

- What are people doing and why, problem unknown: five or so conversations about recent real behavior, ideally where it happens.
- A candidate design or flow: three to five people doing real tasks, one at a time, nobody helping. Section "Watching people" in design-critique's checks, if installed, is the quick version.
- What happened, how much, where: analytics or existing records first, then people for why.
- Which of two wins: a live comparison, only with enough traffic and one pre-stated metric.
- Opinion polling and focus groups answer neither "what do they do" nor "will they buy".

Participant counts are rough guides, never statistics. Three to five for a quick check of one kind of user; five to eight per kind when there are several kinds or a fix-and-retest cycle. Stop when new sessions stop changing your conclusions; add a few when they still do. Details in [plan, screener and asking](references/plan-screener-asking.md).

## Participants

One test: would this person do the task this week? Screen on what they did recently, not on skill or opinions, and bury the target activity among others so the topic cannot be guessed. Keep the screener short, exclude people who guess to win the incentive. Say who the sample leaves out.

## Asking

Ask for stories about the last real time, not opinions or predictions. Open questions, "tell me more", silence. Never mention the product or sponsor before the materials show it. Get consent for recording and for any unseen observers; end a session if the person is driving or distressed. The designer of the thing is the worst facilitator of its test.

## Synthesis of supplied material

1. Code every note to its source; separate what happened from what it means.
2. Group bottom-up, then name each group as a need, barrier, trigger or word people use.
3. Count as n of N, with the sample's source and bias ("7 interviews; support tickets come from people who write in").
4. Chain: observation, pattern, insight, a decision to make. Rank by evidence strength and by importance to the goal; mark single-source items as leads. Set aside outliers who could not be users and say why.
5. End with what is still unknown and the cheapest next check.

Depth and personas in [synthesis, findings and evidence](references/synthesis-findings-evidence.md).

## Usability findings

Each problem: task, how many of N hit it, what happened, severity (blocks, slows, annoys). Weight by how central the task is. Preference is not a finding. Fix by renaming, moving or removing before adding explanation; retest with new people. Frequency bands are a sorting aid at this size.

## Numbers

Analytics says what and where, people say why. An experiment needs one metric chosen first, a run covering whole weeks, no early peeking and enough traffic; a few days and hundreds of visitors is a lead, not a result. See [stakeholders and experiments](references/stakeholders-experiments.md).

## When not to use

- Judging a design someone shows you: design-critique if installed. Form field design: form-design if installed.
- Surveys at scale, statistical modeling, market sizing: give a short recommendation and say a specialist should run it.
- Children, patients, regulated or sensitive topics, or politically charged organizations: recommend a trained researcher and give a plan outline only.
- The user's constraints, schedule and stated method win when they can work; flag the risk in one line.

## Output discipline

Deliver the requested artifact first (plan, screener, guide, synthesis, ranked list) with no preamble, because the reader came for the work. Give exactly the count asked for. Honor any length cap and count rather than assert. After the work, at most two one-line notes (assumption, what a human must do). If the existing plan, screener or guide already works, say so and change at most a word.

## Quick checks

- The decision and the result that would change it are named.
- Every number, quote and participant came from the user's material.
- Counts are n of N with the sample's bias; no percentages from small groups.
- No question asks for wants, likes or predictions; no leading words.
- What a human must do (recruit, consent, run, record) is stated.

## References

- [references/plan-screener-asking.md](references/plan-screener-asking.md): load for a plan, screener, interview guide, leading-question rewrite, bias or consent text.
- [references/synthesis-findings-evidence.md](references/synthesis-findings-evidence.md): load for notes or tickets to analyze, usability findings, personas, scenarios, or reviewing existing evidence.
- [references/stakeholders-experiments.md](references/stakeholders-experiments.md): load for mapping stakeholders, a success-and-scope note, split tests or analytics interpretation.
