# Alignment and optical fixes

Load this when edges look slightly off, a layout feels untidy without an obvious cause, or you are aligning icons, numerals, bullets, or round shapes.

## Shared edges

- Every element should share an edge or an axis with at least one neighbor. Look for strays; each unexplained left edge is a small cost to the whole.
- Choose one primary text edge. For left-to-right languages that is the left edge; for right-to-left, the right. Headings, body, buttons, and form labels hang from it.
- Interior axes matter too: a column of labels and a column of values each need their own consistent edge, and a row of cards needs consistent top edges.
- Break alignment on purpose or not at all. A one-pixel miss reads as an error; a clear offset, large enough that nobody takes it for a rounding slip, reads as a choice.

## When centering is right

- Default to flush at the reading start. Centered text is slower to scan because each line starts somewhere new.
- Center when the composition is short, ceremonial, or single-focus: an invitation, a certificate, a short hero with two or three brief lines, an empty state, a modal confirmation.
- When you center, center the whole group and keep it consistent. Never put a centered heading over flush-left paragraphs, and keep centered paragraphs to two or three lines at most.
- Symmetric layouts are a style, not a failure. If the user asks for one, make it clean and do not force an asymmetric edge onto it.

## Aligning by visual mass

- **Hanging marks.** Bullets, numbered markers, opening quotation marks, and large leading numerals can sit just outside the text edge so the text itself lines up. In a tight card or button, keep them inside.
- **Round shapes overshoot.** Circles, rounds, and pointed shapes look smaller than squares of the same box. Let them pass the line slightly (a few percent) so they look aligned.
- **Optical centering.** A play triangle centered by its bounding box looks pulled left; nudge it toward its heavy side. Icons with a heavy corner or a thin side need the same eyeballed correction. Check every icon button, not only one.
- **Optical middle.** In a poster or an empty state, the visual center sits a little above the geometric middle; a block placed exactly in the middle looks low. Use this as a tie-breaker for single-mark compositions, not as a habitual nudge applied to all compositions.
- **Filled boxes.** A solid button or card is judged by its box, so align the box edges; correct the glyph inside it, not the box.

## Baselines and rows

- In a row of mixed sizes (a large number beside a small label), align text baselines, not tops or boxes, unless the items are blocks of equal height.
- Choose tops or bottoms for a row of cards or images and do it the same way throughout.
- Across columns, a heading and its first data line should share a baseline relationship in every column.
- Tabular figures, where available, keep numeric columns lined up; right-align numbers so place values stack. The exact figure styling is a typesetting detail, not a hierarchy one.

## Diagonals and tilted elements

Avoid rotating things a few degrees off axis; it reads as a mistake. If you tilt something, tilt it enough that it is obviously intended, and only when the angle is part of the content or brand.
