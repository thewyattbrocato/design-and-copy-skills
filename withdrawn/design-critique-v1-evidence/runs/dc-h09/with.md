**Verdict:** Your friend is right, but the problem is hierarchy rather than polish. The most important number on screen, moves remaining, is the hardest to see. About 40% of the screen is dead space. I'm working from your description only, with no screenshot, so contrast figures are estimates.

## Fix first, in this order

**1. Moves counter (blocker).** Moves are the resource every decision in a match-3 game depends on, and this one is nearly invisible.
- It's 11px, in a color close to the background, in the top-left corner above the score. That's the smallest, lowest-contrast text on the screen. I'd estimate it's under the 4.5:1 minimum, and it likely sits under the status bar or notch.
- At 3 moves it turns red but stays 11px. Red-on-dark-blue is weak contrast, and color alone fails colorblind players. It also doesn't create any urgency.
- **Fix:** Make it at least 20px bold in white and put it in the header's center or next to the score. At 3 moves, scale it up, pulse it, and add an icon or shake so it isn't color-only.

**2. Level goal (major).** Players can't tell what they're working toward.
- A 6px bar with no label doesn't say what the goal is, how far along they are, or where the star thresholds fall. It also reads as a header border.
- **Fix:** Show the goal as an icon plus a count (e.g. a shell icon with "12/20"). If there are star thresholds, mark them on the bar. Make the bar about 12px and give it its own contrasting color.

**3. Power-ups (major).**
- With no counts, players can't tell whether they own 0 or 5. A locked icon at 40% opacity on teal also looks the same as "out of stock" or "disabled". Locked and empty are different states and need different looks.
- They're in the top center, the hardest spot for a thumb on a phone. You use them mid-play, so they should be reachable.
- **Fix:** Add a count badge on each icon, and give locked icons a padlock instead of just fading them. Move the row into the empty space below the board.

**4. Header with no hierarchy (major).** Score, power-ups and pause all share the same teal background, so nothing leads.
- **Fix:** Give score and moves the visual weight. Make pause a small, quiet icon with no filled block. Power-ups shouldn't live in this bar at all once they move down.

**5. Layout and wasted space (major).** This is a rough tally from your numbers.
- Header (120) + bar (6) + board (322) + empty (180) + ad (50) = 678px. That leaves about 166px unaccounted for, so you have roughly 340px of unused vertical space.
- The board is 322px wide on a 390px screen, which leaves 34px margins on each side.
- **Fix:** Grow the tiles to about 52px (364px board, 13px margins). Use the freed space for the power-up row and a clear gap above the ad. Keep the ad separated from tappable controls so players don't tap it by accident.

**Minor:** Check the safe areas. The status bar and notch at the top and the home indicator at the bottom (about 34px on notched iPhones) can overlap your 11px text and the ad.

## Keep

- Portrait layout with a centered 7×7 board.
- 46px tiles, which clear the ~44pt touch minimum. You can grow them, but don't shrink them.
- The ad stays at the very bottom, away from the board.
- Changing the counter's color at 3 moves is the right instinct. It just needs a size or motion change alongside it, as in fix 1.

## Next check

Hand the phone to three or four people who haven't seen the game. Ask them to play one level without help, then ask how many moves they have left and what the goal is. If they can't answer, the HUD still isn't working.

I can sketch a revised layout with pixel values if you want one.
