Here's the tidied file. There's one real bug, and you need to make a decision about it before you send this.

**Bug:** `--ref-slate-300` was referenced by `--color-border-strong` but never defined. In light theme that token was silently invalid. I added `--ref-slate-300: #9aa8b3` as a proposal. I haven't checked its contrast, and strong borders on inputs usually need about 3:1 against the surface. Please pick the value you actually want.

**Changes:**
- The header says raw values live in `--ref-*`, but the dark block had 11 inline hex values. I moved them into the ref palette and left the values identical. The dark block is now only role-to-ref mappings.
- I put the slate ramp in order and grouped the ref palette by hue.

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
  --ref-teal-900: #0a3d3b;
  --ref-teal-950: #123f3d;

  --ref-slate-50: #f6f8f9;
  --ref-slate-200: #dde3e7;
  --ref-slate-300: #9aa8b3; /* proposed: was referenced but undefined */
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
  --color-accent-subtle: var(--ref-teal-950);
  --color-on-accent: var(--ref-slate-900);
  --color-focus-ring: var(--ref-teal-200);
  --color-danger: var(--ref-red-400);
  --color-warning: var(--ref-amber-400);
  --color-success: var(--ref-green-400);
}
```

**Left alone, for you to decide:**
- **Near-duplicates:** `slate-500` (`#5b6976`) and `slate-600` (`#566471`) are almost the same color. So are `teal-900` (`#0a3d3b`) and `teal-950` (`#123f3d`). They serve different roles today, so I didn't merge them, because merging changes live values. Collapsing each pair is a safe follow-up.
- **No system dark mode:** dark theme only applies through `[data-theme="dark"]`. There's no `prefers-color-scheme` fallback and no `color-scheme` declaration. I can add both if you want.
- **Contrast:** I haven't checked text/surface pairs in either theme. I'd run that before she builds on it.
