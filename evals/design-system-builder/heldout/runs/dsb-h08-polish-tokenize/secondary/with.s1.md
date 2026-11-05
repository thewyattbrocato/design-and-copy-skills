```css
:root {
  /* Color */
  --color-primary: #0f766e;
  --color-primary-hover: #0d6b63;
  --color-primary-tint: #e6f4f2;
  --color-danger: #c0392b;
  --color-danger-hover: #a93226;
  --color-on-primary: #fff;
  --color-surface: #fff;
  --color-border: #dde2e1;
  --color-text-strong: #14201f;
  --color-text-muted: #5a6b69;

  /* Shape and elevation */
  --radius-md: 6px;
  --radius-lg: 10px;
  --shadow-card: 0 1px 4px rgba(16, 24, 40, .10);

  /* Type */
  --font-size-sm: 13px;
  --font-size-md: 15px;
  --font-size-lg: 19px;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* Spacing scale */
  --space-1: 6px;
  --space-2: 10px;
  --space-3: 12px;
  --space-4: 14px;
  --space-5: 18px;
  --space-6: 20px;

  /* Motion */
  --transition-fast: .18s ease;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: var(--space-2) var(--space-5);
  font-size: var(--font-size-md);
  font-weight: var(--font-weight-semibold);
  border-radius: var(--radius-md);
  background: var(--color-primary);
  color: var(--color-on-primary);
  border: 0;
  transition: background var(--transition-fast);
}
.btn:hover { background: var(--color-primary-hover); }

/* 1px border is inside the padding, so padding is reduced by 1px to keep the same box size */
.btn-secondary {
  background: transparent;
  color: var(--color-primary);
  border: 1px solid var(--color-primary);
  padding: calc(var(--space-2) - 1px) calc(var(--space-5) - 1px);
}
.btn-secondary:hover { background: var(--color-primary-tint); }

.btn-danger { background: var(--color-danger); color: var(--color-on-primary); }
.btn-danger:hover { background: var(--color-danger-hover); }

/* Card */
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  box-shadow: var(--shadow-card);
}

.card-title {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-bold);
  margin: 0 0 var(--space-2);
  color: var(--color-text-strong);
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

Notes:

- **Same output:** Every token resolves to the original literal value, and the class names, selectors, and specificity are unchanged. `.btn-secondary` keeps its 10px/18px outer box by subtracting the 1px border from its padding, which is the same calculation the original numbers did.
- **Spacing scale:** The original values (6, 10, 12, 14, 18, 20) become a six-step scale. New components can pick from it, and off-scale values will stand out in review.
- **Left alone on purpose:** I didn't add `:focus-visible` styles or a disabled state, since they would be visible changes. They are good candidates for a follow-up.
- **Not verified in a browser:** I checked the values by reading them against the originals, not by rendering. A quick visual diff of a few pages would confirm it.
