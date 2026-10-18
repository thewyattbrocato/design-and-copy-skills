**Verdict: the copy is warm and clear, but the page contradicts itself on the one rule it leads with, and it never says where you are.** Fix those two before printing.

I assumed a first-time visitor on a phone who has just scanned the flyer. I only saw the HTML, so I haven't checked CSS, contrast or tap size.

## Blockers

1. **Monday 5pm return doesn't fit your opening hours.**
   - The H1 says "back by Monday 5pm", but you're open Saturday 10-1 and Wednesday 6-8. Nobody is there on Monday.
   - Is there a drop box or a key arrangement? If not, the deadline is unmeetable. A new member will either worry about it or turn up Wednesday and feel late.
   - The same problem shows in the popular list. Post hole digger "3 days" from a Saturday lands on Tuesday, which is also closed.
   - Fix: state the real return window, such as "return Wednesday 6-8" or "drop box by the door". Make every loan length in the list end on an open session. Then rewrite the H1 around that.

2. **There is no address, map or next open date.**
   - "The back of the Eastgate Methodist hall" is the only location, and it's the only thing a QR scanner needs to act on. There's no street, door, parking or map link.
   - Fix: add an address line and a map link directly under the hours. Add "next open: Sat 17 Oct" if you can keep it current.

## Major

3. **The button says "Join for $20" but the body says "pay what you can".**
   - The people who most need pay-what-you-can will see $20 on the only join button and leave.
   - Fix: make the label "Join ($20, or pay what you can)", and check that `/join` actually offers that option.

4. **No viewport meta tag, `<title>`, `lang` or `<main>` (the snippet may be a fragment).** On a QR page, nearly every visitor is on a phone. Without `<meta name="viewport" content="width=device-width, initial-scale=1">`, mobile browsers render a shrunken desktop layout. If that tag lives in your template, ignore this. Test by scanning the printed flyer on a real phone.

5. **Joining is unclear.**
   - Step 1 says "Join (bring photo ID the first time)". Do you join online at `/join` and then show ID in person? Can you borrow on the day you join? Which ID counts?
   - ID is the biggest barrier in the whole flow and it's tucked in brackets.
   - Fix: split it into "Join online, then bring photo ID to your first visit" and say which ID works.

## Minor

6. **The loan lengths in "Popular this month" are unlabeled.** "Wet tile saw: 2 days" reads as a description, not a loan period. Use "Loan: 2 days". Also, the list is stale by design, so decide who updates it each month. Otherwise cut the "this month" framing.

7. **The email address is plain text.** Wrap it in `mailto:`. Phone users can't tap it otherwise.

8. **The two buttons are the same class family.** I can't see the CSS, so check that "Join" clearly outranks "See what we have". Whether browsing should come first for sceptical visitors is a taste call. I'd keep Join primary.

## Keep

- **The specific headline.** A tile saw for the weekend is concrete in a way "Borrow tools, save money" never is. Keep the example and fix the rule.
- **"400-odd tools, run by volunteers, free for members".** It's honest, human and states the offer in one line.
- **The three-step "How borrowing works".** It's short, in order, and "If something breaks, tell us, it happens" reduces borrowing anxiety.
- **Naming Renata and the Saturday desk.** It gives a nervous newcomer a person to look for.

**Fix order:** 1 and 2 first, since both are factual and take minutes. Then 3 and 5, then the viewport tag, then the rest.
