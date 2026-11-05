The page reads well, but I found several problems that could embarrass you in front of the committee. Worst first.

## Will cause real problems

1. **The headline contradicts your opening hours.** You say "return by Monday 5pm", but you're only open Saturday 10-1 and Wednesday 6-8. Nobody can hand a tool back on Monday. The same problem runs through the popular list:
   - Wet tile saw and pressure washer, 2 days: borrowed Saturday, due Monday, shed closed.
   - Post hole digger, 3 days: due Tuesday, closed.
   - Only the 1-week sander lines up with your hours.

   Either there's a Monday drop-off (a locker, a box, a volunteer) and the page doesn't say so, or the loan periods are wrong. Fix this before printing, because it's the first thing a confused borrower will ask.

2. **There is no address.** You say "back of the Eastgate Methodist hall" with no street address, no map link, and no entrance info. The flyer sends people to this page, and this page doesn't tell them where to go. Add the address, a "Directions" link, and which door to use.

3. **`lend@loanshed.example` is a placeholder.** `.example` is a reserved domain, so mail to it goes nowhere. Replace it, and make it a `mailto:` link so phone users can tap it.

4. **The HTML is a bare fragment.** It has no `<!doctype>`, `<html lang>`, `<title>`, or `<meta name="viewport">`. Everyone arriving from the QR code is on a phone, and without the viewport tag many phones render the page at desktop width, shrunk to tiny text. Also wrap the content in `<main>`. I haven't seen your CSS, so I can't vouch for how `.btn` and `.btn-secondary` look.

## Messaging problems

5. **"Pay what you can" conflicts with the "Join for $20" button.** Someone who can't afford $20 sees the button and assumes the offer isn't for them. Try "Join (from $0, suggested $20)", or put a "pay what you can" note directly under the button. Also decide whether there's a floor, and whether the signup form actually lets people pick an amount.

6. **The photo ID requirement is buried in step 1.** People will show up without ID and get turned away. Say what counts as ID, and whether joining online and showing ID in person are two separate steps. As written, it's unclear whether `/join` completes the process.

7. **Safety and liability are missing.** You lend wet tile saws and pressure washers to the public. The committee will ask about inductions, PPE, a waiver or insurance, and what happens when a tool is late or damaged. "It happens" is warm, but it will worry a treasurer. Even one line helps, for example "Our volunteers will show you how to use anything unfamiliar."

8. **The headline leads with a rule, not the benefit.** "Return it clean by Monday 5pm" is the least inviting part of the pitch. Try something like "Borrow a tile saw for the weekend. Free for members." Keep the return rules for the how-it-works section.

## Smaller things

- **"Popular this month" will go stale.** Someone has to update it monthly. Rename it "Popular tools" or drop it, unless you have a plan for keeping it current.
- **Hours are ambiguous.** "10-1" should be "10am-1pm", and "6-8" should be "6-8pm". Also say whether holidays change them.
- **Naming Renata is fragile.** Volunteers move on, and the flyer will outlast the rota. Use "the Saturday desk" or "ask any volunteer in a Loan Shed shirt."
- **The only contact is email.** A phone number or social link helps people who are standing outside a locked hall.
- **Wording:** "400-odd" is fine for a volunteer-run library, but "Return it clean" and "Bring them back clean" repeat the same instruction. The list punctuation (`Wet tile saw: 2 days`) is fine.

## Before printing

- Scan the actual QR code on a phone, and confirm that it points to a permanent URL and that `/join` and `/catalogue` both resolve.
- Confirm the QR code still works if the site moves, for example by using a redirect you control.

If you tell me the real return arrangement and the address, I can rewrite the page with a proper `<head>` and fixed copy.
