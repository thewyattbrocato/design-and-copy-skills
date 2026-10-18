The flow reads like an e-commerce checkout, and that's what feels off. It has a payment step, "Place order," and a confirmed booking on submit, but nothing is paid and nothing is booked until the harbormaster approves. The fix is mostly copy and one step label. The structure stays the same.

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
  <h2>Choose your slip</h2>
  <label>Arrival <input type="date" name="a"></label>
  <label>Departure <input type="date" name="d"></label>
  <button>Continue to review</button>
</section>

<section id="s3">
  <h2>Review your request</h2>
  <p>The harbormaster will review this request. Your slip is not reserved until it is approved.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Submit request</button>
</section>

<section id="s4">
  <h2>Request submitted</h2>
  <p>Thanks! We've received your slip request. You'll be notified once the harbormaster approves it.</p>
</section>
```

What changed:
- **Step 3:** "Payment" became "Review," since no payment happens.
- **Step 4:** "Done" became "Requested," so the last step doesn't imply a booking exists.
- **s2 button:** "Continue to payment" became "Continue to review."
- **s3 heading, copy, and button:** "Review & confirm" became "Review your request," with a note that the slip isn't reserved until approval. "Place order" became "Submit request."
- **s4 heading and copy:** "Thank you for your purchase! / Your booking is confirmed." became "Request submitted," with a note that approval comes later.

Two things the markup alone can't fix:
- **The review values are hardcoded.** The `<dd>` values say "Sea Wren," 9, and the July dates no matter what the boater entered. The script that drives these screens has to fill them from the inputs before showing step 3. If it doesn't, that's a bug to fix first.
- **The "Requested" text needs the right backend behavior.** The copy now says the slip is not reserved until approval. Make sure submitting creates a pending request, not a booking, and that the harbormaster's approval is what changes it to a booking. I haven't seen that code, so I can't confirm it.

I didn't add validation, such as requiring a name or checking that departure is after arrival. That's a separate change, and I can add it if you want.
