**Ship B, with two fixes before Friday.** It answers the question the empty state exists for: what can I do right now? A gives the user nothing to act on except "Get Started," which doesn't say what starts or what happens next.

**Findings**

1. **Major, copy contradiction in B.** The heading says "No walks booked this week," but the primary button says "Book Marta for Tuesday." Today is Friday, so "Tuesday" most likely means next week's Tuesday. Fix: "No walks booked yet" as the heading, or name the date on the button ("Book Marta for Tue, Oct 20").
2. **Major, B depends on live data.** "Marta's usually free Tuesday and Thursday mornings" is only true if it comes from her real availability. If she's full, or the user is in an area with no walkers, the copy and button are wrong. Fix: pull the name and slots from the data, and fall back to the generic "See other walkers" layout when no match exists.
3. **Moderate, B's buttons look unfinished.** Two default-looking buttons with equal weight give the user no clear primary action. Fix: make "Book Marta…" the one filled button in the brand color, and turn "See other walkers" into a text or outline button. This is partly taste, but the equal weight is a function problem.
4. **Minor, the "vetted and local" link is in the wrong place.** It answers a question the user hasn't asked yet. It's fine as a small link, but it belongs next to the walker list, not in the empty state.
5. **Minor, A's copy is vague.** "Your journey" and "We can't wait" are filler. A's illustration and spacing are clean, but they don't help someone decide what to do.

**What to keep from B**
- The specific walker and time. Concrete names are what make a first booking feel safe.
- "She'll send you a photo halfway through." It's the most persuasive line on either screen. Confirm it's a real feature before shipping it.
- Left alignment and plain type. They read as direct, which suits a utility flow.

**Not checked:** I haven't seen either screen rendered, so I can't measure contrast or tap target sizes. I have no data on how Marta's availability is actually sourced, and no user testing. A cheap test before Friday: show five people each version and ask what they would do next. If they tap the primary button in B without hesitation, the copy is working.
