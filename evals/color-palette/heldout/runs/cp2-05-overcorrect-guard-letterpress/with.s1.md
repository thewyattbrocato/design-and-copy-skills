Your palette already works, so I wouldn't change any of the five colors. I did this by hand, so treat the contrast ratios as estimates.

**What's already working**
- **Neutrals:** Ink and Muted lean slightly blue-green, and Paper leans warm. That's why it feels like stationery and not default black on white.
- **One accent:** Rust is the only warm saturated color, so links and buttons stand out clearly.
- **Contrast on Paper:**
  - Ink: about 13:1.
  - Muted: about 4.9:1.
  - Rust: about 4.8:1, which passes for body-size links.

**Small fixes**
1. **Sage tags with text.** Sage is about 3:1 against Paper, which is fine for rules but too low for text. Ink on a Sage tag is about 4.3:1, just under 4.5. Keep tag text at 14px or larger and semibold, or use a paler tag fill of `#dfe6df` with Ink text, which is roughly 11:1. Sage then stays as the rule or border color.
2. **Rust hover state.** Add `#8f3720` for link and button hover. It's about 6.8:1 on Paper, and the darker shade reads as a deliberate press. You don't have a hover color yet.
3. **Rust on a card.** If you add a card or panel color such as `#ede6d6`, Rust text on it drops to about 4.4:1. Keep small Rust links on Paper itself, or use the `#8f3720` shade on cards.

**What will make it feel more premium**
Your friend's impression probably comes from how the colors are used, not from the colors. These help most:
- Use Rust sparingly, on one button or link per screen and not on headings.
- Leave generous Paper space around things.
- Use thin Sage hairlines as dividers.
- Don't add gradients or shadows.

**Print**
Hex values won't match your printed price list. Paper stock, ink, and press impression shift the result, so proof Rust and Sage on your actual stock. If you print with spot inks, pick the nearest ink match by eye on that stock.
