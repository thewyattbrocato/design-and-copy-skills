**Pick: Dev A's 4px base with a 1.2 ratio.** It's the only option that fits both the dense desktop tables and the gloved tablet targets, and it matches Tailwind's spacing.

**Why**

- **Density needs 4px steps.** Dense table rows at 28px and 36px are multiples of 4 but not of 8. An 8px grid makes you round to 32 or 40, which costs rows on desktop.
- **Gloves set the floor, not the grid.** Interactive targets on tablet should be at least 48px. A 4px grid reaches that as easily as an 8px grid does.
- **1.333 is too coarse for UI.** Starting from 14px, it jumps 14 → 19 → 25 → 33. That's fine for editorial pages, but in a data UI you need small steps between table text, labels, and headers.
- **Dev C's Tailwind is already a 4px base.** Its spacing unit is 0.25rem (4px). Its type scale is hand-picked, not a ratio, so "use Tailwind" can't settle the type question. If you use Tailwind, keep its spacing scale and define your own type tokens.

**Spacing tokens (px, 4px base)**

| Token | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 10 | 12 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Value | 0 | 4 | 8 | 12 | 16 | 20 | 24 | 32 | 40 | 48 | 64 |

**Type tokens (1.2 ratio, anchored at 14px desktop body)**

| Token | Size / line-height | Use |
|---|---|---|
| `text-xs` | 12 / 16 | Column metadata, badges |
| `text-sm` | 14 / 20 | Table cells, body (desktop base) |
| `text-md` | 17 / 24 | Labels, form fields |
| `text-lg` | 20 / 24 | Section headers |
| `text-xl` | 24 / 32 | Page titles |
| `text-2xl` | 29 / 36 | Rare, KPI numbers |
| `text-3xl` | 35 / 40 | Rare, empty states |

Sizes are rounded to whole pixels from the 1.2 steps (16.8 → 17, 20.2 → 20, 28.8 → 29, 34.8 → 35). Line-heights stay on the 4px grid.

**Density and touch**

| Context | Row height | Control height | Min target |
|---|---|---|---|
| Desktop compact | 28 | 28 | 28 |
| Desktop default | 36 | 32 | 32 |
| Tablet (gloves) | 48 | 48 | 48 |

**Tablet mode:** set the root font size to 16px instead of 14px. Every `rem` token then scales by 16/14 (about 1.14) and the 1.2 ratio stays intact, so the same token names work on both surfaces.

**Trade-off:** a 1.2 ratio gives you more tokens to remember than 1.333 does. Limit product code to `text-sm`, `text-md`, and `text-lg` for most UI, and reserve the larger steps for page-level headers.
