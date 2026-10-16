I won't write "Only 2 seats left," a nightly-resetting timer, or "sold out within 48 hours." You've told me none of it is true, and it would mislead the people paying you $240. It also tends to backfire in a small studio. Students talk, and a repeat visitor who sees the timer reset will stop trusting you. In some places it also counts as a deceptive practice.

You do have real urgency. The class starts in five days, the room is capped at ten, and a wheel class needs a small group. Here's copy that uses that.

## Email

**Subject:** Wheel-throwing starts Monday, and there's still a seat for you
**Preview:** Six weeks, ten seats, all clay and firing included.

Hi [First name],

Our next 6-week wheel-throwing class starts **October 20**, and we have [X] of 10 seats open.

Here's what the six weeks look like:
- Week 1: centering clay, which is the hard part and the most satisfying
- Weeks 2–4: cylinders, bowls, and pulling walls
- Weeks 5–6: trimming, glazing, and finishing pieces you'll take home

**$240** covers [clay, tools, glazes, and firing. Edit to match what's true].

Classes are capped at ten so everyone gets real time with the instructor. That also means once the seats are gone, the next session is [date]. Registration closes **[Oct 19 at 5 pm]** so we can get materials ready.

**[Reserve your seat →]**

Questions? Just reply to this email.

[Your name]
Marrowfield Pottery

## Landing page block

> ### Learn to throw on the wheel in 6 weeks
> **Starts October 20 · $240 · limited to 10 students**
>
> Small groups, plenty of wheel time, and a finished set of pieces to take home.
>
> **[X] seats left. Registration closes [Oct 19].**
>
> [Reserve my seat]
>
> *Not ready? The next session starts [date]. [Get notified]*

## Optional honest countdown

This timer counts down to your real registration deadline and doesn't reset:

```html
<p>Registration closes in <span id="cd"></span></p>
<script>
  const end = new Date("2026-10-19T17:00:00"); // your real cutoff
  const el = document.getElementById("cd");
  function tick() {
    const ms = end - new Date();
    if (ms <= 0) { el.textContent = "— closed"; return; }
    const d = Math.floor(ms / 864e5), h = Math.floor(ms % 864e5 / 36e5), m = Math.floor(ms % 36e5 / 6e4);
    el.textContent = `${d}d ${h}h ${m}m`;
  }
  tick(); setInterval(tick, 30000);
</script>
```

Two more things that should help with slow sign-ups:
- **Use the real seat count.** If only 3 are left by Saturday, say so. If 7 are left, "3 seats taken" still works as social proof.
- **Add a reason to book now.** A small early bonus works, such as a free open-studio hour for sign-ups before Saturday. I can word that if you'd like.

If you tell me what's included and who teaches, I can fill in the placeholders.
