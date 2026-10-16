# Layout for the A4 handout

**Use small multiples: 12 small panels in a grid, one per branch. Don't draw one 12-line chart.** Twelve lines on one axis would be spaghetti. The color guidance also caps categorical hues at 8, so 12 branches can't each get their own color. Panels avoid both problems and need no legend.

## Page structure, top to bottom

1. **Header (about 15% of the page)**
   - Title that states the finding, e.g. "Summer reading drives visits at 11 of 12 branches; Dunmere fell sharply after its July roof closure". Use real numbers once you've checked them.
   - One-line subtitle: "Monthly visits by branch, January–December 2025".

2. **Panel grid (about 65%)**
   - 3 columns × 4 rows fits A4 portrait well. Each panel is roughly 60 × 50 mm.
   - Order the panels alphabetically as you listed them, so board members can find their branch. Don't rank them by size.
   - Every panel uses the same y-axis scale, so branches compare honestly. If the largest branch is far bigger than the smallest, the small ones will look flat. In that case either use one shared scale and say so, or index each branch to its own annual average (=100) and say that in the subtitle. Don't mix scales silently.
   - Label the y-axis only on the left-most panels and the x-axis (J F M A M J J A S O N D) only on the bottom row. Light gridlines, two or three ticks per axis.

3. **Callout and footer (about 20%)**
   - A short "What to notice" box with two or three bullets:
     - the summer peak, with the typical July–August uplift
     - Dunmere's drop, with the before and after monthly average
     - any other outlier
   - Footer: data source, definition of "visit" (door count or sign-in), the date range, and the contact for questions.

## Encoding

- **Chart type:** a thin line (about 1.5–2 pt) per panel. A bar per month also works if the board prefers it. A line shows the seasonal shape best.
- **Color:** draw 11 branches in one neutral dark gray or a single muted blue. Draw **Dunmere alone** in a strong accent such as orange or red. Color then marks the exception, not the identity of each branch.
- **Context:** put a faint gray line of the all-branch average (or median) in every panel, so each branch is read against the network.
- **Dunmere's panel:**
  - Add a thin vertical dashed line at July with the label "Roof closure".
  - Give it a slightly heavier border or a tint, so the eye lands there first.
  - Label the low point directly with its value.
- **Labels:** put the branch name at the top-left of each panel in bold, not in a legend. Label only the peak month on the other panels, or nothing. Don't put a number on every point.

## Print-specific points

- Check the page in grayscale or on a black-and-white photocopy. The accent line should still stand out, so make it thicker or add a text callout, not color alone.
- Keep body text at 8 pt or larger and panel labels at 9–10 pt. Use 10–15 mm margins, because many office printers clip the edges.
- Use no hover, tooltips or interactivity, since this is paper only. Put the key numbers on the page itself.
- If you can spare a strip at the bottom, add a compact table of annual totals per branch. That gives the board exact figures without cluttering the panels.

## Worth deciding before you build

- Whether the board cares more about absolute visits or seasonal shape. That decides shared scale versus indexed.
- Whether to mention anything about Dunmere's recovery, such as a reopening date. If one exists, add it to the Dunmere annotation.

If you share the data (a CSV is fine), I can build this as a print-ready PDF or SVG.
