The flow treats the request as a purchase: it has a Payment step, a "Place order" button, and a "Your booking is confirmed" message. Nothing is paid and nothing is booked until the harbormaster approves it. Here is the corrected markup with the text and step changes only:

```html
<ol class="steps"><li class="on">Boat</li><li>Dates</li><li>Review</li><li>Done</li></ol>

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
  <h2>Review &amp; submit request</h2>
  <p>Please check your details. Submitting sends a request to the harbormaster. It is not a booking until it is approved.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Submit request</button>
</section>

<section id="s4">
  <h2>Request submitted</h2>
  <p>Thanks. The harbormaster will review your slip request and contact you. You will receive a booking confirmation only after it is approved.</p>
</section>
```

**Changes:**
- Step 3: "Payment" → "Review". Nothing is paid.
- s2 heading: "Choose your slip" → "Choose your dates". The screen only collects dates, so the old heading promised a slip choice that doesn't exist.
- s2 button: "Continue to payment" → "Continue to review".
- s3 heading: "Review & confirm" → "Review & submit request", so it's clear that submitting doesn't confirm anything.
- s3 text: added one sentence saying it's a request and not a booking until approved.
- s3 button: "Place order" → "Submit request".
- s4 heading: "Thank you for your purchase!" → "Request submitted". The old heading was wrong for a request flow.
- s4 text: "Your booking is confirmed" → the request is pending, and confirmation comes only after approval.

**Not changed, but worth fixing in the app code:**
- The s3 values (Sea Wren, 9, the dates) are hardcoded. They need to be filled from what the boater entered in s1 and s2.
- The Info field collected in s1 isn't shown on the review screen. Add it if the harbormaster needs it.
- Nothing stops a departure date before the arrival date. Add a `min` on the departure input tied to the arrival value, or validate it on submit.
