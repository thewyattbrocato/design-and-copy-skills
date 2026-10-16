I've tidied it below. Two changes need your attention before you send it.

**Bug fixed:** `--color-border-strong` pointed at `--ref-slate-300`, which was never defined. In light mode that declaration was invalid, so strong borders silently fell back to the inherited or initial value. I added `--ref-slate-400: #8795a1` and pointed the role at it. That hex is my proposal, not a value from your design. By my hand calculation it gives about 3:1 against white, but I haven't run a contrast tool on it. Swap in your designer's value if one exists.

**Header rule enforced:** the file says raw values live in `--ref-*`, but the dark block had 11 literal hexes. I moved each into a ref token and left the dark block as role-to-ref remaps only. The rendered colors are unchanged.

```css
/* Tidewater Co-op, app tokens v3
   Raw values live in --ref-*. Components only use --color-*, --space-*, --radius-*, --font-*.
   Themes only remap roles to --ref-* values; they never define raw values or change --ref-*. */
:root {
  color-scheme: light;

  /* reference palette: teal */
  --ref-teal-100: #d9f0ee;
  --ref-teal-300: #7fd8d2;
  --ref-teal-400: #4fc4bd;
  --ref-teal-500: #1a8a85;
  --ref-teal-700: #0f5d5a;
  --ref-teal-800: #123f3d;
  --ref-teal-900: #0a3d3b;

  /* reference palette: slate */
  --ref-slate-50: #f6f8f9;
  --ref-slate-200: #dde3e7;
  --ref-slate-300: #a9b5bf;
  --ref-slate-400: #8795a1;
  --ref-slate-500: #5b6976;
  --ref-slate-600: #566471;
  --ref-slate-700: #3d4954;
  --ref-slate-900: #16202a;
  --ref-slate-950: #0f161d;

  /* reference palette: status */
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
  color-scheme: dark;

  --color-text: var(--ref-slate-50);
  --color-text-muted: var(--ref-slate-300);
  --color-surface: var(--ref-slate-900);
  --color-surface-sunken: var(--ref-slate-950);
  --color-border: var(--ref-slate-700);
  --color-border-strong: var(--ref-slate-500);
  --color-accent: var(--ref-teal-400);
  --color-accent-hover: var(--ref-teal-300);
  --color-accent-subtle: var(--ref-teal-800);
  --color-on-accent: var(--ref-slate-900);
  --color-focus-ring: var(--ref-teal-300);
  --color-danger: var(--ref-red-400);
  --color-warning: var(--ref-amber-400);
  --color-success: var(--ref-green-400);
}
```

**Other changes:**
- I grouped the ramps by hue and sorted each by step.
- I reworded the header's dark-theme sentence to match what the dark block now does.
- I added `color-scheme: light` and `color-scheme: dark`. These make native form controls and scrollbars follow the theme.

**Flagged but left alone, since changing them would alter visible colors:**
- `--ref-slate-500` (`#5b6976`) and `--ref-slate-600` (`#566471`) are nearly identical. The same goes for `--ref-teal-800` (`#123f3d`) and `--ref-teal-900` (`#0a3d3b`). Merging each pair would drop two ref tokens. That is a design call for you or your designer.
- Nothing applies dark mode from the OS setting. `[data-theme="dark"]` only works if something sets the attribute. If you want it to follow the OS, add a `prefers-color-scheme` rule or set the attribute from JS.
