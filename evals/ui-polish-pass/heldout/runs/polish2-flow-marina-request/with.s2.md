The flow is written like an online checkout, but it's a request that the harbormaster approves. Payment, order, purchase and "confirmed" all promise something that doesn't happen. I only changed the copy that says that.

```html
<ol class="steps"><li class="on">Boat</li><li>Dates</li><li>Review</li><li>Requested</li></ol>

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
  <button>Continue</button>
</section>

<section id="s3">
  <h2>Review &amp; send request</h2>
  <p>Please check your details. Nothing is charged, and your slip isn't held until the harbormaster approves.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Send request</button>
</section>

<section id="s4">
  <h2>Request sent</h2>
  <p>The harbormaster will review your request and get back to you. Your slip is not booked until it's approved.</p>
</section>
```

What changed and why:
- **Step bar:** "Payment" is now "Review" and "Done" is now "Requested". The old labels implied a payment step.
- **s2:** The heading said "Choose your slip", but the screen only asks for dates, so it's now "Choose your dates". The button "Continue to payment" is now "Continue".
- **s3:** "Place order" is now "Send request". I added one sentence saying nothing is charged and nothing is held yet.
- **s4:** "Thank you for your purchase! Your booking is confirmed." was wrong on both counts. It now says the request was sent and the booking isn't confirmed until approval.

I left a few other things alone to keep the change small. You may want to look at them later:
- **Units:** Length has no unit (feet or meters?).
- **Label:** "Info" is vague.
- **Contact details:** There's no field for an email or phone number, so the harbormaster has no way to reply.
