```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
}

.card {
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: var(--space-3);
}

.card.featured {
  padding: var(--space-6);
}

.card h3 {
  margin-bottom: var(--space-2);
}

.card p {
  margin-bottom: var(--space-4);
}

.card .meta {
  margin-bottom: var(--space-3);
}

.card .actions {
  margin-top: var(--space-1);
  margin-bottom: var(--space-4);
}

.card .actions button {
  margin-right: var(--space-2);
  padding: var(--space-1) var(--space-2);
}

.grid {
  display: flex;
}

.grid > .card {
  margin-right: var(--space-2);
  margin-bottom: var(--space-4);
}

.section-title {
  margin-block: var(--space-6);
}

.toolbar a {
  margin-right: var(--space-3);
}
```

**What changed**
- **Spacing scale:** Replaced the one-off values (3, 5, 6, 7, 9, 11, 13, 14, 17, 19, 22, 23px) with a 4px-based scale (4, 8, 12, 16, 24px) defined as custom properties. Each value was rounded to the nearest step, and ties (6px and 14px) went up.
- **Rounding:** 13→12, 22→24, 7→8, 19→16, 11→12, 5→4, 14→16, 9→8, 3→4, 6→8, 17→16, 23→24. Visible shifts are at most 3px.
- **Formatting:** Expanded the single-line rules to one declaration per line.
- **Section title:** Combined the duplicate `margin-top` and `margin-bottom` (both 23px) into `margin-block: var(--space-6)`.

I kept the `margin-right` on `.grid > .card` rather than switching to `gap`. `gap` would drop the trailing margin on the last card, which changes the layout. It's worth considering if you're happy with that.
