Most important first:

1. **Make phone number optional (or justify it).** Requiring it adds friction and abandonment, and most checkouts don't need it. Collect it only if the carrier or fraud checks actually require it, and say why next to the field.

2. **Validate on blur, not on every keystroke.** Red text while someone is still typing their first character punishes them for not being finished. Show errors after the user leaves the field, and clear them live as soon as the value becomes valid.

3. **Keep the Pay button enabled and validate on submit.** A disabled button gives no explanation of what's wrong, and it's a problem for screen readers and keyboard users. On click, show inline errors and move focus to the first invalid field.

4. **Drop floating labels in favor of persistent labels above the fields.** Floating labels shrink to small, low-contrast text, hurt autofill and placeholder clarity, and have a poor accessibility record. A plain label above the input is more legible and more reliable.

5. **Mark optional fields instead of asterisking every field.** If everything is required, asterisks are noise and carry no information. Flag the few optional fields with "(optional)" and drop the asterisks.

6. **Don't rely on red alone for errors.** Color-only signaling fails for color-blind users and fails WCAG. Pair red with an icon and specific message text, such as "Card number must be 16 digits", and link it to the field with `aria-describedby`.

7. **Add autofill and input hints.** Set `autocomplete` attributes, appropriate `inputmode` values, and card-number formatting. These speed up completion more than any visual styling decision.

If the spec is fixed and I can't change it, I'd at least do #2, #3 and #6 within it, since they cause the most harm to users and to conversion.
