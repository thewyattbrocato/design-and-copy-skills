Here's the revised form:

```html
<form>
  <h2>Sign in to your library account</h2>

  <div>
    <label for="card">Library card number</label>
    <input id="card" name="card" type="text" inputmode="numeric"
           autocomplete="username" autocapitalize="off" spellcheck="false">
  </div>

  <div>
    <label for="pin">PIN</label>
    <input id="pin" name="pin" type="password" autocomplete="current-password">
  </div>

  <div>
    <label>
      <input type="checkbox" name="remember">
      Keep me signed in on this computer for about a month
    </label>
    <p class="small">Leave this unticked on shared computers, including the library's.</p>
  </div>

  <button type="submit">Sign in</button>

  <p class="small">We'll ask for your PIN again before anything involving fines or payments.</p>
</form>
```

**Changes:**
- **"Remember me" is now unticked by default.** Many of your members use shared computers, and a pre-ticked box would leave their accounts open to the next person for a month. The label says what it does, and the hint under it speaks to shared computers.
- **The old line "you stay connected for as long as you need" is gone.** It wasn't accurate, because sign-in lasts about a month if the box is ticked. The new line says that PINs are still required for fines and payments.
- **Smaller wording changes:**
  - "Welcome back!!" became a plain "Sign in" heading.
  - "LOGIN" became "Sign in", so the heading and button use the same words.
  - The labels are now tied to their inputs, so clicking a label focuses its field.

I added `inputmode="numeric"` to the card field, which assumes card numbers are all digits. Remove it if yours include letters. I left the PIN field as plain text entry in case PINs can be non-numeric.

If the portal has a "Sign out" link, consider adding "Remember to sign out when you're done" near the button for shared computers. I held off because I don't know your layout.
