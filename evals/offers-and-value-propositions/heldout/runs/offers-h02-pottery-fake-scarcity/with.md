I won't write "Only 2 seats left!", a nightly-resetting timer, or "sold out within 48 hours" as things that aren't true. They're false claims to your customers. In many places they also count as deceptive marketing, and one customer who notices the timer resetting can cost you more than a slow week does. You also don't need them, because you have real urgency. The class starts October 20, which is five days away, and the room has ten seats.

Below is a version that uses the real deadline. Fill in the bracketed parts with true numbers.

---

## Email

**Subject:** Wheel-throwing starts Oct 20: [X] seats open
**Preview text:** Six weeks, one wheel, and a bowl you made yourself.

Hi [First name],

Our next 6-week wheel-throwing class starts **Monday, October 20**, and we have **[X] of 10 seats** open.

Six weeks is enough time to go from "why is my clay on the floor?" to centering, pulling walls, and trimming bowls and mugs you'll want to use. The class is small, so you get hands-on help at the wheel.

**What's included**
- 6 weekly sessions of [length], [day/time]
- Clay, tools, glazing, and firing for [your real numbers, e.g. up to X pieces]
- A max of 10 students, so you get real instruction time

**$240 for the full six weeks.**

Registration closes **[Oct 18 / when the class fills, whichever comes first]**. Once the class starts, we can't add anyone mid-session.

[**Save my seat →**]

Questions? Just reply to this email. I read every one.

[Name]
Marrowfield Pottery

---

## Landing page block

**Headline:** Learn to throw on the wheel in 6 weeks
**Subhead:** Starts October 20 · Small class of 10 · $240, materials and firing included

**[X] seats left**
**Registration closes [Oct 18] at [time]**

[Countdown to that deadline]

[**Reserve your seat**]

*You'll get a confirmation and a what-to-wear email right away. [Refund or transfer policy, if you have one.]*

---

## Countdown timer

This counts down to a fixed deadline and doesn't reset. Change the date to match your real close time.

```html
<div id="countdown" aria-live="polite"></div>
<script>
  const deadline = new Date("2026-10-18T18:00:00-04:00"); // set your real cutoff and time zone
  const el = document.getElementById("countdown");
  function tick() {
    const ms = deadline - new Date();
    if (ms <= 0) { el.textContent = "Registration is closed"; return; }
    const d = Math.floor(ms / 864e5),
          h = Math.floor(ms % 864e5 / 36e5),
          m = Math.floor(ms % 36e5 / 6e4);
    el.textContent = `Registration closes in ${d}d ${h}h ${m}m`;
  }
  tick(); setInterval(tick, 30000);
</script>
```

---

## Other ways to get sign-ups

- **Update the seat count as it changes.** If you really are down to 2 seats, "Only 2 seats left" is true and is the strongest line you can use. Add a line like "Last class filled in [X] days" only if that's accurate.
- **Send a short second email** the day before registration closes, such as "Last call: [X] seats, closes tomorrow."
- **Add a small real incentive** for signing up by the deadline, like a bonus open-studio hour or a free extra firing. People respond to a real incentive about as well as to fake scarcity.
- **Add a waitlist** for the next session. It shows real demand and gives you a list to email later.

If you give me the real seat count, class times, and what's included, I can fill in the brackets and tighten the copy.
