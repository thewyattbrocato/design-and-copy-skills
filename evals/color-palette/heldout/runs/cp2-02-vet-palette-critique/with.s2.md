**The problem is that every color is the same color.** I worked these ratios out by hand (WCAG 2.x), so treat them as estimates.

| Pair | Ratio | Needed |
|---|---|---|
| Body text #a39b82 on background #cfc8b0 | about 1.7 : 1 | 4.5 |
| Links #9c8b5e on background | about 2.0 : 1 | 4.5 for link text |
| Primary button #8a7f5c on background | about 2.4 : 1 | 3 |
| Secondary button #7d8a6b on background | about 2.2 : 1 | 3 |
| Error #b5654a on background | about 2.5 : 1 | 4.5 |
| Primary vs. secondary button | about 1.1 : 1 | visibly different |

1. **Everything sits at the same mid lightness.** The background, text, buttons and links are all mid-tone khaki. Nothing is clearly lighter or darker than anything else, so the page has no edges. Your body text is the worst case: it's nearly the same tone as the page it sits on.
2. **Everything sits in the same hue.** Primary, secondary, link and text are all low-saturation yellow-olive. A user can't tell a button from a link from a paragraph. Your two button colors are close to identical.
3. **The saturation is low everywhere, and the background is the dullest color.** A grayish-khaki page fills the whole screen, which is where the "muddy and tired" feeling comes from. Warm and friendly usually comes from a light, creamy ground with a few clear, saturated colors on it.
4. **Error is too quiet.** A muted terracotta at about 2.5 : 1 doesn't read as an alert. It also sits in the same earthy family as everything else.

**Proposed replacement.** I kept the earthy, green-leaning character but separated the roles by lightness and hue:

| Role | Value | Check |
|---|---|---|
| Page background | #FBF6EA (warm cream) | — |
| Body text | #2E2A1F (warm near-black) | about 13 : 1 on background |
| Primary button | #2F6B4F with white text | about 6.3 : 1 text on button, about 5.8 : 1 button on background |
| Secondary button | #E4EFE6 fill, #2F6B4F text and 1px border | text about 5 : 1 |
| Links / highlight | #1F6F8B | about 5.2 : 1 on background |
| Error | #B23A26, with an icon and the word "Error" | about 5.5 : 1 on background |

- **Why green:** it reads as calm and caring for a health product, and it stays close to your current olive.
- **Why the link color is different:** the blue-teal link can't be mistaken for a button. The green stays reserved for actions.
- **Why the error is red:** it's clearly separate from the brand green, and the icon and label mean it doesn't depend on color alone.

I couldn't run a contrast checker here, so verify these in one before you ship. If you want more warmth, a soft amber like #F2B84B works as a fill for highlights with the dark text on top. Don't use it for text on the cream.
