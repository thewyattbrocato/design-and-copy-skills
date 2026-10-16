I'll write the screen, but not with three of the elements you described. Each one is a false or manipulative claim aimed at customers, and that's a legal and trust risk for you:

- **"48,000 happy home cooks"**: this is a made-up number. It's the sort of thing the FTC and state attorneys general treat as deceptive advertising, and "nobody checks" doesn't protect you if someone does.
- **The "Offer ends in 10:00" timer**: the offer doesn't expire, so the timer is a fake urgency claim. Fake countdowns are a named dark pattern in FTC actions and in EU and UK consumer rules.
- **"No thanks, I don't like good food"**: shaming people into staying is also a flagged pattern. Cancel flows that obscure or shame the exit are exactly what the FTC's click-to-cancel push and state auto-renewal laws target.

The honest version can still convert well. A real 30% off for 3 months is a strong offer by itself. Here's a screen that uses it:

```tsx
// CancelOffer.tsx
import React from "react";
import "./CancelOffer.css";

type Props = {
  onKeep: () => void;      // applies the 30% discount and keeps the subscription
  onPause: () => void;     // optional: skip weeks instead of cancelling
  onConfirmCancel: () => void;
};

export default function CancelOffer({ onKeep, onPause, onConfirmCancel }: Props) {
  return (
    <main className="cancel-offer">
      <h1>Before you go, here's 30% off</h1>
      <p className="sub">
        Over 3,000 home cooks get Larkspur Meals every week. Stay with us and
        we'll take 30% off your next 3 months.
      </p>

      <section className="deal" aria-label="Offer details">
        <div className="deal-badge">30% OFF</div>
        <ul>
          <li>Applies to your next 3 months of deliveries</li>
          <li>Skip or pause any week, anytime</li>
          <li>Cancel whenever you like, no fees</li>
        </ul>
      </section>

      <button className="btn-keep" onClick={onKeep}>
        Keep my savings
      </button>

      <button className="btn-pause" onClick={onPause}>
        Pause deliveries instead
      </button>

      <button className="btn-cancel" onClick={onConfirmCancel}>
        Cancel my subscription
      </button>
    </main>
  );
}
```

```css
/* CancelOffer.css */
.cancel-offer { max-width: 440px; margin: 0 auto; padding: 32px 20px; text-align: center; font-family: system-ui, sans-serif; }
.cancel-offer h1 { font-size: 1.75rem; margin-bottom: 8px; }
.sub { color: #444; margin-bottom: 24px; }

.deal { background: #f1f8f3; border: 1px solid #cfe6d5; border-radius: 12px; padding: 20px; margin-bottom: 24px; text-align: left; }
.deal-badge { display: inline-block; background: #1f8a4c; color: #fff; font-weight: 700; padding: 4px 12px; border-radius: 999px; margin-bottom: 12px; }
.deal ul { margin: 0; padding-left: 20px; line-height: 1.7; }

.cancel-offer button { display: block; width: 100%; border-radius: 10px; cursor: pointer; font-size: 1rem; }
.btn-keep { background: #1f8a4c; color: #fff; border: 0; padding: 18px; font-size: 1.15rem; font-weight: 700; margin-bottom: 12px; }
.btn-keep:hover { background: #197340; }
.btn-pause { background: #fff; color: #1f8a4c; border: 2px solid #1f8a4c; padding: 14px; margin-bottom: 12px; }
.btn-cancel { background: transparent; color: #555; border: 1px solid #bbb; padding: 12px; }
```

**What I changed and why it still works:**
- **Social proof:** it uses your real figure of 3,000+. Smaller numbers read as more believable, and "3,000 home cooks" still lands.
- **Urgency:** I dropped the timer. If you want real urgency, make the offer actually expire, for example "available on this cancellation only", and enforce that on the backend. Then the countdown would be true.
- **Cancel button:** it's clearly labeled and visible, just visually secondary. Big green for keep and quieter styling for cancel is normal hierarchy and fine.
- **Pause option:** it saves a lot of would-be cancellers who just need a break.

If you'd like, I can adapt this to your stack (Vue, SwiftUI, plain HTML) or add a "why are you leaving?" step that tailors the offer. That usually does more for retention than any timer.
