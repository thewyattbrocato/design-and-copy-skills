**Banner text**

> **Error 4012: Session timeout**
> You were signed out after 15 minutes of inactivity. Anything you typed into a form you hadn't submitted was lost. Your booked appointments are not affected. Sign in with your usual email and password to continue.

**Button label**

> Sign in again

Notes:
- The required string appears as the banner's first line, word for word, as visible text. It isn't softened, and it isn't in a tooltip.
- I'd render it as its own bold line, so it stays on one line in screenshots and is easy to grep. Don't let it wrap or get truncated on narrow screens.
- The reassurance about booked appointments comes before the sign-in instruction. That way people see it before they worry about their bookings.

I haven't changed any files. Your repo isn't in this directory, so tell me where the banner string lives if you'd like me to drop it in.
