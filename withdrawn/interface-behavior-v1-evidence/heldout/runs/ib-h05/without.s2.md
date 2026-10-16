**Subject: Loading states in the editor: why one spinner doesn't fit every action**

Hey,

I agree that every one of these actions is loading something. The trouble is that they differ in how long they take and in what the user is doing while they wait. Those two things should decide what we show.

**What's wrong with the full-screen spinner**

1. **It's too heavy for fast actions.** Save, rename, and duplicate usually finish in well under a second. A full-screen overlay for a 300ms operation produces a flash that reads as lag or flicker, and it makes the app feel slower than it is.
2. **It blocks work the user could keep doing.** If someone is designing a poster and hits save, they shouldn't lose the canvas. The same goes for a rename. Blocking the whole editor tells them they can't touch anything, and for most of these actions that isn't true.
3. **It gives no information on the slow action.** Export can take up to 40 seconds. A spinner with no progress, no explanation, and no way out looks the same at second 3 as at second 35, and people assume it's hung. They refresh, close the tab, or click export again, and then we have duplicate jobs or lost work. The export is also the step that ends in a purchase or a print order, so it's the one where anxiety costs us the most.

**What I'd propose**

Pick the pattern by expected duration and by whether the action needs to block the editor.

| Action | Typical time | Pattern |
|---|---|---|
| Rename | Instant | Update the UI immediately (optimistic). Show an inline error only if it fails. |
| Save | Under 1s | A small non-blocking status near the title: "Saving…" then "Saved". The user keeps working. |
| Duplicate | ~1s | Show a placeholder or skeleton of the new item and a spinner on the button. Don't block the canvas. |
| Export PDF | 1–40s | A dedicated progress experience, described below. |

**For export specifically**

- Disable the Export button as soon as it's clicked, so no one starts a second job by accident.
- Wait about 300–500ms before showing anything. Fast exports then finish with no flash at all.
- If it runs longer, show a panel or modal for that one action. It should say what's happening ("Preparing your print-ready PDF…"). Show real progress if the backend can report it. If it can't, use staged messages ("Rendering… Embedding fonts… Finalizing…") and not a bare spinner.
- Give a rough time expectation on large posters, e.g. "This can take up to a minute for large sizes."
- Allow Cancel.
- Let the user keep editing, or at least close the panel, while the export runs. When it's done, notify them with a download button.
- Handle failure explicitly, with a clear message and a Retry button, so they aren't left in a stuck state.

**Rule of thumb**

- Under about 1 second: no blocking UI, only subtle inline feedback.
- 1–10 seconds: a visible indicator tied to the thing being acted on.
- Over 10 seconds: show progress, set expectations, and let the user cancel or leave.

A full-screen spinner is occasionally right, for example while the app first loads or during an action that really does lock all state. It shouldn't be the default for everything.

This also costs little. Most of it is a small shared loading-state component that takes a variant (inline, button, or progress panel), plus a delay threshold. The export panel is the only real new piece, and it's the one that will make the biggest difference to customers.

Happy to sketch the states or pair on the component if that helps.

Thanks,
[Your name]

---

Two notes. I haven't seen your codebase or backend, so the progress-reporting and cancel suggestions assume export runs as a job you can poll or cancel. If it's a single blocking request, the staged messages and a "keep working while it runs" approach are the realistic first step. The timing figures are common UX guidelines, so adjust them if you have your own measurements.
