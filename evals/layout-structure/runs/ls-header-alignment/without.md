The mismatch comes from the header and the content using different width rules. The header spans the full viewport, while the content is capped at 1100px. On a wide screen the logo drifts far left of the content's left edge.

**Fix:** Keep the header's background full-bleed, but put its contents in the same centered 1100px container as the page body. Then the logo lines up with the content's left edge, and the nav is centered within that column.

```css
:root { --content-width: 1100px; }

.header {
  width: 100%;              /* background stays full-width */
}

.header-inner,
.page-content {
  max-width: var(--content-width);
  margin-inline: auto;
  padding-inline: 24px;     /* keeps edges off the screen on small windows */
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
```

```html
<header class="header">
  <div class="header-inner">
    <a class="logo">…</a>
    <nav>…</nav>
  </div>
</header>
<main class="page-content">…</main>
```

**Tips:**
- Use one shared variable or class for the width so the two can't drift apart.
- For the nav to be truly centered with a logo on one side only, use a three-column grid (`grid-template-columns: 1fr auto 1fr`) or add a right-hand spacer. `space-between` centers the nav only if the left and right items are the same width.
