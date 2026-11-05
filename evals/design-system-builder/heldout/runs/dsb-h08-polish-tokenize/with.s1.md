```css
:root {
  /* Color: raw values, used only through the roles below */
  --color-accent: #0f766e;
  --color-accent-hover: #0d6b63;
  --color-accent-subtle: #e6f4f2;
  --color-danger: #c0392b;
  --color-danger-hover: #a93226;
  --color-on-solid: #fff;
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
  --font-size-meta: 13px;
  --font-size-control: 15px;
  --font-size-title: 19px;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* Shape, border, elevation, motion */
  --radius-control: 6px;
  --radius-container: 10px;
  --border-width: 1px;
  --shadow-raised: 0 1px 4px rgba(16, 24, 40, 0.1);
  --duration-fast: 0.18s;
  --easing-standard: ease;
}

/* Button */
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-2) var(--space-5);
  font-size: var(--font-size-control);
  font-weight: var(--font-weight-semibold);
  border-radius: var(--radius-control);
  background: var(--color-accent);
  color: var(--color-on-solid);
  border: 0;
  transition: background var(--duration-fast) var(--easing-standard);
}
.btn:hover { background: var(--color-accent-hover); }

/* Border adds 1px per side, so padding shrinks by the same amount to keep the size identical */
.btn-secondary {
  background: transparent;
  color: var(--color-accent);
  border: var(--border-width) solid var(--color-accent);
  padding: calc(var(--space-2) - var(--border-width)) calc(var(--space-5) - var(--border-width));
}
.btn-secondary:hover { background: var(--color-accent-subtle); }

.btn-danger {
  background: var(--color-danger);
  color: var(--color-on-solid);
}
.btn-danger:hover { background: var(--color-danger-hover); }

/* Card */
.card {
  background: var(--color-surface);
  border: var(--border-width) solid var(--color-border-subtle);
  border-radius: var(--radius-container);
  padding: var(--space-6);
  box-shadow: var(--shadow-raised);
}
.card-title {
  font-size: var(--font-size-title);
  font-weight: var(--font-weight-bold);
  margin: 0 0 var(--space-2);
  color: var(--color-text-primary);
}
.card-meta {
  font-size: var(--font-size-meta);
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
- `#0f766e` → `--color-accent`. It was used for the button background, the secondary text and the secondary border.
- `#dde2e1` → `--color-border-subtle`. It was used for both the card border and the footer rule.
- `#fff` → `--color-on-solid` for text on filled buttons, and `--color-surface` for the card background. They are the same value today but now change independently, for example in dark mode.
- The `9px 17px` secondary padding is now derived from the base padding minus the border width, so the two buttons can't drift apart.

**Notes:**
- Every value is unchanged, so nothing shifts visually. That leaves spacing at six steps, with 10, 12 and 14 close together. Merging them would be a small visible change, so I left it for you to decide.
- Class names and the cascade are untouched. Component CSS reads only the role tokens, so a dark theme only needs to re-map the `--color-*` values.
