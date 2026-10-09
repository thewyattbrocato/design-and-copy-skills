```css
:root {
  /* Raw values */
  --teal-700: #0f766e;
  --teal-800: #0d6b63;
  --teal-50:  #e6f4f2;
  --red-700:  #c0392b;
  --red-800:  #a93226;
  --white:    #fff;
  --slate-200: #dde2e1;
  --slate-500: #5a6b69;
  --slate-900: #14201f;

  /* Semantic roles */
  --color-surface:        var(--white);
  --color-border-subtle:  var(--slate-200);
  --color-text-primary:   var(--slate-900);
  --color-text-secondary: var(--slate-500);
  --color-text-on-accent: var(--white);
  --color-accent:         var(--teal-700);
  --color-accent-hover:   var(--teal-800);
  --color-accent-subtle:  var(--teal-50);
  --color-danger:         var(--red-700);
  --color-danger-hover:   var(--red-800);

  /* Spacing */
  --space-1: 6px;
  --space-2: 10px;
  --space-3: 12px;
  --space-4: 14px;
  --space-5: 18px;
  --space-6: 20px;

  /* Type */
  --font-size-meta:  13px;
  --font-size-body:  15px;
  --font-size-title: 19px;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;

  /* Radius, elevation, motion */
  --radius-sm: 6px;
  --radius-md: 10px;
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
  border-radius: var(--radius-sm);
  background: var(--color-accent);
  color: var(--color-text-on-accent);
  border: 0;
  transition: background var(--duration-fast) var(--ease-standard);
}
.btn:hover { background: var(--color-accent-hover); }

.btn-secondary {
  background: transparent;
  color: var(--color-accent);
  border: 1px solid var(--color-accent);
  /* 1px less than .btn so the border doesn't change the overall size */
  padding: calc(var(--space-2) - 1px) calc(var(--space-5) - 1px);
}
.btn-secondary:hover { background: var(--color-accent-subtle); }

.btn-danger {
  background: var(--color-danger);
  color: var(--color-text-on-accent);
}
.btn-danger:hover { background: var(--color-danger-hover); }

/* Card */
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border-subtle);
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
  border-top: 1px solid var(--color-border-subtle);
  display: flex;
  gap: var(--space-3);
  justify-content: flex-end;
}
```

**Merge map (old value → token):**
- `#dde2e1` (card border and footer rule) → `--color-border-subtle`
- `#fff` (button text, card background) → `--color-text-on-accent` / `--color-surface`, both pointing at `--white`
- `#0f766e` (button background, secondary text and border) → `--color-accent`
- `6px` (button gap and radius) → `--space-1` / `--radius-sm`
- `10px` (button padding, title margin) → `--space-2`
- `14px` (meta margin, footer padding) → `--space-4`
- `18px` (button padding, footer margin) → `--space-5`
- `9px 17px` → `calc(... - 1px)` on the same tokens. It renders identically and stays in sync if the button padding changes.

**Notes:**
- Every rendered value is unchanged. Components read only the semantic roles, so a dark theme or second brand later means remapping the roles in the middle block, not editing components.
- The spacing scale (6/10/12/14/18/20) has close neighbors, such as 12/14 and 18/20. I kept them to avoid any visible shift. If you accept a 1–2px nudge, collapsing it to something like 6/10/14/20 would give a cleaner scale.
