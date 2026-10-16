# Two-week plan: validating the pet-insurance add-on

**Assumptions:** consumer marketplace, you can email past bookers, and there are no existing interviews on this topic.

## The decision this feeds
At the planning meeting, will you propose (a) building the add-on, (b) a smaller step first, or (c) not doing it? A wrong "build" costs a quarter or more of engineering plus an insurance partner. So the aim isn't to "validate" the idea. It's to find out what would make it right or wrong, so the VP can decide with evidence.

Interviews can't tell you whether people will pay. They can tell you whether the problem it solves is real, and whether checkout is where people would think about it. Say that to the VP up front.

## Week 1: use what you already have (about 3 hours of your time, 1 hour of the designer's)
Look for these in existing data. Report counts as "n of N" and note where each source is biased:
- **Support tickets and sitter messages:** how many mention a vet bill, an injury, an illness, a lost dog or damage during a stay? What happened, and who paid?
- **Incident or claims records, if you have them:** how often do bad events happen per booking, and what do they cost? This sizes the real problem.
- **Checkout analytics:** which add-ons exist today, what share of bookers take them, and where people drop off. This tells you how much price sensitivity and friction to expect.
- **Reviews and app-store comments:** do people mention worry or trust?
- **Sales or ops notes** from anyone who has fielded this request.

Also ask a non-customer question now: **can you legally and practically offer insurance?** It's regulated, usually needs a licensed underwriting partner, and may be sold differently by state. Ask legal or finance for a one-paragraph answer. If it's a six-month blocker, that changes the meeting more than any interview will.

## Week 1–2: 6 to 8 conversations (30 minutes each, you run them)
Run them yourself and have the designer take notes. The designer is better as a second pair of ears than as the facilitator.

**Who to recruit:**
- Dog owners who booked a sitter in the last 60 days.
- A mix of people who had something go wrong or cost money (a vet visit, damage, a scare) and people who didn't.
- Optionally 2 sitters, since they carry the liability when something happens.
- Email recent bookers and offer a small booking credit if you're allowed to. If not, ask plainly and expect a lower response rate.

**Screener:** "Booked a sitter in the last 60 days" plus a couple of unrelated care questions, such as boarding or grooming. Don't mention insurance or the add-on. Exclude anyone who works in pet services or insurance.

**Ask about real past events, not predictions:**
1. Walk me through the last time you left your dog with a sitter. What did you do before and after you booked?
2. What, if anything, worried you? What did you do about it?
3. Tell me about the last time your dog had a health issue or an unexpected vet bill. What happened, and how did you pay?
4. What coverage or plan do you have for your dog now, if any? How did you choose it?
5. If something went wrong at a sitter's, who did you expect to handle it, and who pays?
6. Near the end, show a mock of your checkout page with the add-on slot. Ask them to talk through what they notice and what they'd do. Don't ask "would you buy this?"

Ask in that order. If you mention the add-on early, you'll get polite answers instead of real ones.

## Optional: a fake-door test
If checkout traffic is high enough, you could put a non-binding "Add protection" line at checkout that leads to a "coming soon" page. Treat the result as a lead, not proof. Choose the one metric before you start (click rate on that line), and run it for whole weeks. It also shows a option that doesn't exist at the point of payment, so check with legal or brand that you're comfortable with that.

## What to bring to the meeting (one page)
- The decision and what you found, each point with its source ("4 of 7 interviewees…", "tickets show…").
- What's still unknown, and the cheapest next check.
- A recommendation: build, test smaller (such as a partner-referral link instead of a built-in product), or drop it.
- Which evidence would change that recommendation.

## Time budget
| Who | Task | Hours |
|---|---|---|
| You | Data review and legal question | ~3 |
| You | Recruit, run and write up 6–8 conversations | ~8–10 |
| Designer | Checkout mock, note-taking, helping with synthesis | ~6 (their full budget) |

## What a human has to do
Someone has to send the recruiting emails, get consent to record or take notes, run the conversations, and get answers from legal and analytics. I can draft the email, the screener or the full guide next if you want.

If you can't get 6 recent bookers in time, go with 4 and say so. Four conversations plus real data is still better than a survey.
