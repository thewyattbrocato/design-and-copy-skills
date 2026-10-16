# Audit and priorities

Load this when asked what motion an existing product needs, what to do first, or what to leave out. It orders work; the other files say how each piece is built.

## Classify each moment

List candidate moments from the product's real screens, then give each one kind:

- **Place change:** the person ends up somewhere else (drawer, page, tab, route).
- **Context added:** something appears or leaves without the person leaving (toast, inline row, panel).
- **Cause to result:** an action is linked to its outcome (save, delete, move).
- **Demonstration:** a short loop shows how something works, instead of a paragraph.
- **Decoration:** none of the above.

Write one sentence per item saying what a viewer learns or what confusion goes away. If the sentence will not come, the item is decoration: drop it.

## Where confusion hides

- Instant swaps of place: a drawer or view that pops in with no origin.
- Silent insert and removal: rows that appear or vanish and shift everything below.
- Changes outside the person's focus: a total, badge or row that updates while they look elsewhere.
- A paragraph explaining a process that a few seconds of movement would show.

## Rank, then cut

Place each item by value (effort it saves a person) against cost (build effort, and how many teams it touches). Then:

| | Cheap | Costly |
|---|---|---|
| **High value** | Ship first. | Prototype one, then decide. |
| **Low value** | Park. | Drop. |

Frequent paths come first in value: a drawer opened all day outranks a first-run welcome.

## Output shape

A ranked list sized to the capacity given (people, sprints), not a catalogue. Each item: the moment, the question it answers, the one-sentence purpose, rough effort, and the spec in a line (duration, easing). Then a **Not animating** list with a reason each. Typical entries: table row hover lifts, scroll reveals, parallax, page-load fades on content already in view, count-ups on numbers people read, anything on a constant-use control beyond a press state. Polish nobody sees is dropped, not parked.

Do not give eight to fifteen items of equal weight in screen order. Three to six ranked items plus a skip list is the usual right size; a short budget means fewer, not smaller.

## When asked "should we change this?"

Compare the existing motion against the duration bands and the four questions. If it already has a job, is quick, interruptible and respects reduced motion, answer "leave it" with the one reason, and name the cost of the change (slower on a constant path, lift on a control under the pointer). Offer the narrow alternative only if asked.

## Posture with a stated downside

When the brief is vague ("make it feel premium"), pick one posture and say what it costs: "restrained, so it may read as plain next to playful competitors" is a decision the person can overrule; "tasteful and delightful" is not.
