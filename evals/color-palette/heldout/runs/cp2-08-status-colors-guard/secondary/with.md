I wouldn't pull the status colors from the brand palette. Status colors have to be read at a glance and told apart from each other, and brand colors are picked for mood and recognition, not for that job. Brand colors often sit close together (several reds, oranges, or muted tones) and can't always be distinguished quickly on a dashboard.

Your red is the main problem. #d93a35 is the color most people expect for "failed," so if your buttons use it too, a red button can read as an error and a failed deploy can look like a call to action. You have three options:

1. **Keep the brand red for buttons and use a different failure treatment.** For example, use a deeper or more orange-leaning red for failed, paired with an icon and the word "Failed." This keeps the red family but still separates it from the brand accent.
2. **Make the brand red the primary button color and keep status colors out of the red family entirely.** Failed would be a different hue, which is less conventional. This works only if people will learn it quickly.
3. **Use a neutral or dark primary for buttons** and let red stay reserved for failure and destructive actions. This is the cleanest option for a status-heavy tool.

For the other statuses, these conventions are familiar and easy to read:
- **Running:** blue or a cool hue, optionally with a subtle animation
- **Succeeded:** green
- **Waiting for approval:** amber or yellow

Some practical rules:
- Don't rely on color alone. Pair each status with an icon and a text label, since red/green confusion affects a meaningful share of users.
- Check contrast in both light and dark mode, and make sure the four statuses still look distinct in each.
- Keep the status palette separate from the brand palette in your design tokens, so brand changes don't alter what "failed" looks like.

If you want, I can use the color-palette skill to build a status palette with contrast checks for light and dark mode, and show how it sits next to #d93a35.
