Here's a draft you can send:

---

**Subject: Replacing the full-screen spinner in the editor**

Hey,

You're right that these are all waiting states. The problem is that the right feedback depends on two things: how long the wait is, and whether the user has to wait at all. Our four actions differ a lot on both.

A full-screen spinner says "stop, you can't do anything until this finishes." That's the right message for almost none of our actions. It also has two specific costs:

- **Fast actions feel slow.** A full-screen flash for a sub-second save or rename makes the app feel heavier than it is.
- **Long actions feel broken.** In a 40-second export, a spinner with no progress, no cancel, and no end in sight looks like a hang. People will refresh and lose the export, or file a support ticket.

**What I'd propose**

| Action | Blocks the user? | Feedback |
|---|---|---|
| **Save** | No | Small inline status near the title ("Saving…" → "Saved"). Ideally autosave. Show an error only if it fails. |
| **Rename** | No | Update the name immediately (optimistic), save in the background, and revert with an error message if it fails. |
| **Duplicate** | No | Show the new item right away in a pending state (skeleton or "Copying…"). Swap it for the real one when it's ready. |
| **Export PDF** | No, but it's the one that needs real UI | See below. |

**Export**

- Don't show anything for the first ~300–500ms. Most small posters finish in that time, and a flash of UI is worse than none.
- After that, show a non-blocking progress indicator, either a panel or the export button turning into a progress state. The user can keep working or leave the editor.
- Use real progress if we can get it (page or stage based). If we can't, show stage labels like "Rendering → Embedding fonts → Finalizing" instead of an endless spinner. Even rough stages make a long wait feel shorter.
- Let them cancel.
- Export a snapshot of the design taken when they clicked, so edits made during the export don't affect the file.
- When it finishes, give a clear completion signal with a download button (a toast, plus a notification if the tab isn't focused).
- If it fails, say so and offer a retry. Don't fail silently.

**Where a block is still OK**

If there's a case where the user truly can't continue (for example, the first load of a design), a blocking state is fine there. It should be the exception we pick on purpose, not the default for every action.

**Suggested rollout**

1. Make save and rename non-blocking. This is the cheapest change and gives the biggest "feels faster" win.
2. Do duplicate next.
3. Build the export progress experience last. It's the most work, and it's the one customers will notice most.

Happy to talk through any of it. If there's a technical reason one of these has to block (for example, the backend can't take edits mid-export), I'd like to know, since that would change the export design.

---

If you tell me more about the stack, such as whether the backend can report export progress, I can tighten the export section to match.
