**Undo for note deletion in Reedbed**

- **Soft delete:** Deleting sets `deleted_at` and hides the note. Nothing is purged yet.
- **Snackbar:** Show "Note deleted · Undo" for 8 seconds. Tapping Undo clears `deleted_at` and restores the note in its original position, with content, tags, and attachments intact.
- **Trash:** Keep deleted notes in a Trash view for 30 days. Users can restore from there. A background job purges expired notes.
- **Batch delete:** One snackbar and one undo for the whole batch.
- **Sync:** Sync `deleted_at` as a normal field, so undo works across devices. The latest timestamp wins.
- **Accessibility:** Announce the snackbar to screen readers. Keep it open while a screen reader is focused on it.
