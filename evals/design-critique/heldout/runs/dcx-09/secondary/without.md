Don't print this yet. The biggest problems are logistical, and a committee member will catch them.

**Blockers (fix before printing)**

1. **The email is a placeholder.** `lend@loanshed.example` uses `.example`, a reserved domain that never resolves. Check the real address, and make sure the QR code points at the real domain too, not a `.example` URL.
2. **The return instruction has no return point.** Everyone is told to return tools "by Monday 5pm," but the only staffed times are Saturday 10-1 and Wednesday 6-8. Monday 5pm is a closed time. The page needs to say where and how to return on Monday: a drop box, a key-safe, a volunteer's house, or something else.
3. **The price contradicts itself.** "$20 a year, or pay what you can" followed by a button that says "Join for $20" tells people the pay-what-you-can option doesn't exist. Pick one, or make the button say "Join" and state both options.
4. **No directions.** "Back of the Eastgate Methodist hall" with no street address, no entrance, and no parking or access note will leave first-timers standing outside. Add the address and which door to use. A QR code on a flyer is often scanned while someone is already trying to find the place.

**Real problems**

5. **Nothing says what a loan costs.** Is there a deposit? A late fee? What happens if a tool comes back dirty or broken? "Bring them back clean" with no consequence is vague, and the "it happens" line reads as if breakage is free. Say what the policy is.
6. **Joining is underspecified.** "Bring photo ID the first time" doesn't say what counts as ID. Does `/join` take payment online, or do people join in person? If they can only join in person on Saturday or Wednesday, the "Join for $20" button is misleading.
7. **The "Popular this month" list will be wrong by the time it's printed, and it's tiny.** Four tools out of 400, no availability, and "this month" on a printed flyer will go stale. Replace it with something evergreen, or cut it.
8. **Naming Renata on a public flyer is fragile.** It ties the page to one volunteer who may not always be on the desk, and it's a personal name on a print item. "Ask a volunteer at the Saturday desk" works.
9. **Hours have no closure note.** Printed holiday and closure info will be wrong eventually. Consider "Check /catalogue for current hours" or a line like "Hours may change; see [site]."
10. **Small copy issues:** "Wednesday evenings" should be "Wednesdays" to match "Saturdays." "400-odd tools" is vague; use the real count, or "over 400." The headline is a loan rule, but the page's job is recruiting members, so the H1 should say what Loan Shed is ("Loan Shed: a volunteer tool library in Eastgate"), with the weekend-tile-saw line as a subhead.

**If this is the full page and not just the body**

11. The snippet has no `<title>`, `<meta name="viewport">`, or `lang`. On a phone, that means a tiny, zoomed-out page and a generic tab title.
12. The copy says "free for members," but nothing says whether the catalogue and the `/join` and `/catalogue` pages exist. Click every link from the phone before you print.

Fix 1 through 4 first. Those are the ones a committee member or a first-time visitor will hit. If you tell me the real address, the return arrangement, and the join rules, I can rewrite the page.
