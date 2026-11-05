The copy is good: it's concrete, warm, and tells people what to do. The problems are in the logistics it implies and in the missing basics. In order of severity:

**Fix before printing**

1. **You can't return it by Monday 5pm.** You're open Saturday 10-1 and Wednesday 6-8, so there's no Monday opening. The headline, the tile saw ("back by Monday") and the pressure washer ("2 days") all promise something the hours contradict. The same goes for the post hole digger: 3 days from Saturday is Tuesday, and you're closed. If there's a drop box or an arrangement, say so. If there isn't, the headline is wrong.

2. **No address.** "The back of the Eastgate Methodist hall" doesn't help a stranger who scanned a flyer. Add the street address, a map link, and which door to use. People will walk around the hall looking for you.

3. **`lend@loanshed.example` is a placeholder.** `.example` is a reserved TLD and can never receive mail. If that's the real address, it will bounce. If it's a stand-in, replace it. Make it a `mailto:` link too.

4. **The page isn't a valid mobile page.** There's no doctype, `<html lang>`, `<title>` or `<meta name="viewport">`. Without the viewport tag, phones render it at desktop width with tiny text, and a QR page is read almost entirely on phones. Even if your template adds these, check that it does.

5. **"Join for $20" contradicts "pay what you can."** The only button tells people who can't afford $20 that the price is $20. Rename it "Join" and say "$20, or pay what you can" on the `/join` page and next to the button. Otherwise the pay-what-you-can policy is invisible to the people it's meant for.

**The committee will ask about these**

6. **Nothing on safety or liability.** You're lending wet tile saws and pressure washers to the public with no mention of induction, a waiver, a deposit, or late fees. The page doesn't have to carry all of that, but "What if I'm late?" and "What if I've never used one?" are the first two questions you'll get.

7. **The ID step is unclear.** Step 1 says "Join (bring photo ID the first time)", but the button joins online. Can I join and pay online and show ID later, or do I have to come in? Spell out the order.

8. **"Popular this month" will go stale.** It's a printed flyer pointing at a permanent URL. Rename it "Popular tools" or "Most borrowed", or accept that someone must update it monthly. The durations ("2 days", "1 week") also don't say what they are. Write "loan: 2 days".

9. **Naming Renata.** It's friendly, but flyers outlive volunteer rosters. Use "ask at the Saturday desk" instead, or accept that the flyer needs a reprint when Renata moves on.

**Smaller things**

- "Loan Shed" never appears in a heading, only in the first paragraph. Someone landing from a QR code should see the name straight away.
- "10-1" and "6-8" have no am/pm. It's obvious, but cheap to fix.
- Check whether the hours change on holidays or over winter.
- The hours sit between the pitch and the buttons, so they're easy to miss. They're the most important logistical fact on the page, so consider giving them their own line.

**Print checks (I can't see the QR code)**

- Scan it from the printed proof at final size, on a cheap phone, in bad light.
- Use a short, stable URL with no tracking parameters, so the code stays simple and scannable.
- Put the URL in small text under the code for people who can't scan it.

I'd fix #1 first, because the page's main promise breaks on contact with your own opening hours. Do you have a Monday drop-off arrangement I should be writing around, or is that a real gap?
