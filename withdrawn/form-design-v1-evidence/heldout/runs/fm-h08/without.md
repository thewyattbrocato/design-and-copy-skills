This review is based on your description only, since I don't have the markup or a screenshot.

**What works**
- **One field and one action.** There's no friction beyond the email itself, and a single filled button gives a clear primary action.
- **Visible label.** "Email address" as a real label is better than placeholder-only, which disappears on input and hurts accessibility.
- **Expectation-setting microcopy.** "One email a week. Unsubscribe anytime." answers the two main objections, frequency and commitment.

**Issues and suggestions**
1. **The microcopy may be too small or low-contrast.** Reassurance text is often styled light gray at 11–12px. Keep it at least 12–14px and meet 4.5:1 contrast (WCAG AA).
2. **It doesn't say what people get.** Nothing in what you described tells people what the emails contain. Add a short value line above the form, such as "A weekly digest of X for Y." Without it, "one email a week" reassures people about something they haven't yet decided they want.
3. **Button label.** "Subscribe" is fine but generic. "Get the weekly email" or "Subscribe, it's free" ties the action to the benefit. This is a minor gain.
4. **Placement of the reassurance.** Below the button works, but it's read after the decision point. Putting it directly under the input, or keeping it close to the button, helps. Make sure it's visually grouped with the form.
5. **Accessibility checks:**
   - The label must be programmatically tied to the input (`<label for>` or `aria-labelledby`).
   - Use `type="email"`, `autocomplete="email"` and `inputmode="email"`.
   - The button needs a visible focus state.
   - Error and success messages need `aria-live`/`role="status"`.
6. **States not described.** Design and test these:
   - Validation error, with inline text rather than color alone.
   - Loading, with the button disabled to prevent double submits.
   - Success, which should replace or confirm the form and say what happens next, for example "Check your inbox to confirm."
   - Already subscribed.
7. **Privacy and consent.** If you have EU/UK users, you may need a link to a privacy policy or an explicit consent line. "Unsubscribe anytime" shouldn't be the only legal text. Make "Unsubscribe" accurate, so the emails actually carry a one-click unsubscribe.
8. **Spam and bots.** Use a honeypot or invisible CAPTCHA rather than a visible challenge, to keep the single-field simplicity.

**Verdict:** This is a solid, minimal pattern. The biggest improvements are stating the value of the emails, making sure the small print is legible, and covering the error, success and accessibility states.

If you share the HTML/CSS or a screenshot, I can check the contrast, markup and states concretely.
