# Maps, percentages and chart sets

Load this for a map, for a percentage or rate that is combined, compared or rebased, for a screen or slide that holds several charts, for results from a small group of people, or for a chart that will be projected.

## Percentages and comparable scales

- Default: recompute a combined rate from counts, never average the rates. Two sites at 9% of 500 and 29% of 300 make 132 of 800, 16.5%, not 19%. Print the counts beside the rates so the weights show. Change when each site is itself the unit (a median across sites): say so.
- A move between two percentages is in points: 6.2% to 6.8% is "up 0.6 points" or "about 10% higher, relative"; never "up 0.6%". Name the base of every percent change. Down 50% then up 50% ends 25% below the start, so multi-period changes compound and are not averaged.
- Compute at full precision from the inputs and round only for labels.
- Two series of unlike size or unit in separate charts: Default one chart of percent change from a shared start. Change when the amounts matter: give every panel the same percentage span (say 15% below to 45% above its own start) so equal slopes mean equal growth. Auto-scaled panels make a $5 gain on a $20 item look the same as on a $200 one.
- Fit the range: the line fills about two thirds of the plot height, ticks fall on round steps (1, 2, 5, 10, 25), reference levels the reader compares against sit inside the range, and no first tick sits just above zero.
- Missing values: Default for one or two gaps in a long series: leave a visible gap (no zero, no silent bridge) and footnote it. Change when more than about two in ten are missing: plot fewer chosen points or say the series is too sparse. A pie never gets a missing slice.
- One value dwarfs the rest of the bars: Default keep the bars honest, print the big value at its tip, or give it its own panel. A broken bar only when there are about ten or more bars, one value is about three times the next, the value is verified, the outlier is not the story, and the break and value are both visible.
- A long history with one recent move: add a labeled magnified panel or inset of the recent window instead of rescaling the whole axis.

## Maps

- Default: sorted bars. Change to a map when position or neighbors explain the pattern (a spread from a source, a regional divide), not to answer "which place is highest".
- Area shading takes rates (per person, per household); totals go in proportional symbols, because shading gives big areas the weight and a dense small place disappears. A rate from a tiny population swings wildly: show the count or flag it.
- Proportional symbols scale area to value and the legend shows the smallest, the largest and one in between. Graduated symbols give each class one size, tell only rank, and the legend lists the ranges.
- Classes: Default five on a screen, break values rounded, and every class present on the map. Change to three to five when projected, printed in gray or drawn as small patches; more than about nine cannot be matched to a key. Skewed values need uneven breaks so the top class is not one outlier; state the breaks. An unclassed gradient only when the pattern matters more than any value, labeled low and high.
- Ramp: lightness leads (darker is more), with a slight hue drift. No rainbow: its lightest, loudest band lands on an arbitrary middle value and reads as a threshold. Reverse the direction only when the topic is a deficit, and say so in the legend.
- Two-ended ramp only for a real midpoint (zero change, a national rate, a target). If the midpoint sits inside a class, that class is the light one (odd class count); if it falls on a break, two light classes of different hue meet there (even count). A midpoint that is not mid-range gets an uneven ramp with its light class fixed on the midpoint.
- Color-vision-safe ends: the common deficiencies blur the red-green axis and leave lightness and blue-yellow intact. Put a blue end against a warm end and make them differ in lightness; red against green, or any two of orange, brown, olive, red, green at similar lightness, fail. A brand red and green are not the good and bad ends by default.
- Categories on a map: about five hues on small patches; past that vary lightness as well and label directly. The same category keeps its color across every map.
- Check each class as a small patch inside the colors around it, in the final medium, not only in the legend. Legend swatches sit on the same ground as the map.
- Projection: a country or world map that shades areas or shows density uses an equal-area projection (not a stretched plate carrée or a Mercator, which inflates high latitudes); a single city or small region can use a local one.
- Keep the base quiet: thin light boundaries, no label that does not help, a scale bar or north arrow only when readers measure or north is not up, nothing boxed for decoration.
- Legend title names the measure and unit ("Tickets per 1,000 customers", never "Legend"), breaks are rounded, high sits on top, and a one-line note defines the calculation and year. Test: a stranger can say back what the map shows.
- A series of maps shares classes, colors and one legend; when change is the point, map the computed difference.

## Several charts on one screen

- Write the one question the screen answers; each chart answers one part of it. Charts that share no scale, color meaning, time axis or selection are cards side by side, not a view of anything. Default: no more charts than questions, and a single figure with its comparison is a number, not a chart.
- Shared decisions: the same category keeps one color and one order everywhere, time axes use the same range, same measures use the same decimals, and charts to be compared share axis ranges and size.
- Reader compares one measure across groups: panels per measure with groups in the same order. Reader compares measures inside a group: group by group. Reader wants a gap, share or rank change: derive it and plot that.
- One frame for up to about five lines when the task is reading values at a moment; panels for more series, or when the task is which series changed most across the whole period. Order panels by that change.
- Whole and part: one chart for the whole, one for the selected part, and a list when names must be found. A control that changes what a chart shows says so on the chart (active filter, count shown, count hidden).
- A selection is marked with one highlight (outline, or fade the rest); do not recolor the series so the color code disappears.
- When a chart shrinks to a tile, keep what must not be missed (a breach, a latest value) and drop detail first. "Other" never swallows an item that crossed a limit.

## Small-group study charts

- Default: counts ("7 of 9") or one mark per person, not percentages to a decimal. If a rate is needed under about thirty participants, show its range once and headline only what the range supports. Change when the sample is large enough that the range is tight.
- A range goes on a dot as a whisker, not on a bar. Say what it is ("95% range for the average") in the subtitle.
- Overlapping ranges for two designs: title the chart "no clear difference", not the leader. Same people on both designs: draw each person's pair (slope or paired dots) so a consistent shift shows through the overlap.
- Ratings: show the spread by level (a 100% bar of up to four levels, or dots), with the average only beside it. Never average ordered levels such as severity or rank; count them.
- Times for fewer than about thirty participants: one dot per person plus the median; keep the slow people visible and label them rather than let two of them squash everyone else.
- Several targets: count people who met all of them ("3 of 10"); averages can pass while few individuals do. Show tasks as rows of dots, not a radar or a line across tasks.
- Expected against actual per task: scatter with a diagonal and the favorable corner at upper right, tasks labeled.

## Projected charts

- Labels no smaller than the slide's body text, and the chart as large as the slide allows; the room cannot zoom. Deck-level choices (one claim per slide, tables to the handout, fixed axes across a run of slides) belong to presentation-design if installed.
- Projection washes out pale steps and thin lines: fewer categories or classes, bigger lightness gaps, thicker lines, and call the extremes out in words.
