The page is flat because it treats every room and every number the same, so nothing tells you where to look. The alert is also the weakest element on the page.

**What's wrong**

- **Status is encoded in the least visible way.** The only signal is a slightly darker orange on one number, and the word "alert" is 11px grey in a corner. A problem is quieter than the healthy data around it. In Room 5's case, a humidity of 61% in a flat 28px orange number could easily pass as normal.
- **The cards hide the state.** Eight identical white tiles give no sense of whether anything is wrong until you read each one. There's no summary, such as "2 rooms out of range," and no sorting that puts problems first.
- **The four metrics are ranked equally, but they aren't equal.** Humidity and CO2 can ruin a flush within hours. Days-to-harvest is planning information. Giving all four the same size and weight means the harvest countdown competes with the alarms.
- **The page shows a snapshot with no time context.** "61%" tells you nothing about whether it just dropped or has been wrong for six hours. Time-in-state is the detail that would have caught Room 5, and the page doesn't show it.
- **Targets are missing.** A number without its acceptable range makes you do the comparison in your head, which is the work a monitoring page should do for you.

**What to change first**

1. **Make out-of-range the primary state, not a tint.** Give a tile that's out of range a clear status treatment: a solid colored left edge or header band, and a labeled status line such as "HUMIDITY HIGH · 61% · target 85–95% · 6h". Use text and shape, not just color, so it still reads for people with color-vision differences.
2. **Add a summary strip at the top.** Show a count such as "2 rooms out of range" and sort rooms with problems first. Healthy rooms can collapse to a smaller, quieter row.
3. **Show duration out of range on every alert.** This is the change that addresses last week's incident directly. Show how long each metric has been out of range, and make it more prominent after a threshold, for example 30 minutes.
4. **Reorder the metrics by importance.** Make humidity and CO2 the large numbers, and show temperature and days-to-harvest smaller. Put the target range next to each number.

One caveat: a visual change only helps if someone is looking at the page. If Room 5 sat at 61% for six hours, the bigger gap may be that nothing pushed an alert to a phone. If you don't already have that, a notification for any metric that stays out of range beyond a set time is probably worth adding alongside the visual fixes.

If you point me to the page's source file, I can make the first two changes directly. I haven't seen the code, so these recommendations are based on your description.
