I couldn't save the file because the Write tool is disabled in this session. The full HTML is below, so you can save it as `empty-state.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Reading list – empty state</title>
<style>
  :root {
    --bg: #ffffff;
    --text: #1b1f27;
    --muted: #596273;
    --accent: #1f5fd1;
    --accent-hover: #194fb0;
    --accent-tint: #e8f0fd;
    --on-accent: #ffffff;
    --border: #c5ccd8;
    --surface-hover: #f2f4f8;
    --illo-main: #1f5fd1;
    --illo-soft: #9dbcf0;
    --illo-line: #6f8fc9;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #14171d;
      --text: #eceff4;
      --muted: #a2abbb;
      --accent: #6ea0f5;
      --accent-hover: #8bb4f8;
      --accent-tint: #1d2a44;
      --on-accent: #0c1424;
      --border: #3a4252;
      --surface-hover: #1e232c;
      --illo-main: #6ea0f5;
      --illo-soft: #3b5a96;
      --illo-line: #8fb2f2;
    }
  }

  * { box-sizing: border-box; }

  body {
    margin: 0;
    min-height: 100vh;
    display: grid;
    place-items: center;
    padding: 24px;
    background: var(--bg);
    color: var(--text);
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }

  .empty {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 420px;
    text-align: center;
  }

  .empty__art {
    display: grid;
    place-items: center;
    width: 88px;
    height: 88px;
    margin-bottom: 24px;
    border-radius: 50%;
    background: var(--accent-tint);
  }
  .empty__art svg { width: 48px; height: 48px; }

  .empty__title {
    margin: 0 0 8px;
    font-size: 1.375rem;
    font-weight: 650;
    line-height: 1.25;
    letter-spacing: -0.01em;
  }

  .empty__body {
    margin: 0 0 28px;
    font-size: 1rem;
    color: var(--muted);
    text-wrap: balance;
  }

  .empty__actions {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px;
    width: 100%;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 44px;
    padding: 0 20px;
    border: 1px solid transparent;
    border-radius: 10px;
    font: inherit;
    font-size: 0.9375rem;
    font-weight: 600;
    text-decoration: none;
    cursor: pointer;
    transition: background-color .15s, border-color .15s;
  }
  .btn--primary { background: var(--accent); color: var(--on-accent); }
  .btn--primary:hover { background: var(--accent-hover); }
  .btn--secondary { background: transparent; color: var(--text); border-color: var(--border); }
  .btn--secondary:hover { background: var(--surface-hover); }

  .btn:focus-visible,
  .empty__link:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
  }

  .empty__link {
    margin-top: 20px;
    padding: 4px 2px;
    font-size: 0.875rem;
    color: var(--muted);
    text-decoration: underline;
    text-underline-offset: 3px;
  }
  .empty__link:hover { color: var(--text); }

  @media (max-width: 380px) {
    .btn { width: 100%; }
  }
  @media (prefers-reduced-motion: reduce) {
    .btn { transition: none; }
  }
</style>
</head>
<body>
  <section class="empty" aria-labelledby="empty-title">
    <div class="empty__art" aria-hidden="true">
      <svg viewBox="0 0 48 48" fill="none">
        <rect x="6" y="10" width="9" height="30" rx="2" fill="var(--illo-soft)"/>
        <rect x="18" y="6" width="9" height="34" rx="2" fill="var(--illo-main)"/>
        <rect x="21" y="12" width="3" height="3" rx="1" fill="var(--accent-tint)"/>
        <rect x="30.5" y="12" width="9" height="28" rx="2" transform="rotate(14 35 26)" fill="var(--illo-soft)"/>
        <path d="M4 42h40" stroke="var(--illo-line)" stroke-width="2.5" stroke-linecap="round"/>
      </svg>
    </div>

    <h2 class="empty__title" id="empty-title">Your reading list is empty</h2>
    <p class="empty__body">Save articles you want to read later. They’ll show up here for you and your friends.</p>

    <div class="empty__actions">
      <a class="btn btn--primary" href="#add">Add an article</a>
      <a class="btn btn--secondary" href="#import">Import from browser</a>
    </div>

    <a class="empty__link" href="#learn-more">Learn more</a>
  </section>
</body>
</html>
```

**What changed and why**
- **One primary action.** "Add an article" is the filled blue button. "Import from browser" is now an outlined secondary button, and "Learn more" is a small muted link. Before, both buttons were the same medium blue, so nothing told the user where to start.
- **Clearer type hierarchy.** The heading is now a real `<h2>` at 22px semibold, and the body text is 16px in muted gray. Before, the heading and paragraph were both 14px. The heading says "Your reading list is empty" instead of "Nothing here yet!". The body text is tighter and wraps in balanced lines, with a narrower max width.
- **Lighter illustration.** The 96px gray books are now a 48px accent-colored SVG inside an 88px tinted circle. It ties in with the blue buttons and is less visually heavy.
- **Accessibility.** The illustration is hidden from screen readers, and the section is labelled by its heading. Buttons are at least 44px tall, and keyboard focus rings are visible. I also added a `prefers-reduced-motion` rule.
- **Dark mode and mobile.** Colors switch with `prefers-color-scheme`. The buttons stack full-width on very narrow screens.
- **Buttons are links for now.** They're `<a>` tags with placeholder `href`s. Swap in your real routes, or use `<button>` where they trigger actions.
