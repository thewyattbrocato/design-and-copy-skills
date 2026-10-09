**Build (c), the interactive setup with a live preview.**

- **It fixes the actual failure.** New users struggle because the four settings interact. A height range that's fine on paper can be impossible with the wind limit you picked. A passive explanation (a or b) teaches what each setting means, but people still have to guess how they combine. With (c), they see the effect of each choice on today's real conditions as they make it.
- **It gives feedback they can check.** A preview like "this alert would have fired 2 of the last 7 days at your beach" shows whether the setup makes sense, and users can see the result without trusting the explanation.
- **It targets the first alert.** The first alert is the moment users either trust the product or leave. Getting that one right probably matters more for retention than general education.
- **It reuses what you already have.** You already compute current tide and swell conditions, so the preview is mostly a UI on existing data. The risk is in the scope of the flow, not in building new infrastructure.

The case against (c) is that it's the most work and the most that can go wrong in one sprint. To limit that:

- Keep it to the four inputs with sensible defaults pre-filled, so a user can finish in a few taps and still see the preview.
- Ship it behind a flag or to a slice of new users, so you can compare it with the current setup.
- Skip the video. It's the most expensive to produce and update, and most people skip it.
- Treat the carousel as a cheap fallback if (c) slips. It can be a help screen attached to each setting later.

Since you have no data yet, instrument the flow from day one so the sprint produces an answer as well as a feature. Track:

- setup completion rate (started vs. first alert saved)
- time to first alert
- how many first alerts are edited or deleted within 48 hours
- whether the first alert fires and the user opens the app afterward

If (c) ships and completion is high but edits are also high, the preview is probably working but the defaults are off. If completion is low, the flow is too long.
