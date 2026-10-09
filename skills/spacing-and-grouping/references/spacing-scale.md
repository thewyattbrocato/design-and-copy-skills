# Spacing scale

Load this when you pick spacing values, audit existing ones, or define custom properties.

## Why a scale

A scale turns "how much space?" into "which step?". It keeps the same relationship at the same distance everywhere, shortens decisions, and makes later changes one edit. Five to eight steps are enough for most products. More steps invite near-duplicates that nobody can tell apart.

## Two ways to build one

**From a base unit.** Pick 4 px (finer, good for dense tools) or 8 px (coarser, good for marketing and reading pages). Use multiples, and let the steps grow faster as they get larger, because the eye cannot tell 60 from 64 but can tell 4 from 8.

| Step | 4 px base | Typical use |
| --- | --- | --- |
| 1 | 4 | icon to its label, tight chips |
| 2 | 8 | label to field, items inside a small group |
| 3 | 12 | between related rows, small padding |
| 4 | 16 | default padding, gap between fields |
| 5 | 24 | between groups, card padding |
| 6 | 32 | between larger groups |
| 7 | 48 | between sections |
| 8 | 64-96 | page sections, hero breathing room |

**From the text.** When prose dominates, derive steps from the body line height (say 1.5 times a 16 px body, which is 24 px). Use half a line, one line, and two lines as the main steps, with a quarter line for tight pairs. Space then scales with the text if the user changes the font size, as long as you write it in `rem` or `em`.

Pick one method per project. If an existing system has its own steps, use those and skip this file.

## Naming

Name steps by size (`space-2`, `space-md`), not by use (`card-padding`, `form-gap`). A use-name breaks the first time a second place needs the same distance. Keep use-names, if any, as a thin layer on top.

```css
:root {
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.5rem;
  --space-6: 2rem;
  --space-7: 3rem;
  --space-8: 5rem;
}
```

Prefer relative units (`rem`) for spacing that sits around text, so it follows the user's text size. Fixed pixels are fine for hairlines and small icon gaps.

## Using the scale

- Pick the within-group step first, then pick between-group steps at least two steps larger or about double.
- Tighten pairs that share one idea (title and subtitle, label and input) with the smallest steps; give clearly separate regions a step that survives a squint.
- Let an occasional exception be a documented step, not a stray number. If you keep needing a value between two steps, the scale may be missing one step; add it once.
- Fluid section spacing is a good fit for `clamp(min, preferred, max)`, with min and max both from the scale.

## Auditing existing CSS

1. Collect every `margin`, `padding`, and `gap` value in the file.
2. Round each to the nearest step. Where two values round to different steps and the elements have the same relationship, pick one.
3. Replace sibling margins with a parent `gap` where you can (see the component reference).
4. Re-read the result: groups should still look like groups, and the larger gaps should still be clearly larger.
