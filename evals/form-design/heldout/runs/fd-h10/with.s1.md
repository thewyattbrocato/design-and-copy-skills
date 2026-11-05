```html
<form>
  <h2>Sign in to Millrace Public Library</h2>

  <label for="card">Library card number</label>
  <p id="card-hint" class="small">Enter the number on your library card.</p>
  <input id="card" name="card" inputmode="numeric" autocomplete="username"
         autocapitalize="off" spellcheck="false" aria-describedby="card-hint">

  <label for="pin">PIN</label>
  <input id="pin" name="pin" type="password" autocomplete="current-password">

  <label>
    <input type="checkbox" name="remember">
    Keep me signed in on this computer for about a month
  </label>
  <p class="small">Only tick this on your own device. On a library computer, leave it unticked and sign out when you're done. You'll still be asked for your PIN before anything involving fines or payments.</p>

  <button type="submit">Sign in</button>
</form>
```

- **"Remember me" is now unticked by default, and I removed the old "stay connected as long as you need" line.** On shared library computers, a pre-ticked box would leave the next person signed in to someone else's account for a month. The old line also didn't say how long, which was about a month. The new wording says so and explains the PIN exception.
- **Other changes:**
  - The heading and button now both say "Sign in" instead of "Welcome back!!" and "LOGIN".
  - Labels are tied to their fields.
  - The card field brings up a numeric keypad but isn't `type="number"`, so spaces or dashes in a card number still work.
  - Autofill tokens are set so password managers behave.
  - I didn't add a show-PIN toggle or error messages, since you didn't ask for them. They'd be worth adding next, and error text like "That card number and PIN don't match. Check both and try again." fits here.
