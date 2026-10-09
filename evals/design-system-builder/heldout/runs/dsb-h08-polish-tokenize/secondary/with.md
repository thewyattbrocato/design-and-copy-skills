Here's the cleaned-up CSS. Every selector name is unchanged, and the selector order and specificity are the same, so the cascade behaves as before (for example, `.btn-secondary:hover` still overrides `.btn:hover`).

```css
:root {
  /* Color */
  --color-brand: #0f766e;
  --color-brand-hover: #0d6b63;
  --color-brand-tint: #e6f4f2;
  --color-danger: #c0392b;
  --color-danger-hover: #a93226;
  --color-white: #fff;
  --color-text: #14201f;
  --color-text-muted: #5a6b69;
  --color-border: #dde2e1;

  /* Elevation */
  --shadow-card: 0 1px 4px rgba(16, 24, 40, 0.1);

  /* Radius */
  --radius-md: 6px;
  --radius-lg: 10px;

  /* Spacing */
  --space-1: 6px;
  --space-2: 10px;
  --space-3: 12px;
  --space-4: 14px;
  --space-5: 18px;
  --space-6: 20px;

  /* Type */
  --font-size-sm: 13px;
  --font-size-base: 15px;
  --font-size-lg: 19px;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* Motion */
  --duration-fast: 0.18s;
}

/* Button */
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-2) var(--space-5);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
  border-radius: var(--radius-md);
  background: var(--color-brand);
  color: var(--color-white);
  border: 0;
  transition: background var(--duration-fast) ease;
}

.btn:hover {
  background: var(--color-brand-hover);
}

.btn-secondary {
  background: transparent;
  color: var(--color-brand);
  border: 1px solid var(--color-brand);
  /* Inset by the 1px border so the button's overall size matches .btn */
  padding: calc(var(--space-2) - 1px) calc(var(--space-5) - 1px);
}

.btn-secondary:hover {
  background: var(--color-brand-tint);
}

.btn-danger {
  background: var(--color-danger);
  color: var(--color-white);
}

.btn-danger:hover {
  background: var(--color-danger-hover);
}

/* Card */
.card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
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

What changed:

- **Tokens:** Colors, spacing, type sizes, radii, shadow, and transition timing now live in `:root` custom properties. New components can reuse them, and a future color change happens in one place. The custom property names are my choice, so rename them if your codebase has a convention.
- **Secondary button padding:** It is written as `calc(token - 1px)` to make the reason explicit. The 1px border is subtracted so the button stays the same size as `.btn`. The computed values are identical to `9px 17px`.
- **Dropped duplication:** `#dde2e1` appeared three times and is now `--color-border`. The `.btn` and `.card` declarations are otherwise unchanged.

Caveats:

- I checked the values by reading them, not by rendering the app. If you want certainty, compare a few buttons and cards in a before/after screenshot.
- `:root` is global. If your app already defines variables with these names, they will collide.
- Values that were already in use were kept as-is, so there are no visual changes. Some values are close to each other, such as `10px`, `12px`, and `14px` spacing. Merging them would be a visible change, so I left them separate.
