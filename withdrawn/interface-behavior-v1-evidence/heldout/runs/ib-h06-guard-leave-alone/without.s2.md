I found three real inconsistencies and fixed them in the revised spec below. Two gaps need a decision from you before Monday.

**What I changed**
- **Item 3 vs. 4:** Item 4 adds a "Waiting for signal" state that item 3 doesn't list. I listed all four states in item 3 and gave them an order of precedence. Without that, engineers will have to guess what a row shows when the photo is uploading and also missing an amount.
- **Item 2:** The category comes from the merchant, but only amount and date are read from the photo. I added merchant to the fields read from the photo. I also said what happens offline, since the draft has to be created with no signal.
- **Item 1 vs. 7:** "One photo saves a draft" contradicts multi-page mode, where several photos make one receipt. I added the rule that in multi-page mode the draft saves when the rep taps Done.
- **Item 5:** I changed "a month" to 30 days so it can be tested.

**Revised spec**

**Receipt capture**

Who and how often: field sales reps, a few receipts a day, usually standing in a parking lot with one hand free. Speed matters more than completeness at capture; the full detail can be filled in later.

1. Tapping Capture opens the camera immediately. In single-receipt mode, one photo saves a draft expense right away; there is no save step. In multi-page mode, each photo adds a page, and the draft saves when the rep taps Done. Done sits within thumb reach.
2. The draft is pre-filled: merchant, amount and date read from the photo when legible. Category is set to the rep's most recent category for that merchant (blank for a new or unreadable merchant). Currency is set to the rep's home currency. Reading happens on the device so it works offline. If it can't, the fields stay blank and are filled in when the photo uploads.
3. Each draft shows its state on its own row, and the state changes in place. Reps never have to open a draft to find out whether it went through. States, in order of precedence:
   - **Waiting for signal:** the photo is on the phone and not yet uploaded.
   - **Uploading**
   - **Needs details:** amount or category is missing.
   - **Ready**
4. If there is no signal, the photo is kept on the phone and the row shows "Waiting for signal". It uploads on its own when the connection returns. Nothing is lost if the app is closed.
5. Deleting a draft removes it at once and shows "Draft deleted. Undo" for 10 seconds. After that it moves to a Recently deleted list that keeps it for 30 days. There is no confirmation dialog.
6. Submitting a report to a manager is the one step that does ask: the sheet shows the total, the number of expenses and the manager's name, and the button reads "Submit 7 expenses to Dana". After submitting, reps can recall the report until the manager opens it.
7. A rep can switch the camera between single receipt and multi-page receipt. The current mode is shown on the capture screen and resets to single when the camera closes.

**Decisions for you**
- **Submitting with incomplete drafts:** The spec doesn't say what happens if a report includes drafts that are Needs details, Uploading or Waiting for signal. I'd block submit and show the count of drafts that aren't Ready, with a shortcut to them. That's your call, but engineers will hit it immediately.
- **Closing the camera mid-way through a multi-page receipt:** Should the pages save as a draft or be discarded? Given "nothing is lost," I'd save them.
