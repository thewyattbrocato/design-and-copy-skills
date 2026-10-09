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
  --color-text: #14201f;
  --color-text-muted: #5a6b69;

  /* Type */
  --font-size-meta: 13px;
  --font-size-body: 15px;
  --font-size-title: 19px;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* Spacing */
  --space-1: 6px;
  --space-2: 10px;
  --space-3: 12px;
  --space-4: 14px;
  --space-5: 18px;
  --space-6: 20px;

  /* Shape and effects */
  --radius-sm: 6px;
  --radius-md: 10px;
  --border-width: 1px;
  --shadow-card: 0 1px 4px rgba(16, 24, 40, .10);
  --transition-fast: .18s ease;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-2) var(--space-5);
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
  /* padding is reduced by the border width so the size matches .btn */
  padding: calc(var(--space-2) - var(--border-width)) calc(var(--space-5) - var(--border-width));
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
  padding: var(--space-6);
  border: var(--border-width) solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-surface);
  box-shadow: var(--shadow-card);
}

.card-title {
  margin: 0 0 var(--space-2);
  font-size: var(--font-size-title);
  font-weight: var(--font-weight-bold);
  color: var(--color-text);
}

.card-meta {
  margin: 0 0 var(--space-4);
  font-size: var(--font-size-meta);
  color: var(--color-text-muted);
}

.card-footer {
  display: flex;
  justify-content: flex-end;
  gap: var(--space-3);
  margin-top: var(--space-5);
  padding-top: var(--space-4);
  border-top: var(--border-width) solid var(--color-border);
}
```

- **Rendering:** Every computed value is identical to the original, so nothing should shift visually. Class names are unchanged.
- **Secondary button padding:** `.btn-secondary` now derives its `9px 17px` from the base padding minus the border width. If you change `.btn` padding later, the secondary button stays the same size.
- **Danger button:** `.btn-danger` still inherits `border: 0` from `.btn`, as before.
- **Tokens:** They're named by role (`--color-primary`, `--space-*`), so new components can reuse them. The spacing scale only contains the values already in use (6, 10, 12, 14, 18, 20). I didn't round them to a 4px grid because that would change the look.
- **Hover colors:** They're separate literal tokens rather than computed with `color-mix()`. That keeps the exact original hex values.
