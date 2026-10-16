I found one real bug and made one change. I kept everything else as it was.

**Bug:** `--color-border-strong` points at `--ref-slate-300`, which doesn't exist. The variable would silently resolve to nothing in light mode, so strong borders would vanish. I added `--ref-slate-300: #b9c3cb;` between slate-200 and slate-600. **That value is my guess, so check it against your design file** before you send this.

```css
/* Tidewater Co-op, app tokens v3
   Raw values live in --ref-*. Components only use --color-*, --space-*, --radius-*, --font-*.
   Dark theme only remaps roles; it never touches --ref-*. */
:root {
  /* reference palette */
  --ref-teal-100: #d9f0ee;
  --ref-teal-500: #1a8a85;
  --ref-teal-700: #0f5d5a;
  --ref-teal-900: #0a3d3b;
  --ref-slate-50: #f6f8f9;
  --ref-slate-200: #dde3e7;
  --ref-slate-300: #b9c3cb;
  --ref-slate-600: #566471;
  --ref-slate-700: #3d4954;
  --ref-slate-900: #16202a;
  --ref-red-600: #b83227;
  --ref-amber-600: #a86a0a;
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
  --color-text-muted: #a9b5bf;
  --color-surface: var(--ref-slate-900);
  --color-surface-sunken: #0f161d;
  --color-border: var(--ref-slate-700);
  --color-border-strong: #5b6976;
  --color-accent: #4fc4bd;
  --color-accent-hover: #7fd8d2;
  --color-accent-subtle: #123f3d;
  --color-on-accent: var(--ref-slate-900);
  --color-focus-ring: #7fd8d2;
  --color-danger: #f0776b;
  --color-warning: #e3a84a;
  --color-success: #5fc58c;
}
```

**One inconsistency I left alone:** the header says raw values live in `--ref-*`, but the dark block has about ten raw hex values. A new dev may notice that. The fix is to move them into `--ref-*` tokens, for example `--ref-teal-300` and `--ref-teal-200`. I didn't, because that means inventing scale names, and that's your call. Or you could soften the header to say dark-theme overrides may use literals. I can make either change if you'd like.

I also didn't check contrast ratios, so I can't say the color pairs meet accessibility guidelines.
