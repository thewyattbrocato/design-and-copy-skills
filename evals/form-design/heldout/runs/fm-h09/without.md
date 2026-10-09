**Recommendation: a single text input with a format hint, not a native date picker.** Use three separate fields only if you have a specific reason to.

**Why not a date picker**
- Birth dates are far in the past. With a calendar widget, a 55-year-old has to click back through hundreds of months or find a year dropdown, which is slow.
- Native `<input type="date">` looks and behaves differently across browsers and devices. Mobile pickers are okay, but desktop ones are awkward for dates this far back.
- Typing is quicker than picking for anyone who knows their own birth date.

**Why not three dropdowns**
- A year dropdown of 70+ entries is tedious to scroll.
- Dropdowns are slow on desktop and fiddly on phones.
- The advantage is that they prevent invalid dates. Good validation gives you the same protection.

**What to build**
- **Format.** Use three separate text inputs (Day, Month, Year) with `inputmode="numeric"`. This is the GOV.UK Design System pattern, and it was tested with a broad adult audience. It avoids the ambiguity of MM/DD vs. DD/MM in a single field, which matters if your users or audience span locales.
- **Single field alternative.** If you prefer one field, use `inputmode="numeric"` and a hint such as "MM/DD/YYYY", with an example like "03/27/1985". Match the format to your user locale, and accept flexible separators (`/`, `-`, `.`, spaces).
- **Labels.** Keep visible labels. Don't use placeholder text as the only hint, because it disappears when the user starts typing.
- **Autofill.** Set `autocomplete="bday-day"`, `"bday-month"` and `"bday-year"` (or `"bday"` for a single field) so browsers can fill it in.
- **Validation.** Check on blur or submit, not on every keystroke. Error messages should be specific, for example "Year must be four digits" or "Enter a date in the past". Also check for plausible ages and for any minimum-age rule your program has.
- **Accessibility.** Group the three fields in a `<fieldset>` with a `<legend>`, and associate errors with `aria-describedby`.

**Choosing between the two text options**
- If your users are all in one locale and the form is short, a single input is fine.
- If the audience is mixed or the data matters (identity checks, eligibility), use the three-field version. It removes the day/month ambiguity.

If you tell me your framework or component library, I can write the markup and validation.
