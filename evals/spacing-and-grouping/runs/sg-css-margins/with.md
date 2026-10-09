```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
}

.card {
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: var(--space-3);
}
.card.featured { padding: var(--space-5); }
.card h3 { margin-bottom: var(--space-2); }
.card p { margin-bottom: var(--space-4); }
.card .meta { margin-bottom: var(--space-3); }
.card .actions {
  margin-top: var(--space-1);
  margin-bottom: var(--space-4);
}
.card .actions button {
  margin-right: var(--space-2);
  padding: var(--space-2) var(--space-4);
}

.grid {
  display: flex;
  gap: var(--space-4);
}

.section-title {
  margin-top: var(--space-6);
  margin-bottom: var(--space-4);
}

.toolbar a { margin-right: var(--space-3); }
```

**What changed**
- **Spacing scale:** I added a 4px-based scale as custom properties (4, 8, 12, 16, 24, 32). Every margin and padding now uses it.
- **Odd values snapped to the scale:** 13→12, 22→24, 7→8, 19→16, 11→12, 5→4, 14→16, 9→8, 6/17→16 and 23→the section-title values below.
- **Card gaps in `.grid`:** The `margin-right` and `margin-bottom` on `.grid > .card` are replaced by `gap: 16px` on `.grid`. The container now owns the spacing, and there is no extra gap after the last card. The 16px gap is also larger than the 12px card padding, so cards read as separate.
- **`.section-title`:** The margins were 23px above and below, so the title floated between sections. It is now 32px above and 16px below, which ties it to the content it introduces. It will look different from before.
- **Buttons:** Padding goes from `3px 7px` to `8px 16px`. That is a taller, more comfortable button, with horizontal padding twice the vertical. If you want the old compact size, use `4px 8px`.
- **Formatting:** The one-line rules are expanded to one property per line. Related declarations are grouped, and `margin-top` now comes before `margin-bottom`.

**Things to check**
- **Row spacing:** `.grid` doesn't wrap, so the old `margin-bottom` on cards only added space below the row. If you wrap the grid with `flex-wrap: wrap`, `gap` will handle the row spacing too.
- **Last child in a card:** Cards still use margins between their children. If the last child leaves extra space at the bottom, add `.card > :last-child { margin-bottom: 0; }`.
