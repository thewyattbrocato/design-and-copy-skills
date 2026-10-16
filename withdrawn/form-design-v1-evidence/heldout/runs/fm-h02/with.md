# Critique of the checkout address form

## Biggest problems

**1. Placeholders are the only labels.**
- The field name disappears as soon as someone types, so they can't check their entry or find a mistake later.
- Placeholder text is usually low-contrast, and screen readers handle it unreliably.
- Autofill also becomes harder to verify.
- **Change:** use a visible label above each field, associated with the input (`<label for>`). Keep placeholders only for examples, or drop them.

**2. The submit button is grayed out until everything is valid.**
- A disabled button gives no reason for being disabled. The shopper can't tell which field is wrong, and disabled buttons are often unreachable by keyboard or screen reader.
- **Change:** keep the button always pressable. Explain problems after the press. The only time to block it is while the request is in flight, and then show progress so nobody double-submits.
- **Label it with a verb:** "Continue to payment" or "Review order" rather than "Submit".
- **Placement:** put it directly under the last field.

**3. The only error message is "Invalid input" in red at the top of the page.**
- It doesn't say which field is wrong or how to fix it.
- It relies on color alone.
- It sits far from the problem and may be off-screen.
- **Change, per field:** show the message next to the field, with an icon or text cue as well as color, and name the fix. For example: "Enter a 5-digit ZIP code, like 94110."
- **Change, summary:** with two or more problems, add a summary at the top listing each one as a link to its field. Move focus to the summary and put the error count in the page title.
- **Also:** avoid the word "invalid", and keep everything the shopper typed.

## Field-level changes

| Field | Problem | Fix |
|---|---|---|
| **Name** | Fine as a single field. | Label "Full name", `autocomplete="name"`. |
| **Address line 1 / 2** | Line 2 looks required. | Label line 2 "Apartment, suite, etc. (optional)". Use `autocomplete="address-line1"` and `address-line2`. |
| **City** | Often not needed first. | Keep it, with `address-level2`. Consider autofilling it from the postal code. |
| **State** | A free-text box produces "Calif.", "CA" and "California", and typos. | Use a select or autocomplete of valid states or regions. Make it depend on country. Use `address-level1`. |
| **ZIP** | Probably full width, with a US-only format. | Make it short, with `autocomplete="postal-code"` and `inputmode="numeric"` for US only. Accept spaces and dashes and normalize them in code. Label it "Postal code" for non-US countries. |
| **Country** | A text input invites typos and mismatches. | Use a select or autocomplete, defaulted sensibly (for example from the shop's shipping regions), with `autocomplete="country"`. Put it first, because it controls the State and postal code format. |
| **Phone** | Required with no explanation. | Ask only if the carrier needs it. If so, print the reason beside the field ("For delivery updates only"). Otherwise cut it or mark it "(optional)". Use `type="tel"`, `autocomplete="tel"`, and accept human formatting. |

## Plant-shop specifics

- **Shipping restrictions:** plants can't ship to some regions (agricultural rules in California, Hawaii and others), and delivery timing matters for live goods. Check this early, at the country and state step, and say so there instead of failing at the end.
- **Delivery notes:** consider an optional "Delivery instructions" field, since someone must be home or the plants may sit in cold or heat.

## Validation timing

- Don't show errors while someone is still typing a first attempt, because the first characters of a valid value aren't valid yet.
- Validate on submit. After a field has shown an error, re-check it as the shopper edits so the message clears as soon as it's fixed.
- Always run the same checks on the server, and keep entered values if the server rejects the form.

## Layout and mechanics

- Use a single column. Make field widths hint at the expected length: ZIP and State short, Address wide.
- Use 16px or larger input text so iOS doesn't zoom on focus. Keep touch targets about 44px tall. Keep the focus outline visible.
- Mark the minority of optional fields with the word "optional". If everything is required, say so once or mark nothing. Don't use unexplained asterisks.
- Offer guest checkout, and show a review step before payment so the address can be edited.

## Suggested order

1. Country
2. Full name
3. Address line 1
4. Address line 2 (optional)
5. City
6. State/region
7. Postal code
8. Phone (only if justified)
9. **Continue to payment** (always enabled)

If you want, I can write this as accessible HTML/CSS with the error summary pattern.
