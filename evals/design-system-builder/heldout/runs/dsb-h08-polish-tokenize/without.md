```css
:root {
  /* Color */
  --color-primary: #0f766e;
  --color-primary-hover: #0d6b63;
  --color-primary-tint: #e6f4f2;
  --color-danger: #c0392b;
  --color-danger-hover: #a93226;
  --color-on-accent: #fff;
  --color-surface: #fff;
  --color-border: #dde2e1;
  --color-text-strong: #14201f;
  --color-text-muted: #5a6b69;

  /* Spacing */
  --space-6: 6px;
  --space-10: 10px;
  --space-12: 12px;
  --space-14: 14px;
  --space-18: 18px;
  --space-20: 20px;

  /* Type */
  --font-size-meta: 13px;
  --font-size-body: 15px;
  --font-size-title: 19px;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* Shape and effects */
  --border-width: 1px;
  --radius-sm: 6px;
  --radius-md: 10px;
  --shadow-card: 0 1px 4px rgba(16, 24, 40, .10);
  --transition-fast: .18s ease;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-6);
  padding: var(--space-10) var(--space-18);
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-semibold);
  border: 0;
  border-radius: var(--radius-sm);
  background: var(--color-primary);
  color: var(--color-on-accent);
  transition: background var(--transition-fast);
}
.btn:hover {
  background: var(--color-primary-hover);
}

.btn-secondary {
  /* Padding is reduced by the border width so the size matches .btn */
  padding: calc(var(--space-10) - var(--border-width)) calc(var(--space-18) - var(--border-width));
  border: var(--border-width) solid var(--color-primary);
  background: transparent;
  color: var(--color-primary);
}
.btn-secondary:hover {
  background: var(--color-primary-tint);
}

.btn-danger {
  background: var(--color-danger);
  color: var(--color-on-accent);
}
.btn-danger:hover {
  background: var(--color-danger-hover);
}

/* Cards */
.card {
  padding: var(--space-20);
  border: var(--border-width) solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  box-shadow: var(--shadow-card);
}

.card-title {
  margin: 0 0 var(--space-10);
  font-size: var(--font-size-title);
  font-weight: var(--font-weight-bold);
  color: var(--color-text-strong);
}

.card-meta {
  margin: 0 0 var(--space-14);
  font-size: var(--font-size-meta);
  color: var(--color-text-muted);
}

.card-footer {
  display: flex;
  justify-content: flex-end;
  gap: var(--space-12);
  margin-top: var(--space-18);
  padding-top: var(--space-14);
  border-top: var(--border-width) solid var(--color-border);
}
```

- **Appearance:** Every computed value is identical to the original, so nothing should look different. Class names and selectors are unchanged.
- **Tokens:** Repeated values now live in `:root` as custom properties. For example, the teal appears three times and the border grey twice. New components can reuse them.
- **Secondary button padding:** The original `9px 17px` was just the base padding minus the 1px border. It's now written as a `calc()` of the same tokens, so the two buttons stay the same size if the base padding changes.
- **Spacing names:** The tokens are named by pixel value (`--space-10`) because the original values don't follow a regular scale. If you later settle on a scale, rename them (for example `--space-sm`) in one place.
- **Property order:** Within each rule I grouped properties as layout, spacing, type, then visual. This doesn't affect rendering, because no rule sets the same property twice.
