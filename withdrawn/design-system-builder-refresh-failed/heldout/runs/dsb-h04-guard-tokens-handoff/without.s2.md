I tidied it below. There's no file on disk, so this is just the revised text.

**Changes**
1. **Bug fix:** `--color-border-strong` referenced `--ref-slate-300`, which didn't exist. The variable was silently invalid in light mode. I added `--ref-slate-300: #b8c2ca`. That value is my guess, halfway between slate-200 and the dark theme's strong border, so please swap in the one your designer intended.
2. **Header consistency:** The header says raw values live in `--ref-*`, but the dark theme had 11 inline hex values. I moved them into new ref tokens with the same hex values, so nothing changes visually. The dark theme now only remaps roles, as the comment says.
3. **Ordering:** I sorted each ref scale from light to dark and grouped it by hue.

```css
/* Tidewater Co-op, app tokens v3
   Raw values live in --ref-*. Components only use --color-*, --space-*, --radius-*, --font-*.
   Dark theme only remaps roles; it never touches --ref-*. */
:root {
  /* reference palette */
  --ref-teal-100: #d9f0ee;
  --ref-teal-200: #7fd8d2;
  --ref-teal-300: #4fc4bd;
  --ref-teal-500: #1a8a85;
  --ref-teal-700: #0f5d5a;
  --ref-teal-800: #123f3d;
  --ref-teal-900: #0a3d3b;

  --ref-slate-50: #f6f8f9;
  --ref-slate-200: #dde3e7;
  --ref-slate-300: #b8c2ca; /* TODO: confirm value, was previously undefined */
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

  --ref-white: #ffffff;

  /* color roles */
  --color-text: var(--ref-slate-900);
  --color-text-muted: var(--ref-slate-600);
  --color-surface: var(--ref-white);
  --color-surface-sunken: var(--ref-slate-50);
  --color-border: var(--ref-slate-200);
  --color-border-strong: var(--ref-slate-300);
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

**Worth knowing before Monday**
- The ref names (`teal-200`, `slate-400` and so on) are my labels. They sit in sensible places on each scale, but rename them if your design tool uses different numbers.
- I didn't check contrast ratios. If you want, I can check the text and accent pairs in both themes.
