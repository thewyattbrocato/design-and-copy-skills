The spec is mostly sound. Immediate capture, no save step, in-place state, undo instead of a confirm on delete, and a single specific confirm on submit all fit reps working one-handed. I found three real problems and one smaller gap, and fixed them in the revised text below.

**What I changed**
1. **Item 1 conflicts with item 7.** In multi-page mode, "one photo saves a draft" would create one draft per page. I added a Done step for multi-page, so the pages become one draft.
2. **Item 3 leaves out states.** Item 4 introduces "Waiting for signal", but item 3 lists only three states. Nothing says what a draft shows when it is uploading and also missing details. Nothing covers an upload that fails for a reason other than signal. I made one list and gave it an order.
3. **Item 2 never says where the merchant comes from.** The category default depends on the merchant, but only amount and date are read from the photo. I added merchant to the fields read. I also stated that the read happens on the phone, because it has to work offline.
4. **Item 6 doesn't say what happens to drafts that aren't ready.** I added a rule so the "7 expenses" count is clear. I put it in the revised text, but you may want to confirm it.

**Revised spec**

**Receipt capture**

Who and how often: field sales reps, a few receipts a day, usually standing in a parking lot with one hand free. Speed matters more than completeness at capture; the full detail can be filled in later.

1. Tapping Capture opens the camera immediately. In single mode, one photo saves a draft expense right away; there is no save step.
2. The draft is pre-filled on the phone, so it works offline. Merchant, amount and date are read from the photo when legible. Category is set to the rep's most recent category for that merchant, or left blank for a new or unreadable merchant. Currency is set to the rep's home currency.
3. Each draft shows its state on its own row, and the state changes in place. Reps never have to open a draft to find out whether it went through. One state shows at a time, in this order of precedence:
   - **Waiting for signal:** the photo is on the phone and not yet uploaded.
   - **Uploading.**
   - **Upload failed. Retry:** shown for failures that aren't a lack of signal. The app also retries on its own.
   - **Needs details:** the upload is done, but the amount or category is missing.
   - **Ready.**

   Details can be filled in while a draft is waiting or uploading, so a missing amount or category is also flagged on the row beside the upload state.
4. If there is no signal, the photo is kept on the phone and uploads on its own when the connection returns. Nothing is lost if the app is closed.
5. Deleting a draft removes it at once and shows "Draft deleted. Undo" for 10 seconds. The message is announced to screen readers. After that the draft moves to a Recently deleted list that keeps it for a month. There is no confirmation dialog.
6. Submitting a report to a manager is the one step that does ask. The sheet shows the total, the number of expenses and the manager's name, and the button reads "Submit 7 expenses to Dana". Drafts that aren't Ready are left out and listed on the sheet as "2 need details", with a link to fix them. After submitting, reps can recall the report until the manager opens it.
7. A rep can switch the camera between single receipt and multi-page receipt. The current mode is shown on the capture screen and resets to single when the camera closes. In multi-page mode, each photo adds a page and a visible Done button saves all the pages as one draft. Closing the camera before Done still saves the pages taken so far as a draft, so nothing is lost.

**Check before Monday:** I assumed that unready drafts are excluded from a submission rather than blocking it. If your policy is that a report can't go out with incomplete expenses, change item 6 to say so.
