The flow reads like a checkout. The "Payment" step, "Place order," "purchase," and "booking is confirmed" all imply an instant paid booking, but a booking only exists after the harbormaster approves it. The confirmation screen is the most serious problem because it tells the boater they're booked before anyone has approved anything.

Here is the revised markup with the same four screens and structure:

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
  <button>Continue to review</button>
</section>

<section id="s3">
  <h2>Review &amp; submit request</h2>
  <p>Please check your details. This is a request only. You are not booked until the harbormaster approves it.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Submit request</button>
</section>

<section id="s4">
  <h2>Request submitted</h2>
  <p>Thanks! The harbormaster will review your request and contact you once it is approved. No payment is due now.</p>
</section>
```

What changed (11 text edits, no structural changes):
- Step 3 "Payment" → "Review", and step 4 "Done" → "Submitted".
- s2 button "Continue to payment" → "Continue to review".
- s3 heading "Review & confirm" → "Review & submit request", with a line saying it's a request and not a booking until approved.
- s3 button "Place order" → "Submit request".
- s4 heading "Thank you for your purchase!" → "Request submitted", and "Your booking is confirmed" → a note that the harbormaster will review and contact them, with no payment due.

Things I didn't change, which you'll want to handle in the code that renders these screens:
- The review `<dl>` values are hardcoded ("Sea Wren", "9", the dates). They need to be filled from the inputs, or the boater will submit whatever placeholder is shown.
- The review doesn't show the Info field, so boaters can't check what they wrote there.
- Nothing checks that Departure is after Arrival.
- There's no slip selection, even though the heading says "Choose your slip." If the marina assigns slips, consider renaming that heading to "Choose your dates."
