Most of this was already solid, so I made light edits.

| Screen | Element | Revised copy |
|---|---|---|
| 1 | Title | Reset your password |
| 1 | Body | Enter your account email and we'll send you a reset link. |
| 1 | Button | Send reset link |
| 1 | Error (email not found) | We couldn't find an account with that email. Check for typos or try another address. |
| 2 | Title | Check your email |
| 2 | Body | We sent a reset link to **{email}**. It expires in 60 minutes. Don't see it? Check your spam folder or [resend it]. |
| 2 | Link | Resend link |
| 3 | Title | Choose a new password |
| 3 | Button | Save password |
| 3 | Success toast | Password updated. You're signed in. |

**What changed and why**
- **Screen 1 body:** "the email you signed up with" became "your account email". It's shorter and means the same thing.
- **Screen 2 body:** I added "reset" before "link" so the screen matches the Screen 1 button. "Didn't get it?" became "Don't see it?", which is shorter and fits the moment better because the email may have arrived somewhere else. I also made the resend action inline so the body and the link don't repeat each other.
- **Screen 2 link:** "Resend link" is shorter and matches the button's wording.
- **Everything else:** I left the titles, the button labels, the error and the toast alone. They're clear, consistent and in the same voice.

**Two things to check before shipping**
1. **Account enumeration:** The Screen 1 error confirms whether an email has an account. If that matters for Tallow, use a neutral flow instead. Always go to Screen 2 and say "If an account exists for {email}, we sent a reset link." That would also let you drop the error state.
2. **Screen 3 gaps:** There's no error copy for an expired or already-used link. That's a likely dead end, and it needs something like "This link has expired. Request a new one." with a button back to Screen 1. Also add a hint about password requirements if you enforce any.

I can draft the expired-link and validation error copy if you'd like.
