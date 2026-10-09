# Many series and accessible charts

Load this for many series, tiny inline trend lines, or any chart that must be accessible or work without hover.

## Small multiples

Use a grid of small charts, one per group, when one plot would need more than about five lines or when the point is comparing shapes across groups.

- Same chart form, same scales, same axes order in every panel. Shared scales make panels directly comparable. If one group dwarfs the rest, use independent scales only with a visible note in each panel, and say that panel heights are not comparable.
- Arrange panels in a meaningful order: by total, by growth, by region from north to south, or by the quantity the reader cares about. Use alphabetical order only when readers will look things up by name.
- Keep the panels adjacent and compact so the eye can scan across. Remove repeated axis labels: put the scale on the left column and the bottom row only.
- Label each panel with its name at the top left, in plain text.
- Add one reference in each panel: a gray line of the overall average, last year's series, or a target. Highlight the panel that matters with the accent color.
- Aim for roughly 6 to 20 panels. Fewer: use one plot. More: filter, group, or switch to a table.

## Tiny inline trend lines

- A tiny line with no axes shows the shape of recent history beside a number. Put it next to the figure it describes, at about the height of the text.
- Mark the latest point with a dot, and optionally the minimum and maximum. A faint band can show an acceptable range.
- State the window in nearby text or a caption ("last 12 weeks"). Without it, the shape is ambiguous.
- Skip it when the reader needs exact magnitudes; use a labeled mini chart or a table instead.
- Use the same vertical scale across a column of them only if comparing size matters; otherwise let each fill its own height and label the value.

## Text alternatives

- Provide a short text summary of the takeaway near the chart, not just an `alt` attribute: "Page load time fell from 4.1 s to 2.3 s over 12 weeks; most of the drop came after the image change in week 7."
- For inline SVG, give the root element `role="img"` with `aria-labelledby` pointing to a `<title>` and a `<desc>`; the description states the finding and the range.
- If the chart is interactive or complex, give a longer description or link to the data table.

## Data available as a table

- Offer the underlying values as a table beneath the chart, or behind a disclosure control. A visually hidden table works for screen readers, but a visible one helps everyone.
- Do not make values available only in hover tooltips. Print key values on the chart (latest, peak, target) and keep the rest in the table.

## Not only color

- Direct labels and line styles (solid, dashed) distinguish series without color.
- In bar and area charts, use patterns or direct labels when adjacent fills have similar lightness.
- Markers (circle, square, triangle) help distinguish lines in a scatter or when printed in grayscale.
- Status encoded as red, amber and green also needs text or an icon.

## Interaction without hover

- Hover can add detail, not carry the story. Touch screens have no hover.
- Provide keyboard access to any interaction: focusable elements, visible focus, arrow keys to step through points, and an escape to dismiss.
- Keep tooltips short and large enough to read; tie them to the nearest point rather than a tiny target.
- Respect the reduced-motion preference: skip animated entrances or draw the final state immediately.
- Zoom and filter controls need text labels and sensible defaults. The default view should answer the main question without any interaction.

## Responsive

- A chart in a narrow column should be simplified, not just shrunk: fewer tick labels, direct labels moved inside, horizontal bars in place of vertical.
- Keep the text size readable at the smallest width; if it cannot be, reduce the number of labels, not the size.
