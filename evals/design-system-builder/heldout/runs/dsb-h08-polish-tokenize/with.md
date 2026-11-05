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

  /* Shape, border, elevation, motion */
  --radius-sm: 6px;
  --radius-md: 10px;
  --border-width: 1px;
  --shadow-raised: 0 1px 4px rgba(16, 24, 40, 0.10);
  --duration-fast: 0.18s;
  --easing-standard: ease;

  /* Button inset (secondary subtracts its border so all variants stay the same size) */
  --btn-pad-y: var(--space-2);
  --btn-pad-x: var(--space-5);
}

/* Button */
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--btn-pad-y) var(--btn-pad-x);
  font-size: var(--font-size-md);
  font-weight: var(--font-weight-semibold);
  border-radius: var(--radius-sm);
  background: var(--color-accent);
  color: var(--color-on-accent);
  border: 0;
  transition: background var(--duration-fast) var(--easing-standard);
}
.btn:hover {
  background: var(--color-accent-hover);
}

.btn-secondary {
  background: transparent;
  color: var(--color-accent);
  border: var(--border-width) solid var(--color-accent);
  padding: calc(var(--btn-pad-y) - var(--border-width)) calc(var(--btn-pad-x) - var(--border-width));
}
.btn-secondary:hover {
  background: var(--color-accent-subtle);
}

.btn-danger {
  background: var(--color-danger);
  color: var(--color-on-accent);
}
.btn-danger:hover {
  background: var(--color-danger-hover);
}

/* Card */
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

**Merge map (old value → token):** every value resolves to its exact original, so the rendering is pixel-identical. `9px 17px` on the secondary button is now derived from the button padding minus the border, so it can't drift.

- **Colors:** `#0f766e` → `accent`, `#0d6b63` → `accent-hover`, `#e6f4f2` → `accent-subtle`, `#c0392b` → `danger`, `#a93226` → `danger-hover`, `#fff` → `on-accent` / `surface`, `#dde2e1` → `border-subtle`, `#14201f` → `text-primary`, `#5a6b69` → `text-secondary`.
- **Spacing:** 6 → `space-1`, 10 → `space-2`, 12 → `space-3`, 14 → `space-4`, 18 → `space-5`, 20 → `space-6`.

**Trade-off:** I kept 12/14 and 18/20 as separate steps, because merging them would shift things by 1–2px. They're close enough to confuse, so consider collapsing each pair later, with a visual check, to get a four-step scale.

I assumed a single light theme. Components read only the semantic roles, so adding dark mode later means remapping the `:root` color values.
