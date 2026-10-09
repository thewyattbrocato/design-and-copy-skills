Here's the cleaned-up version. Colors, radii, the shadow, and the transition duration now come from custom properties. Every resolved value matches the original, and the class names and rule order are unchanged.

```css
:root {
  /* Color */
  --color-primary: #0f766e;
  --color-primary-hover: #0d6b63;
  --color-primary-subtle: #e6f4f2;
  --color-danger: #c0392b;
  --color-danger-hover: #a93226;
  --color-on-primary: #fff;
  --color-surface: #fff;
  --color-border: #dde2e1;
  --color-text: #14201f;
  --color-text-muted: #5a6b69;

  /* Shape and elevation */
  --radius-sm: 6px;
  --radius-md: 10px;
  --shadow-card: 0 1px 4px rgba(16, 24, 40, 0.1);

  /* Motion */
  --duration-fast: 0.18s;

  /* Button sizing */
  --btn-padding-y: 10px;
  --btn-padding-x: 18px;
  --border-width: 1px;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: var(--btn-padding-y) var(--btn-padding-x);
  font-size: 15px;
  font-weight: 600;
  border-radius: var(--radius-sm);
  background: var(--color-primary);
  color: var(--color-on-primary);
  border: 0;
  transition: background var(--duration-fast) ease;
}
.btn:hover {
  background: var(--color-primary-hover);
}

/* Outlined variant: padding shrinks by the border width so the total size matches .btn */
.btn-secondary {
  background: transparent;
  color: var(--color-primary);
  border: var(--border-width) solid var(--color-primary);
  padding: calc(var(--btn-padding-y) - var(--border-width)) calc(var(--btn-padding-x) - var(--border-width));
}
.btn-secondary:hover {
  background: var(--color-primary-subtle);
}

.btn-danger {
  background: var(--color-danger);
  color: var(--color-on-primary);
}
.btn-danger:hover {
  background: var(--color-danger-hover);
}

.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
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
  border-top: 1px solid var(--color-border);
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
```

What changed:

- **Colors:** `#0f766e` appeared in three places and `#dde2e1` in two, so each is now a single token. Hover states have their own tokens. Text and muted text are named so new components can reuse them.
- **Button padding:** `.btn-secondary` used to hard-code `9px 17px` to make room for its 1px border. It now derives that from the `.btn` padding tokens, so changing the button padding keeps both variants the same size.
- **Left as literals:** the one-off spacing, font sizes, and `.card` padding. Tokenizing them is easy if you want a full spacing scale, but I didn't want to invent names for values used once.
- **Rule order:** kept as-is. `.btn-secondary` and `.btn-danger` depend on coming after `.btn` and `.btn:hover` to win the cascade.

Things to check before shipping:

- The custom properties are defined on `:root`. If this CSS is scoped into a shadow root or an iframe, move the `:root` block to a matching scope.
- If your codebase already defines variables with these names, rename the new ones to avoid collisions.
- I haven't rendered this. Since the repo isn't under git here, the easiest check is a before/after screenshot comparison of a page with buttons and cards in default, hover, and disabled states.
