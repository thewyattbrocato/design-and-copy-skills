The flow is written as a purchase, but it's a request. Payment, order and "confirmed" all appear, and none of them happen. These are the smallest edits that fix it, all text only:

```html
<ol class="steps"><li class="on">Boat</li><li>Dates</li><li>Review</li><li>Sent</li></ol>

<section id="s2">
  <h2>Choose your dates</h2>
  ...
  <button>Continue</button>
</section>

<section id="s3">
  <h2>Review &amp; send request</h2>
  <p>Please check your details. Nothing is charged, and the harbormaster must approve your request.</p>
  ...
  <button>Send request</button>
</section>

<section id="s4">
  <h2>Request sent</h2>
  <p>The harbormaster will review it. It isn't a booking until they approve it.</p>
</section>
```

- **Step bar:** "Payment" becomes "Review", since there's no payment step. "Done" becomes "Sent", because the request isn't finished until it's approved.
- **s2:** The boater picks dates, not a slip. The harbormaster assigns the slip, so the heading is now "Choose your dates". "Continue to payment" would lead people to expect a card form.
- **s3:** "Place order" becomes "Send request", and the added line says no money is taken and approval is still needed.
- **s4:** "Thank you for your purchase!" and "Your booking is confirmed." were both false. The new text says the request is sent and the booking isn't confirmed yet.

I left two things alone to keep the change small. You may want to fix them too:
- "Length" has no unit. "Length (ft)" or "Length (m)" would help.
- "Info" is vague. A label like "Anything the harbormaster should know" would work better.
