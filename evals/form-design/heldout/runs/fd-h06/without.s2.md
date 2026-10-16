I'd split it into short steps, and move the effortful items (bank details, document uploads) out of the first-time path.

**Step 1: Create the account (about 3 fields)**
- Contact name, email, phone
- Optionally a password, or a magic link
- Create the account here and save the draft. Anyone who drops off later can get a "finish your application" email, which is usually your best recovery tool.

**Step 2: About your business (about 5 fields)**
- Legal business name, trading name (with a "same as legal name" checkbox), tax ID
- Business address as one group. Use address autocomplete so city, state and postal code fill in from one input.

**Step 3: What you offer (2 fields)**
- Cuisines as multi-select chips
- Delivery distance as a slider or a few preset options (5 / 10 / 25 / 50 miles)
- This is the fun, easy step. Putting it second or third gives people momentum before the paperwork.

**Step 4: Get verified and paid (the heavy part)**
- Food handler permit and insurance certificate uploads
- Bank account name, routing number and account number
- Terms checkbox, then submit

**Things that matter more than the grouping:**
1. **Make the heavy items deferrable.** Ask yourself whether vendors need to submit the permit, insurance and bank details to get approved, or only before their first payout or first order. If it's the latter, let them submit after step 3 and finish the rest from a dashboard checklist ("2 of 4 setup tasks done"). That could cut the sign-up form to about 10 fields.
2. **Show progress and set expectations up front.** Use a step indicator and a line like "About 5 minutes. You'll need your permit, insurance certificate and bank details." People abandon when they hit a document they don't have on hand.
3. **Allow save and resume.** Auto-save each step. Uploads are where people leave to go find a file, so they have to be able to come back.
4. **Make uploads easy.** Accept phone photos and PDFs, support drag-and-drop, and show a clear success state. Let people skip an upload and finish it later if the business process allows.
5. **Reduce typing errors in the bank step.** Validate the routing number checksum inline. Say why you need the details ("for weekly payouts"), and add a short security note near the fields. Bank fields are the biggest trust hurdle in the form.
6. **Use single-column layouts and inline validation.** Show errors as people leave a field, not all at once on submit. Set the right input types and `autocomplete` attributes so mobile keyboards and autofill work.
7. **Show the tax ID prompt in context.** Say what format you accept (EIN or SSN) and why you need it.

If you tell me whether the permit, insurance and bank details are required before approval, I can say how aggressively to defer them. I can also sketch the component structure or write the form if you tell me your stack.
