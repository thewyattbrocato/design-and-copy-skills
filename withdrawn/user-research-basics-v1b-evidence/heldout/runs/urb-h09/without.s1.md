Organize by what you're asking the team to do, not by screen or by the order you tested. Lead with the decision you need, then group findings into action tiers.

## Suggested structure

**1. Opening slide: the headline and the ask (1 slide)**
Something like: "Booking mostly works, but seat selection is failing people, including one who couldn't finish at all. We need a fix owner for seat selection and an investigation of the payment error before the next release." Put the asks first so people hear the rest as support for them.

**2. Tiered findings (1 slide, then a detail slide per top item)**

| Tier | Finding | Why it's here |
|---|---|---|
| **Fix now** | Seat picker: 4/5 couldn't tell which seats were available, 2 bought the wrong deck | Highest frequency, and it caused real wrong purchases |
| **Fix now** | Screen reader user couldn't complete seat selection | A total blocker, and probably an accessibility compliance risk |
| **Investigate** | Card entry error caused 1/5 to abandon | Only one person, but it's lost revenue. Check logs and analytics to see if it's a bug or a one-off |
| **Fix next** | Promo code field unnoticed by 3/5 (1 would have used one) | Likely discoverability, with a smaller revenue effect |
| **Fix next** | Terminal map link missed by 2/5, both first-time visitors | A clear segment pattern. First-timers are the people who need it most |
| **Watch** | Date picker: 1/5 picked the wrong month, then self-corrected | The recovery worked, so low urgency |
| **Park** | Home screen colors "a bit dull" (2/5) | Taste, with no task impact |
| **Keep** | Confirmation page: 5/5 found their ticket | Say what's working so nobody "improves" it |

**3. One slide per Fix-now item**
Use the same format each time: what we saw, what it cost the user, a recommended fix, a proposed owner. Include a short clip or screenshot if you have one. A 20-second recording of someone buying the wrong deck persuades more than any statistic.

**4. Next steps (1 slide)**
List owners and dates, and say what you'll re-test and when.

## Tips

- **Merge the seat picker and screen reader findings into one "seat selection" workstream.** They're the same screen. Presenting them together makes the case stronger and avoids two competing tickets.
- **Report counts ("4 of 5"), not percentages.** With five people, percentages look more precise than they are. Add one line saying this is qualitative, so you're looking for problems rather than measuring rates. That also makes the single-person findings easier to defend.
- **Don't let severity depend on count alone.** The payment error and the screen reader failure are each 1 of 5, but both end in task failure. Say that explicitly, because people will otherwise discount "only one person."
- **Frame the map link finding around the segment.** "First-time visitors miss it" is more actionable than "2 of 5."
- **Put the low-priority items in an appendix or a single "also noted" line.** If the dull-colors comment gets airtime, it can pull the discussion away from the seat picker.
- **Bring a recommendation for each Fix-now item**, even a rough one, such as clearer sold-out styling or proper labels and focus order for screen readers. Teams act faster when they're reacting to a proposal than when they're handed a problem.

If you want, I can draft the slide text or a one-page written summary from this.
