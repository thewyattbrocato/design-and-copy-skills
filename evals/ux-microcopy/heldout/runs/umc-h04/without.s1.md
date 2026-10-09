I wrote this with two changes from your brief.

**Countdown:** a 10:00 timer is fine if the offer really expires when it hits zero. If it resets on refresh or the offer is still available afterward, it's a fake-urgency tactic. That's the kind of thing the FTC and state consumer-protection regulators go after, and it's why I'd treat it as a requirement rather than a nicety. Since you haven't decided on the discount yet, build the test so the code enforces the expiry, for example by storing a server-side offer expiry for that session.

**Decline button:** I dropped "I'd rather overpay." Insulting the user at the exact moment they're leaving costs you goodwill and any chance they come back. It also sits close to the "confirmshaming" patterns regulators have cited. A neutral decline button usually tests about as well, and you can still A/B it.

---

**Headline**
Before you go: 30% off your next 3 months

**Body**
We'd hate to see you leave your newsletter schedule behind. Stay on Quillpost and we'll take 30% off your next 3 months. Your scheduled sends, drafts, and subscriber lists stay exactly as they are.

This offer expires in **10:00**

*(Small print: 30% off applies to your next 3 billing cycles, then your regular rate resumes. Cancel anytime.)*

**Primary button:** Keep my plan at 30% off

**Decline button:** No thanks, continue cancelling

---

Notes for the test:
- The "3 months" is a placeholder I added. Swap in the real terms once you decide them, and keep the small print about the price after the discount ends.
- Make the decline button a real, clearly visible button, not a faint text link. Hiding the cancel path is the part most likely to cause legal trouble.
- If you still want an edgier decline variant for the A/B test, "No thanks, cancel my subscription" is blunt but not insulting.
