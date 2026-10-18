**Fix before printing:**

1. **The email address is a placeholder.** `loanshed.example` ends in `.example`, a reserved TLD that never resolves. Anyone who emails will bounce. Check the real domain and the `href` on the page too.

2. **The H1 promises a Monday 5pm return, but you're never open on Mondays.** The hours are Saturday 10–1 and Wednesday 6–8. Where and how do people return a tool on Monday? A drop box, a volunteer's house, nothing? Someone will be stuck with a tile saw at 5:01pm on Monday. This is the most likely real-world failure.

3. **Pricing contradicts itself.** "Free for members," then "$20 a year, or pay what you can," then a button that says "Join for $20." The button hides the pay-what-you-can option, which is probably the one that matters most to the people you most want to reach. Pick one model and state it plainly, e.g. "Membership: $20/year, or pay what you can. Members borrow free."

4. **Joining is undefined.** The button goes to `/join`, but step 1 says "bring photo ID the first time." Is joining online or at the desk? Does the $20 get paid online? Is there a way to join without the Saturday desk?

5. **Loan terms are missing or inconsistent.** The list says "2 days, back by Monday" and "1 week," but the H1 says "for the weekend," and no general loan period is stated. Also missing: what "clean" means, whether there's a late fee, and what happens if a tool breaks or is damaged. "It happens" is not a policy, and volunteers will get asked.

6. **No location.** "Back of the Eastgate Methodist hall" gives no street address, no map link, and no entrance directions. A flyer reader on a bus needs an address.

7. **Hours are ambiguous.** "10-1" and "6-8" read as 10pm–1am to some people. Write "10am–1pm" and "6–8pm." Also say whether it's Saturday only or Saturdays every week.

8. **"Popular this month" will be wrong within weeks.** It's a printed QR page, so the list is stale the moment the flyer goes up. Cut it, or make it evergreen ("Popular tools" with no claims about this month).

9. **Smaller issues:**
   - The H1 names a tool but never names the organisation. Someone scanning from a flyer should see "Loan Shed" first.
   - "Find Renata at the Saturday desk" puts one volunteer's name on a public page and gives Wednesday visitors no contact. Use a role ("ask any volunteer") or a general contact.
   - The email should be `<a href="mailto:lend@...">`.
   - The fragment has no `<title>`, `lang`, or viewport meta. Probably handled by your template, but confirm.
   - The page doesn't say when it was last updated. A printed flyer's details go stale quietly.

**Before it goes to print,** I'd fix items 1–4 at minimum. Items 1 and 2 would waste people's trips. Share the real domain, the Monday return plan, and the membership model, and I'll rewrite the page with them.
