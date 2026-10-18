**Don't print yet.** Three things on this page will generate questions at the desk or get people turned away.

**Blockers (factual contradictions or gaps)**

1. **Returns have nowhere to go.** The h1 says "Return it clean by Monday 5pm," but the only open times are Saturday 10-1 and Wednesday 6-8. Someone who borrows a wet tile saw for the weekend can't return it at the stated deadline. Either add drop-off details (a box, a key-safe, a hall-caretaker arrangement) or change the deadline.
2. **Price is contradictory.** "Free for members" plus "$20 a year, or pay what you can" plus a button reading "Join for $20" means the button tells people who can't pay $20 that they can't join. Say what "pay what you can" means (any amount? a minimum?), and make the button label match the sliding scale, e.g. "Join: from $0 to $20" or "Become a member."
3. **There's no address.** "At the back of the Eastgate Methodist hall" is not findable from a flyer. Add a street address, a map link, and where the entrance is (car park side, back door, etc.).
4. **The email is probably a placeholder.** `.example` is a reserved domain that can never receive mail (RFC 2606). If this is what's printed, nobody can reach you. Confirm the real address before it goes to print.
5. **No late-return or damage policy.** "If something breaks, tell us, it happens" is friendly, but the committee will ask what happens if it's two days late or the saw is wrecked. Even one sentence each prevents arguments at the desk.
6. **The join flow is unclear.** The button sends people to `/join` online, but step 1 says to bring photo ID, which implies in-person. Say whether they can join online and then verify at the shed, or whether the first visit must be in person.

**Fix before print**

7. **The h1 doesn't name the place.** Someone scanning a flyer lands on a sentence about a tile saw and doesn't learn what Loan Shed is until paragraph two. Something like "Loan Shed: borrow tools free for members" with the saw line as a subhead would work better.
8. **"Popular this month" on a printed flyer is stale within a week**, and the page will stay live for months. Drop it, or replace it with a link to live catalogue search.
9. **Naming Renata is fragile.** A volunteer's name on a printed flyer goes stale when rotas change. Use "any volunteer at the Saturday desk."
10. **Hours need explicit times and days.** "10-1" and "6-8" should read "10am-1pm" and "6pm-8pm," and consider a line saying whether the shed is closed on public holidays.

**Markup (minor, but this page will be read on phones)**

11. The fragment has no `<title>`, `<meta name="viewport">`, `lang`, or meta description. Without the viewport tag, the page will render tiny on most phones, and that's where the QR code gets scanned.
12. The two `<a>` buttons are fine, but the primary CTA should be visually obvious at phone width. Check it at 375px before sending.

If you send me the real address, email, return procedure, and the actual pricing rule, I can rewrite the page with those filled in.
