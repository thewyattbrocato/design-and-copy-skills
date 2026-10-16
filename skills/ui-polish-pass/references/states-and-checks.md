# States and checks

Walk each component through its row. Skip any state that cannot happen. A state is done when the person can tell what is going on and what to do next.

## States by component

- **Any control:** default, hover, keyboard focus (visible, distinct from hover), pressed, disabled (with a reason), busy (after press, before result). Pressing again while busy does nothing harmful.
- **List, table, feed:** loading (placeholder rows at final size; a reload keeps the old rows), empty (first use, no results, cleared), error (load failed: retry and keep stale data marked stale; one row failed: mark and retry that row), one item and many (paging or windowing, count stated), very long cells. After removing an item, focus lands on the next item or the list heading.
- **Form:** pristine, invalid (message beside the field, in words), submitting, failed (input kept; summary on top when several), success (what happened and what comes next, persistent), unsaved changes on leaving. A server rejection shows on its field. Offline or expired mid-entry keeps the draft.
- **Async action (save, send, pay, sync):** idle, working, done (outcome in words), failed (cause if known, retry), slow (progress and a cancel past about a second), cancelled, partly done. An optimistic update that fails rolls back visibly with a reason.
- **Upload and import:** idle, drag-over, validating (type, size), uploading (per-file progress, cancel), done, failed per file (reason, retry that file), partly failed (counts), removed (undo), no permission or quota.
- **Media:** loading (reserved space), failed (alt text or placeholder with retry), missing (designed fallback), odd sizes (fixed frame, crop), captions or transcripts for speech.
- **Navigation:** current place marked by more than color, a useful not-found with a way back, no access (say why and who can grant it), offline.
- **Dialogs, menus, toasts:** focus moves in, is contained for modals, Escape closes, close returns focus to the trigger. A toast confirms low-stakes success only, is readable and pausable, carries the undo, and is never the only record of a failure.
- **First run versus returning:** first run says what the thing is for and offers the first action, no tour; returning resumes where they left off.

## Thresholds and fast tests

- Keyboard only: every action reachable, order matches reading order, no trap, Escape closes overlays.
- Focus indicator at least 3:1 against its surroundings in every theme. Body text about 4.5:1; large text, meaningful icons and input borders about 3:1; recheck hover, disabled and text on images.
- Names say what the control does ("Delete task: Buy milk"), and inputs have real labels, not placeholders. Progress and success go in a polite live region; only a blocking failure is assertive.
- Targets at least about 24 CSS pixels with spacing, near 44 on touch; pad small icon buttons rather than enlarging the icon. Hover-only actions need a focus and touch path.
- Zoom to 200% text and 320 CSS pixels: no clipping, no two-way scrolling for text. Headings in order, landmarks for page regions, empty alt for decorative images. Timeouts warn and can be extended.
- Dark theme (only where one exists): layers raised by lightness, page off pure black and text off pure white, borders visible against both neighbors, saturated accents softened and button text contrast rechecked, bright images dimmed or framed, focus and error colors recomputed, forced-colors keeps borders and focus (real outlines, `currentColor` icons). Fix through theme variables.
- Text: longest realistic name, long unbroken strings, right-to-left, short labels that can double in translation. Containers: narrow columns, not only narrow pages. Check at the size it will really appear.
- Consistency: values come from the existing scale; replace a one-off with the nearest token. One primary action per decision; same action, same name, same place.

For full procedures: form-design, ui-motion, color-palette, typesetting, visual-hierarchy, spacing-and-grouping, responsive-layout, each if installed.
