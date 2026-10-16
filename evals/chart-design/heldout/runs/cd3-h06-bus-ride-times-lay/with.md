**Show one bar, not a histogram.** Make it a single horizontal bar representing 100 trips, split into four labeled segments. Parents don't need to read an axis. They need to see how many trips were short, typical, or long.

I checked the totals (they sum to 380) and converted to "out of every 100 trips":

| Ride time | Trips | Per 100 trips |
|---|---|---|
| Under 20 min | 110 | 29 |
| 20–29 min | 211 | 56 |
| 30–39 min | 50 | 13 |
| 40 min or more | 9 | 2 |

**Design**
- Use gray for the first two segments, since that's the usual ride. Use one accent color for 30–39 and a darker shade of it for 40+.
- Print the number and the range inside or directly above each segment, like "56 trips · 20–29 min". Don't use a legend.
- Don't use a pie, a line, or an average. An average hides the long rides that parents are actually complaining about.
- Put the same four numbers in a small text line under the bar, for screen readers and for anyone who prints it black and white.

**Headline (states the finding)**
"8 in 10 Route 14 morning rides took 15–29 minutes. About 1 in 6 took 30 minutes or more."

Those figures are 303 of 380 trips (80%) and 59 of 380 (16%).

**Caption**
"Ride time for all 380 Route 14 morning trips, [start date]–[end date] last term. Out of every 100 trips, 29 took under 20 minutes, 56 took 20–29, 13 took 30–39, and 2 took 40 or more. The typical trip took about 20–24 minutes. The scheduled ride time is [X] minutes. [Source: district trip records.]"

**Two cautions**
- **Ride time isn't lateness.** Your data shows how long trips took, not whether they arrived late. Until you add the scheduled ride time or arrival time, don't write "on time" or "late". If a trip started late, that wouldn't show up in these numbers. Once you have the schedule, the most useful sentence is "X of every 100 trips took longer than scheduled". Send me the number and I'll work it out. It will be exact if the schedule falls on a boundary like 25 or 30 minutes.
- **Don't soften the tail.** Roughly 1 in 6 rides running 30 minutes or more is a real finding. A note like "the district is looking at the longest trips" would fit under the chart, if that's true.

I can build the bar as an SVG for the newsletter if you'd like.
