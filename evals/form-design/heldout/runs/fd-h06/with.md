I'd split it into short steps with saved progress, and move the hard-to-gather items (documents and bank details) to the end. 17 fields on one page reads as a chore. Four small steps with the easy ones first feel much shorter.

**Step 1 of 4: About your business** (easy facts, and it gets you an email address)
- Legal business name
- Trading name, marked *optional*, with the hint "If different from your legal name"
- Contact person's full name (one field)
- Email (`autocomplete="email"`)
- Phone, with the reason printed beside it, such as "So we can reach you about orders." If you can't give a reason, drop the field.

Create the draft application when they continue from this step. Then you can email a "pick up where you left off" link to anyone who stops, which probably recovers more abandoners than any layout change.

**Step 2 of 4: What you offer**
- Cuisines: checkboxes, or a multi-select with search if the list is long
- Delivery distance: a stepper or a few radios in miles or km, with the unit shown
- Business address: street, postal code, city, state. Use address autofill tokens and a short postal field. If you can look up city and state from the postal code, fill them in automatically.

**Step 3 of 4: Verification**
- Tax ID: `inputmode="numeric"`, accepting dashes and spaces and normalizing them in code
- Food handler permit upload
- Insurance certificate upload

Say which file types and sizes are accepted, and let phones use the camera. Uploads are where most people stall, because they have to go find the files. Add an "I'll upload this later" option, and show "Documents needed" on their dashboard until they do.

**Step 4 of 4: Payouts and review**
- Bank account name, prefilled from the legal business name and editable
- Routing number and account number: text inputs with numeric keyboards, not spinner number inputs. Check the routing number's length and checksum on submit. Add one line about how the data is protected.
- A summary of all answers, each section with an "Edit" link
- Terms checkbox: "I agree to the [Terms]"
- A button that reads **Submit application**

**Throughout**
- Put the step in the heading ("Verification, step 3 of 4"). Back keeps all answers.
- Put visible labels above the fields. Mark only the optional ones. Validate on submit, with a clear message at each field. Never clear what the person typed.
- The confirmation should say what happens next, such as "We review applications within [X days]", and what to do if they hear nothing. I haven't filled in the timeline for you.

**Two things to decide**
- **Further deferral:** If your compliance rules allow it, you could ask for the bank details and tax ID only after approval, before the first payout. That would cut the application to about 11 fields. Do you need all of it before approval?
- **Measuring it:** Track drop-off per step. My guess is that step 3 will lose the most people, and the data will show whether to defer more.
