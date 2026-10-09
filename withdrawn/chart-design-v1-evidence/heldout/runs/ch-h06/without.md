## Why dual-axis charts mislead

**1. The visual relationship is arbitrary.** Each axis has its own scale, and you choose where each starts and ends. Stretch the signups axis a bit and the two lines overlap perfectly. Squash it and they look unrelated. The "correlation" a reader sees comes from your formatting choices, not from the data.

**2. Crossing lines look meaningful but aren't.** When the spend line crosses the signups line, readers read it as "signups overtook spend." Those are different units, so the crossover has no meaning.

**3. Truncated or non-zero baselines exaggerate change.** Each axis can start wherever you like. A 5% bump in spend can look as large as a 50% jump in signups.

**4. It implies causation and timing.** Two lines moving together suggest spend *caused* signups. But there's often a lag (spend today, signups next week), seasonality, and other drivers such as organic traffic, promos and launches. Overlaying the lines hides all of that.

**5. It's hard to read.** Viewers have to work out which line belongs to which axis, and they often get it wrong.

## What to do instead

**Best default: plot the thing you actually care about, which is efficiency.**
- **Cost per signup (CAC)** = spend ÷ signups, as a single line on one axis. It answers "are we getting more or less for our money?" directly.

**If you need to show both series:**
- **Stacked small multiples.** Put spend on top and signups below, with a shared x-axis (time) and separate y-axes. The timing lines up, and neither scale can distort the other.
- **Index both to 100** at a starting period and plot them on one axis. This shows relative change, such as "spend is up 40%, signups up 15%." Say clearly what the base period is.

**If the question is "does spend drive signups?":**
- Use a **scatter plot** (spend on x, signups on y), optionally with a trend line.
- Check **lagged** relationships (e.g., this week's spend vs. next week's signups).
- Be upfront that correlation isn't proof. Spend often rises during already-busy periods.

## Quick checklist before you chart
- Does the chart answer a specific question? If so, plot that metric directly (e.g., CAC).
- Do both axes start at zero where appropriate (especially for bars)?
- Would the story change if I rescaled one axis? If yes, don't use dual axes.
- Are labels and units clear on every series?

**Rule of thumb:** if you're reaching for a second y-axis, you probably want a ratio, an index, or two stacked panels instead.
