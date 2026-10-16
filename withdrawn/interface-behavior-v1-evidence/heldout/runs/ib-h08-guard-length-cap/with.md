**Assumption:** Phone users, frequent short sessions, deleting one note at a time or a few at once.

**Delete spec**

- **Delete is immediate, with no confirmation dialog.** A note is recoverable, so asking first only adds friction.
- **Show an Undo toast right away.** It reads "Note deleted · Undo" and stays about 8 seconds (placeholder, tune in testing). Tapping Undo restores the note to its original position and folder with its content intact. The toast is announced to screen readers and its timer can be extended.
- **Soft-delete into Recently Deleted.** Notes stay there for a retention period (placeholder, e.g. N days). Users can restore a note or delete it permanently from there. Permanent deletion is the only action that needs a specific confirmation, and it names the note.
- **Bulk delete works the same way.** The toast says "3 notes deleted · Undo" and restores all three in one tap.
- **Undo survives navigation.** Leaving the screen doesn't cancel it. Starting a new delete replaces the toast, and the earlier note stays in Recently Deleted.
- **Sync deletions as tombstones.** Restoring on one device restores the note on all of them.
