Your six colors are too close together, so nothing stands out. I couldn't run code here, so these contrast ratios are hand-calculated estimates.

**What's going wrong, by impact**

1. **Body text is nearly invisible.** `#a39b82` on `#cfc8b0` is about **1.7:1**. Body text needs about 4.5:1. This is the main reason the app looks tired.
2. **Every color is the same muted olive-khaki at mid-lightness.** Hues sit in a narrow yellow-olive band and saturation is low. Everything except the background has about the same lightness.
3. **The buttons and links can't be told apart.** Primary `#8a7f5c`, secondary `#7d8a6b` and links `#9c8b5e` differ by about 1.1:1 from each other. Users can't see which button is the main action or which text is a link.
4. **Nothing separates from the page.** Primary on background is about 2.4:1, secondary about 2.2:1 and links about 2.0:1. Controls need about 3:1.
5. **The error color is the only different hue, but it's weak.** `#b5654a` on the background is about 2.5:1. It's also a dusty terracotta, close to the khaki family, so it doesn't read as a warning.
6. **The background is a dark khaki.** A tan page with khaki content reads as faded paper, not friendly. Warm and friendly usually means a light, creamy ground with a few clear colors on it.

**Replacement palette**

I used a deep teal as the lead because it's calm and trustworthy for health, and it stays warm when paired with cream and apricot.

| Role | Hex | Pair and ratio |
|---|---|---|
| Page background | `#fbf6ec` (warm cream) | — |
| Cards / surfaces | `#fffdf8` | — |
| Body text | `#2e2a22` (warm near-black) | on cream about 13:1 |
| Primary button | fill `#2f6f5e`, text `#ffffff` | text about 5.9:1, fill on cream about 5.5:1 |
| Secondary button | fill `#dcebe3`, text and border `#2f6f5e` | text about 4.8:1 |
| Links | `#24604f`, underlined | on cream about 7:1 |
| Highlight (badges, "online now") | fill `#f6c177`, text `#2e2a22` | text about 9:1 |
| Error | `#b42318`, with an icon and a message | on cream about 6:1 |

- **Lead and accent:** Teal dominates the buttons and links. Apricot appears only in small highlights, which gives the warmth without adding a second loud color.
- **Primary versus secondary:** They differ by form (solid versus pale tint with outline), so they don't rely on a hue difference.
- **Error color:** Red is clearly separate from the teal and apricot. Pair it with an icon and words so it doesn't rely on color alone.

**Notes**
- You gave no brand color, so I chose teal. If you have a logo color, tell me and I'll rebuild around it.
- Run the final pairs through a contrast checker before launch, since my ratios are estimates.
