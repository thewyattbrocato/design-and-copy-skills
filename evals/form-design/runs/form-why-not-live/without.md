Showing errors mid-typing flags people as wrong before they've had a chance to finish. An address like "sam@" is invalid until the last character is typed, so the user sees a red error for something they're still in the middle of doing.

Why that hurts:

- **It feels like scolding.** The error appears while the user is doing nothing wrong, which creates anxiety and friction.
- **It's noisy.** Most of what gets flagged is just incomplete input, so the message is wrong nearly every time it shows up.
- **It distracts.** Shifting text and warning colors pull attention away from typing.
- **It erodes trust.** Users learn to ignore error messages that fire constantly.

The better pattern is to validate when the user leaves the field (on blur) or submits. If an error is already showing, clear it live as soon as the input becomes valid. That gives users feedback when it's useful and keeps it out of the way when it isn't.
