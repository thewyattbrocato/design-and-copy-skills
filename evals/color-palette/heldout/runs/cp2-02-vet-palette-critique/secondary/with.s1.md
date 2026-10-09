**What's going wrong:** every color sits in the same muted, mid-tone khaki band, so nothing anchors the page. The background is tan, the text is a greyed tan, and the buttons are dusty olive-browns. Without a clean light or a true dark, the whole screen reads as flat and dusty.

Findings by impact (contrast ratios are hand-calculated estimates, not measured with a tool):

1. **Body text is nearly invisible: about 1.7:1 on the page background.** Text needs 4.5:1. Your body text is about the same lightness as the background, so it reads as faded rather than as text.
2. **Every pair fails:**
   - Primary button, white label: about 4.0:1
   - Secondary button, white label: about 3.7:1
   - Links on background: about 2.0:1
   - Error text on background: about 2.5:1
3. **Low chroma everywhere.** All six colors are desaturated, so none reads as warm or friendly. Warmth comes from one clean, saturated accent against a light base, not from greying everything toward brown.
4. **Error red is the same family as the brand.** It is dusty terracotta, so it doesn't signal alarm, and it is too close to a warm primary.
5. **Primary and secondary buttons are close in lightness,** so the hierarchy between them is weak.

**Proposed palette**

| Role | Hex | Reason | Contrast |
|---|---|---|---|
| Page background | `#FBF6EE` | Warm cream, light enough to anchor the page | Base |
| Body text | `#3B2F26` | Deep warm brown, keeps the warmth | About 11.8:1 on background |
| Primary button | `#B4532F` | Warm terracotta, the friendly accent; white label | About 5.0:1 with white text |
| Secondary button | `#3F6B5A` | Calm sage-teal, a cool counterweight; white label | About 6.1:1 with white text |
| Links / highlight | `#2E6A5C` | Darker teal, readable on cream | About 5.7:1 on background |
| Error | `#B3261E` | Clear red, darker and cooler than the primary | About 5.9:1 on background |

**Notes**

- Primary terracotta and error red are close in hue. Keep the error icon and the word "Error" on every message so meaning doesn't rely on color alone, and check the pair in grayscale.
- Only the two button colors are used as fills. Keep the cream as the main surface so the terracotta stays small and warm. Cards can use white (`#FFFFFF`) for separation.
