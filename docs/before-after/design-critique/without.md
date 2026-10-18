**Fix before printing**

1. **The headline promises something your hours don't allow.** You're open Saturday 10-1 and Wednesday 6-8, but the headline says to return it by Monday 5pm. If nobody is there on Monday, either there's a drop box or the promise is wrong. The page doesn't say which.

2. **The loan periods don't fit the hours.** Counting from the days you're open:
   - Wet tile saw, 2 days: Saturday pickup means a Monday return, and you're closed.
   - Pressure washer, 2 days: a Wednesday pickup means Friday, and a Saturday pickup means Monday. You're closed both times.
   - Post hole digger, 3 days: Saturday pickup means Tuesday, and you're closed.
   - Only the 1-week sander lines up.

   Either say "back at the next open session" or explain the return arrangement. As written, a first-timer will turn up on Monday to a locked hall.

3. **The button contradicts the copy.** The text says "$20 a year, or pay what you can", but the button says "Join for $20". Someone who can't afford $20 will see the button and leave. Use something like "Join (from $0, suggested $20)", or make sure `/join` shows the sliding scale up front.

4. **There's no viewport meta tag, `<html lang>`, `<title>` or doctype.** The page is only reached by QR code, so everyone will be on a phone. Without `<meta name="viewport" content="width=device-width, initial-scale=1">`, most mobile browsers render a shrunken desktop layout. This is the most likely thing to make the page look broken.

5. **There's no address.** "The back of the Eastgate Methodist hall" doesn't tell a newcomer where to go. Add a street address and, ideally, a map link and where to find the entrance. Also add "am" and "pm" to the hours.

6. **`lend@loanshed.example` is a placeholder domain.** If that's the real address, fine. If it's a stand-in, a printed flyer with a dead address is the sort of mistake you only catch after it's printed.

**Should fix**

7. **The photo ID requirement is buried at the end of step 1.** People who dislike handing over ID will find out at the desk. Say what counts as ID and why you ask for it. Say whether `/join` is completed online or in person.

8. **Some basics are missing.** There's nothing on what "clean" means, late returns or fees, deposits, or whether the tile saw and other risky tools need a quick induction. Committee members will ask. A line each is enough, even "no late fees, just tell us".

9. **The headline leads with the rule, not the benefit.** "Return it clean by Monday 5pm" is a condition, and it's the first thing people read. Try "Borrow a tile saw for the weekend. Free for members." and put the return rule lower down.

10. **"Popular this month" will go stale.** If someone has to edit it by hand each month, it won't get updated. Either automate it or rename it "Things people borrow a lot".

11. **Naming Renata on a public page has costs.** Volunteers move on, and it's their name on the open web. "Find a volunteer at the Saturday desk" ages better.

**Minor**

- Two adjacent `<a>` buttons with no wrapper or spacing may touch on mobile. Check the CSS.
- The `<strong>Wet tile saw</strong>:` pattern is fine, but "2 days, back by Monday" duplicates the problem in item 2.
- The only call to action is "Join". There's no "come see us Saturday" for people who aren't ready to commit.
- Test the QR code on a phone off your Wi-Fi, in the printed size and on the printed paper.

Items 1, 2 and 4 are the ones I wouldn't print without fixing. If you tell me how Monday returns actually work, I can rewrite the headline and the list to match.
