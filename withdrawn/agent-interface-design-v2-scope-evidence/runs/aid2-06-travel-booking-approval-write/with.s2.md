**Push notification**

> **Approve a $640 rebooking? Held for 30 min**
> Your 6:40pm to Boston was cancelled. Seat on United 9:15pm tonight, arrives 2:55am. Needs your OK.

**Approval screen** (opens from the notification)

> **Your 6:40pm flight was cancelled**
> I found a replacement. Held for you until **[7:42pm]** (28:14 left)
>
> **United · Tonight**
> Denver **9:15pm** → Boston **2:55am** (arrives tomorrow)
>
> **$640**, nonrefundable
> Over your company's $500 limit, so I need your OK before I buy.
>
> **[ Book for $640 ]**
>
> **[ Not this one ]**
>
> See other options · Talk to a person
>
> *If you don't answer, the hold lapses and I won't book anything. You can still ask me to look again.*

**Design notes**
- **Placeholders:** The bracketed expiry time and the countdown should come from the real hold timestamp. I left out a flight number, a fare comparison with the cancelled ticket, and any other options, because I don't have those facts.
- **Notification:** It leads with the decision and the deadline. The flight details are enough to say yes from the lock screen, but the buy button is only on the screen, so one tap can't spend $640.
- **"Not this one":** I used this instead of "Decline" because it leaves her free to ask for something else. It should open a short choice: look for other flights, or I'll handle it myself.
- **Reminder:** If she hasn't responded with about 10 minutes left, send one follow-up. That's the only repeat I'd allow.
- **Expiry:** When the hold lapses, send a single "Hold expired, nothing was booked" message with a button to search again.
