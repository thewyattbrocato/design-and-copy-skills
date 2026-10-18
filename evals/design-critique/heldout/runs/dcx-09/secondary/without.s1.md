**Don't print this yet.** The biggest problems are factual gaps a visitor will hit immediately.

## Blockers

1. **The return deadline can't be met.** You say "return by Monday 5pm," but you're open only Saturdays 10-1 and Wednesdays 6-8. Nobody can return a tool on Monday in person. Either state a drop-off method for Monday, or change the deadline to something you're open for, like Saturday 1pm or Wednesday 8pm.

2. **There's no address.** The page says "at the back of the Eastgate Methodist hall" and nothing else. Someone who scans a flyer on the street needs a street address, and ideally a map link and a note on where to find the shed in the hall.

3. **The contact email is a placeholder.** `loanshed.example` is a reserved domain that doesn't resolve. Replace it with a real address before printing, and test that it receives mail.

4. **Loan periods contradict each other.** The headline implies a weekend loan. The list says the tile saw is "2 days, back by Monday," the digger is "3 days," and the sander is "1 week," with no start date for any of them. Someone who picks up a saw Saturday at 1pm and reads "2 days" will expect Monday 1pm, but the page says Monday 5pm. Give one rule per tool, or a single policy with exceptions, and say when the clock starts.

5. **The page never says what happens when things go wrong.** "Bring them back clean" doesn't define clean. "If something breaks, tell us, it happens" doesn't say whether there's a deposit, a repair fee, or a late fee. The committee will get asked about this on day one, so state the policy, even if it's "no late fees, damage charged at cost."

## Fix before print

6. **The join button hides the sliding scale.** The body says "$20 a year, or pay what you can," but the button says "Join for $20." Make the button "Join from $20" or "Become a member."

7. **Non-members aren't addressed.** It says "free for members," but doesn't say whether non-members can borrow, can't borrow, or must join first. Step 1 implies you must join before borrowing, so say that directly.

8. **"Find Renata" will break.** A named volunteer on a flyer becomes wrong the first time they take a week off. Use "ask a volunteer at the Saturday desk."

9. **The brand name is missing from the heading.** "Loan Shed" appears only in the body. For a QR landing page, the name should be in the `<h1>`, with the headline as a subhead or tagline. Add a `<title>` tag too, since it appears in the browser tab and in search results.

10. **"Popular this month" is stale on arrival.** It's static and undated, with no availability and no links to the catalogue. Either link each item or cut the section. A dated "Popular in October" will go stale on its own, so it's better to cut it.

11. **The hours have no context.** "Open Saturdays 10-1" lacks a timezone, a location, and a note on whether it's the same hall entrance. Add the address near the hours and say whether Saturday desk and shed are the same place.

12. **No accessibility info.** For a shed behind a church hall, people will ask whether there's step-free access, parking, and whether the shed is accessible during the day. One line helps.

## Technical

13. **The QR code must encode the absolute URL,** not a relative path. The `/join` and `/catalogue` links work on the site, but test the printed code on an actual phone from outside your Wi-Fi.

14. **The styles aren't in this file.** `.btn` and `.btn-secondary` assume a stylesheet. Confirm the page renders correctly on its live URL, not just in a local preview.

15. **The page needs `lang`, a viewport meta tag, and a `<title>`.** Without a viewport tag, the page can render at desktop width on phones, which is most of your visitors.

**The fix list, in order:** pick a return rule that matches your open hours, add the address, replace the example email, define the loan periods, and state the damage and late-fee policy. Those five fixes will matter more than any cosmetic change. If you give me the address, a real contact email, and your actual loan rules, I'll rewrite the page.
