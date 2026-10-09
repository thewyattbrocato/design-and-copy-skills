```html
<form action="/login" method="post">
  <h2>Welcome back</h2>

  <div>
    <label for="email">Email</label>
    <input type="email" id="email" name="email" autocomplete="username" required>
  </div>

  <div>
    <label for="password">Password</label>
    <input type="password" id="password" name="password" autocomplete="current-password" required>
  </div>

  <div>
    <label for="code">Enter the code we texted you</label>
    <input type="text" id="code" name="code"
           inputmode="numeric" pattern="[0-9]{6}" maxlength="6"
           autocomplete="one-time-code" required>
  </div>

  <button type="submit">Log in</button>
</form>
```

**What changed and why**

1. **Real `<label>`s instead of placeholders.** Placeholders vanish when the user types and are not reliably announced by screen readers. Labels linked with `for`/`id` stay visible, are announced, and enlarge the click target.
2. **`type="email"` for the email field.** This gives validation and the right mobile keyboard. The name stays `email`.
3. **`name="pw"` is now `name="password"`.** This is clearer and more conventional. Update the server handler to match.
4. **`autocomplete` attributes.** `username` and `current-password` let password managers and browsers fill the form correctly.
5. **`required`.** The browser blocks empty submissions without any JavaScript.
6. **The six code boxes are now one input.** The six boxes had no labels or names, so the values wouldn't submit meaningfully. They also broke paste, backspace, and screen-reader use. A single field with `autocomplete="one-time-code"` lets iOS and Android autofill the SMS code. `inputmode="numeric"` brings up the number pad, and `pattern`/`maxlength` enforce six digits. This also removes the need for the script.
7. **The code field now sits before the button.** The original put the submit button above the code, so the order didn't match the flow.
8. **The button text "Submit" is now "Log in".** It says what the button does.
9. **Each field is wrapped in a `<div>`.** This gives you a styling hook and a clear structure.

If you want the six-box look, keep separate inputs. Give each an `aria-label` ("Digit 1 of 6", and so on) and handle paste and backspace in the script. Otherwise, style the single input with `letter-spacing` and a monospace font.
