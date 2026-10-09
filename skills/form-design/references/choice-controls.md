# Choice controls

Load this when choosing between radios, checkboxes, selects, autocomplete, segmented controls and switches, or when building a filter panel.

## Decision table

| Situation | Control | Notes |
|---|---|---|
| One of two to about seven options, people compare them | Radio group | Visible options; a group label; default only if most people keep it |
| Yes or no | Two radios, or one checkbox for an agreement | Not a select |
| One of many known options (country, month) | Select, or autocomplete when the list is long | Native select on phones |
| One of many open-ended options (city, product) | Autocomplete with real matches | Do not suggest values you cannot fulfill |
| Any number of options | Checkboxes | Group label; consider "Select all" when lists are long |
| A setting that applies the instant it changes | Switch | Not for form values sent on submit |
| A short list of modes that change the view | Segmented control | Not for form answers that need comparing text |
| A choice with long text per option (delivery slots, plans) | Radio cards with the comparing details inside | The whole card is the click target |
| A command ("Delete", "Export") | Button | Never a dropdown value |

Round means choose one; square means choose any. Do not mix the shapes.

## Radio groups

- Give the group a visible label ("Delivery slot") that is associated with the group.
- Put the comparison data in each option: a time and a fee, a price and what it includes.
- Avoid nesting groups inside groups; ask the first choice earlier instead.
- Do not preselect a value people must understand. Preselect only when most will keep it.
- "Other" with a text field that appears when chosen is fine; keep the text on the same screen.

## Selects and autocomplete

- A select is a good fit for known lists of moderate length. Sort the list in a way people expect and put common choices first only if the order stays obvious.
- Replace a select of fifty or more options with autocomplete.
- Autocomplete turns a long string into a pick list and removes typing on phones. Keep typed entry working, and do not hide the field's label.
- Do not use a select with two options or with "Select..." as the only label.

## Defaults and unchecked boxes

- Set a default only when most people will keep it. Otherwise you created work.
- Do not default sensitive answers, and never precheck a box that opts someone into messages.
- If the person must understand the choice, make them answer it.

## Filter panels

- A filter earns its place when the list is too long to scan.
- Use a group label per filter ("Brand") with checkboxes or radios inside, never links styled like checkboxes.
- Default: batch. People choose several values and press "Apply filters". This avoids the panel snatching focus and reloading after the first tick. Use live filtering only with an in-place update that keeps focus and scroll position, and with a way to pick several values.
- Show active filters as removable chips or a summary above the results, plus a "Clear all" control.
- An empty result says "No products match" and offers to remove a named filter.
- The page structure reads in order: page title, filter heading, results heading.
- Preserve filter state in the URL when the page might be shared or refreshed.

## Sorting

A sort control is a single select near the results labeled "Sort by". Keep sort separate from filters.
