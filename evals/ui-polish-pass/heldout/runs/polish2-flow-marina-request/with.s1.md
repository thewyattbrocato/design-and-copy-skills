The flow is written like a store checkout, but this is a request. It promises payment, a purchase, and a confirmed booking, none of which happen. The fix is copy-only, with no structural changes:

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
  <p>Please check your details. Nothing is booked or charged until the harbormaster approves.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Send request</button>
</section>

<section id="s4">
  <h2>Request sent</h2>
  <p>The harbormaster will review your request. Your slip is not booked until it is approved.</p>
</section>
```

What changed and why:
- **Step 3 "Payment" → "Review", step 4 "Done" → "Requested".** There's no payment step, and "Done" suggests the booking is finished.
- **"Choose your slip" → "Choose your dates".** The screen only asks for dates. The harbormaster assigns the slip.
- **"Continue to payment" → "Continue".** It no longer points to a payment screen.
- **"Review & confirm" / "Place order" → "Review & send request" / "Send request".** "Confirm" and "order" imply a finished transaction.
- **A line on screen 3 says nothing is charged or booked yet.** Boaters see this before they submit.
- **"Thank you for your purchase! Your booking is confirmed." → "Request sent" plus a pending-approval message.** The old text was the most misleading part. A boater could show up expecting a slip.

I left the markup alone, but two things are still worth a look:
- The Length field has no unit.
- The summary on screen 3 is hardcoded.
