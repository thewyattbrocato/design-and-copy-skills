**Pick: a 4px spacing base, a 1.125–1.2 type scale, and a fixed set of named steps. Don't follow the 1.333 ratio or raw Tailwind.**

Tallyard needs two things that pull in opposite directions. Dense desktop tables need fine control at the small end. Gloved tablet use needs big targets and no cramped rows. A 4px base handles both: 8px steps are too coarse for 28–36px table rows, and you can still reach 48px+ targets with it. A 1.333 ratio grows too fast. Going from 14px to 19px to 25px leaves you with no usable sizes between body and heading, and tables can't use any of them. Tailwind's defaults are a reasonable raw material, but they are 4px-based with irregular type steps. So Dev C's answer is close to Dev A's, and you should still own the token names and the short list of steps.

**Spacing (px, 4px base, 9 steps)**

| Token | Value | Typical use |
|---|---|---|
| `space.1` | 4 | icon-to-label gap, cell inner gap |
| `space.2` | 8 | dense cell padding, inline gaps |
| `space.3` | 12 | control padding, compact stack |
| `space.4` | 16 | default inset, form field gap |
| `space.5` | 24 | card padding, section gap |
| `space.6` | 32 | touch-mode gaps, group separation |
| `space.7` | 48 | page margins, large gaps |
| `space.8` | 64 | layout regions |
| `space.9` | 96 | rare page-level separation |

I left out 20 and 40 on purpose. They sit too close to their neighbors to be distinct choices.

**Type (base 14px desktop, 16px tablet, ratio about 1.2, 6 roles)**

| Role | Desktop | Tablet | Line height |
|---|---|---|---|
| `text.caption` | 12 | 14 | 16 / 20 |
| `text.body-dense` (tables) | 13 | 16 | 20 / 24 |
| `text.body` | 14 | 16 | 20 / 24 |
| `text.label-lg` / `text.title-sm` | 17 | 20 | 24 / 28 |
| `text.title` | 20 | 24 | 28 / 32 |
| `text.display` | 24 | 29 | 32 / 36 |

Two notes on the table:
- Desktop `body-dense` and `body` are only 1px apart. If that's too close for you, merge them and use `space.2` padding to get density instead.
- Use tabular numerals (`font-variant-numeric: tabular-nums`) in every quantity column.

**Density modes**

The platforms differ in density, not in the scale. Switch a `density` theme (`compact` for desktop, `touch` for tablet) that remaps the role tokens. Components read those roles and never the raw steps.

| Role | Compact | Touch |
|---|---|---|
| `control.height` | 32 | 48 |
| `table.row-height` | 32 | 56 |
| `target.min` | 32 | 48 |
| `cell.padding-x` | `space.2` | `space.4` |

Choose touch mode by device, with a manual override. Don't use viewport width, because a 10-inch tablet and a small laptop window can overlap.

**Two caveats**
- 48px is a sensible minimum for gloved use, but check it with real gloves. Warehouse gloves may need 56px for primary actions such as Confirm count.
- I assumed a web product with one brand, so check that against your setup.

**Settle the disagreement**

Dev A's base wins. Dev B's "cleaner" 8px grid still exists as a subset: `space.2, 4, 6, 7, 8, 9` are all multiples of 8. Dev C's Tailwind point is covered by exporting these tokens into the Tailwind config as the only allowed values. Disable Tailwind's default spacing and font-size keys so nobody reaches for `p-5` or `text-lg` by accident.
