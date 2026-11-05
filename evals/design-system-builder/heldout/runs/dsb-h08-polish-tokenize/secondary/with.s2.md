```css
:root {
  /* Color */
  --color-brand: #0f766e;
  --color-brand-hover: #0d6b63;
  --color-brand-subtle: #e6f4f2;
  --color-on-brand: #fff;
  --color-danger: #c0392b;
  --color-danger-hover: #a93226;
  --color-surface: #fff;
  --color-border: #dde2e1;
  --color-text: #14201f;
  --color-text-muted: #5a6b69;

  /* Shape, elevation, motion */
  --radius-sm: 6px;
  --radius-md: 10px;
  --shadow-sm: 0 1px 4px rgba(16, 24, 40, 0.1);
  --transition-hover: background 0.18s ease;
}

/* Button */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 10px 18px;
  font-size: 15px;
  font-weight: 600;
  border: 0;
  border-radius: var(--radius-sm);
  background: var(--color-brand);
  color: var(--color-on-brand);
  transition: var(--transition-hover);
}
.btn:hover {
  background: var(--color-brand-hover);
}

/* Secondary: the 1px border is subtracted from padding so the box matches .btn */
.btn-secondary {
  padding: calc(10px - 1px) calc(18px - 1px);
  border: 1px solid var(--color-brand);
  background: transparent;
  color: var(--color-brand);
}
.btn-secondary:hover {
  background: var(--color-brand-subtle);
}

.btn-danger {
  background: var(--color-danger);
  color: var(--color-on-brand);
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
  box-shadow: var(--shadow-sm);
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

Notes:

- **Visual output should be unchanged.** I checked each declaration against the original, including the cascade order and the `.btn-secondary` padding that offsets its 1px border.
- **Class names are unchanged.**
- **Possible collision:** the `:root` variable names are generic. If the app already defines `--color-brand` or similar, rename the new ones or scope them.
- **Not added:** the button has no `:focus-visible` style. Adding one would be a visible change, so I left it out, but it's worth a follow-up for keyboard accessibility.
- **Not rendered:** I verified this by reading the declarations, not by loading the page.
