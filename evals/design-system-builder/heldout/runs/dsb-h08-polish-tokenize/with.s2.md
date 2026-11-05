```css
:root {
  /* color: raw palette → roles */
  --color-accent:          #0f766e;
  --color-accent-hover:    #0d6b63;
  --color-accent-subtle:   #e6f4f2;
  --color-danger:          #c0392b;
  --color-danger-hover:    #a93226;
  --color-on-solid:        #fff;
  --color-surface:         #fff;
  --color-border-subtle:   #dde2e1;
  --color-text-primary:    #14201f;
  --color-text-secondary:  #5a6b69;

  /* spacing */
  --space-1: 6px;
  --space-2: 10px;
  --space-3: 12px;
  --space-4: 14px;
  --space-5: 18px;
  --space-6: 20px;

  /* type */
  --font-size-meta:  13px;
  --font-size-body:  15px;
  --font-size-title: 19px;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;

  /* shape, border, elevation, motion */
  --radius-sm: 6px;
  --radius-md: 10px;
  --border-width: 1px;
  --shadow-raised: 0 1px 4px rgba(16, 24, 40, .10);
  --duration-fast: .18s;
  --ease-standard: ease;
}

/* Button */
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-2) var(--space-5);
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-semibold);
  border: 0;
  border-radius: var(--radius-sm);
  background: var(--color-accent);
  color: var(--color-on-solid);
  transition: background var(--duration-fast) var(--ease-standard);
}
.btn:hover { background: var(--color-accent-hover); }

.btn-secondary {
  background: transparent;
  color: var(--color-accent);
  border: var(--border-width) solid var(--color-accent);
  /* padding minus the border keeps the outer size equal to .btn */
  padding: calc(var(--space-2) - var(--border-width)) calc(var(--space-5) - var(--border-width));
}
.btn-secondary:hover { background: var(--color-accent-subtle); }

.btn-danger { background: var(--color-danger); color: var(--color-on-solid); }
.btn-danger:hover { background: var(--color-danger-hover); }

/* Card */
.card {
  background: var(--color-surface);
  border: var(--border-width) solid var(--color-border-subtle);
  border-radius: var(--radius-md);
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

**Merge map:** every value maps one-to-one to a token, so rendering is identical. Class names and cascade order are unchanged.

- **Spacing:** the 10, 12 and 14px steps are close together. I kept them to avoid a visible change. If you later allow small shifts, merge 12 and 14, or 10 and 12, to tighten the scale.
- **Missing states:** the CSS has no focus-visible, disabled or pressed states. Adding them would change behavior, so I left them out, but they're the next gap to fill.
