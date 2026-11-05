**Fix before printing:**

1. **The return promise can't be kept.** The headline says "Return it clean by Monday 5pm," but the shed is only open Saturday 10-1 and Wednesday 6-8. Nothing says where to return a tool on a Monday. Is there a drop box, an after-hours return, or should people bring it back Wednesday? Until that's answered, the headline makes a promise the building can't keep.

2. **`lend@loanshed.example` is a placeholder.** `.example` is a reserved domain and won't receive mail. Replace it with a real address, send a test, and check that someone reads it.

3. **There's no address.** "At the back of the Eastgate Methodist hall" doesn't help someone who scanned a QR code on a noticeboard. Add the street address, which door to use, and a map link. Add a phone number too, since some people won't email.

4. **The page never names the org in its heading.** "Loan Shed" appears only in the second paragraph. The h1 should start with it, or the page needs a header with the name, so a scanner knows whose page they're on.

**Questions the committee will get asked:**

5. **The pricing contradicts itself.** The button says "Join for $20," but the body says "or pay what you can." Anyone who can't pay $20 sees the button and leaves. Either show the sliding option on the button or on the join page, or say how to choose it. Also clarify whether non-members can borrow ("free for members" implies they can't, or pay something).

6. **Borrowing terms are missing.** People will ask about deposits, late fees, what happens if a tool is damaged, whether there's a minimum age, and whether a tile saw or pressure washer needs a induction. "If something breaks, tell us, it happens" reads as "no consequences." State what happens: do they pay for repair or replacement, or does the library cover it?

7. **"Clean" is undefined.** Give one concrete example per tool, or a line like "rinse the blade and clear the tray." Otherwise you'll get returns that don't meet the committee's standard.

8. **"Popular this month" will be wrong next month.** On a printed flyer it goes stale immediately, and it doesn't show availability, so it sends people to tools that are already out. Cut it from the print version.

9. **The join step is ambiguous.** "Join (bring photo ID the first time)" doesn't say whether joining happens online or in person. If it's online, say that ID is needed at the first pickup.

10. **Naming Renata on a printed flyer goes stale.** Use "the Saturday desk" or a role-based contact instead of a person who could move on. Also, "ask a volunteer on the day" implies Wednesday help, but the Renata line only covers Saturday.

**Print and QR:**

11. **Print the URL under the QR code.** Black-and-white photocopies lose the code, and some people won't scan. Also, point the QR at a short, stable URL rather than `/join`, so it can be reused.

12. **If this is the whole document, it's missing the basics.** There's no doctype, `<title>`, `lang`, or viewport meta tag. Phones will render it badly and the page title will be blank.

**Priority:** items 1–4 are blockers. If you tell me the return arrangement, the real email, and the address, I'll rewrite the page with the terms, pricing, and print fixes included.
