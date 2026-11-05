## Push notification

**Title:** Approve $640 rebooking? Seat held 30 min
**Body:** Your 6:40pm to Boston was cancelled. United 9:15pm tonight, lands 2:55am. Tap to review.

## Approval screen

> **Your 6:40pm Denver flight was cancelled**
> I found a replacement. It needs your OK because it's over your $500 limit.
>
> **United · tonight**
> **9:15pm** Denver (DEN) → **2:55am Thu** Boston (BOS)
>
> **$640**, nonrefundable
> $140 over your company's $500 auto-approve limit
>
> ⏱ **Seat held for 28:41**
> If you don't respond, the hold is released and nothing is booked.
>
> **[ Book this flight · $640 ]**
> **[ Don't book ]**

## Design notes

- **The notification carries the decision.** The price, the 30-minute hold, and the new flight are all in it. The late arrival is there too, since she might say no because of it. She can tell what's being asked before opening the app.
- **The screen opens with what happened, then what's needed.** Between meetings she may have forgotten which trip this is.
- **Reasons for asking are on the screen.** It states the price, the limit, and the amount over. That makes the approval request look legitimate and keeps her from having to wonder why she was interrupted.
- **Nonrefundable sits next to the price.** It's the irreversible part, so she sees it before she taps.
- **"Thu" is on the arrival time.** A flight that lands at 2:55am is easy to misread as the same day.
- **The countdown is a live timer.** I didn't write a clock time because I don't know the hold's expiry. If you have it, a line like "until 7:42pm" under the timer helps when she glances at it later.
- **The button label repeats the price.** "Book this flight · $640" makes the tap a deliberate confirmation. Declining is a plain outlined button, not a warning.

## Things to check on your side

- If the agent can offer alternatives, such as a different flight or a rebooking that the airline covers, add a "See other options" link. I left it out because I don't know whether the agent can do that.
- If the cancelled ticket is refundable or credited, one line about it would help her judge the $640. I didn't state anything about it because the details weren't given.
- Send a reminder when about 5 minutes remain on the hold. After expiry, the notification should update to "Hold expired. Nothing was booked." so she doesn't tap into a dead screen.
