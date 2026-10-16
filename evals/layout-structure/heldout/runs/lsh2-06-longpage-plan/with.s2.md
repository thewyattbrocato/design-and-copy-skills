# Ledgerlark landing page plan

**Intake.** The reader is a freelance electrician or plumber. They are probably on a phone between jobs, skeptical of "software", and short on patience. They want to know what it is, whether it handles their mess (receipts, mileage, tax), and what it costs. You have a lot of material, but it's separate chunks of different kinds: features, proof, a comparison, and a price. That makes it a **stack of full-width bands that share one content edge**, with each band shaped by its content. That's what stops it becoming a wall of boxes.

## What the top has to do

The first screen answers three things in plain words, with the action visible and no scrolling.

- **What it is:** a headline in the trade's language, such as "Bookkeeping for electricians and plumbers that you can do from the van." Name the trades. That is your strongest filter.
- **What they can do:** one line naming the loop: snap a receipt, track miles, send invoices, know your tax.
- **Why it suits them:** "$12 a month. 30 days free." This sits right by the button.
- **The action:** one primary button, "Start free trial". A quieter "Watch the demo (90 sec)" sits beside it.
- **The visual:** a phone screenshot of a receipt being categorised, shown whole and uncropped. It sits to the right on wide screens, and below the buttons when stacked.

The hero is left-aligned and asymmetric. Keep the header logo on the same left edge as the headline. On a phone the order is headline, buttons, then image, so the button stays near the top.

## Section sequence

The order follows the reader's questions.

| # | Band | Answers | Pattern | Density |
|---|------|---------|---------|---------|
| 1 | **Hero** | What is this? | Headline and CTA, with a phone image beside them | Open |
| 2 | **Demo video** | Show me | One large video, with a one-line caption | Open, with a big visual |
| 3 | **The problem, as one statement** | Is this for me? | One large sentence, e.g. "Receipts in the glovebox. Miles you forgot. A tax bill you didn't see coming." | Open, the quietest band |
| 4 | **Receipts and mileage** (the two daily-habit features) | How does it work? | Text beside a large screenshot, then flipped for the next feature | Woven |
| 5 | **Invoices and bank feed** | How do I get paid and stay current? | A flipped pair again, but with a different visual treatment (see below) | Woven |
| 6 | **Quarterly tax estimate** | The thing I dread | **The loud section.** A full-colour field, the biggest type, and one large number from the product | Loud |
| 7 | **Customer quotes** | Is it real? | Three quotes in a row, with names and trades | Full |
| 8 | **Spreadsheet comparison** | Why not what I already do? | Two columns with shared row labels: "Spreadsheet" and "Ledgerlark" | Full |
| 9 | **Price** | What does it cost? | One plan, stated plainly. No tiers to compare. | Open |
| 10 | **Closing CTA** | What now? | One line and one button, repeating the hero action | Open |

**Notes on the choices:**

- **Five features are not five cards.** Receipts and mileage get big, alternating text-and-image treatments because they are the daily habits and the easiest to picture. Invoices and the bank feed are shorter. The tax estimate is promoted to its own band because it is the emotional payoff, the thing they dread. Note that the same flipped pattern appears in 4 and 5. If it starts to feel like a template, make 5 a single wide screenshot with two short callouts.
- **Put the video second.** It is your best "show me" and it stands alone. Don't put it in a box among other boxes.
- **Don't put the comparison next to the quotes.** Both are "full" bands, so they fatigue the reader if adjacent. If you want to separate them, move the price band between them. The order would be quotes, price, comparison, closing. The cost is that the price comes before the "why not a spreadsheet" objection is answered. I'd keep the original order and accept two full bands, since the quotes row is light.
- **Quotes need to be specific.** Three quotes in a row is a fine pattern for parallel content. Make them short, with a real name and trade, and lead with the line that has a concrete outcome ("saved me two hours at tax time").
- **Put the price after the proof.** By then the $12 reads as cheap rather than as a hurdle. The $12 and the trial also appear in the hero, so nobody has to hunt for them.
- **Skip an FAQ unless you have real questions.** If you do (data security, switching from a spreadsheet, cancelling), a short list between price and the closing band fits.

## Rhythm

- **Sequence of density:** open, open, open (short), woven, woven, **loud**, full, full, open, open. The two fulls and the open runs at the ends are the weakest points, so shorten band 3 and keep band 2 visually big to stop the top feeling thin.
- **One loud band only:** the tax estimate. Everything else stays on the calm background. Use the strong colour field there and nowhere else, except possibly a tinted closing band.
- **One shared content edge:** backgrounds can run edge to edge, but text and images align to the same left edge throughout. Variation lives inside the bands: image side, background tint, scale.
- **Measure:** body text capped at about 60ch. Wide elements are images and the comparison only.
- **Named breaks:** the video runs wider than the text column because it is the demo. The tax band runs full-bleed colour because it is the loud moment. Don't add a third without a job.

## Worst cases to check

- **Narrow phone:** the stack order should read hero, video, problem statement, features, tax, proof, comparison, price, close. Check that the comparison table fits at 360px. If it doesn't, turn each row into a pair of stacked lines.
- **Quotes:** one long quote shouldn't stretch the row. Cap the length or let the cells grow equally.
- **Screenshots:** show the phone screens whole. Don't crop them into card ratios.
- **Video:** use a poster frame and don't autoplay with sound.

If you'd like, I can sketch each band as a wireframe in HTML, or draft the headline and copy for the hero and the tax band, since those two carry most of the page.
