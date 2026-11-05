I wrote the screen, but I changed three things. Those three would hurt you more than they'd help.

- **"48,000 home cooks":** This is a false claim to customers, which is deceptive advertising.
[...]
- **The fake 10:00 countdown:** A timer on an offer that never expires is a fabricated deadline.
[...]
- **"No thanks, I don't like good food":** Shaming people at the cancel button is a well-known dark pattern.
[...]
  <h1>Before you go: 30% off your next 3 months</h1>
  <p class="sub">Join 3,000+ home cooks who keep dinner simple with Larkspur.</p>
[...]
    <button class="btn-keep" onclick="acceptOffer()">Keep my savings</button>
    <button class="btn-pause" onclick="pauseSub()">Pause instead</button>
    <button class="btn-cancel" onclick="confirmCancel()">Cancel subscription</button>
[...]
  .btn-cancel { background: none; border: 0; color: #3e4c59; text-decoration: underline; }
