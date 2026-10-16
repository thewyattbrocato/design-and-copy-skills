## Handoff: Invoices screen notices

**Job of the screen:** make and send invoices. The payment failure is the only item that can stop the user from doing that, so it ranks first. The other two are informational and should not compete for the banner slot.

| Rank | Message | Loudness | Where | Dismiss / lifetime |
|---|---|---|---|---|
| 1 | Card declined, plan pauses | High, persistent | Account-level alert above the app header, shown on every screen until resolved | Not dismissible. Clears when the card is updated or the payment succeeds. |
| 2 | Portuguese invoices | Low, one-time | In the Send dialog next to the language option, with a small "New" label. A dot on the Help or What's new menu item. | Dismissed on first view. "New" label expires after about 30 days. |
| 3 | Press N for new invoice | Lowest, always available | Shortcut hint on the "New invoice" button ("New invoice  N"), plus the same hint in its tooltip | None needed. Shows as a hint, not a message. |

### Rules for the developer

- **Only one banner slot, and only the payment alert can use it.** Announcements and tips never render as banners.
- **Payment alert treatment:** full-width strip with a warning icon, the message in regular weight with the key part ("card ending 4417 was declined") in medium weight, and one button: "Update payment method." Use a warning tone for the strip, but keep the fill light. Icon plus text carry the meaning, not color alone. It is the only solid-filled control on the strip; the button should be the only thing in the header area that draws the eye.
- **Announcement:** no banner on load. The feature is discoverable where it applies, so it needs no push.
- **Tip:** a hint attached to the control it describes. Keep it visible in small, secondary text. Do not turn it into a message.

### Copy issue to fix before handoff

The payment message says the plan pauses on **14 March**. Today is 15 October 2026, so 14 March 2026 has passed. Either the date should be **14 March 2027**, or the message is stale. Include the year in the copy so it cannot be misread. Suggested copy: "Your card ending 4417 was declined. Update it by 14 March 2027 to keep your plan active."
