**Undo for note deletion in Reedbed**

- **Soft delete first.** Deleting sets `deleted_at` and hides the note. Nothing is purged yet.
- **Snackbar.** Show "Note deleted · Undo" for 8 seconds. It persists across screen changes and is dismissed by a new delete or by timeout.
- **Undo action.** Clears `deleted_at`. The note returns with its original position, content, and metadata.
- **Trash.** After the snackbar, the note stays in Trash for 30 days and can be restored there. A background job purges it after that.
- **Sync.** Delete and restore are synced as timestamped operations, and the latest one wins.
- **Bulk delete.** One snackbar and one undo restore the whole batch.
- **Accessibility.** Announce the snackbar to screen readers.
