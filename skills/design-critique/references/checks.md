# Checks

Short passes; use only those the design contains. Thresholds match the focused skills (form-design, ui-motion, chart-design, data-tables, if installed).

## Interaction and state

- **Clear controls.** Does each control look like what it does? Clickable flat text, icon-only buttons with no label or accessible name, inputs that look like plain text are findings. Labels name the action ("Save changes", not "Submit"). Primary, secondary and destructive actions look different. Controls sit near what they change.
- **Visible state.** Selected, active filter, on or off, loading, saved, disabled, signed in. A disabled button with no reason is a finding.
- **Feedback.** Acknowledge an action within about a tenth of a second; show progress if longer.
- **Errors are a design fault first.** Prevention (constraints, sensible defaults, tolerant formats), then a message that says what happened and how to fix it next to the field, then recovery (undo, confirmation only for destructive acts, nothing lost). A message that only shows in a disappearing toast or only in color, or that blames ("Invalid input"), is a finding.
- **Forms.** Visible labels (placeholder-only labels vanish while typing); ask only what is needed; validate when a field is finished, not on each keystroke; right input types; many errors summarized and linked.
- **Deep page.** Can a stranger tell the site, the page, the main sections, the current item (clearly marked), how to search, how to go back? Page names match the link that led there.

## Accessibility

- Keyboard reach in logical order, visible focus, real buttons and links, names and states exposed.
- Contrast: 4.5:1 for body text, 3:1 for large text and control boundaries. Color is never the only signal.
- Touch targets about 44px (24px is the floor); nothing needs hover; text resizes and layout reflows; reduced motion respected.
- Say what you checked by inspection and what needs a person using assistive technology.

## Content

- The first line carries the point; headlines say what and for whom.
- Labels, buttons and messages are specific, short, in the user's words; one name for one thing across the product.
- Empty states and errors say what to do next.

## Motion

Does it explain a change or only decorate? About 150 to 300ms for small changes, nothing blocks input, no loops competing with content. A static view cannot judge timing; say so.

## Charts, tables, dashboards

- Wrong outranks ugly: a finding that can mislead a decision ranks high.
- Bars start at zero; a bar axis starting near the minimum exaggerates gaps (major). Lines may use a labeled non-zero baseline. One axis per measure; dual axes invite false links; log scales labeled, and bars for amounts do not belong on one.
- Form matches the question: comparison, change over time, parts of a whole (a pie only for a few slices that sum to a whole), distribution, relationship.
- No 3D or decoration that changes how size reads. Direct labels over distant legends. Colors kept to a handful with one highlight; not red and green alone.
- A number needs context: prior period, target or benchmark.
- Tables: numbers right-aligned with consistent precision, units in the header, missing values explained, status not by color alone, a plan for narrow screens.
- Dashboards: do the first-screen answers match the viewer's top questions? Status color only where attention is needed; consistent time ranges and scales; freshness and filters visible; count the tiles and ask which decision each supports.
- Quote the exact scale or value that misleads, who could be misled, and the corrected form.

## Manipulative patterns

Report with place, who is affected, harm (money, privacy, time, trust) and an honest alternative that still serves the business goal. Major by default when it touches money, consent or leaving; a blocker when it deceives enough to cause real harm.

- Fees or taxes first shown at the last step; show the total early.
- Account required before it is needed.
- Marketing opt-ins, insurance or donations pre-selected; default to what a reasonable person would choose.
- Decline buttons worded to shame; use neutral, equal wording.
- Countdowns that reset, invented "only 2 left", fake activity notices; allowed only when true and verifiable.
- Cancel or delete harder than sign-up.
- Controls disguised as content; the prominent button does the less wanted thing.
- Invented reviews, counts or endorsements.
- A common convention is not a defense; ask whether the person could decide freely with what is shown.

## Watching people

Use when a finding hinges on comprehension, a team argues over opinion, or someone asks whether to test.

- Three to five people who roughly resemble the audience; people differ enough that a rough match teaches more than waiting for a perfect one.
- Two or three concrete tasks ("find what this costs for two people"), one person at a time, thinking aloud. Do not help or explain; silence is data.
- Same-day debrief: each observer lists the three worst problems; the group fixes the few most serious. Fix by cutting, renaming or moving before adding explanation.
- It shows problems, not preference or statistical difference. Report what happened, not percentages from a handful of people.
- Which of two versions wins at scale: a live comparison with enough traffic. Where a flow is abandoned: analytics first, then watch people for why.
- In the critique, state the question, the task, how many people, and the result that would change the design, in a few lines.
