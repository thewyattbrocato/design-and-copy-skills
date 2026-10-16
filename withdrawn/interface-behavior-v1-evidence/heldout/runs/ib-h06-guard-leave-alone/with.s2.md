I found four things to fix. The rest holds up: no save step, in-place state, undo instead of a confirm dialog, and a single deliberate confirmation at submit.

**What I changed**
1. **Item 1 vs item 7 conflict.** "One photo saves a draft right away" contradicts multi-page mode, because the first page would save a draft before the rest are shot. Multi-page now saves one draft when the rep taps Done, and the pages are kept if the camera closes before that.
2. **Item 3 vs item 4 mismatch.** "Waiting for signal" shows on the row but isn't in the list of states. I added it. I also added a failed-upload state, since a row that silently stays "Uploading" would break the "never open a draft to find out" promise.
3. **Item 5 recovery gap.** It read as if the draft only reaches Recently deleted after the 10 seconds. It should go there immediately, with the toast as a shortcut. I also covered a draft deleted while still queued for upload, and made the toast readable by screen readers.
4. **Item 6 hole.** The spec didn't say what happens to drafts that are still "Needs details" when the rep submits. I made the sheet leave them out and say so, so the rep doesn't have to fix them mid-submit.

**Revised spec**

**Receipt capture**

Who and how often: field sales reps, a few receipts a day, usually standing in a parking lot with one hand free. Speed matters more than completeness at capture; the full detail can be filled in later.

1. Tapping Capture opens the camera immediately. In single mode, one photo saves a draft expense right away; there is no save step. In multi-page mode (see 7), the rep taps Done after the last page and the pages save as one draft. If the camera closes before Done, the pages already taken are kept as a draft rather than discarded.
2. The draft is pre-filled: amount and date read from the photo when legible, category set to the rep's most recent category for that merchant (or blank for a new merchant), currency set to the rep's home currency. Every pre-filled value can be edited later.
3. Each draft shows its state on its own row: Uploading, Waiting for signal, Upload failed (with a Retry button on the row), Needs details (amount or category missing), or Ready. The state changes in place. Reps never have to open a draft to find out whether it went through. If a draft is both uploading and missing details, the row shows the upload state first and switches to Needs details once the upload finishes.
4. If there is no signal, the photo is kept on the phone and the row shows "Waiting for signal". It uploads on its own when the connection returns, and retries automatically after a failure before showing "Upload failed". Nothing is lost if the app is closed.
5. Deleting a draft removes it from the list at once and puts it in Recently deleted immediately. A "Draft deleted. Undo" message shows for 10 seconds and is announced to screen readers. Undo is also available from Recently deleted, which keeps drafts for a month. There is no confirmation dialog. Deleting a draft that hasn't uploaded yet cancels its pending upload, and Undo restores it to the queue.
6. Submitting a report to a manager is the one step that does ask. The sheet shows the total, the number of expenses and the manager's name, and the button reads "Submit 7 expenses to Dana". Only Ready expenses are included. Drafts that still need details stay out of the report, and the sheet says how many ("2 drafts need details and won't be included") with a link to them. After submitting, reps can recall the report until the manager opens it.
7. A rep can switch the camera between single receipt and multi-page receipt. The current mode is shown on the capture screen, and the mode resets to single when the camera closes.

One thing I left alone, since it's your call. Item 2 sets currency to the home currency, which will be wrong for reps who travel. If that happens, you could read the currency from the receipt when it's legible, the same way as amount and date.
