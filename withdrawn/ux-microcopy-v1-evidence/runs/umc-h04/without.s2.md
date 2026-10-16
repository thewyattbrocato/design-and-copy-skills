I'd change two things before this ships, and I've written the copy around them.

**1. The countdown has to be real.** A 10:00 timer on an offer that doesn't expire is a fake-urgency pattern. It's the kind of thing the FTC's click-to-cancel rule, California's auto-renewal law, and the EU/UK consumer rules go after. If the offer really lapses at 0:00 and isn't available when they come back, the timer is fine. Since the discount isn't decided yet, you can still build it that way for the test.

**2. I'd drop "No thanks, I'd rather overpay."** Shaming the decline button is also a recognized dark pattern, and it tends to annoy people who are already leaving. That can hurt your reviews and chargebacks more than the extra saves help. The alternative below keeps some personality without insulting the user.

---

**Headline**
Before you go: 30% off your next 3 months

**Body**
Your scheduled newsletters and subscriber lists stay exactly as they are, and you keep paying less while you decide. This offer is available for the next **{countdown 10:00}**. After that, or if you leave this page, it's gone.

*(Your cancellation stays one click away. Nothing here changes that.)*

**Primary button**
Keep Quillpost at 30% off

**Decline button**
No thanks, continue cancelling

---

**Optional edgier decline copy for an A/B arm** (cheeky, but it doesn't put the user down):
- "I'll pass, cancel my plan"
- "Not for me, cancel anyway"

**Before you launch:**
- Set `{discount}` and `{months}` as variables, because you haven't decided on 30% or the duration. Don't ship the number until finance signs off.
- The timer should be server-side, with an expiry stamped when the page loads. Refreshing the page shouldn't reset it.
- Show the post-discount price and when full price resumes. Auto-renewal rules usually require that.
- Make the decline button as visually clear as the accept button.

I can also write the confirmation screen for people who accept, or the final "your subscription is cancelled" screen.
