```css
:root {
  /* color */
  --color-surface: #fff;
  --color-on-primary: #fff;
  --color-primary: #0f766e;
  --color-primary-hover: #0d6b63;
  --color-primary-tint: #e6f4f2;
  --color-danger: #c0392b;
  --color-danger-hover: #a93226;
  --color-border: #dde2e1;
  --color-text: #14201f;
  --color-text-muted: #5a6b69;

  /* radius */
  --radius-sm: 6px;
  --radius-md: 10px;

  /* shadow */
  --shadow-card: 0 1px 4px rgba(16, 24, 40, .10);

  /* motion */
  --transition-fast: .18s ease;

  /* button sizing */
  --btn-pad-y: 10px;
  --btn-pad-x: 18px;
  --btn-border-width: 1px;
}

/* Button */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: var(--btn-pad-y) var(--btn-pad-x);
  font-size: 15px;
  font-weight: 600;
  border: 0;
  border-radius: var(--radius-sm);
  background: var(--color-primary);
  color: var(--color-on-primary);
  transition: background var(--transition-fast);
}
.btn:hover {
  background: var(--color-primary-hover);
}

.btn-secondary {
  /* padding is reduced by the border width so the size matches .btn */
  padding: calc(var(--btn-pad-y) - var(--btn-border-width))
           calc(var(--btn-pad-x) - var(--btn-border-width));
  border: var(--btn-border-width) solid var(--color-primary);
  background: transparent;
  color: var(--color-primary);
}
.btn-secondary:hover {
  background: var(--color-primary-tint);
}

.btn-danger {
  background: var(--color-danger);
  color: var(--color-on-primary);
}
.btn-danger:hover {
  background: var(--color-danger-hover);
}

/* Card */
.card {
  padding: 20px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  box-shadow: var(--shadow-card);
}
.card-title {
  margin: 0 0 10px;
  font-size: 19px;
  font-weight: 700;
  color: var(--color-text);
}
.card-meta {
  margin: 0 0 14px;
  font-size: 13px;
  color: var(--color-text-muted);
}
.card-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 18px;
  padding-top: 14px;
  border-top: 1px solid var(--color-border);
}
```

What changed:
- **Tokens:** Repeated or shared values (colors, radii, shadow, transition, button padding) are now custom properties in `:root`. New components can reuse them.
- **Secondary button padding:** `9px 17px` is now derived as the base padding minus the 1px border, so it stays in sync. It still computes to exactly `9px 17px`.
- **Property order:** Properties are grouped as layout, box, then visual. Order has no effect on rendering here.
- **Unchanged:** Class names, selectors, rule order (so the `.btn-secondary` and `.btn-danger` overrides still win) and every computed value are the same. The output should be pixel-identical.

I left one-off values as literals: font sizes, the card padding, margins and gaps. They don't repeat across rules, so tokens for them would add indirection without real reuse. If you want a spacing or type scale, tell me and I'll add one. Snapping those values to a scale (for example 10→8 or 18→16) would change the look, so I didn't.
