The flow was built as a purchase, but it's a request. The "Payment" step has no payment fields, and the last two screens say "Place order," "purchase," and "booking is confirmed." Those words tell the boater they've paid and are booked, before the harbormaster has approved anything. The fix is to change the labels and copy so the flow matches a request. The structure stays the same.

```html
<ol class="steps"><li class="on">Boat</li><li>Dates</li><li>Review</li><li>Submitted</li></ol>

<section id="s1">
  <h2>Vessel information</h2>
  <label>Name <input name="n"></label>
  <label>Length <input name="len"></label>
  <label>Info <textarea name="info"></textarea></label>
  <button>Next</button>
</section>

<section id="s2">
  <h2>Choose your slip</h2>
  <label>Arrival <input type="date" name="a"></label>
  <label>Departure <input type="date" name="d"></label>
  <button>Review request</button>
</section>

<section id="s3">
  <h2>Review &amp; submit</h2>
  <p>Please check your details. Submitting sends a request to the harbormaster. Your slip is not reserved until the harbormaster approves it.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Submit request</button>
</section>

<section id="s4">
  <h2>Request submitted</h2>
  <p>Your request has been sent to the harbormaster. It is not a booking until it is approved. We'll notify you when the harbormaster decides.</p>
</section>
```

**Changes:**
- Step 3 label: "Payment" → "Review". Step 4 label: "Done" → "Submitted".
- s2 button: "Continue to payment" → "Review request".
- s3 heading: "Review & confirm" → "Review & submit". Added a line saying the slip isn't reserved until approval. Button: "Place order" → "Submit request".
- s4 heading: "Thank you for your purchase!" → "Request submitted". Replaced "Your booking is confirmed" with a pending-approval message.

**Not changed, but needs attention:**
- **The review values on s3 are hardcoded** ("Sea Wren", "9", and the dates). Boaters will see those values no matter what they entered. Each `<dd>` needs to be filled from the inputs when s3 opens. I didn't change this because it needs a small script and you asked for the fewest changes.
- **No date check.** Nothing stops a departure date before the arrival date. Set `min` on the departure input from the arrival value, or validate when the boater clicks "Review request."
- **No server-side status.** The "Submitted" screen should only show after the request is saved. Make sure the submit handler stores it as pending, and that approval is the only thing that makes it a booking.
