## Push notification

**Title:** Flight cancelled. Rebooking needs your OK
**Body:** 9:15pm United to Boston, $640. Seat held until [7:42pm].

Put the actual clock time in the push, not "30 min". A countdown goes stale as soon as the notification sits on the lock screen.

## Approval screen

**Your 6:40pm to Boston was cancelled**

**Proposed replacement**
United [UA ####]
Denver (DEN) → Boston (BOS)
Tonight, 9:15pm → **Arrives 2:55am** (Thu, Nov 5)

**$640**, nonrefundable
Needs your approval because it's over your company's $500 limit.

⏱ Seat held until **[7:42pm]** ([28] min left). After that it may be released.

**[ Approve $640 ]** (primary button)
**[ Decline ]** (secondary button)

Small link below: *See other options*

### Notes for the build

- **Arrival is the detail she'll most want to catch.** It's 2:55am the next day, so the screen spells out the date rather than showing only "2:55am".
- **Include the expiry time and a live countdown.** The time survives a stale screen, and the countdown creates the right urgency. When the hold lapses, disable Approve and say "Seat released. Tap to find new options."
- **Fill in the placeholders from real data:** flight number, expiry time, and minutes left. I left the flight number out because I don't have it.
- **I didn't say anything about a refund or credit for the cancelled flight.** If the agent knows what happens to the original fare, add one line such as "Your original ticket will be refunded." Don't add it unless it's confirmed.
- **Decide what Decline does before launch.** I assumed it leads to "See other options", but if the agent will keep searching on its own, change the button to "Decline, keep looking". Whichever you pick, the button label should say what happens next.
- **Make Approve a single tap** with no confirmation dialog. The screen already shows the price and the nonrefundable status, and she has limited time.
