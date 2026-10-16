I found four real problems and a few smaller gaps. There's no file in the working directory, so the corrected text is below for you to paste.

**What was wrong**

1. **Items 1 and 7 contradict each other.** "One photo saves a draft" doesn't work in multi-page mode, where several photos make one expense. The spec also doesn't say when the camera closes, so "resets to single when the camera closes" can't be tested.
2. **Item 3 is missing states.** "Waiting for signal" (item 4) isn't in the list of states. A draft can also be uploading and missing an amount at once, and no rule says which state shows.
3. **Item 5 leaves a gap.** It says the draft is removed "at once" but only moves to Recently deleted after 10 seconds, so it's unclear where the draft is during those 10 seconds. "A month" is also vague. Deleting a draft that's still uploading is undefined.
4. **Item 6 doesn't say what happens to drafts that aren't Ready.** Engineers will have to guess whether Needs details drafts can be submitted. The button label also needs a singular form ("Submit 1 expense to Dana").

**Corrected spec**

**Receipt capture**

Who and how often: field sales reps, a few receipts a day, usually standing in a parking lot with one hand free. Speed matters more than completeness at capture; the full detail can be filled in later.

1. Tapping Capture opens the camera immediately. In single mode (the default), one photo saves a draft expense right away and closes the camera. There is no save step.
2. The draft is pre-filled:
   - Amount and date are read from the photo when legible.
   - Category is set to the rep's most recent category for that merchant, or left blank if the merchant is new or can't be read.
   - Currency is set to the rep's home currency.
3. Each draft shows its state on its own row, and the state changes in place. Reps never have to open a draft to find out whether it went through. If more than one state applies, the row shows the first match in this order:
   1. Waiting for signal (photo is stored on the phone, not yet uploaded)
   2. Uploading
   3. Needs details (amount or category missing)
   4. Ready
4. If there is no signal, the photo is kept on the phone and the row shows "Waiting for signal". It uploads on its own when the connection returns. Nothing is lost if the app is closed.
5. Deleting a draft hides it at once and shows "Draft deleted. Undo" for 10 seconds. It goes straight to the Recently deleted list, where it is kept for 30 days, so Undo is a shortcut for restoring it. There is no confirmation dialog. Deleting a draft that is uploading or waiting for signal cancels the upload.
6. Submitting a report to a manager is the one step that does ask.
   - The sheet shows the total, the number of expenses and the manager's name. The button reads "Submit 7 expenses to Dana", or "Submit 1 expense to Dana".
   - Only Ready expenses are included. If any drafts are Needs details, the sheet says how many are left out, and the rep can tap through to fix them.
   - After submitting, reps can recall the report until the manager opens it.
7. A rep can switch the camera between single receipt and multi-page receipt, and the current mode is shown on the capture screen.
   - In multi-page mode, each photo adds a page to the same draft, and the camera stays open until the rep taps Done. The draft is saved when they tap Done, or if the camera is closed after at least one page.
   - The mode resets to single whenever the camera closes.

**Decisions for you to confirm**

- **Item 6:** I assumed Needs details drafts are excluded from submission. If you'd rather block submission until they're fixed, change that line.
- **Item 7:** I assumed a multi-page draft saves when the camera closes. If you'd rather discard an unfinished set, that needs to be explicit.
- **Item 5:** I chose 30 days for "a month". Swap in whatever number you want.
