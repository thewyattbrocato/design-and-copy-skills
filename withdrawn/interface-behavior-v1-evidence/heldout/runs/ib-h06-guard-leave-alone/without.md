I found two real problems and a few gaps. Below are the corrected spec and a list of what I changed.

## Corrected spec

**Receipt capture**

Who and how often: field sales reps, a few receipts a day, usually standing in a parking lot with one hand free. Speed matters more than completeness at capture; the full detail can be filled in later.

1. Tapping Capture opens the camera immediately. The first photo saves a draft expense right away; there is no save step. In multi-page mode (see 7), the first photo creates the draft and each further photo adds a page to that same draft. The camera stays open until the rep closes it.
2. The draft is pre-filled where possible. Amount, date and merchant are read from the photo when legible. Category is set to the rep's most recent category for that merchant, or left blank for a new or unreadable merchant. Currency is set to the rep's home currency.
3. Each draft shows its state on its own row: Uploading, Waiting for signal, Upload failed, Needs details (amount or category missing), or Ready. The state changes in place. Reps never have to open a draft to find out whether it went through.
   - Upload state takes precedence. A draft shows Needs details or Ready only once its upload has finished.
   - A draft that is still missing details when it finishes uploading shows Needs details.
4. If there is no signal, the photo is kept on the phone and the row shows "Waiting for signal". It uploads on its own when the connection returns. Nothing is lost if the app is closed. If an upload fails for any other reason, the row shows "Upload failed". The app retries automatically, and the rep can also tap the row to retry.
5. Deleting a draft removes it at once and shows "Draft deleted. Undo" for 10 seconds. After that it moves to a Recently deleted list that keeps it for 30 days. There is no confirmation dialog.
6. Submitting a report to a manager is the one step that does ask: the sheet shows the total, the number of expenses and the manager's name, and the button reads "Submit 7 expenses to Dana" (singular: "Submit 1 expense to Dana"). After submitting, reps can recall the report until the manager opens it.
   - **[Decision needed]** Drafts in Needs details, Uploading or Waiting for signal are excluded from the report and not counted. The sheet says how many were left out.
7. A rep can switch the camera between single receipt and multi-page receipt. The current mode is shown on the capture screen and resets to single when the camera closes.

## What I changed

- **Contradiction between 1 and 7.** "One photo saves a draft" can't hold in multi-page mode. I made the first photo create the draft and later photos append to it. This keeps the "no save step" rule. If you'd rather have an explicit Done step that creates the draft, say so, because engineers will build something different.
- **State list in 3 was incomplete.** Item 4 introduces "Waiting for signal", but item 3 didn't list it. I added it. I also added "Upload failed", because without it the promise that reps never have to open a draft can't hold when an upload errors. I added a precedence rule for the case where a draft is both uploading and missing details.
- **Merchant in 2.** The category lookup depends on knowing the merchant, but the spec never said it's read from the photo. I added that, plus a fallback to blank when it can't be read.
- **"A month" in 5.** I changed it to 30 days so engineers and QA test the same thing.
- **Singular button text in 6.** I added "Submit 1 expense".

## Open question

I flagged the one thing I couldn't decide for you: whether unfinished drafts can be submitted (item 6). I assumed they can't. Please confirm or correct that before you send the spec.
