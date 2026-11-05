I'd split it into five short steps, save progress automatically, and let vendors skip the fields that don't need to be filled in now. By my count it's 18 fields, because the terms checkbox makes one more than your 17.

**Steps, easiest and least committal first**

1. **About you** has contact name (one field), email and phone. Print a reason under the phone field, such as "We call this number about order problems." Email goes first so you can create the account here. That lets you save progress and email a resume link to anyone who drops out.
2. **Your business** has legal business name, trading name, tax ID and address.
   - Mark trading name "optional" and add the hint "if different from legal name".
   - Use address autocomplete, or put postal code first and fill in city and state from it.
   - Add the standard autofill tokens for the address fields.
3. **What you cook** has cuisines and delivery distance.
   - Cuisines are checkboxes, or a searchable multi-select if the list is long.
   - Delivery distance is a few radio options or a stepper, in miles or km based on locale.
   - These are quick and engaging, so they break up the paperwork.
4. **Documents** has the food handler permit and the insurance certificate.
   - Accept PDF and photos, and let phone users take a picture directly.
   - Show the filename and a Replace button after upload.
   - Say which file types and sizes are allowed before they pick a file.
   - Let them save and come back later, since this is where most people stall while hunting for paperwork.
5. **Payouts and review** has bank account name, routing number and account number, then a summary with edit links, the terms checkbox and a "Submit application" button.

**Two changes that could shorten the form**

- **Bank details:** if you don't need them until a vendor's first payout, collect them after approval. That drops three of the most off-putting fields from the sign-up. If you do need them up front, keep them last, as above.
- **Tax ID:** explain in a line why you need it, for example "needed for payout tax reporting". Sensitive fields are where people hesitate.

**Details that reduce abandonment**

- Put the step name and count in the heading, like "Documents, step 4 of 5". Going back keeps answers.
- Validate on submit of each step, not while people are typing. Keep the Continue button pressable and put errors beside the field, written as fixes. For example: "Routing numbers have 9 digits."
- Use numeric keyboards for routing and account numbers, but not spin-button number inputs. Accept spaces and dashes and strip them in code.
- Don't make people type the account number twice. Mask it with a show control instead.
- Leave the terms checkbox unchecked, with the link in the label.
- After submitting, say what happens next, how long review takes, and who to contact if they hear nothing. I've left that timeline blank because I don't know your actual turnaround.

I can sketch the field-level spec for any step, including labels, input types and error copy, if that would help.
