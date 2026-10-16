Here's the tidied file. The biggest problem was a bug: `--color-border-strong` pointed at `--ref-slate-300`, which didn't exist. That means the variable was invalid wherever it was used.

```css
/* Tidewater Co-op, app tokens v3
   Raw values live in --ref-*. Components only use --color-*, --space-*, --radius-*, --font-*.
   Dark theme only remaps roles; it never touches --ref-*. */
:root {
  /* reference palette */
  --ref-teal-100: #d9f0ee;
  --ref-teal-300: #7fd8d2;
  --ref-teal-400: #4fc4bd;
  --ref-teal-500: #1a8a85;
  --ref-teal-700: #0f5d5a;
  --ref-teal-900: #0a3d3b;

  --ref-slate-50: #f6f8f9;
  --ref-slate-200: #dde3e7;
  --ref-slate-300: #a9b5bf;
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
  --color-text-muted: var(--ref-slate-300);
  --color-surface: var(--ref-slate-900);
  --color-surface-sunken: var(--ref-slate-950);
  --color-border: var(--ref-slate-700);
  --color-border-strong: var(--ref-slate-600);
  --color-accent: var(--ref-teal-400);
  --color-accent-hover: var(--ref-teal-300);
  --color-accent-subtle: var(--ref-teal-900);
  --color-on-accent: var(--ref-slate-900);
  --color-focus-ring: var(--ref-teal-300);
  --color-danger: var(--ref-red-400);
  --color-warning: var(--ref-amber-400);
  --color-success: var(--ref-green-400);
}
```

**What changed**
- **Undefined variable:** I defined `--ref-slate-300` as `#a9b5bf`. I reused a value you already had in dark mode, because I didn't want to guess a new color.
- **Header rule:** The header says raw values live in `--ref-*`, but the dark theme had 9 hex literals. They're now ref tokens (`teal-300/400`, `slate-300/950`, `red/amber/green-400`), so the comment is true.
- **Ramps:** I grouped the palette by hue and sorted each ramp light to dark.

**Merges that change a rendered value (please look at these)**

| Dark role | Was | Now | Difference |
|---|---|---|---|
| `border-strong` | `#5b6976` | `slate-600` `#566471` | nearly identical |
| `accent-subtle` | `#123f3d` | `teal-900` `#0a3d3b` | slightly darker |
| `text-muted` | `#a9b5bf` | `slate-300` | none, same value |

If you'd rather keep the old values exactly, give them their own ref tokens. I'd merge them, since each pair was a near-duplicate.

**Check before Monday**
- Light `border-strong` on white is about 2.1:1 by my rough calculation. That's fine for decorative dividers. It's below the 3:1 WCAG asks for input borders, so if inputs use this role, you'll want a darker `slate-300` for light mode. I didn't contrast-check any other pairs, in either theme.
- The spacing, radius and type scales are short and well spaced, so I left them alone.
