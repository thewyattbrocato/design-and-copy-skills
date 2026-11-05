No, positive tabindex values are an anti-pattern. They pull those fields out of the natural tab order, so anything not numbered (links, header, skip links, other widgets) gets tabbed *after* all six. They're also brittle: any new field breaks the numbering.

The real problem here is the CSS `order`. It changes the visual order but not the DOM order, so tab order and visual order diverge. The tabindex values are patching that mismatch.

**Fix:**
1. Remove all the `tabindex` attributes.
2. Remove the `order` styles and put the DOM in the order you want: First name, Last name, Email, Newsletter, Gift Aid, Sign up.
3. Keep the flex layout for appearance only.

Tab order then follows the DOM automatically and matches what sighted users see, which is what WCAG 2.4.3 (Focus Order) and 1.3.2 (Meaningful Sequence) expect.

Your current tabindex values also don't match the visual order. Gift Aid (`tabindex=5`) is displayed before Newsletter (`tabindex=4`), so keyboard focus jumps backwards on screen.
