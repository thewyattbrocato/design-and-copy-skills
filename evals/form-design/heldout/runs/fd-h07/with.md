Neither is fully right, but your designer is closer. I'd go with a hybrid that's mostly "validate on submit."

**Why per-keystroke validation is wrong**
- The first characters of a valid value are never valid yet. Someone typing `sam` into the email field sees "Enter a valid email" before they've finished.
- It's noisy on the password field. They'd see "too short" at 1, 2, 3... characters, which only tells them what they already know.
- Tabbing away or autofill can also trigger errors mid-task, so validating on blur isn't a clean fix either.

**Why submit-only isn't enough**
- A unique username is the one case where waiting until submit is bad. Someone fills in everything, hits submit, and learns their username is taken.
- Once a field has shown an error, it should clear as soon as the fix is made. Otherwise the stale error stays on screen while they correct it.

**What I'd do, field by field**

| Field | Behavior |
|---|---|
| **Email** | Check on submit. After an error appears, re-check as they edit so the message disappears the moment it's fixed. |
| **Username** | Check availability after a short pause in typing (about 500 ms), not on every keystroke. Show a quiet "checking…" state, then "Taken" or "Available". This is where your developer's instinct is right. |
| **Password** | Show the rule before they type ("At least [N] characters") in the hint under the label. Optionally tick it off as they meet it, and don't show it as an error. |

**Other details**
- Keep the submit button always pressable. Don't gray it out until the form is valid, because that gives no reason and is often unreachable by keyboard.
- Put each error next to its field, in words, with an icon or text cue as well as red. Say how to fix it, for example "Enter an email address with an @, like name@example.com". Avoid "Invalid email".
- If two or more fields fail, add a summary at the top that links to each one.
- Keep everything they typed after any error, including server errors.
- Run the same checks on the server. The username check especially has to be enforced there too, since someone can claim it between the live check and the submit.
- Use the right input types and autofill: `type="email"` with `autocomplete="email"`, `autocomplete="username"` with autocapitalize and spellcheck off, and `autocomplete="new-password"` with a show-password toggle. Allow paste.

**How to settle it**
Your developer gets instant feedback where it helps, on username availability and the password checklist. Your designer gets calm fields that don't yell while people are still typing. The rule is that errors don't appear on a first attempt, and once they do appear, they clear live.

I didn't touch any code, since there's no project here. If you share the form's markup or component, I can implement this.
