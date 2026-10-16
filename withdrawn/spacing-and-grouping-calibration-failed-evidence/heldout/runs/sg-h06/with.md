I'd ship the spacing as it is. I didn't change anything.

The card has three groups, and the gaps between them grow in the right order:

- **Route and time:** 4px apart, so they read as one unit.
- **Meta row:** a hairline rule with 16px on each side, so it reads as its own group.
- **Button:** 24px below the meta row, the largest gap on the card, so it reads as the action.

The within-group gap (4px) is well under the between-group gaps (16 to 24px), which is what makes the grouping clear. Other checks:

- Every value (4, 12, 16, 20, 24) sits on a 4px scale.
- The 44px button height is a good touch target.
- The 20px padding is even on all sides.
- The last child adds no stray space, because the meta row owns the gap above the button.

One optional tweak. The 12px gap between "1 adult", "1 child" and "Seat 12B" is only a little wider than a normal word space at 14px. If the items ever read as one run-on phrase in your screenshots, raise it to 16px (`gap: 16px`). The row has room, since three short items fit easily in the 298px content width. At 12px it isn't wrong.
