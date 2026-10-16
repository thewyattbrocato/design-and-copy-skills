# What's happening

**The queasiness.** Rolling digits put a lot of motion in the middle of the screen. Many people feel mild discomfort from large, fast, repeating movement. Vestibular sensitivity is the clinical version, but milder versions are common. Several digit columns spinning at once is also visual noise, and you can't focus on any one of them. This is why iOS and Android have "Reduce Motion" settings. The tester may not have that setting on, but it's the same kind of reaction. It's also likely to get worse with repetition, because the animation plays on every open.

**The waiting.** This one is more important. People open a balance screen to get one fact, and the animation makes them wait 2.5 seconds for it. Two things make it worse:

- **The number is wrong the whole time.** It shows $0, then $412, then $1,890, and so on. Until it lands, the reader can't trust anything on screen. Your tester's instinct to wait for it to finish was correct. Reading a number that is still changing risks misreading it.
- **2.5 seconds is long for UI.** Feedback motion usually runs 150–400ms. Anything over about 1 second is a performance, and people tolerate performances once, not on every visit.

In a budgeting app, the balance is sometimes a stressful number. A counter that makes people wait for it can add to that stress.

**Why the PM loves it.** The PM probably sees it rarely, and the first time something is delightful. It also reads as "the app is doing something with my money." That's a real quality, but it is a first-impression effect that fades. Your testers are closer to everyday use, where the cost keeps being paid and the delight doesn't.

# Is it worth keeping?

Not as built. The delight can survive in a much smaller form, but the 2.5s count-up from $0 on every open should go. I'd frame it for the PM as keeping the moment while fixing the cost, not as cutting it.

# What I'd keep

1. **Show the real number immediately.** On a normal open, the balance is there, correct and readable at frame one. No animation, no delay.
2. **Animate only when the number changes.** If a sync brings in a new transaction and the balance goes from $1,890.00 to $1,847.50, a short roll or crossfade on the changed digits explains why the number moved. The motion carries information, which is the best use of it.
3. **If you want a celebratory moment, do it rarely.** Examples are first launch, a first connected account, or hitting a savings goal. Make it a one-off, not the default behavior.
4. **Keep it short and quiet.** Aim for 300–500ms, ease-out, and a small travel distance. Roll only the digits that changed. Don't start from $0, and don't animate the cents when the dollars changed.
5. **Respect Reduce Motion.** Check the OS setting and swap the roll for an instant update or a quick fade. This is an accessibility requirement as well as a comfort feature.
6. **Make it skippable.** If any longer version survives, tapping anywhere should snap it to the final value.

# How to test it

Run a quick comparison with your testers or a few more people: the current version against the "instant, animate on change" version. Measure how long it takes them to say their balance out loud, and ask which one felt more trustworthy. I expect the instant version to win on both. If the PM sees the time-to-read numbers, that will probably persuade them more than the queasiness reports.
