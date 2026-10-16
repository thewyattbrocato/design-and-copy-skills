**Undo for note deletion in Reedbed**

- **Soft delete first.** Deleting sets `deleted_at` and hides the note. Nothing is purged yet.
- **Snackbar.** Show "Note deleted · Undo" for about 8 seconds. Tapping Undo clears `deleted_at` and restores the note to its original position.
- **Trash.** Deleted notes stay in Trash for 30 days, so undo still works after the snackbar is gone. A background job purges them after that.
- **Batch delete.** One snackbar and one undo for the whole batch.
- **Sync.** `deleted_at` syncs like any other field. Undo wins if it is the latest write.
- **Permanent delete.** This is only available from Trash and needs confirmation. It cannot be undone.
