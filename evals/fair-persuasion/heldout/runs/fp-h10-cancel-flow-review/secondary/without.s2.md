**Yes, this is a dark pattern, and parts of it are likely illegal.** The sign-up is two taps, but cancelling takes four screens and a phone call during business hours. That asymmetry is the core problem. Step 4 (phone-only cancellation) is the most serious issue.

## Step by step

| Step | Verdict | Why |
|---|---|---|
| **1. Cancel buried under "Billing FAQs"** | Not fine | Hiding the cancel option behind a FAQ and styling it as a small grey link makes it hard to find. Regulators treat hard-to-find cancellation as a roadblock. |
| **2. "Keep" big and green, "Continue" small and grey** | Borderline | Visual emphasis that makes the exit look like the wrong choice is a common dark pattern. The "3x more likely" stat is fine only if you can substantiate it. If you can't, it's a misleading claim. |
| **3. Pause offer** | Fine | A relevant alternative, free, presented once. Keep it, but make "No thanks" equal in size and weight to "Pause." |
| **4. Required reason dropdown + "call us" with limited hours** | **Not fine** | Making the reason mandatory blocks progress for no good reason. Phone-only cancellation with narrow hours is the clearest problem here. Many jurisdictions require cancellation through the same channel used to sign up. |
| **5. Confirmation email only after the call** | **Not fine** | The user has no proof they cancelled, and they'll keep getting charged until the call happens. This is also what generates chargebacks and complaints. |

## Legal exposure (verify with counsel)

I'm not a lawyer, and these rules change, so treat this as a starting point.

- **US:** The FTC's federal click-to-cancel rule was vacated in 2025, but several states have their own auto-renewal laws. California's amended law, for example, requires online cancellation when sign-up was online and prohibits making users navigate extra steps to cancel.
- **UK and EU:** Consumer protection rules on subscriptions and dark patterns apply, and more are coming.
- **App stores:** Apple and Google both require subscription cancellation to be discoverable and not blocked by phone-only flows, depending on how billing is handled.

If Gripline sells to customers in any of these places, the phone-gated step is the one most likely to draw a complaint.

## What to change

1. **Put "Cancel membership" at the top level of Settings > Membership**, not under FAQs.
2. **Cut the flow to two screens max:**
   - Screen 1: one retention offer, using the pause option as the alternative, with "Keep membership" and "Cancel anyway" at equal size and weight.
   - Screen 2: a final "Confirm cancellation" button showing the end date and what happens to any prepaid time or credits.
3. **Make the reason dropdown optional** with a "Skip" option. Use the answers as feedback, not a gate.
4. **Complete cancellation in-app.** Keep the phone number as an optional support channel, not a requirement.
5. **Send the confirmation email immediately**, with the effective date and a note that no further charges will be made.
6. **Keep the "3x" stat only if it's accurate and sourced.** Otherwise cut it.

## How to measure it

Track cancellation-completion rate, chargebacks and card disputes, and app-store reviews mentioning cancellation before and after the change. Phone-gated cancellations usually show up as disputes and one-star reviews, which cost more than the retention you gain from the extra friction.

If you want, I can draft the revised screen copy for the designer.
