I found three real problems and a few smaller gaps. Here is the corrected spec, with the changes listed after it.

**Receipt capture**

Who and how often: field sales reps, a few receipts a day, usually standing in a parking lot with one hand free. Speed matters more than completeness at capture; the full detail can be filled in later.

1. Tapping Capture opens the camera immediately. One photo saves a draft expense right away; there is no save step.
2. The draft is pre-filled. Merchant, amount and date are read from the photo when legible. If the date is unreadable, it defaults to the capture date. Category is the rep's most recent category for that merchant, or blank for a new merchant. Currency is the rep's home currency. Values the app filled in or guessed are marked as such on the draft, so reps can spot and correct them.
3. Each draft shows its state on its own row: Uploading, Waiting for signal, Needs details (amount or category missing), Upload failed (with a Retry action), or Ready. The state changes in place. Reps never have to open a draft to find out whether it went through.
4. If there is no signal, the photo is kept on the phone and the row shows "Waiting for signal". It uploads on its own when the connection returns. Nothing is lost if the app is closed.
5. Deleting a draft removes it at once and shows "Draft deleted. Undo" for 10 seconds. The message is announced to screen readers and stays until the time is up. After that the draft moves to a Recently deleted list that keeps it for a month and lets the rep restore it. There is no confirmation dialog.
6. Submitting a report to a manager is the one step that does ask: the sheet shows the total, the number of expenses and the manager's name, and the button reads "Submit 7 expenses to Dana". Drafts that still Need details are listed on the sheet with a link to fix each one, and they are not included in the count. After submitting, reps can recall the report until the manager opens it.
7. A rep can switch the camera between single receipt and multi-page receipt. The current mode is shown on the capture screen. In multi-page mode, the first photo still saves the draft immediately, and each further photo is added to that same draft. A visible "Done" button ends the receipt. The mode resets to single when the camera closes.

**What I changed and why**

- **Item 7 contradicted item 1.** "One photo saves a draft" can't hold in multi-page mode. I made the first page save the draft and later pages attach to it. Nothing is lost if the rep gets interrupted mid-receipt, and there is still no save step.
- **Item 3 left out a state that item 4 uses.** "Waiting for signal" wasn't in the list of states, so I added it. I also added "Upload failed" with Retry. Without it, a failed upload had no visible state, which breaks the promise that reps never need to open a draft to check.
- **Item 2 used merchant without reading it.** The category lookup depends on the merchant, but only amount and date were read from the photo. I added merchant and a fallback for an unreadable date. I also added a marker for guessed values so reps can see what was assumed.
- **Item 6 didn't say what happens to incomplete drafts.** The sheet now lists them and doesn't count them, instead of letting the rep submit them or failing silently.
- **Item 5 got one accessibility note.** The Undo message is announced to screen readers and isn't removed early.

Items 1, 4 and the confirmation in item 6 are fine as written. The confirmation is justified because the submission goes to another person, and the recall option covers the rest.

Open questions for engineering, since the spec doesn't say:
- How many upload retries happen before a row switches to "Upload failed"?
- Can a rep submit if a draft is still Uploading?
