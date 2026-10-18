The flow reads like a checkout. It has a Payment step, a "Place order" button, and a "purchase" confirmation that says the booking is confirmed. None of that is true for a request that the harbormaster still has to approve. The fix is to change the copy and step labels, not the structure. Four screens and their fields stay as they are.

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
  <p>Please check your details. This is a request only. No payment is taken, and the slip is not reserved until the harbormaster approves it.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Submit request</button>
</section>

<section id="s4">
  <h2>Request submitted</h2>
  <p>Thanks! The harbormaster will review your request. You are not booked until it is approved.</p>
</section>
```

**Changes (7 lines of text, no structural changes):**
- Step 3 "Payment" → "Review", step 4 "Done" → "Submitted".
- S2 button "Continue to payment" → "Continue to review".
- S3 heading "Review & confirm" → "Review & submit request", with a sentence saying no payment is taken and the slip isn't reserved until approval.
- S3 button "Place order" → "Submit request".
- S4 heading "Thank you for your purchase!" → "Request submitted", and "Your booking is confirmed" → a pending message.

**Not changed, but you should look at these:**
- The review table in S3 is hardcoded ("Sea Wren", 2025-07-04). It has to be filled from the inputs by your script, or every request will show the same data. Length and Info are also missing from it.
- The example dates are in 2025, but today is 2026-10-17, so past dates would pass through. Setting `min` on the date inputs to today and checking that departure is after arrival would fix that. I left it alone because you asked for the fewest changes.
- The step-indicator markup has no state for "pending approval". If the harbormaster's decision needs to show up in the boater's view later, that's a separate piece of work.
