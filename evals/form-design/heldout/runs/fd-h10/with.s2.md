```html
<form>
  <h2>Welcome back</h2>

  <label>Library card number
    <input name="card" autocomplete="username" autocapitalize="off" spellcheck="false">
  </label>

  <label>PIN
    <input name="pin" type="password" autocomplete="current-password">
  </label>

  <label>
    <input type="checkbox" name="remember">
    Keep me signed in on this computer for about a month
  </label>
  <p class="small">Only tick this on your own device, not a shared library computer. If you don't, remember to sign out when you're done. We'll still ask for your PIN before anything involving fines or payments.</p>

  <button>Sign in</button>
</form>
```

**What changed and why**
- **"Remember me" is now unticked.** Many members sign in on shared computers, so a month-long sign-in that's on by default could leave someone's account open to the next person. The label now says what it does, and the note beside it says when to use it. The old note ("stay connected for as long as you need") didn't match what the box does.
- **Smaller copy fixes.**
  - "Welcome back!!" is now "Welcome back".
  - "LOGIN" is now "Sign in", in normal case.
  - The fields have the right autofill settings. Autocapitalize and spellcheck are off for the card number, so browsers and password managers won't mangle it.

Two things you could add. A "Show PIN" toggle helps people who mistype on unfamiliar keyboards. Also, if card numbers and PINs are digits only, add `inputmode="numeric"` to both fields for a number keypad on tablets. I left it off because I don't know your formats.
