I'd split it into three short steps, and make the last one resumable so it doesn't have to be finished in one sitting. People abandon at the fields that need a document or a bank detail they don't have on hand, so I'd keep those out of the first sitting.

**Step 1 of 3: About your business** (easy facts, and creates the account)
- Legal business name
- Trading name (optional, with a hint: "If different from your legal name")
- Contact name (one field)
- Email (`autocomplete="email"`, no auto-capitalize or spellcheck)
- Phone, with the reason printed beside it, such as "So we can reach you about orders." If you can't name a use, drop it. Use `type="tel"` and accept spaces and dashes.

Button: **Continue**. Creating the account here means vendors who leave can pick up where they stopped, and you have their email to follow up.

**Step 2 of 3: What you cook** (the fun part, and it's what the marketplace shows)
- Cuisines: checkboxes if the list is short, or a searchable multi-select if it's long.
- Delivery distance: one control with the unit shown, such as radios for a few preset ranges or a stepper that stops at your maximum. Don't use a free-text number.
- Business address: street, then postal code, with city and state filled in from the postal code but still editable. Use the standard address autofill tokens, and make the postal code field short.

**Step 3 of 3: Get paid and get verified** (the hard stuff, last)
- Tax ID
- Bank account name, routing number, account number. Use `inputmode="numeric"` on a text input, not a number spinner. Run a routing-number checksum and say what's wrong in words. State how the data is protected, as a plain sentence beside the fields.
- Food handler permit and insurance certificate. Accept a phone photo or PDF, show the filename after upload, and allow replacing it.
- One unchecked checkbox for the terms, with the link inline: "I agree to the Vendor Terms."

Then a review screen with edit links, since this involves bank details. The submit button should say **Submit application**, not "Submit".

**Questions that could cut this further:**
1. **Do the tax ID, bank details and uploads need to be collected before approval?** If they only gate the first payout or going live, I'd move them out of sign-up entirely. Vendors would finish steps 1 and 2 (about 10 fields), then see a "Finish setup to start getting orders" checklist. That change would probably cut abandonment the most. The permit may be a safety or legal requirement before listing, so that's your call.
2. **Are you collecting the phone number and trading name for a reason?** If not, drop the phone and keep the trading name optional.

**Details that help completion:**
- Put the step in the heading ("Your business, step 1 of 3"), not in unnamed dots.
- Check on submit, not while typing. Once a field has shown an error, re-check it live. Keep the button pressable.
- Show a summary of problems at the top with links to each field, and keep everything typed after any error.
- Mark the optional fields in words, and don't use asterisks.
- Keep Back and answers persistent. Use 16px text and 44px touch targets, since many caterers will do this from a phone, with the permit photo taken on the phone.
