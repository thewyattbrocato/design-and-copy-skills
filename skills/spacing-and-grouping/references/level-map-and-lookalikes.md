# Level map and look-alikes

Load this when a layout needs spacing assigned across several nested groups, when it looks squashed and every gap is the same, when someone wants boxes removed, or when a static element sits next to a control.

## Map spacing by nesting level

1. Sketch the tree: page, sections, groups, items, then the parts of one item (a title and its price line, an icon and its label).
2. Give the innermost level the smallest step and move one scale step up for each level outward. Siblings at one level get one value.
3. Pin four or five fixed rules and reuse them everywhere: gap inside an item, padding of a surface, gap between sibling groups, gap between a section heading and its content, vertical padding of a section. A new component takes its values from the level it sits at, not from a new number.

A map for a rental-listing page on the 4 px scale in the scale reference:

| Level | Example | Value |
| --- | --- | --- |
| Parts of an item | title to price line | 8 |
| Items inside a surface | photo, text, button | 16 |
| Surface padding and gap between sibling surfaces | each listing card | 24 |
| Section heading to its content | "Nearby" over the grid | 32 |
| Section padding | band above and below a block | 80 |

Checks: values never shrink going outward, and two neighboring levels never share a value. If the second check fails, the tree has a level nobody can see; merge the levels instead of inventing a step. Default: one step per level. Change when the tree is deep in a compact tool: let two inner levels share a step and separate them with alignment or a rule.

## Three distances in a form

A form with groups needs three different gaps, not two: label to its field (smallest), field to the next field in the same group (a step or two more), and group to group with its heading (larger again, at least one step above the field gap). Two gaps make the groups vanish; one gap makes labels float between fields. Test by covering the labels: the fields should still fall into the groups you meant.

## Step up from the first instinct

Default: when a value falls between two steps, take the larger. Gaps that are too tight hide groups and flatten the order, and the error is hard to see; gaps that are slightly loose are easy to spot and trim.

Change when the larger step would equal the next level out, because a within-group gap that reaches the between-group value merges the groups. Then keep the inner value and raise the outer one a step too. Also change for dense pointer-only tools, where the smaller step is the point.

Test: squint. If two groups blur into one, raise the gap between those two by one step, then confirm the gaps inside each group are still visibly smaller. Do not inflate every value together; a uniformly looser page has the same problem at a bigger size.

## Look-alikes read as the same kind of thing

Elements sharing shape, fill, border and radius read as one family and as one behavior. The risk is a static item dressed as a control.

- Default: a tag, status pill, count badge or icon chip next to a button does not copy the button's border, fill, radius or accent color. Make the static one fully rounded or borderless, a tint with dark text, and use a status color rather than the action color. Leave the control alone. Moving them apart does not fix this.
- Change when the item is meant to be pressed (a filter chip, a toggle tag): give it the control family's shape, a hover state and a focus ring, and keep static tags visibly different from it.
- The reverse holds too: controls that do different things should not be twins. A delete control does not share a fill and border with the safe action beside it.

Test: for every pill, tag or icon in a row with a button, ask whether a person would press it, then check whether its style says so. Where the answer and the style disagree, restyle the static item.

## Remove boxes in stages

A box often hides loose spacing. Taking it away without replacing its job leaves equal gaps and a mess, which is why "remove the borders" can seem to fail.

1. Remove the outermost surface first, the one that holds other surfaces. Keep the inner ones for now.
2. After each removal, name what the box was doing: separating, aligning, or labeling. Replace it with a gap one step above the inside gap, a shared left edge, or a heading.
3. If groups still blur, bring back the lightest device first (a hairline rule, then a faint tint), and a card last.
4. Stop when every remaining surface wraps an object, or when the next removal would make two groups read as one.

Default: flatten nesting and boxes that wrap only a heading and text. Change when the user asked to keep the card look; then keep the outer surface and drop the surfaces inside it.

## When the spacing is already sound

Default: when every value is a scale step, the groups survive a squint, and no surface repeats without a reason, say that plainly and change nothing or one value. Rewriting spacing that works is a regression. Change when the person names a problem that remains, or the check above finds one.
