Here's the cleaned-up CSS. Every computed value matches the original, and the class names are unchanged.

```css
:root {
  /* Color */
  --color-brand: #0f766e;
  --color-brand-hover: #0d6b63;
  --color-brand-tint: #e6f4f2;
  --color-danger: #c0392b;
  --color-danger-hover: #a93226;
  --color-white: #fff;
  --color-border: #dde2e1;
  --color-text: #14201f;
  --color-text-muted: #5a6b69;

  /* Radius, elevation */
  --radius-sm: 6px;
  --radius-md: 10px;
  --shadow-card: 0 1px 4px rgba(16, 24, 40, .10);

  /* Spacing */
  --space-xs: 6px;
  --space-sm: 10px;
  --space-md: 12px;
  --space-lg: 14px;
  --space-xl: 18px;
  --space-2xl: 20px;

  /* Type */
  --font-size-button: 15px;
  --font-size-card-title: 19px;
  --font-size-card-meta: 13px;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* Motion */
  --transition-color: background .18s ease;

  /* Button geometry */
  --btn-pad-y: var(--space-sm);
  --btn-pad-x: var(--space-xl);
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-xs);
  padding: var(--btn-pad-y) var(--btn-pad-x);
  font-size: var(--font-size-button);
  font-weight: var(--font-weight-semibold);
  border-radius: var(--radius-sm);
  background: var(--color-brand);
  color: var(--color-white);
  border: 0;
  transition: var(--transition-color);
}
.btn:hover {
  background: var(--color-brand-hover);
}

/* Secondary padding is 1px smaller on each axis to offset its 1px border */
.btn-secondary {
  background: transparent;
  color: var(--color-brand);
  border: 1px solid var(--color-brand);
  padding: calc(var(--btn-pad-y) - 1px) calc(var(--btn-pad-x) - 1px);
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
  border-radius: var(--radius-md);
  padding: var(--space-2xl);
  box-shadow: var(--shadow-card);
}
.card-title {
  font-size: var(--font-size-card-title);
  font-weight: var(--font-weight-bold);
  margin: 0 0 var(--space-sm);
  color: var(--color-text);
}
.card-meta {
  font-size: var(--font-size-card-meta);
  color: var(--color-text-muted);
  margin: 0 0 var(--space-lg);
}
.card-footer {
  margin-top: var(--space-xl);
  padding-top: var(--space-lg);
  border-top: 1px solid var(--color-border);
  display: flex;
  gap: var(--space-md);
  justify-content: flex-end;
}
```

**What changed**
- Repeated hex values, radii, shadows, and sizes are now custom properties on `:root`, so new components can reuse them.
- Spacing tokens use the values already in the file. I didn't round them onto a scale, since that would change the look.
- `.btn-secondary`'s padding is now derived from the primary button's padding minus the border width. The computed result is still 9px 17px.

**What to keep in mind**
- Keep the rule order. `.btn-secondary` and `.btn-danger` override `.btn` only because they come after it, and the hover rules depend on the same ordering.
- I checked the values by reading the CSS, not by rendering the page. A quick visual pass on a button and card page would confirm nothing shifted.
