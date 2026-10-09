```css
:root {
  /* Color */
  --color-brand: #0f766e;
  --color-brand-hover: #0d6b63;
  --color-brand-tint: #e6f4f2;
  --color-danger: #c0392b;
  --color-danger-hover: #a93226;
  --color-on-brand: #fff;
  --color-surface: #fff;
  --color-border: #dde2e1;
  --color-text: #14201f;
  --color-text-muted: #5a6b69;

  /* Shape and elevation */
  --radius-sm: 6px;
  --radius-md: 10px;
  --shadow-card: 0 1px 4px rgba(16, 24, 40, 0.1);

  /* Button sizing */
  --btn-padding-y: 10px;
  --btn-padding-x: 18px;
  --btn-font-size: 15px;
  --btn-font-weight: 600;
  --btn-transition: background 0.18s ease;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: var(--btn-padding-y) var(--btn-padding-x);
  font-size: var(--btn-font-size);
  font-weight: var(--btn-font-weight);
  border-radius: var(--radius-sm);
  background: var(--color-brand);
  color: var(--color-on-brand);
  border: 0;
  transition: var(--btn-transition);
}
.btn:hover { background: var(--color-brand-hover); }

/* 1px border is taken out of padding so outlined buttons match solid ones in size */
.btn-secondary {
  background: transparent;
  color: var(--color-brand);
  border: 1px solid var(--color-brand);
  padding: calc(var(--btn-padding-y) - 1px) calc(var(--btn-padding-x) - 1px);
}
.btn-secondary:hover { background: var(--color-brand-tint); }

.btn-danger {
  background: var(--color-danger);
  color: var(--color-on-brand);
}
.btn-danger:hover { background: var(--color-danger-hover); }

/* Cards */
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 20px;
  box-shadow: var(--shadow-card);
}
.card-title {
  font-size: 19px;
  font-weight: 700;
  margin: 0 0 10px;
  color: var(--color-text);
}
.card-meta {
  font-size: 13px;
  color: var(--color-text-muted);
  margin: 0 0 14px;
}
.card-footer {
  margin-top: 18px;
  padding-top: 14px;
  border-top: 1px solid var(--color-border);
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
```

What changed:
- Colors, radii, the card shadow, and button typography now live in `:root` custom properties, so new components can reuse them. Each value is identical to the original.
- `.btn-secondary` padding is now computed from the button's padding tokens minus the 1px border. It still resolves to `9px 17px`, so outlined and solid buttons keep the same size.
- Rule order is unchanged. The hover and variant rules still come after the base rules, so the cascade resolves the same way.

What I didn't do:
- I didn't render this, so the check is by reading. Computed values and cascade order match the original, but a quick visual pass in the app is still worth doing.
- Spacing (6, 10, 12, 14, 18, 20px) is still literal. These values don't follow a clean scale, so tokenizing them would be a judgment call about which values to round. I can propose a scale if you want one.
- If the app already defines any of these custom property names elsewhere, the `:root` block will override them, so check for collisions.
