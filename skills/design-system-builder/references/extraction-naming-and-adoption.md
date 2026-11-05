# Extraction, naming and adoption

Load when a system is being grown out of existing screens, copies of one part are being merged, a part is being named or admitted, someone must decide who contributes and when, or the question is how to measure and present a system. Examples are invented; adapt the pattern, not the words. The decisions below are part of the requested plan or spec, not notes beside it.

## Connected or copied

Default to consumers installing the system as a versioned dependency (a package, a shared library in the design tool) so fixes and updates travel both ways. Pasted snippets and detached instances make a library, not a system: each copy forks quietly, and the first upstream change forces a choice between losing local edits and skipping the update. Change when the starter is meant to be forked (a template): say so and expect no updates.

- Test: does each consumer carry a version and take the next release without hand-merging? If not, call it a library and name the first step that connects it (publish a package, one import path, library updates switched on).
- Copies already exist: list each copy's local edits, send the ones several copies share back into the system, replace the rest with the dependency plus an override.
- Building a screen for a team that has a system: use its tokens and parts. A gap becomes a clearly named local component whose values come from the system's tokens; do not edit or fork the system's own file to change one property.

## The first parts

Default to growing from shipped work: extract about three parts that another team could use now, each shown by the screens where it already runs. One part that saves a team a few hours already pays for itself, so a small first release is correct. Change when nothing has shipped: ask for the first product screens or build them first, then extract; do not draw a forty-part catalog from a mood board. Change when a rebrand, replatform or migration is already scheduled: attach the work to it, since money and urgency exist there.

- When copies differ, name the one priority that defines "best" (loads fastest, fewest complaints, most accessible, best coded) before choosing among them.
- Pick the first product to build with it by a short list: parts it would reuse, a champion on that team, fits a few weeks, depends on no other work. Scores are a talking aid, not a measurement.
- A swap-only migration changes no visible design. Improvements found on the way go on a list for the next release.
- Ask what the organization needs, not what people want; wish lists make parts nobody installs. Start with the boring recurring problems (alert, field row, list item, checkbox) before distinctive ones.

## Merging copies of one part

Default to listing every trait across all copies and sorting by how many copies share it.

| Shared by | Decision |
|---|---|
| Every copy | Mandatory in the canonical part |
| Most | Recommended default, documented |
| Some | Decided with the owners in one short meeting, with the tiebreaker (for example, the highest-traffic page's version) agreed beforehand |
| Few | Deferred; stays local until more copies adopt it |

The result should look familiar to most owners, or it becomes one more competing version. Deliver the table, the canonical spec and a migration map (old component, new part, places affected, order). Change when there are only two copies: choose by the stated priority and skip the meeting.

Invented case: six pagination controls. All show previous, next and the current page (mandatory); four number the pages (recommended); two add a jump-to-page field (owners decide); one shows rows per page (deferred).

## Names and admission

Default to generalizing and renaming on the second real use, and admitting a part to the shared, supported catalog when another team will use it now or this quarter. A part someone might use someday waits. Change when one team owns a security or compliance pattern that others must reuse: admit it at once.

- Name for structure: `vertical-tabs`, not `career-paths-block`.
- Keep content and display apart. Content types (event, article, offer) have fields; display parts (media card, list row) draw any content that fits. `event-card` used only for events is a content name on a display part; rename it when an article would fit.
- Local components may sit beside the system's, marked as local; they reach the catalog only through the contribution path.
- Raw color steps carry one number per hue from a single ordered scale (for example 0 to 1000 by contrast), with halfway steps (`gray.250`) instead of renumbering, so names sort in visual order.
- Semantic color names use up to four slots, general to specific: element, tone, emphasis, state (`text.danger`, `fill.success.subtle`, `border.strong`, `fill.accent.hover`). Components get no color names of their own; a component token exists only for a knob that component needs.
- One word per concept across tokens, component names, props and docs ("surface" or "background", never both). A token used in one place is a local value; a token nothing references is deleted at the next release.
- Depth follows need. One brand, one platform and no themes can keep a flat semantic set over a single ramp; add the raw tier when a second brand, theme or platform must remap it.

## Who contributes, and when

Default, when several teams consume the system: product teams invent and ship, and the system owners extract, abstract, document and announce. A checklist that product teams must pass before contributing lowers contribution. Change when the product teams include system specialists (federated): they contribute directly.

- Give extraction a fixed beat, not the end of a release: a few weeks of product work, then a short block for system work in which new parts are audited, abstracted, documented (only that handful) and announced.
- Fit the existing workflow instead of adding a parallel one. Write down how work really happens before changing it, and answer two questions in it: when do I use the system versus build my own, and how does something new come back.
- Make the system the easiest path: a starter project with the dependency installed, a lint rule that flags raw values. A mandate such as a new brand or accessibility rule is the best argument for the system when the system makes complying cheaper.
- When the system's goal (adoption) and a product's goal (customer value) conflict, the product wins; tie the system team's goals to the products it serves.
- Change for one squad: one owner, a changelog and review in the normal pull request; no beat, no committee. Teams plan on few contributors per consumer, so do not assume volunteers will appear.

## Measures

Default to stating success as what the system's users can now do ("a settings page ships in days, not weeks"), backed by counts you can scan: the share of a screen's parts from the system (search code for system imports or a class prefix; library analytics in the design tool).

- Coverage stays below 100%. Start with one part used by a few teams, even a trivial one to prove the install path; treat about four-fifths of a page as the ceiling. Forks, overrides and custom parts are tracked, not shamed.
- Keep room for work the system does not cover yet. If everything new must come from it, the people who invent leave.
- Set the first target modestly and expect to change the measure after a quarter; share results monthly with the people whose work it affects.
- Change when there is no codebase to scan: say it is unmeasured and give the query to run, marked `[count from your repo]`. Never present time saved, return on investment or team-size ratios as the user's own.

## Presenting the system

Default the reference site's order to finished products built with it, then collections of patterns, then parts by type, then granular parts, with a short labeled note on where local components live. Show anatomy of real screens and live examples from production code, and put guidance where the work happens (the design tool, the editor) as well as on the site. Change for a one-squad system: one page of tokens and parts.

## Quick checks

- Every consumer named has a version or a first step to get one.
- A first release lists about three parts, each tied to screens where it already runs.
- A merge shows the four groups of traits and a migration map, with the owner decision named.
- Admission and generalization are stated as two rules, and no part is named for the content it first held.
- Color names have at most four slots and none are named for a component.
- Contribution has an owner on the system side and a beat; a one-squad plan has neither committee nor beat.
- Success is phrased as what users can do, coverage is below 100%, and any count is scanned or marked.
