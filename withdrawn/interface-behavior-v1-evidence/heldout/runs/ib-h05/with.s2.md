**Subject: Why "loading is loading" doesn't hold for the editor, and what I'd do instead**

Hi [name],

I agree the spinner is simple and consistent. The trouble is that our four actions don't take the same time and don't carry the same risk, so one blocking treatment is wrong for most of them. Here is the case.

**1. The actions fall into different wait categories**

| Action | Typical wait | What the customer needs |
|---|---|---|
| Save | Well under a second | Almost nothing. It shouldn't feel like an event. |
| Rename | Instant | The new name, shown right away. |
| Duplicate | About a second or less (assumed) | Confirmation that the click registered, then the copy. |
| Export PDF | Under 1 second to about 40 seconds | Progress, a way out, and a way to keep working. |

As a rule of thumb, anything under about a quarter second shouldn't flash a spinner. Up to roughly a second, people only need to see that their click registered. Past about 10 seconds they need real progress, a way to cancel, and ideally the freedom to do something else while they wait. Our actions span that whole range, and a full-screen spinner treats them all as the worst case.

**2. A full-screen spinner makes the fast actions feel slow**

Save and rename are tiny operations. If each one blacks out the editor, the customer sees a flash of blocking UI hundreds of times per session. It reads as "something heavy is happening" when nothing is. Save is the sharpest example. It should run continuously and quietly, and it should only be noticed if it fails.

**3. Forty seconds behind a blocking spinner is where we lose people**

A spinner with no progress, no cancel, and no escape for 40 seconds looks like a hang. The customer can't tell whether it's working, and they can't back out if they clicked export by mistake or on the wrong size. They can't touch the design either, so they may reload and lose the export. A poster customer who has just finished designing is at their most invested, and this is the moment we'd be making them nervous.

**4. What I'd propose**

- **Save:** Make it automatic and silent. Show a small "Saved" / "Saving…" indicator in the editor chrome. Only a failure gets attention, and it stays visible until resolved. No success popup.
- **Rename:** Edit in place and update immediately. No spinner. If the save fails, revert and say so next to the field.
- **Duplicate:** Show a brief busy state on the button or the new item's placeholder. If it takes longer than a second, show a skeleton of the copy. The editor stays usable.
- **Export:** Treat it as a background job.
  - Show a progress indicator in place. Use a determinate bar if we can estimate size or page count, otherwise a clear step label such as "Rendering…" or "Preparing PDF…".
  - Include a Cancel button.
  - Let the customer keep editing while it runs.
  - When it's done, show a toast with a Download action, and keep a visible "Export ready" state in the UI in case they miss it.
  - If it fails, say so plainly and offer Retry.
  - Disable only the export button while it runs, and say why, to prevent double submits.
  - If the PDF is based on the design at the moment they clicked, tell them that, so edits made during the export aren't a surprise.

**5. Where I'm making assumptions**

I don't have timing data per action, so the numbers above for save, rename, and duplicate are assumptions. Can we pull real p50 and p95 durations from our logs, especially for export by poster size? That would tell us where the thresholds really sit, and whether we can show determinate progress or only an indeterminate state.

**6. Scope**

This doesn't need a redesign of the editor. The big change is export becoming a non-blocking job with progress and cancel. The rest is mostly removing the spinner from actions that don't need one. If you'd like, we can ship export first, since that's where the pain is, and then clear out the spinner from the other three.

Happy to talk it through. If you have a case where a blocking spinner is the right call (for example, a step where the document must not change), I'd like to hear it and we can handle that case specifically.

Thanks,
[your name]

---

I used placeholders for names and left the three short-action durations marked as assumptions rather than inventing figures. If you have real timing data, drop it into section 1 and the message gets stronger.
