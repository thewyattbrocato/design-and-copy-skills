Here's a draft you can send:

---

**Subject: Why one spinner for every editor action isn't enough**

Hey, I see the argument for "loading is loading." One component is simple, and it's consistent. But the actions behind it aren't the same, and a full-screen spinner treats them as if they were.

**Where it goes wrong**

- **Save, rename and duplicate are usually quick.** A full-screen block for something that takes a moment makes the editor feel slower than it is. It also flashes on and off. Under about a quarter second, people shouldn't see a spinner at all.
- **Export can run up to 40 seconds.** A spinner with no progress, no end point and no way out looks the same as a hang. People will reload, click Export again, or close the tab, and they may lose work. Customers are about to send a design to print, so they have a lot riding on it.
- **The full-screen block locks the whole editor** even though none of these actions need that. For export, the customer can't tweak the design, and they can't leave the page to check something. They're stuck watching.

**What I'd do instead**

Treat waits by how long they take, using these as starting values to tune:

| Action | Behavior |
|---|---|
| Save | Autosave quietly. Show a small "Saving… / Saved" indicator in the toolbar, and surface a message only if it fails. |
| Rename | Update it in place right away and sync in the background. Show an error only if it fails. |
| Duplicate | The new item appears with an inline pending state, such as a placeholder card. The rest of the editor stays usable. |
| Export | Runs in the background. The editor stays editable. |

For export specifically:
- Show a progress indicator near the Export button (or a small panel) with steps or a bar, rather than a spinner. If we can't estimate time, show named stages like "Preparing → Rendering → Finalizing".
- Add a Cancel button.
- Disable the Export button while a job is running, and say why, so double-clicks don't start duplicate jobs.
- When it finishes, give a persistent Download action. A toast with a Download link is fine, as long as the file is also reachable afterward.
- If the customer edits during export, say clearly that the file reflects the design as of when they clicked Export.
- On failure, keep the message visible with a Retry button.

The rule underneath: normal success stays quiet, long waits show progress and can be cancelled, and failures stay visible until the customer notices them.

**What stays shared**

We can still keep one loading system. It would have a few variants (inline indicator, button state, progress panel) behind one API, so the code stays consistent and the experience matches what's actually happening.

**Open questions for you**

- Can the export job report real progress, or only start and finish?
- Does export already run server-side as an async job, or does the request block until it's done?
- What should happen if the customer closes the tab mid-export?

Happy to talk through it. The export flow is the one I care most about, since that's the 40-second case.

---

I don't know your stack, so I left the technical details as questions. If you tell me how export works today, I can make the proposal more specific.
