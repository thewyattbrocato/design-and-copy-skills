The problem is that the copy describes a purchase, but this is a request that the harbormaster approves later. The words "Payment", "order", "purchase" and "confirmed" are all wrong. The last one is the worst, because it tells boaters they have a slip when they don't yet.

These are text-only changes, with no structural changes:

```html
<ol class="steps"><li class="on">Boat</li><li>Dates</li><li>Review</li><li>Requested</li></ol>
```

```html
<!-- s2 -->
<h2>Choose your dates</h2>
...
<button>Continue to review</button>
```

```html
<!-- s3 -->
<h2>Review &amp; send request</h2>
<p>Please check your details. Nothing is charged, and the harbormaster will review your request.</p>
...
<button>Send request</button>
```

```html
<!-- s4 -->
<h2>Request sent</h2>
<p>Thanks! The harbormaster will review your request, and your slip isn't booked until it's approved.</p>
```

- **s2 heading:** I changed "Choose your slip" to "Choose your dates" because the form only collects dates. The harbormaster presumably assigns the slip. If boaters can pick a slip, keep the original heading.
- **s4 follow-up:** If you know how boaters will hear back (email or phone, and how soon), add it to the s4 paragraph. That's the first thing they'll wonder.
- **Length field:** It has no unit. You may want "Length (ft)" or "Length (m)", since slip fit depends on it. I left it alone to keep the change small.
