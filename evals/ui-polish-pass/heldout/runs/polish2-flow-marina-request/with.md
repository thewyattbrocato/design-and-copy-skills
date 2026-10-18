The flow is written like a store checkout, but nothing is bought or confirmed. The step bar says "Payment", the button says "Continue to payment", and the last screen says "Thank you for your purchase! Your booking is confirmed." A boater could think they have a slip when they only have a pending request.

I only changed the wording, in six places:

```html
<ol class="steps"><li class="on">Boat</li><li>Dates</li><li>Review</li><li>Request sent</li></ol>

<section id="s1">
  <h2>Vessel information</h2>
  <label>Name <input name="n"></label>
  <label>Length <input name="len"></label>
  <label>Info <textarea name="info"></textarea></label>
  <button>Next</button>
</section>

<section id="s2">
  <h2>Choose your dates</h2>
  <label>Arrival <input type="date" name="a"></label>
  <label>Departure <input type="date" name="d"></label>
  <button>Continue to review</button>
</section>

<section id="s3">
  <h2>Review &amp; send request</h2>
  <p>Please check your details. The harbormaster will review your request. No payment is needed now.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Send request</button>
</section>

<section id="s4">
  <h2>Request sent</h2>
  <p>Thanks! The harbormaster will review your request. Your slip is not booked until it is approved.</p>
</section>
```

- **Step bar:** "Payment" is now "Review", and "Done" is now "Request sent". "Done" also suggested the booking was finished.
- **s2:** The screen only collects dates and doesn't pick a slip, so the heading is now "Choose your dates". The button now goes to review, not payment.
- **s3:** The heading and button now say "send request" instead of "confirm" and "Place order". A line tells the boater that nothing is charged and that the harbormaster decides.
- **s4:** The "purchase" thank-you and "booking is confirmed" are gone. The screen now says the request was sent and that the slip isn't booked until it is approved.

I left two things alone because they're outside the flow itself. The "Length" field has no unit, and the review screen shows just "9". Adding "(ft)" to the label and the review would help. The "Info" field is also vague, and something like "Notes for the harbormaster" would be clearer. Do you want me to change those?
