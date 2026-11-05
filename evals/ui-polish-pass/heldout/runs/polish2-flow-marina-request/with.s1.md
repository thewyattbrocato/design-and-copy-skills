The flow is written like a store checkout (Payment, Place order, "purchase", "booking is confirmed"), but nothing is paid and nothing is booked until the harbormaster approves. A boater would reasonably expect to be charged, or to be guaranteed a slip. The fix is only wording, with no structural changes.

```html
<ol class="steps"><li class="on">Boat</li><li>Dates</li><li>Review</li><li>Sent</li></ol>
```

```html
<!-- s2 -->
<h2>Choose your dates</h2>
...
<button>Review request</button>

<!-- s3 -->
<h2>Review your request</h2>
<p>Please check your details. Nothing is booked or charged yet.</p>
...
<button>Send request</button>

<!-- s4 -->
<h2>Request sent</h2>
<p>The harbormaster will review it and get back to you. Your slip is not booked until they approve it.</p>
```

What changed and why:
- **Step bar:** "Payment" became "Review", and "Done" became "Sent". There is no payment step, and "Done" suggests the process is finished.
- **s2:** "Choose your slip" became "Choose your dates", because the boater only picks dates and the harbormaster assigns the slip. "Continue to payment" became "Review request".
- **s3:** "Review & confirm" became "Review your request", since "confirm" implies a booking. "Place order" became "Send request". I also added a line saying nothing is booked or charged yet.
- **s4:** "Thank you for your purchase! / Your booking is confirmed." was the biggest problem, since it is false. It now says the request was sent and is pending approval.

Two things I left alone because they need your input:
- **Length unit:** "Length" has no unit. Feet or meters would help, because slip fit depends on it.
- **Contact details:** Nothing asks for an email or phone number. If the harbormaster needs to reply, the form should collect one.
