**Assumption:** phone users, daily use, one-handed. Retention values are placeholders.

1. **Delete:** When a note is deleted, remove it at once with no confirmation, because it's recoverable.
2. **Undo toast:** Show "Note deleted · Undo" at the bottom for about 8 s (placeholder). Announce it to screen readers and pause the timer while it has focus. Undo restores the note to its original position with its content, tags and attachments.
3. **Trash:** Deleted notes go to Trash and are kept for N days (placeholder). Trash shows days remaining and offers Restore. Permanent delete lives only there.
4. **Empty Trash:** This is the single confirmation, because it can't be undone. Name the count: "Permanently delete 12 notes?"
5. **Bulk delete:** Treat it as one undo action: "12 notes deleted · Undo".
6. **Sync:** The delete syncs as a soft-delete flag, so restoring on one device restores it on all. Offline deletes queue and sync later.
7. **Multiple deletes:** A new toast replaces the old one, but earlier notes stay in Trash.
