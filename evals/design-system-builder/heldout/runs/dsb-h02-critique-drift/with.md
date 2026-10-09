**What's going on:** there are no shared decisions. Each rule was written with a hand-picked value, so near-identical values pile up. No one value looks wrong, but the whole thing never lines up. From your snippet:

| Property | What's in use | Problem |
|---|---|---|
| Blue | `#2f6fed`, `#2e6dea` | Same color, one step apart. `.btn-big` is a copy-paste drift. |
| Muted grays | `#8a8f98`, `#8d929b`, `#858a93` | Three names for one role. |
| Success green | `#e6f6ea`/`#1f7a3a` and `#e4f5e8`/`#217c3d` | Alert and badge are the same role with different values. |
| Borders | `#e3e5e8`, `#e1e4e8` | Same role, two values. |
| Radii | 4, 5, 6, 7, 9, 10, 12 | Seven values, with no scale. Inputs and selects, which sit side by side in forms, differ (6 vs 4). |
| Spacing | 9, 11, 13, 14, 17, 18, 19, 22, 26, 34 | 1–2px steps that nobody can perceive as intentional. |
| Control heights | input 38, select 40 | Adjacent controls that don't align. |
| Shadows | `.12`/2/7, `.10`/3/9, `.28`/12/40 | Card and panel are nearly the same elevation but not identical. |
| Type | 31, 23, 19, 17 (h4 = btn-big) | An unsystematic scale with no rationale. |

Card and panel also look like one component with two names, and `.muted`/`.hint`/`.caption` look like one role.

Roughly 40 distinct values are doing the work of about 12 decisions. The inconsistency comes from the drift, not from any single bad choice. That's why nobody can point at it.

**What I'd do, in order:**

1. **Inventory from the real repo.** Grep every color, radius, spacing, font-size and shadow, with counts (`[count from your repo]`). Your snippet already shows the pattern, but the counts tell you which value in each cluster wins.

2. **Fix the scales on paper.** Pick short scales and a merge map (old → new). A starting proposal:
   - Spacing: 4, 8, 12, 16, 24, 32, 48
   - Radius: 4, 8, 12 (control, container, overlay)
   - Elevation: 2 levels (raised, overlay)
   - Type: 5 roles, such as caption 12, body 14, lead 17, heading 23, display 31
   - Colors: one value per role. Pick the most-used one from the inventory, not an average.
   - Control height: one value, so inputs, selects and buttons align.

3. **Add semantic CSS custom properties.** Name them by role: `--color-accent`, `--color-text-muted`, `--color-border-subtle`, `--color-success-surface`, `--space-3`, `--radius-control`. Define them once in `:root`. Don't add component-level tokens yet.

4. **Migrate in blast-radius order.**
   1. Colors, which are mechanical and nearly invisible.
   2. Radius and control heights, where you'll see small, visible alignment changes.
   3. Spacing, which shifts layouts, so do it screen by screen with visual diffs.
   4. Type and shadows last.

   Merge `.card`/`.panel` and `.muted`/`.hint`/`.caption` as you go.

5. **Add a guard so drift can't come back.** Use a stylelint rule that bans raw hex and off-scale px values outside the token file. Add a short guide page, with an owner who can say no to new values. Without this step, the mess returns within a quarter.

Don't start with a redesign or a component library. The bulk of the problem is value drift, and steps 1–3 remove most of it without changing the intended look.

Assumptions: a web product with one brand and a small team, no existing design system, and no dark mode yet. The proposed scales are starting points, not checked against your screens. Contrast on the grays (about `#8a8f98` on white is roughly 3:1) needs checking before you pick the winner, since body-size muted text likely fails AA.
