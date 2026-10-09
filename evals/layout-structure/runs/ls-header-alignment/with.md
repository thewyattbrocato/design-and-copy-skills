**The problem:** the header and the content have different containers and different alignment. The logo sits at the viewport edge, the nav is centered, and the content is a left-aligned column in the middle. On a wide monitor the three share no vertical edge, so the header looks detached from the page.

**The fix:** put the header's contents in the same 1100px container as the page content. The header background can stay full width. The logo then lines up with the content's left edge, and the nav shares that edge too.

```css
:root { --page-max: 1100px; --page-pad: 1.5rem; }

.site-header { background: #fff; border-bottom: 1px solid #e5e5e5; }

.site-header__inner,
.page {
  max-width: var(--page-max);
  margin-inline: auto;
  padding-inline: var(--page-pad);
}

.site-header__inner {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.site-header nav { margin-left: auto; } /* links on the right, or drop this to sit them next to the logo */
```

**Nav placement:** don't center the links over left-aligned content. Either put them at the right edge of the container (as above) or left-align them right after the logo. Both keep the header on the content's edges.

**Markup:** use `<header class="site-header"><div class="site-header__inner">…</div></header>`. The inner wrapper carries the max-width, and the outer element carries the full-bleed background.

If you'd like the header to stay wider than the content on purpose, offset it by a deliberate amount. Don't let it end up wider by accident.
