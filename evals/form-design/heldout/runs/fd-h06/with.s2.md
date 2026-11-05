I'd split it into short steps, and move the payout details and documents out of the critical path. The goal is to get vendors to "account created" quickly and collect the rest while they have a reason to.

**Step 1 of 4: Your business** (creates the account)
- Legal business name
- Trading name (optional, with the hint "If different from your legal name")
- Contact name (one field)
- Email (this is their login)
- Phone, with the reason printed beside it, such as "So we can reach you about an order." Only keep it if you have a real use for it.

**Step 2 of 4: Location and menu**
- Business address: street, postal code, city, state. Use address autocomplete with the standard autofill tokens, and let the postal code fill in city and state where it can.
- Delivery distance: a stepper or a few radios, in miles or km based on locale.
- Cuisines: checkboxes (square means pick many). Use a searchable list if there are more than about 10.

**Step 3 of 4: Documents**
- Food handler permit upload
- Insurance certificate upload
- Say the accepted formats and size limit beside each one (use your real limits, not a guess). Allow phone camera capture.
- Add an "I'll upload this later" option, and save their progress. People often don't have the files at hand, and that's a common point where they quit.

**Step 4 of 4: Review and agree**
- Show a summary with an edit link per section.
- One terms checkbox, with a link to the terms.
- A button that says **Create vendor account**.

**Move to after sign-up: tax ID and bank details** (bank account name, routing number, account number)
- You only need these when you first pay the vendor. Asking for them up front is the most sensitive ask and the likeliest reason people leave.
- Put them in a "Set up payouts" checklist on the vendor dashboard, with the reason stated: "Needed to pay you for orders."
- Prefill the bank account name from the legal business name.
- Use text inputs with numeric keyboards (not spin-button number inputs). Accept spaces and dashes and strip them in code.

**Mechanics that cut abandonment**
- Show the step in the heading ("Location and menu, step 2 of 4"). Back keeps all answers, and the form resumes on reload or return via a saved draft.
- Only mark the optional fields, in words.
- Check fields on submit, not while people are typing. Once a field has an error, re-check it as they edit. Keep the button pressable, show errors at the field with a summary at the top, and keep everything they typed.
- Run the same checks on the server.
- The confirmation should say what happens next, such as how approval works and how long it takes. Fill in the real timeline, and I haven't assumed one.

**Two checks for you**
- Is the tax ID legally needed before approval? If it is, put it in step 1 or the documents step instead of deferring it.
- Your list actually totals 18 items, not 17. It's worth confirming whether one of them is already covered elsewhere.
