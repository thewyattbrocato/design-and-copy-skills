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

  /* Shape, elevation, motion */
  --radius-sm: 6px;
  --radius-md: 10px;
  --border-width: 1px;
  --shadow-card: 0 1px 4px rgba(16, 24, 40, 0.1);
  --duration-fast: 0.18s;

  /* Button */
  --btn-gap: 6px;
  --btn-padding-y: 10px;
  --btn-padding-x: 18px;
  --btn-font-size: 15px;
  --btn-font-weight: 600;
  --btn-radius: var(--radius-sm);
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--btn-gap);
  padding: var(--btn-padding-y) var(--btn-padding-x);
  font-size: var(--btn-font-size);
  font-weight: var(--btn-font-weight);
  border-radius: var(--btn-radius);
  background: var(--color-brand);
  color: var(--color-on-brand);
  border: 0;
  transition: background var(--duration-fast) ease;
}

.btn:hover {
  background: var(--color-brand-hover);
}

/* Padding is reduced by the border width so the button's outer size matches .btn */
.btn-secondary {
  background: transparent;
  color: var(--color-brand);
  border: var(--border-width) solid var(--color-brand);
  padding:
    calc(var(--btn-padding-y) - var(--border-width))
    calc(var(--btn-padding-x) - var(--border-width));
}

.btn-secondary:hover {
  background: var(--color-brand-tint);
}

.btn-danger {
  background: var(--color-danger);
  color: var(--color-on-brand);
}

.btn-danger:hover {
  background: var(--color-danger-hover);
}

.card {
  background: var(--color-surface);
  border: var(--border-width) solid var(--color-border);
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
  border-top: var(--border-width) solid var(--color-border);
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
```

**What changed**
- Repeated hex values, radii, the shadow, and the button metrics now live in `:root` custom properties. Building a new component means reusing those names.
- `.btn-secondary` padding is now `calc(token - border)`. It produces the same 9px 17px as before, but it stays correct if the button tokens change.
- Selectors, class names, property names, and rule order are unchanged. The overrides depend on order and on equal specificity, so the order has to stay as it is.
- One-off values (`19px`, `13px`, `20px`, `12px`) stay literal. Tokenize them only when you start reusing them.

**Things to check**
- I checked each value by reading the CSS, not in a browser. Before merging, compare a few buttons and cards on a page against the old build, including hover states.
- These `:root` names are global. If the app already defines `--color-brand` or similar with different values, the names will collide.
- This directory isn't a git repo, so I couldn't produce a diff. Running a visual regression check would confirm the no-visible-change requirement.
