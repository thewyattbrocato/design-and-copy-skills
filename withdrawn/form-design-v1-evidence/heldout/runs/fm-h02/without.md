# Critique and recommended changes

## Biggest problems

**1. Placeholders as labels**
- The label disappears once the user types, so they can't check what they entered. This hurts people who are interrupted mid-form.
- Placeholder text has low contrast, and screen readers don't reliably treat it as a label.
- **Change:** Use visible, persistent `<label>` elements above each field, tied to the input with `for`/`id`. Keep placeholders only for format hints, such as `(555) 123-4567`.

**2. Error handling: "Invalid input" at the top of the page**
- It doesn't say which field is wrong, what is wrong, or how to fix it.
- The message is far from the problem, and the user may not see it if it's above the fold.
- Red alone fails color-blind users.
- **Change:**
  - Show errors inline, directly under each field, with specific text. For example: "Enter a 5-digit ZIP code" or "Phone number needs 10 digits."
  - Add an icon or text prefix in addition to the red color.
  - Link each message to its input with `aria-describedby` and set `aria-invalid="true"`.
  - On submit, add a summary at the top that links to each failing field, and move focus to the first error.
  - Validate on blur, not on every keystroke, and clear the error as soon as the value becomes valid.

**3. Submit button disabled until everything is valid**
- Users can't tell why it's disabled, and disabled buttons are often skipped by keyboard and screen reader users.
- It also conflicts with your own after-submit error design: if the button can't be pressed with invalid data, the errors can't be shown.
- **Change:** Keep the button always enabled. On click, validate and show the specific errors. If you want a loading state, disable it only while the request is in flight, to prevent double orders.

## Field-level issues

**4. State as free text**
- This invites typos and variants ("Calif.", "CA", "california") and makes shipping and tax lookup harder.
- **Change:** Use a select, or a combobox, populated according to the chosen country. Label it "State/Province/Region" for non-US addresses, and make it optional where the country has no equivalent.

**5. Country as free text**
- Same problem, and it's also a shipping-eligibility issue. Plants have real restrictions on cross-border and some interstate shipping (for example, agricultural rules, and California or Hawaii limits on certain species).
- **Change:** Use a country select with type-ahead, defaulting by locale or IP. **Put Country first**, because it determines the formats and labels of the fields below it (ZIP vs. postal code, State vs. Province). If you ship to only a few places, say so and list just those.

**6. ZIP**
- It's US-specific, and it will reject valid international postal codes.
- **Change:** Relabel it by country, validate with a per-country pattern, and use `inputmode="numeric"` for US ZIPs. Optionally auto-fill City and State from the ZIP.

**7. Phone**
- It's not clear whether it's required. If it's there only for delivery contact, say so.
- **Change:** Explain why you're asking ("For delivery updates"), make it optional if you can, accept any common format, and normalize it server-side rather than rejecting spaces, dashes, or parentheses. Use `type="tel"`.

**8. Address line 2**
- Without a label, users won't know it's for an apartment, suite, or unit number.
- **Change:** Label it "Apartment, suite, etc. (optional)", and mark other optional fields explicitly.

**9. Name**
- A single "Name" field is acceptable and is often better than separate first and last fields, since it's more inclusive of different naming conventions.
- **Change:** Label it "Full name". Don't enforce a minimum length or character set.

## Missing pieces and polish

- **Autocomplete attributes.** Add `autocomplete="name"`, `address-line1`, `address-line2`, `address-level2` (city), `address-level1` (state), `postal-code`, `country`, and `tel`. This allows browser autofill, which speeds up checkout a lot, especially on mobile.
- **Address autocomplete.** Consider a lookup service such as Google Places, which reduces typing and bad addresses.
- **Mobile keyboards.** Set `inputmode` and `type` appropriately for each field.
- **Layout.** Use a single column, with City, State, and ZIP sharing a row only if the labels remain clear on small screens.
- **Required vs. optional.** Mark whichever set is smaller. Don't use red asterisks as the only signal.
- **Preserve input.** A failed submit must never clear what the user typed.
- **Plant-shop context.** Show shipping eligibility and delivery estimates once the address is entered, and note weather-related shipping holds if relevant. Offer a delivery-instructions field, such as "leave in shade" or "don't leave outside in freezing weather."
- **Accessibility check.** Make sure the focus order, visible focus rings, and a 4.5:1 text contrast ratio all hold up. Test with keyboard-only use and a screen reader.

## Priority order

1. Add real labels.
2. Show inline, specific errors, and keep the button always enabled.
3. Use a country select (placed first) and a state select.
4. Add `autocomplete` attributes.
5. Make ZIP and phone international-friendly.

The first three changes are the ones that most affect completed orders. The rest are refinements.
