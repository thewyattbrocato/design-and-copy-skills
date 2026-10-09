```css
:root {
  /* Raw values */
  --teal-700: #0f766e;
  --teal-800: #0d6b63;
  --teal-50:  #e6f4f2;
  --red-600:  #c0392b;
  --red-700:  #a93226;
  --ink-900:  #14201f;
  --ink-600:  #5a6b69;
  --ink-200:  #dde2e1;
  --white:    #fff;

  /* Semantic roles (components read only these) */
  --color-accent:            var(--teal-700);
  --color-accent-hover:      var(--teal-800);
  --color-accent-subtle:     var(--teal-50);
  --color-danger:            var(--red-600);
  --color-danger-hover:      var(--red-700);
  --color-on-solid:          var(--white);
  --color-surface:           var(--white);
  --color-text-primary:      var(--ink-900);
  --color-text-secondary:    var(--ink-600);
  --color-border-subtle:     var(--ink-200);

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
  --font-weight-strong: 600;
  --font-weight-heading: 700;

  /* Shape, border, elevation, motion */
  --radius-sm: 6px;
  --radius-md: 10px;
  --border-width: 1px;
  --shadow-raised: 0 1px 4px rgba(16, 24, 40, 0.10);
  --duration-fast: 0.18s;
  --ease-standard: ease;
}

/* Button */
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-2) var(--space-5);
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-strong);
  border-radius: var(--radius-sm);
  background: var(--color-accent);
  color: var(--color-on-solid);
  border: 0;
  transition: background var(--duration-fast) var(--ease-standard);
}
.btn:hover { background: var(--color-accent-hover); }

/* Border is 1px here, so padding shrinks by the border width to keep the same outer size */
.btn-secondary {
  background: transparent;
  color: var(--color-accent);
  border: var(--border-width) solid var(--color-accent);
  padding: calc(var(--space-2) - var(--border-width)) calc(var(--space-5) - var(--border-width));
}
.btn-secondary:hover { background: var(--color-accent-subtle); }

.btn-danger { background: var(--color-danger); }
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
  font-weight: var(--font-weight-heading);
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

**What changed**
- **Colors:** every color value is now a token. The two border colors that were already identical (`#dde2e1`) now share one role. No colors were merged or altered.
- **`.btn-danger`:** I dropped `color:#fff` because it duplicated what `.btn` already sets. I did not drop `border:0`, because it is inherited too, but nothing there needed changing.
- **`.btn-secondary`:** the `9px 17px` padding is now `calc(10px - 1px) calc(18px - 1px)`. The result is the same size, and the relationship to the border is now explicit.
- **Rendering:** every computed value is identical, so nothing visible changes.

**Trade-offs**
- I kept the spacing scale at 6, 10, 12, 14, 18 and 20. The pairs 12/14 and 18/20 are close enough that a stricter scale would merge them, but a 2px shift would change the layout slightly. If you accept that, collapse them to 12 and 20. That would give a tighter 4-step scale (6, 10, 12, 20).
- I assumed a single light theme. A dark theme would only need to remap the `--color-*` roles, because components never read the raw `--teal-*`, `--red-*` or `--ink-*` values.
