# Kilnside Glaze Club: Welcome Series

## Email 1: Welcome

**Send:** Immediately after sign-up.
**Subject:** Welcome to the club (you're officially a glaze nerd)
**Preview:** Your first box ships on [ship date]. Here's what to expect.

Hi [First name],

Welcome to Kilnside Glaze Club! We're Marit and Dov, and we spend way too many hours in our Duluth garage testing glazes so you don't have to. Each month you'll get three 4 oz jars of tested glaze, a printed card with firing range and application notes, and a test tile to try them on.

Everything is cone 6, made for mid-range electric kilns. (No cone 10, no raku. We're specialists.)

Your first box ships on [ship date]. As a new member, you also get our free PDF guide to testing glazes on tiles. [Download it here]

Got a question? Just reply to this email. It goes straight to Marit or Dov.

Happy firing,
Marit & Dov

## Email 2: Join the Discord

**Send:** 3 days after sign-up.
**Subject:** Come say hi in the members' Discord
**Preview:** About 30 members are already in there, and the kiln talk is good.

Hi [First name],

Our members-only Discord is where the club actually lives. About 30 potters are in there already, swapping kiln quirks, test tile photos, and the occasional glaze disaster. [Join the Discord]

Introduce yourself and tell everyone what you're hoping to make. Nobody's expecting you to be an expert. Most of us are still figuring out why our glazes run. Good first posts are a photo of your studio, your kiln model, or your most embarrassing test tile. Honest failures are welcome here.

If you're waiting on your first box, use the time to read the PDF guide and get a tile board ready.

Got a question about your box? Reply to this email and it goes straight to Marit or Dov. The Discord is for everything else.

See you in there,
Marit & Dov

## Email 3: Your Box Is Coming

**Send:** 2 days before the member's first ship date (the 3rd, for a 5th ship).
**Subject:** Your first box ships on the 5th
**Preview:** Three glazes, one card, one tile. Here's what to expect when it lands.

Hi [First name],

Your first box ships on the 5th, so it's almost here. Inside:

- Three 4 oz jars of tested glaze
- A printed card with firing range and application notes
- One test tile

Read the card before you open the jars. Each glaze's range and application notes are on it, and they're worth five minutes. Everything is cone 6 only, so check that the range matches your mid-range electric kiln before you fire.

Our tip: test every glaze on a tile before it touches a real pot. The PDF guide walks through the method step by step, so if you haven't read it yet, start there. Keep a notebook handy and log each test. Future you will thank you.

Anything about the box you're unsure of? Reply and it goes to Marit or Dov.

Cheers,
Marit & Dov

## Email 4: How Did It Go?

**Send:** About 10 days after the first box ships, so there's time to fire the tile.
**Subject:** How'd your first box go?
**Preview:** Tell us what worked, what exploded, and what you'd fire next.

Hi [First name],

It's been about ten days since your first box shipped, which should be enough time to get a tile fired. How did it go?

We'd love to know:

- Which glaze surprised you, good or bad
- What you'd change about the firing
- What you'd want in a future box

Just hit reply and it goes straight to Marit or Dov. Photos are welcome in the Discord too. Other members will want to see your tiles. Tile fails count too. Those teach the most.

Boxes ship the first week of every month, and you can cancel anytime from your account page. Thanks for being one of the first members. You're helping us figure out what a good box looks like, and we're grateful for every bit of feedback.

Cheers,
Marit & Dov

---

**Things to check before sending:**

- **Ship date in Email 1.** A sign-up after the 28th ships on the 5th of the month after next, so a hard-coded "5th of next month" would be wrong for those members. Use a merge field like `{{ship_date}}` and compute it from the sign-up date.
- **Email 3 timing.** Trigger it from each member's own ship date, not a calendar date. Otherwise late sign-ups get the "ships on the 5th" email before they have a box.
- **Placeholders.** Fill in `[First name]`, `[ship date]`, the PDF link, and the Discord invite link.
- **Discord details.** Email 2 describes what people post in the Discord. Adjust it if that doesn't match how your server actually runs.
