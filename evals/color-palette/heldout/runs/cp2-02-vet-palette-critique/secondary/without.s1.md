The muddiness comes from three things:

1. **Everything sits in the same middle lightness.** The background, buttons, links, and text are all mid-tones, so nothing anchors the page. Light surfaces and dark text usually make a layout feel fresh, and this one has neither.
2. **The hues are nearly identical.** Primary khaki, secondary sage, link ochre, and body text are all low-saturation olive-brown. Without a clearly different accent, the primary button, secondary button, and link all read as the same color.
3. **Contrast is very low.** I estimated these WCAG ratios by hand, so check them with a tool before shipping:

| Pair | Approx. ratio | WCAG AA (text) |
|---|---|---|
| Body text on page background | **~1.7:1** | Fails badly (needs 4.5:1) |
| Link on page background | ~2.0:1 | Fails |
| Secondary button vs. background | ~2.2:1 | Fails for text |
| Primary button vs. background | ~2.4:1 | Fails for text |
| Error message on page background | ~2.5:1 | Fails |

Body text is the worst problem. At this contrast, a pet owner reading dosage instructions or a vet's notes on a phone in bright light will struggle. For a healthcare product, that is a usability and compliance issue, not just a style one.

**A direction that keeps it warm but stops it looking tired:**

- **Page background:** a light cream, such as `#faf6ee`, with white cards for content.
- **Body text:** a deep warm charcoal, such as `#2e2a22`. This gives about 13:1 on the cream.
- **Primary button:** a clearer hue for the main action, such as a deeper teal `#2a7f75`. It gives about 4.8:1 with white text and stands apart from the khaki family.
- **Secondary button:** keep the sage, but darken it until it clears 4.5:1 as text on cream. Use it as an outlined or tinted button.
- **Links:** use a darker version of the primary teal so they don't blend with the secondary buttons.
- **Error messages:** deepen the terracotta to something like `#9e4a34`. It gives about 5.6:1 on cream and still reads as warm, not alarming.

The warm neutrals can stay for the background and borders. The shift is to light surfaces, one clearly distinct accent for actions, and dark text.

I can apply this to your theme or CSS variables if you point me to the file where these colors are defined.
