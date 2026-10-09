```css
:root {
  /* Color roles */
  --color-accent: #0f766e;
  --color-accent-hover: #0d6b63;
  --color-accent-subtle: #e6f4f2;
  --color-danger: #c0392b;
  --color-danger-hover: #a93226;
  --color-on-accent: #fff;
  --color-surface: #fff;
  --color-border-subtle: #dde2e1;
  --color-text-primary: #14201f;
  --color-text-secondary: #5a6b69;

  /* Spacing */
  --space-1: 6px;
  --space-2: 10px;
  --space-3: 12px;
  --space-4: 14px;
  --space-5: 18px;
  --space-6: 20px;

  /* Type */
  --font-size-sm: 13px;
  --font-size-md: 15px;
  --font-size-lg: 19px;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* Radius, border, elevation, motion */
  --radius-sm: 6px;
  --radius-md: 10px;
  --border-width: 1px;
  --shadow-raised: 0 1px 4px rgba(16, 24, 40, .10);
  --duration-fast: .18s;
  --ease-standard: ease;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-2) var(--space-5);
  font-size: var(--font-size-md);
  font-weight: var(--font-weight-semibold);
  border-radius: var(--radius-sm);
  background: var(--color-accent);
  color: var(--color-on-accent);
  border: 0;
  transition: background var(--duration-fast) var(--ease-standard);
}
.btn:hover { background: var(--color-accent-hover); }

/* Padding is reduced by the border width so it stays the same size as .btn */
.btn-secondary {
  background: transparent;
  color: var(--color-accent);
  border: var(--border-width) solid var(--color-accent);
  padding: calc(var(--space-2) - var(--border-width)) calc(var(--space-5) - var(--border-width));
}
.btn-secondary:hover { background: var(--color-accent-subtle); }

.btn-danger {
  background: var(--color-danger);
  color: var(--color-on-accent);
}
.btn-danger:hover { background: var(--color-danger-hover); }

.card {
  background: var(--color-surface);
  border: var(--border-width) solid var(--color-border-subtle);
  border-radius: var(--radius-md);
  padding: var(--space-6);
  box-shadow: var(--shadow-raised);
}
.card-title {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-bold);
  margin: 0 0 var(--space-2);
  color: var(--color-text-primary);
}
.card-meta {
  font-size: var(--font-size-sm);
  color: var(--color-text-secondary);
  margin: 0 0 var(--space-4);
}
.card-footer {
  margin-top: var(--space-5);
  padding-top: var(--space-4);
  border-top: var(--border-width) solid var(--color-border-subtle);
  display: flex;
  gap: var(--space-3);
  justify-content: flex-end;
}
```

**Merge map (old value → token):**
- Colors: `#0f766e` → `accent`, `#0d6b63` → `accent-hover`, `#e6f4f2` → `accent-subtle`, `#c0392b` → `danger`, `#a93226` → `danger-hover`, `#fff` → `on-accent` and `surface`, `#dde2e1` → `border-subtle`, `#14201f` → `text-primary`, `#5a6b69` → `text-secondary`.
- Spacing: 6, 10, 12, 14, 18 and 20px → `space-1` to `space-6`.
- The secondary button's `9px 17px` is now `calc(space - border-width)`. It renders the same, and it stays correct if either value changes.
- Radius: 6px → `radius-sm`, 10px → `radius-md`.
- Type: 13, 15 and 19px → `font-size-sm`, `-md` and `-lg`.

**Notes:**
- Every rendered value is identical, so nothing changes visually. I did not merge the close spacing steps (12/14 and 18/20), because that would shift layouts by 2px. Merging them is a later decision for you to make deliberately.
- Components read only semantic roles, so a dark or second-brand theme only needs to remap the `:root` color tokens.
- The CSS still has no focus, disabled or pressed states. Add them before more components copy these buttons.
