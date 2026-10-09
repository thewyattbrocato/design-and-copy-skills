```html
<style>
:root {
  --navy: #1f3a5f;
  --navy-dark: #162b47;
  --ink: #1f2933;
  --muted: #5b6770;
  --line: #dde3e9;
  --bg: #f5f7fa;
  --surface: #ffffff;
  --accent: #2f6f5e;
  --accent-dark: #245748;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}
.top {
  background: var(--navy-dark);
  color: #ffffff;
  padding: 16px 32px;
  font-size: 20px;
  font-weight: 600;
  letter-spacing: 0.02em;
}
.welcome {
  background: var(--navy);
  color: #ffffff;
  padding: 32px;
  font-size: 24px;
  font-weight: 500;
}
main {
  max-width: 800px;
  margin: 0 auto;
  padding: 24px 16px;
}
.card {
  background: var(--surface);
  color: var(--ink);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 20px 24px;
  margin: 0 0 16px;
}
.card h3 { margin: 0 0 4px; font-size: 18px; color: var(--navy); }
.card p { margin: 0 0 16px; color: var(--muted); }
.card button {
  background: var(--accent);
  color: #ffffff;
  border: 0;
  border-radius: 6px;
  padding: 8px 20px;
  font: inherit;
  font-weight: 600;
  cursor: pointer;
}
.card button:hover { background: var(--accent-dark); }
.card button:focus-visible { outline: 3px solid #9cc9bb; outline-offset: 2px; }
.note { color: var(--muted); font-size: 14px; margin: 24px 0 0; }
</style>
<div class="top">Oakline Bookkeeping</div>
<div class="welcome">Welcome back, Dana</div>
<main>
  <div class="card"><h3>Your Q3 statements</h3><p>Ready to review and sign.</p><button>Review</button></div>
  <div class="card"><h3>Missing documents</h3><p>We still need two receipts.</p><button>Upload</button></div>
  <p class="note">Questions? Reply to your accountant any time.</p>
</main>
```

What changed:
- **Palette:** The neon colors are now a navy header and welcome band, a white card surface, and one green accent for actions. Text contrast is well above WCAG AA.
- **Layout:** Content sits in a centered 800px column, so cards no longer stretch edge to edge.
- **Cards:** They have a thin border, rounded corners, and consistent spacing. Headings are navy and body text is muted gray.
- **Buttons:** They are solid green with white text, plus hover and keyboard-focus states.
- **Footer note:** It's now small, gray text.
- **Markup:** I wrapped the cards and note in a `<main>` element. The class names and copy are unchanged.
