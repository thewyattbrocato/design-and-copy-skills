**Assumption:** one-handed phone use, frequent, short sessions.

- **Delete:** When a note is deleted, remove it at once with no confirmation. Show a bottom toast, "Note deleted · Undo", for 8 s (placeholder). Reversible actions don't need a confirmation.
- **Undo:** Tapping Undo restores the note to its original position and content, and the toast then disappears. Swiping or navigating away must not dismiss the toast early.
- **Trash:** After the toast expires, the note moves to Trash. Retention is a placeholder of N days. Trash offers Restore and, as the only confirmed step, "Delete forever", which names the note.
- **Bulk delete:** One toast, "3 notes deleted · Undo", restores all of them.
- **Accessibility:** Announce the toast through a polite live region. Make the time limit extendable. Provide a non-gesture route to Undo.
- **Offline:** Deletion and undo work offline and sync later.
