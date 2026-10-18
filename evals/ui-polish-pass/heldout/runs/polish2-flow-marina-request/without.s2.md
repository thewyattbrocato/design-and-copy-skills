The flow is written as a store checkout, but this is a request. It mentions payment, an order, a purchase and a confirmed booking, none of which happen here. The worst part is the last screen, which tells boaters a slip is booked before the harbormaster has approved anything.

Only the wording needs to change. The structure stays the same.

```html
<ol class="steps"><li class="on">Boat</li><li>Dates</li><li>Review</li><li>Sent</li></ol>

<section id="s1">
  <!-- unchanged -->
</section>

<section id="s2">
  <h2>Choose your dates</h2>
  <label>Arrival <input type="date" name="a"></label>
  <label>Departure <input type="date" name="d"></label>
  <button>Continue</button>
</section>

<section id="s3">
  <h2>Review &amp; send request</h2>
  <p>Please check your details.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Send request</button>
</section>

<section id="s4">
  <h2>Request sent</h2>
  <p>The harbormaster will review your request. Your slip is not booked until it's approved.</p>
</section>
```

What changed:
- **Step list:** "Payment" is now "Review", and "Done" is now "Sent". "Done" suggests the process is finished, but approval is still pending.
- **s2:** The heading said "Choose your slip", but the boater only picks dates. The button said "Continue to payment", which doesn't exist, so it now says "Continue".
- **s3:** "Place order" is now "Send request", and the heading matches.
- **s4:** "Thank you for your purchase!" and "Your booking is confirmed" are replaced with text saying the request is pending approval.

Two things I didn't change because they depend on how the marina works:
- **Length unit:** The Length field has no unit. Add "(ft)" or "(m)" to the label if that applies.
- **Contact details:** The form doesn't ask for an email or phone number. The harbormaster has no way to reply with an approval or a decline unless you collect one on s1.
