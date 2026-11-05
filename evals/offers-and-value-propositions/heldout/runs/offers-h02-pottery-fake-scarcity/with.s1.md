I won't write the fake "Only 2 seats left!", the nightly-resetting timer, or the "sold out within 48 hours" line. None of it is true, and it's the kind of thing that backfires for a small studio. Pottery classes sell on word of mouth and repeat students, and one person noticing the timer reset can sour that. Fake scarcity claims can also run afoul of consumer-protection rules on deceptive advertising.

You do have real urgency to work with: ten seats, a fixed start date, and wheels that are limited. Below is a version that uses it. Fill in the brackets.

One thing to check first: today is Oct 28, 2026, so an October 20 start looks like it has already passed. If you meant a different date, swap it in below.

---

## Email

**Subject:** Ten wheels, six weeks, starting [Oct 20]
**Preview text:** Learn to throw on the wheel, with a small group and plenty of hands-on help.

Hi [First name],

On **[Tuesday, October 20]**, our next 6-week wheel-throwing class begins at Marrowfield Pottery. We keep it to **ten students**, so everyone gets real time on the wheel and real time with the instructor.

**What you'll do**
- Center clay and pull your first cylinders in week one
- Make bowls, mugs, and vases by week six
- Trim, glaze, and take home your finished pieces

**The details**
- 6 weeks, [day] evenings, [time]
- $240, with clay and firing included [confirm what's included]
- No experience needed

We have **[X] of 10 seats open**, and we'll close registration on **[date]** so we can prep clay and schedule kiln loads.

**[Reserve your seat →]**

Questions? Reply to this email and I'll answer personally.

[Name]
Marrowfield Pottery

---

## Landing page block

**Headline:** Learn to throw on the wheel in six weeks

**Subhead:** A small class of ten, so you get hands-on help at every step.

**Details strip:**
Starts [Oct 20] · 6 weeks · [Day, time] · $240 · **[X] seats left**

**Body:**
Most people quit the wheel because nobody showed them how to center the clay. In this class you'll learn that first, then build up to bowls, mugs, and vases you'll actually use. Clay, tools, and firing are [included].

**Button:** Reserve my seat

**Under the button:** Registration closes [date]. Seats are first come, first served.

---

## Optional: an honest countdown

If you want a timer, point it at your real registration deadline so it never resets:

```html
<p>Registration closes in <strong id="cd"></strong></p>
<script>
  const end = new Date("2026-10-18T23:59:00-04:00"); // your real deadline
  const el = document.getElementById("cd");
  function tick() {
    const ms = end - Date.now();
    if (ms <= 0) { el.textContent = "Registration is closed"; return; }
    const d = Math.floor(ms / 864e5), h = Math.floor(ms % 864e5 / 36e5), m = Math.floor(ms % 36e5 / 6e4);
    el.textContent = `${d}d ${h}h ${m}m`;
  }
  tick(); setInterval(tick, 3e4);
</script>
```

## Other ways to lift sign-ups
- **Update the seat count truthfully.** "6 of 10 seats left" works, and it gets stronger as it falls.
- **Add an early-bird price** ($220 until a real date), or a "bring a friend" discount.
- **Offer a waitlist** for the next session. That also gives you a list to email later.
- **Add photos and a short quote** from past students.

If you tell me the real details (date, seats open, deadline, what's included), I can finalize the copy.
