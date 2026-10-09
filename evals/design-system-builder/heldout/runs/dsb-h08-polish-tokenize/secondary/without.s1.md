```css
:root {
  --color-primary: #0f766e;
  --color-primary-hover: #0d6b63;
  --color-primary-subtle: #e6f4f2;
  --color-danger: #c0392b;
  --color-danger-hover: #a93226;
  --color-surface: #fff;
  --color-border: #dde2e1;
  --color-text: #14201f;
  --color-text-muted: #5a6b69;

  --radius-button: 6px;
  --radius-card: 10px;
  --shadow-card: 0 1px 4px rgba(16, 24, 40, .10);

  --space-button-y: 10px;
  --space-button-x: 18px;
}

/* Buttons: variants set --btn-* tokens; the base rules read them */
.btn {
  --btn-bg: var(--color-primary);
  --btn-bg-hover: var(--color-primary-hover);
  --btn-fg: #fff;

  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: var(--space-button-y) var(--space-button-x);
  font-size: 15px;
  font-weight: 600;
  border-radius: var(--radius-button);
  background: var(--btn-bg);
  color: var(--btn-fg);
  border: 0;
  transition: background .18s ease;
}
.btn:hover { background: var(--btn-bg-hover); }

/* 1px border is offset by 1px less padding so the button keeps the same size */
.btn-secondary {
  --btn-bg: transparent;
  --btn-bg-hover: var(--color-primary-subtle);
  --btn-fg: var(--color-primary);

  border: 1px solid var(--color-primary);
  padding: calc(var(--space-button-y) - 1px) calc(var(--space-button-x) - 1px);
}

.btn-danger {
  --btn-bg: var(--color-danger);
  --btn-bg-hover: var(--color-danger-hover);
}

/* Cards */
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-card);
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
  border-top: 1px solid var(--color-border);
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
```

What changed:

- **Tokens:** colors, radii, shadow, and button padding now live in `:root`. Each value appears once, so new components can reuse them.
- **Button variants:** `.btn` reads `--btn-bg`, `--btn-bg-hover`, and `--btn-fg`. The variants only set those tokens, so the hover rule is written once. I removed `.btn-secondary:hover`, since `.btn:hover` now picks up its hover color.
- **Unchanged:** class names, the `.18s ease` transition, `border: 0` on `.btn`, and the 1px-border padding offset on `.btn-secondary`.

I checked the cascade by reading it, not in a browser. Before shipping, compare the default, hover, and combined `.btn.btn-danger` states in the running app to confirm they match the originals.
