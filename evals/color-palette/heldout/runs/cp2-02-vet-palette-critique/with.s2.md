**Short answer:** every color sits in the same narrow band of hue, lightness and saturation, so nothing stands out from anything else. I worked the contrast ratios out by hand, so treat them as estimates of about ±0.1.

**What's going wrong, by impact**

1. **Body text is nearly invisible.** `#a39b82` on `#cfc8b0` is about **1.7:1**. The floor is 4.5:1. This is the main reason the app looks tired, because every paragraph fades into the page.
2. **The background is mid-tone khaki.** At roughly 58% luminance it reads as dingy rather than warm. Light backgrounds feel friendly when they're clearly light, like cream. The khaki also takes away the headroom that the buttons and text need.
3. **The buttons, link and page are all the same dull yellow-olive.** The two buttons differ by only about **1.09:1** in lightness, so primary and secondary look like the same button. The link `#9c8b5e` on the page is about **2.0:1**, which is too faint to read as a link.
4. **Nothing has real color.** All of them are low-saturation, so there is no lead color to look warm or alive. Muddy greens and tans read as "field notes", not "caring vet".
5. **The error color is too weak to work as an alert.** `#b5654a` is about **2.6:1** on the page, and it has the same dulled look as everything else.

**Fix**

| Role | Now | New | Check |
|---|---|---|---|
| Page background | `#cfc8b0` | `#faf6ec` (warm cream) | n/a |
| Body text | `#a39b82` | `#2f2a1e` (warm dark brown) | ~13:1 on background |
| Primary button | `#8a7f5c` | `#2f7d5b` (fresh green) with white text | ~5.0:1 text, ~4.6:1 edge on background |
| Secondary button | `#7d8a6b` | `#dcebdd` fill, `#1f5a40` text | ~6.5:1 text; clearly lighter than primary |
| Links | `#9c8b5e` | `#1f5a40`, underlined | ~7.5:1 on background |
| Highlight (badges, selected states, not text) | (shared with link) | `#f0b44c` with `#2f2a1e` text | ~7.7:1 text |
| Error | `#b5654a` | `#a2402a` | ~5.9:1 on background |

**Why this works**
- **Lead color:** green is the one lead color. It suggests care and health, and it avoids the clinical blue of most medical apps. Cream and brown keep it warm.
- **Amber highlight:** it adds a friendly spark. Keep it small so green stays the lead.
- **Error color:** error and amber are both warm, so always pair errors with an icon and words, not color alone.
- **Hover and disabled states:** I haven't set them. Hover can move the primary one step darker, to about `#256548`.

**Two notes**
- I changed the hue family on purpose. Tuning the olives alone can't give you lightness contrast and a lively lead color at the same time. If the olive is a brand requirement, I can build a version that keeps it as the lead, with a deeper and more saturated olive for buttons.
- I had no way to run a contrast checker here, so confirm the figures in one before launch.
