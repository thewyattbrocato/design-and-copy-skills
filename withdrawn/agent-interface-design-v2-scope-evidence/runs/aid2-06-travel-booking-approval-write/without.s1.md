## Push notification

**Title:** Approve new flight? Seat held 30 min
**Body:** Your 6:40pm to Boston was cancelled. United 9:15pm tonight, lands 2:55am. $640, nonrefundable.

## Approval screen

> **Your 6:40pm flight was cancelled**
> Seat held for **29:41**
>
> **United · Tonight**
> **9:15pm** Denver → **2:55am** Boston
> Arrives tomorrow morning
>
> **$640** · Nonrefundable
> $140 over your company's $500 limit, so it needs your OK.
>
> **[ Book this flight ]**
> [ Don't book ]
>
> *If you don't respond, the seat is released and nothing is booked.*

## Choices I made

- **Notification:** It gives the full decision (what happened, the new flight, the price) so she can often decide without opening it. The hold time is in the title because it's the pressure point.
- **Screen:** The countdown goes at the top and the price and reason below the flight, so she sees the time limit first and the cost second. The reason for asking ("over your limit") is one line, so it reads as a policy check rather than a problem.
- **Arrival time:** "Arrives tomorrow morning" is there because 2:55am is easy to misread as the same day.
- **Buttons:** The labels name the action. A bare "Approve" is ambiguous on a screen about a cancellation.

## Assumptions to check

- **Timeout behavior:** The footer assumes the seat is released and nothing is booked if she doesn't respond. If your agent does something else, such as keeping the search going, change that line.
- **"Don't book":** I didn't promise that the agent will keep looking. If it will, make the button "Not this one, keep looking."
- **Flight details:** I left out the flight number, fare class, and alternatives because I don't have them. A "See other options" link would suit a second line under the buttons if the agent has other seats.
- **Countdown:** It should run from the actual hold expiry, not from when the screen opens.
