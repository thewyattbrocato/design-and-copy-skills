Your friend is right, but the problems are fixable and a few of them matter far more than the rest. Here they are in the order I'd fix them.

## Fix first

**1. The moves counter is the worst problem.**
In a match-3 game, moves are the most important number on screen. Yours is 11px, nearly the same color as the background, and tucked into a corner above the score. Players will lose levels without noticing they were running out.
- Make it large, around 20–24px and high contrast.
- Put it next to the goal bar or just above the board, where players are already looking.
- Give it a clear hierarchy: moves and score are primary, and everything else is secondary.

**2. The low-moves warning only changes color.**
- Red alone fails for colorblind players, and it's easy to miss at 11px anyway.
- At 3 moves, also pulse or scale the counter, and add a small shake or sound on each move after that.
- Consider a stronger signal at 1 move.

**3. The progress bar has no meaning.**
A 6px unlabeled bar tells the player nothing. They can't tell what the goal is, how far along they are, or where the star thresholds sit.
- Add the goal as an icon plus a count (for example, "🐚 12/20"), or add star markers along the bar.
- Make the bar thicker, around 12–16px.
- Move it next to the moves counter so the "moves left vs. progress" tradeoff reads as one unit.

## Fix next

**4. The power-ups are in the wrong place and show too little.**
- They're at the top of a tall phone, which is the hardest spot to reach with a thumb. Move them into the 180px of dead space below the board, where they're easy to tap.
- Show a count badge on each one.
- A locked power-up and an out-of-uses one shouldn't look the same. Use a lock icon for locked, and a "0" badge or a dimmed icon with a "+" to buy more.
- 40% opacity alone is ambiguous.

**5. The header has no hierarchy.**
Score, power-ups, and pause share one teal treatment, so nothing stands out. Once the power-ups and moves counter move out, the header can be just score and pause. Give pause a quiet, smaller treatment so it isn't tapped by accident.

**6. The layout wastes space.**
By my math, 120 + 6 + 322 (board) + 180 + 50 = 678px, so you have roughly 166px of unallocated slack on top of the empty strip.
- 46px tiles leave 34px margins on a 390px screen. At 52px, a 7×7 board is 364px wide with 13px margins, which is much easier to read and tap.
- Use the freed vertical space for the power-up row and the moves/goal strip.

## Also check

- **Safe areas:** The top 120px likely includes the status bar and notch, so your content may be cramped. At the bottom, the ad sits on the home indicator, so add safe-area insets.
- **Ad placement:** Keep the ad well away from the power-up row to avoid accidental ad taps, which cause player frustration and can cause policy trouble with ad networks.
- **Tile contrast:** I can't judge tile and background contrast from your description. Check the sea-creature tiles against the dark blue board, including in grayscale.

## Suggested layout (top to bottom)
1. **Header:** score on the left, pause on the right.
2. **Goal strip:** a labeled, thicker progress bar with the moves counter beside it.
3. **Board:** 52px tiles.
4. **Power-up row:** in the thumb zone, with counts and clear locked states.
5. **Ad:** with a gap above it, and respecting the bottom safe area.

If you can share a screenshot or the layout code, I can give more specific feedback on spacing and contrast.
