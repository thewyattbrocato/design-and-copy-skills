**What's wrong:** the page has no ranking. All 8 rooms and all 32 numbers get the same treatment, so the one fact that matters, "this room needs you", looks almost the same as "all fine". Your co-founder's "flat" is that. Room 5 sat at 61% for six hours because nothing on the page made it stand out.

Specific causes, in order of cost:

1. **An alert is a small change to one number.** A slightly darker orange on a 28px number, plus an 11px grey "alert", is the quietest signal on the page. Orange also barely differs from the other numbers in value, so it doesn't register at a glance or in grayscale. The word "alert" is grey and tiny, so it reads as metadata.
2. **Normal and abnormal look alike.** Eight identical cards give the eye nowhere to land. Healthy rooms are as loud as a failing one.
3. **Four equal 28px numbers per card.** Temperature, humidity, CO2 and days-to-harvest compete. The first three are live conditions that can go out of range. Days to harvest is slow-moving planning info. Treating them as equals means the one reading that's off gets lost among three that are fine.
4. **Labels, shadow and border add noise.** The soft shadow and border on every card repeat information the grid already gives. They add no ranking.

**What to change first (one change, biggest payoff):** make the out-of-range state structural, not just a color tweak on a number.

- When any reading is out of range, give that card a strong second cue. A solid status-colored border or header band works, and a tint of the whole card background helps too. Put a plain-language line at the top, such as "Humidity 61% (target 80–90%)", in a readable size and a strong weight. Don't use grey 11px.
- Make the offending number the loudest thing on the card. Leave the in-range numbers as they are.
- Keep this rare. If only alerting cards carry color, they'll be about one in eight, and that's what makes them pop. Healthy cards should be calm: no color at all.

**Next, in order:**

1. **Sort or pin alerting rooms to the top-left,** or add a one-line summary above the grid ("1 room needs attention: Room 5, humidity"). Position beats styling, and the eye reads from the top-left first.
2. **Demote days-to-harvest.** Make it a smaller, grey line at the bottom of the card. That leaves three live readings, and the number that's off will stand out.
3. **Fold labels into the values** ("61% RH", "21 °C", "850 ppm") and shrink them. You'll gain room for the target range, which tells people whether a number is bad without them having to remember.
4. **Drop the shadow** on healthy cards, or all of them. Keep a thin border or none.

**Beyond the page:** a 6-hour miss suggests the page can't carry this alone, since nobody watches a dashboard continuously. Add a push or SMS alert for readings out of range longer than, say, 15 minutes. Fixing the design makes the page better for whoever glances at it, but it won't make anyone look.

Two assumptions: I don't know your target ranges, so the "80–90%" above is a placeholder (use your real ones). I also haven't seen the page's code. If you share the HTML/CSS, I can make these changes directly.
