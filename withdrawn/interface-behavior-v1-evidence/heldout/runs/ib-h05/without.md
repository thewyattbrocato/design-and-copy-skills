**Subject: Why one full-screen spinner for every action isn't enough**

Hey,

"Loading is loading" is true in one sense: the system is busy. But the user doesn't care that it's busy. They care about three things: *Is it working? How long will it take? Can I keep doing something else?* The answers differ a lot across our actions, so one identical full-screen spinner gets most of them wrong.

**The problem with the current approach**

1. **It blocks work that doesn't need blocking.** A full-screen spinner locks the editor. For save, rename, and duplicate, that's overkill. The user should be able to keep designing.
2. **It makes fast actions feel slow.** If a rename takes 200ms, a full-screen overlay flashes on and off. That reads as jank, and it's slower-feeling than the action really is.
3. **It gives no information on the slow one.** Export can run up to ~40 seconds. A spinner with no progress or estimate for that long looks like a hang. People will refresh, close the tab, or click Export again, and we lose the export (or run it twice).
4. **It treats different risks the same.** Losing a save is a serious problem. A slow duplicate is not. They need different feedback.

**What I'd propose, by action**

| Action | Typical time | Treatment |
|---|---|---|
| Rename | Instant | Optimistic update. Change the name immediately and reconcile in the background. Show an error only if it fails. |
| Save | Short | Non-blocking status in the toolbar: "Saving…" → "Saved". No overlay. Keep the editor usable. |
| Duplicate | Short to moderate | Inline indicator on the button, or a placeholder card in the list that fills in when done. Don't block the editor. |
| Export PDF | <1s to ~40s | Treat as a background job (see below). |

**Export deserves its own design**

Because its duration varies so much, I'd handle it in tiers:

- **Under about 1 second:** show nothing special, or a quick button state change. Delay any indicator ~300–500ms so fast exports never flash one.
- **Longer:** show a non-modal progress indicator (a toast or a panel) with the file name and, if we can compute it, a real progress bar. If we can't get true progress, use stage labels ("Preparing… Rendering… Finalizing…") rather than a bare spinner. Even fake-ish stages tell the user it's moving.
- **Let them keep working.** Run it in the background, disable only the Export button for that poster to prevent duplicate runs, and let the user keep editing or leave the page with a clear warning if leaving would cancel it.
- **On completion:** notify them clearly ("Your PDF is ready" with a Download button). If they've switched tabs, a browser notification or an email for long jobs is worth considering.
- **On failure:** say what happened and offer Retry. Don't just drop the spinner.
- **Offer cancel** for long exports.

**A simple rule of thumb**

- Under ~1s: no indicator, or just a subtle one.
- 1–10s: an indicator that's visible but doesn't block.
- Over 10s: show progress, allow multitasking, and notify on completion.

Full-screen blocking should be reserved for the rare case where continuing to edit would actually corrupt something, and none of these four actions seems to be that.

**Why it's worth doing**

Export is the moment the customer is turning a design into a purchase or a physical product. It's the highest-stakes step in the flow, and it's the one where our current UI looks most broken. Better feedback should cut abandoned exports, double-clicks, and support tickets, and it will make the editor feel faster without changing any backend performance.

I'm happy to sketch the states for each of these, or we can start with just the export flow, since that's where the biggest gain is.

Thanks,
[Your name]

---

A few notes: I assumed the editor runs in a browser and that export is something we can run asynchronously. If either is wrong, or if the backend can't report real progress, tell me and I'll adjust those parts. I also don't know your actual save and duplicate timings, so check the table against real numbers before you send it.
