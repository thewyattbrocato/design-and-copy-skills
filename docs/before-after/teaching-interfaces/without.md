Here's a tidied version. I kept it close to your original, since it's already short and clear.

[...]

**Changes**
- **Screen 1:** I added the Oxford comma. I left the rest alone.
- **Screen 2:** The title now says "Set" instead of "Add", because the circle is already placed and the user adjusts it. The text now tells them what to do ("Drag the circle...") instead of "Draw a circle", since there's nothing to draw.
- **Skip:** I'd make the link a bit larger than "small". Small top-right links are easy to miss and hard to tap on mobile. Keep it a quiet text link, but give it a tap target of about 44px.

**One thing to check before you ship:** Screen 3 says "Your first walk is on the calendar." That's only true if the user actually filled in the form on screen 1. As you described it, screen 1 just highlights the form and offers Next, and every screen has Skip. A user who skips or taps Next without saving a walk will see a false statement, then land on an empty calendar. Your metrics show people finish fast and tickets dropped, but that wouldn't show this case.

[...]
