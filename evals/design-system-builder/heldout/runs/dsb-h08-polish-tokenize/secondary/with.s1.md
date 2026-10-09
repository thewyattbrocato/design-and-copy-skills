```css
:root {
  /* Color */
  --color-brand: #0f766e;
  --color-brand-hover: #0d6b63;
  --color-brand-subtle: #e6f4f2;
  --color-danger: #c0392b;
  --color-danger-hover: #a93226;
  --color-on-accent: #fff;
  --color-surface: #fff;
  --color-border: #dde2e1;
  --color-text: #14201f;
  --color-text-muted: #5a6b69;

  /* Type */
  --font-size-sm: 13px;
  --font-size-md: 15px;
  --font-size-lg: 19px;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* Space */
  --space-1: 6px;
  --space-2: 10px;
  --space-3: 12px;
  --space-4: 14px;
  --space-5: 18px;
  --space-6: 20px;

  /* Shape, elevation, motion */
  --radius-sm: 6px;
  --radius-md: 10px;
  --shadow-card: 0 1px 4px rgba(16, 24, 40, .10);
  --duration-base: .18s;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-2) var(--space-5);
  font-size: var(--font-size-md);
  font-weight: var(--font-weight-semibold);
  border-radius: var(--radius-sm);
  background: var(--color-brand);
  color: var(--color-on-accent);
  border: 0;
  transition: background var(--duration-base) ease;
}
.btn:hover { background: var(--color-brand-hover); }

/* Outlined variant: 1px border is offset by 1px less padding so its size matches .btn */
.btn-secondary {
  background: transparent;
  color: var(--color-brand);
  border: 1px solid var(--color-brand);
  padding: calc(var(--space-2) - 1px) calc(var(--space-5) - 1px);
}
.btn-secondary:hover { background: var(--color-brand-subtle); }

.btn-danger { background: var(--color-danger); color: var(--color-on-accent); }
.btn-danger:hover { background: var(--color-danger-hover); }

/* Cards */
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-6);
  box-shadow: var(--shadow-card);
}

.card-title {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-bold);
  margin: 0 0 var(--space-2);
  color: var(--color-text);
}

.card-meta {
  font-size: var(--font-size-sm);
  color: var(--color-text-muted);
  margin: 0 0 var(--space-4);
}

.card-footer {
  margin-top: var(--space-5);
  padding-top: var(--space-4);
  border-top: 1px solid var(--color-border);
  display: flex;
  gap: var(--space-3);
  justify-content: flex-end;
}
```

Notes:

- **Values are unchanged.** Every token holds the exact value the original rule used, and all class names are kept. The `.btn-secondary` padding is now `calc(... - 1px)`, which gives the same 9px/17px as before.
- **Rule order is preserved.** `.btn-secondary:hover` still comes after `.btn:hover` and has the same specificity, so the hover background still wins on a secondary button, as before.
- **Possible collision.** The custom properties are defined on `:root` with generic names like `--color-brand` and `--space-2`. If your app already defines variables with those names, the values here will override them. Grep for `--color-`, `--space-`, and `--radius-` before merging, or add a prefix such as `--ui-`.
- **Not visually tested.** I checked this by reading the rules, not by rendering the components. A quick visual diff of a page with buttons and cards would confirm it.
