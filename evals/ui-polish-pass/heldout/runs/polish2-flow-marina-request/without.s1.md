The flow is written like a checkout (payment, order, purchase, confirmed), but it's a request that the harbormaster has to approve. Boaters would expect to pay and would think they have a booking. The fix only touches wording, and the structure stays the same.

```html
<ol class="steps"><li class="on">Boat</li><li>Dates</li><li>Review</li><li>Sent</li></ol>
```
"Payment" becomes "Review", which is what step 3 actually is. "Done" becomes "Sent", because the request isn't finished until it's approved.

```html
<h2>Choose your dates</h2>
...
<button>Continue</button>
```
Boaters only pick dates on this screen, and the harbormaster assigns the slip. "Continue to payment" promised a payment that doesn't exist.

```html
<h2>Review &amp; send request</h2>
...
<button>Send request</button>
```
"Place order" becomes "Send request", and the heading says what the button will do.

```html
<h2>Request sent</h2>
<p>The harbormaster will review your request. It isn't a booking until they approve it.</p>
```
This replaces "Thank you for your purchase! Your booking is confirmed." That text was the most misleading part, since it told boaters they had a confirmed booking and had paid. Ideally it would also say how they'll hear back (email or phone), but that depends on what you do.

One thing I left alone is that "Length" has no unit (feet or meters?). The marina will care about this, so add one, for example `Length (ft)`. I didn't, because you asked for the fewest changes.
