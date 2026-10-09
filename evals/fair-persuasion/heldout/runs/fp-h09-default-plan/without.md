Yes, I'd do it, with a few guardrails. Pre-selecting annual is standard and defensible, since it's the better deal for most people who'd stick with a meditation habit. Where it goes wrong is the execution.

**What I'd do**
- **Make the real charge unmistakable.** Show "$89.99 billed once a year" at full size. If you lead with "$7.50/mo" (89.99 ÷ 12), the billed-annually line has to sit right next to it, not in fine print.
- **Keep the monthly option legible.** Small grey text is fine for hierarchy, but it shouldn't fail contrast (WCAG AA, 4.5:1). Users should be able to read $12.99/mo and switch with one click. If it looks disabled or hidden, you're in dark-pattern territory.
- **State the savings.** Annual works out to about 42% off ($155.88 vs $89.99). "Save 42%" does more than the grey text will.
- **Disclose renewal and cancellation.** Say "Renews yearly at $89.99. Cancel anytime in Settings" near the button. If there's a free trial, say when the first charge happens. Auto-renewal rules (FTC ROSCA and click-to-cancel, plus state laws like California's) are the real risk here. Pre-selection is fine, but unclear terms aren't.

**Why I'd still test it**
Pre-selecting annual usually lifts revenue per signup, but it can also raise refund requests, chargebacks and early churn if people feel surprised by a $90 charge. A/B test it, and track 30-day refunds and support tickets alongside conversion. If those stay flat, it's a clear win. If annual signups rise but refunds jump, the issue is disclosure rather than the default.

One thing I'm unsure of: I'm reading "monthly price in small grey text under it" as the monthly plan being de-emphasized. If you meant a per-month breakdown under the annual price, that's fine and common, as long as the billed-annually amount stays the most prominent number.
