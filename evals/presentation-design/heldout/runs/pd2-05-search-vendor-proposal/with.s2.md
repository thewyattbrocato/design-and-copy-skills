**Plan:** 15 minutes, 6 content slides (about 9 minutes of talking, 5–6 left for discussion). Priya Shah decides. **Takeaway:** replacing our search with the vendor is faster (180 ms vs 420 ms p95) and frees about 2.5 engineers a year for $96k.

**Room stance:** the four engineers built what you're proposing to replace, so I've put the verdict later. The order is shared question, their best case, evidence, then the verdict and ask. Priya sees every title, so each is a claim.

## Slides

**1. "We want search that is fast, gets results right, and doesn't consume the team"**
- Three criteria, as three words: Speed · Result quality · Cost to run.
- Say aloud: what you're proposing, and that the in-house service is the baseline everything is judged against.

**2. "The in-house service gives us full control and fits our product"**
- Two or three lines, in words the four engineers would sign: [their strongest reasons].
- Ask them for these before Wednesday. I haven't guessed at them, and if you get them wrong, the rest of the talk won't land.

**3. "On the same queries, the vendor's p95 is 180 ms; ours is 420 ms"**
- Two bars, or two big numbers: 420 ms and 180 ms.
- Small footnote: [number of queries and trial dates].

**4. "Keeping it in-house costs about 2.5 engineers a year; the vendor costs $96k"**
- Two columns: 2.5 engineers/year (≈ $[loaded cost]) and $96k/year + $[migration, one-time].
- You need the loaded cost and the migration estimate, or Priya will ask for them immediately.

**5. "An enterprise customer complained about search results twice last quarter"**
- One line: 1 customer, 2 complaints, [what they said].
- This is one case, so it shows that results can hurt us, not how common it is. The trial measured speed, not result quality, so say that here instead of waiting to be asked.

**6. "Recommendation: move to the vendor, and put the freed engineering time on [X]"**
- The ask: Priya approves the migration by [date]. Owner: [name].
- Suggested gate (my addition): run the vendor on the complaint queries first, and make "results at least as good as ours" the go/no-go.
- Leave this slide up during discussion.

## Backup slides (after the end, for the hardest questions)
- **What does migration cost, and how do we exit if the vendor fails or raises prices?**
- **What happens to the four engineers' work and the 2.5 engineers' time?** Answer this out loud even if nobody asks.
- **Can the vendor match our custom ranking and relevance behavior?**

## Notes
- **Rent vs. own:** I'd cut it as a slide. An analogy shouldn't be your only support, and with the builders in the room it can sound like "your work is a rental we can swap out." Owning a house is also often cheaper over the long run, which invites the opposite argument. If you use it, make it one spoken sentence after slide 4.
- **If time shrinks:** shorten slide 1 to a spoken line first, then merge 5 into 6.
- **Assumption:** I'm treating the engineers as opposed because they built the current service. If you know they're open to the change, move the verdict to slide 1 and drop slide 2.
