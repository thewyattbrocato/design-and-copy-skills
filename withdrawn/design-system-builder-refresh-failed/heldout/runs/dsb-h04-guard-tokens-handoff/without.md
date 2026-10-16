I tidied it and fixed one bug. The file only exists in your message, so the result is below for you to paste.

**What changed**
- **Bug fix:** `--color-border-strong` pointed at `--ref-slate-300`, which was never defined. In light mode the variable resolved to nothing, so any border using it silently disappeared. I pointed it at `--ref-slate-400` (`#a9b5bf`), which was already in the file as a hardcoded dark-mode value. I didn't invent a new color.
- **Convention fix:** the header says raw values live in `--ref-*`, but the dark block had 9 hardcoded hex values. I moved them into the reference palette, so the dark block now only remaps roles.
- **Ordering:** reference scales now run light to dark within each hue.

```css
/* Tidewater Co-op, app tokens v3
   Raw values live in --ref-*. Components only use --color-*, --space-*, --radius-*, --font-*.
   Dark theme only remaps roles; it never touches --ref-*. */
:root {
  /* reference palette */
  --ref-white: #ffffff;

  --ref-teal-100: #d9f0ee;
  --ref-teal-200: #7fd8d2;
  --ref-teal-300: #4fc4bd;
  --ref-teal-500: #1a8a85;
  --ref-teal-700: #0f5d5a;
  --ref-teal-800: #123f3d;
  --ref-teal-900: #0a3d3b;

  --ref-slate-50: #f6f8f9;
  --ref-slate-200: #dde3e7;
  --ref-slate-400: #a9b5bf;
  --ref-slate-500: #5b6976;
  --ref-slate-600: #566471;
  --ref-slate-700: #3d4954;
  --ref-slate-900: #16202a;
  --ref-slate-950: #0f161d;

  --ref-red-400: #f0776b;
  --ref-red-600: #b83227;
  --ref-amber-400: #e3a84a;
  --ref-amber-600: #a86a0a;
  --ref-green-400: #5fc58c;
  --ref-green-600: #207a4d;

  /* color roles */
  --color-text: var(--ref-slate-900);
  --color-text-muted: var(--ref-slate-600);
  --color-surface: var(--ref-white);
  --color-surface-sunken: var(--ref-slate-50);
  --color-border: var(--ref-slate-200);
  --color-border-strong: var(--ref-slate-400);
  --color-accent: var(--ref-teal-700);
  --color-accent-hover: var(--ref-teal-900);
  --color-accent-subtle: var(--ref-teal-100);
  --color-on-accent: var(--ref-white);
  --color-focus-ring: var(--ref-teal-500);
  --color-danger: var(--ref-red-600);
  --color-warning: var(--ref-amber-600);
  --color-success: var(--ref-green-600);

  /* spacing, 4px base */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;

  /* radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-pill: 999px;

  /* type */
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, monospace;
  --font-size-sm: 0.875rem;
  --font-size-md: 1rem;
  --font-size-lg: 1.25rem;
  --font-size-xl: 1.75rem;
  --line-height-body: 1.5;
}

[data-theme="dark"] {
  --color-text: var(--ref-slate-50);
  --color-text-muted: var(--ref-slate-400);
  --color-surface: var(--ref-slate-900);
  --color-surface-sunken: var(--ref-slate-950);
  --color-border: var(--ref-slate-700);
  --color-border-strong: var(--ref-slate-500);
  --color-accent: var(--ref-teal-300);
  --color-accent-hover: var(--ref-teal-200);
  --color-accent-subtle: var(--ref-teal-800);
  --color-on-accent: var(--ref-slate-900);
  --color-focus-ring: var(--ref-teal-200);
  --color-danger: var(--ref-red-400);
  --color-warning: var(--ref-amber-400);
  --color-success: var(--ref-green-400);
}
```

**Check before you send**
- **Is slate-400 the border color you wanted?** I picked it only because it was already in the palette. I'd guess `#a9b5bf` on white is around 2:1 contrast. If `--color-border-strong` is used for input borders, WCAG wants 3:1 for UI components, so you may want something darker. That's a design call, so I left it.
- **Are the new names right?** The new `--ref-*` names (`teal-300`, `slate-500` and so on) are my labels for existing hex values. Rename them if your design tool uses different step numbers.
- **Near-duplicate slate colors:** `--ref-slate-500` (`#5b6976`) and `--ref-slate-600` (`#566471`) are almost identical. You could merge them, but it would shift one dark-mode border color slightly, so I left both.
