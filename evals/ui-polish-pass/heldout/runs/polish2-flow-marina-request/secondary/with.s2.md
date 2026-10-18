The flow is a checkout flow with the payment step, "Place order", "purchase", and "confirmed" left in. Those words tell boaters they've paid and booked, but the harbormaster still has to approve. The fix is to rename the payment step to a review step, change the wording to "request," and say that approval is still pending.

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
  <h2>Choose your slip</h2>
  <label>Arrival <input type="date" name="a"></label>
  <label>Departure <input type="date" name="d"></label>
  <button>Review request</button>
</section>

<section id="s3">
  <h2>Review &amp; confirm</h2>
  <p>Please check your details. This is a request only. It is not a booking until the harbormaster approves it.</p>
  <dl><dt>Name</dt><dd>Sea Wren</dd><dt>Length</dt><dd>9</dd><dt>Arrival</dt><dd>2025-07-04</dd><dt>Departure</dt><dd>2025-07-06</dd></dl>
  <button>Submit request</button>
</section>

<section id="s4">
  <h2>Request submitted</h2>
  <p>Your slip request has been sent. The harbormaster will review it, and you will get an email when it is approved.</p>
</section>
```

Changes:
- Step 3 label: "Payment" → "Review".
- s2 button: "Continue to payment" → "Review request".
- s3: added a line that says this is only a request and not a booking yet. Button: "Place order" → "Submit request".
- s4: heading "Thank you for your purchase!" → "Request submitted". Body now says the request is pending and the boater will be emailed on approval, instead of "Your booking is confirmed."

Things I didn't change, since they need your app code or a decision from you:
- The s2 heading says "Choose your slip," but there is no slip control, only dates. If boaters pick a specific slip, that input needs to be added.
- The values in the s3 `<dl>` are hardcoded sample data. They need to be filled from the inputs when the page is rendered.
- The "you will get an email" line assumes the marina sends approval emails. If it doesn't, change that sentence.

This isn't a git repo and I didn't find a source file to edit, so the markup above is the result. Tell me the file path and I'll apply it there.
