**Short answer:** ask for very little. A dispatcher console isn't a consumer app, so "alive" should mean the board tells them what changed. It shouldn't mean the board moves more.

Dispatchers make about 200 assignments per shift over 10 hours, so any motion on the assign path gets paid for 200 times a shift. A 300 ms flourish costs about a minute of waiting per dispatcher per shift. It also slows the next click if input is blocked while it plays. Anything decorative will be tiresome by hour three.

**The feel to give the designer:** quiet and crisp, like a focused productivity tool. The risk is that it looks plain next to the consumer app the owner admired. You can defend that choice, because it's what keeps the board fast.

## Ask for these (ranked)

1. **Assign confirmation: the job row moves to the driver, or settles into the driver's column.**
   - *Question it answers:* did my assignment work, and where did the job go?
   - *Why it matters:* it's the highest-frequency action, and the row would otherwise vanish and shift everything below it.
   - *Spec:* about 200 ms, ease-in-out for the move between two on-screen places, using transform and opacity. Never lock the board while it plays, so the next click retargets it.
   - *Effort:* medium.

2. **Highlight on changes the dispatcher didn't cause.** This covers a new job arriving, a driver's status flipping, an ETA changing, or a job being reassigned by someone else.
   - *Question it answers:* what changed while I was looking elsewhere?
   - *Spec:* about 1 s background tint that fades out (linear opacity). A new row gets a brief highlight and no slide, so it doesn't push the list around under the cursor.
   - *Effort:* low. This is probably the best match for "alive" and also the most useful.

3. **Row insert and removal that doesn't jump.** When a job leaves the board or a new one lands, the rows below should close the gap smoothly.
   - *Spec:* 150 to 200 ms, ease-out. Don't animate the row the pointer is aiming at.
   - *Effort:* low to medium. The framework's layout-animation tools usually handle it.

4. **Press feedback on buttons and rows.** A 100 ms press state, instant hover, and a visible focus ring. It's cheap, and it confirms the click registered.

5. **Failure feedback, if assignment can fail** (a conflict or a driver gone offline). Show an inline message plus a brief color flash on the row, and put the row back where it was. Keep it small, with no shake and no modal.

Also ask for a **reduced-motion variant**. It should drop the movement but keep the highlights, color changes and focus states. Because this is a 10-hour-shift tool, make it a user setting as well as honoring the OS setting.

## Tell the owner you're not doing these

- **Hover lifts or movement on rows.** They move the target out from under the pointer.
- **Entrance animations or fades on the board at load or when switching views.** Dispatchers do this all day, and it only delays them.
- **Count-ups on totals.** They're numbers people read, and the number should simply be there.
- **Looping pulses or ambient motion.** Constant peripheral motion is fatiguing over a long shift and hides the real signals from item 2. A pulse should be reserved for something that really is urgent.
- **Stagger or bounce on lists.** With 200 jobs a shift, the last item shows up late.
- **Long or springy transitions on anything frequent.**

## How to pitch it to the owner

Tell them: "In a consumer app, motion is the product. Here, speed is the product. So the board shows what's happening live, with arrivals and changes highlighted and assignments settling into place, and it never makes a dispatcher wait." You could also have the designer prototype items 1 and 2 first and test them with two or three dispatchers before committing to the rest.

One thing would change this list: how often jobs and driver statuses update. If updates arrive many times a minute, make highlights even subtler and batch them. Otherwise the board will flicker constantly.
