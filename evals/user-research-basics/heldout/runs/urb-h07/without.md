No, you can't tell the board that B won. The data doesn't support it yet.

**The numbers**
- A has about 68 purchases out of 1,900 (3.6%). B has about 78 out of 1,900 (4.1%).
- That's a gap of about 10 purchases.
- A two-proportion z-test gives z ≈ 0.8 and p ≈ 0.42. A gap this size would show up by chance roughly 4 times in 10 even if the labels did nothing.
- The 95% confidence interval for B minus A is about **-0.7 to +1.7 percentage points**. The true effect could be a small loss, nothing, or a decent gain.

**Why waiting until Friday won't fix it**
- To reliably detect a lift from 3.6% to 4.1% (80% power, 5% significance), you need roughly 20–24k visitors per variant. At about 800 per variant per day, that's around a month.
- Two or three days also covers only part of the weekly cycle. Ticketing traffic is lumpy, with on-sale spikes, weekend buyers and event-specific demand. A short window can mislead even if the test looks clean.
- If you check the result daily and stop when it looks good, you inflate the false-positive rate further.

**What you can do instead**
1. **Ship B anyway, but don't call it a win.** A label change is cheap and reversible, and the data doesn't show B is worse. You could say: "B is trending slightly ahead, but the result isn't statistically significant. We're shipping it as low-risk and continuing to monitor." That's honest, and it still lets your boss move on Friday.
2. **Keep the test running** for at least two full weeks, ideally until you hit a sample size you set in advance. Then make the call.
3. **Reframe the claim.** If the board needs a number, give them the interval (-0.7 to +1.7 points) rather than "+0.5 points, B won."

If the label is the only difference and you have no reason to prefer A, option 1 is reasonable. The thing to avoid is telling the board it's proven, because if the lift disappears later, that claim will be hard to walk back.

I can also work out how long the test needs to run for a different minimum lift, if that would help. Or I can draft the wording for the board update.
