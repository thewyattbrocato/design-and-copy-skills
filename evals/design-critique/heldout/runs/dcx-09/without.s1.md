**Fix these before it goes to print**

1. **Your headline promise conflicts with your opening hours.** You're open Saturday 10-1 and Wednesday 6-8. Nobody can return a tool "by Monday 5pm" because the shed is shut on Monday. The same problem affects the other loan periods:
   - "Wet tile saw: 2 days, back by Monday" has the same conflict.
   - Three days for the post hole digger from a Saturday pickup lands on Tuesday, when you're also closed.
   - Only the 1-week sander lines up cleanly (back the next Saturday).

   Either there's an unstated Monday drop-off arrangement, or the headline is wrong. Reword the loan periods around the days you're actually open, for example "Pick up Saturday, back Wednesday evening or next Saturday." This is the one I'd lose sleep over, because the first volunteer to be asked "so where do I return it Monday?" will wince.

2. **"Join for $20" contradicts "pay what you can."** The button is the loudest thing on the page, and it tells someone who can't afford $20 that they can't join. Make the button just "Join", and put the "$20 or pay what you can" detail on the join page or next to the button.

3. **There's no street address.** "Back of the Eastgate Methodist hall" only works if people already know where the hall is. Someone who scans the QR code on a lamppost needs an address or a map link, and a flyer reader will look for it first.

4. **Joining is unclear.** The button goes to `/join`, but step 1 says to bring photo ID. Do I join online and then show ID in person, or do I have to show up first? Say which. It also doesn't say what happens if I turn up on a Saturday without having joined.

**Should fix**

5. **The headline leads with a rule ("Return it clean...") instead of a benefit.** It also doesn't say what Loan Shed is until the paragraph below. Something like "Borrow tools instead of buying them. 400+ tools, $20 a year or pay what you can" would be warmer. The tile saw can stay as the example.

6. **"Popular this month" will go stale.** It's hardcoded, and nobody will update it in March. Either rename it ("Things people borrow a lot") or commit to updating it.

7. **Safety and liability are missing.** You lend a tile saw and a pressure washer, and the page doesn't mention induction, a deposit, age limits, or what happens if someone is late or hurt. The committee will ask, and a one-liner would answer it.

8. **The contact details are thin.**
   - `lend@loanshed.example` needs to be the real address, and it should be a `mailto:` link.
   - "Find Renata at the Saturday desk" ties the page to one person, so it breaks when Renata is away or moves on. Say "the volunteer desk" instead.
   - There's no phone number, which some of your audience will want.

9. **The HTML will render badly on phones, and the QR code makes that the main use case.** There's no `<!doctype html>`, `lang`, `<title>`, or `<meta name="viewport" content="width=device-width, initial-scale=1">`. Without the viewport tag, mobile browsers show a tiny desktop-width page. If this snippet sits inside a template that already has those, ignore this point.

**Before you print**

- Scan the printed QR code with a couple of different phones at the actual print size and from a realistic distance.
- Make sure it points at a short, stable URL that won't change. You can't reprint a thousand flyers.
- Consider adding `?ref=flyer` so you can see whether the flyer is working.
- Make sure `/join` and `/catalogue` work on mobile, since the page is only as good as where it sends people.

The tone is good: "if something breaks, tell us, it happens" is exactly right. The copy is close, and the Monday/opening-hours problem is the one that has to be fixed first.
