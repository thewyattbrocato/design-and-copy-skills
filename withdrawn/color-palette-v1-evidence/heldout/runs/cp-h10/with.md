```html
<style>
body { margin: 0; background: #f7f5ef; color: #1d2421; font-family: system-ui, sans-serif; line-height: 1.5; }
.top { background: #1f4d45; color: #ffffff; padding: 16px 24px; font-size: 20px; font-weight: 600; letter-spacing: 0.01em; }
.main { max-width: 640px; margin: 0 auto; padding: 32px 24px; }
.welcome { color: #1d2421; font-size: 28px; font-weight: 600; margin: 0 0 24px; }
.card { background: #ffffff; color: #1d2421; border: 1px solid #d9d6cb; border-radius: 8px; padding: 20px; margin: 0 0 16px; }
.card h3 { margin: 8px 0 4px; font-size: 18px; }
.card p { margin: 0 0 16px; color: #55605b; }
.tag { display: inline-block; font-size: 13px; font-weight: 600; padding: 2px 10px; border-radius: 999px; }
.tag.ready { background: #e3efe9; color: #1f4d45; }
.tag.todo { background: #fdf0d8; color: #8a4b00; }
.card button { background: #1f4d45; color: #ffffff; border: 0; border-radius: 6px; padding: 10px 20px; font: inherit; font-weight: 600; cursor: pointer; }
.card button:hover { background: #17403a; }
.card button:focus-visible { outline: 2px solid #1f4d45; outline-offset: 2px; }
.note { color: #55605b; font-size: 14px; margin-top: 24px; }
</style>
<div class="top">Oakline Bookkeeping</div>
<div class="main">
  <h1 class="welcome">Welcome back, Dana</h1>
  <div class="card">
    <span class="tag ready">✓ Ready</span>
    <h3>Your Q3 statements</h3>
    <p>Ready to review and sign.</p>
    <button>Review</button>
  </div>
  <div class="card">
    <span class="tag todo">! Action needed</span>
    <h3>Missing documents</h3>
    <p>We still need two receipts.</p>
    <button>Upload</button>
  </div>
  <p class="note">Questions? Reply to your accountant any time.</p>
</div>
```

**What changed**
- **Palette:** The original used eight loud colors, several at about the same lightness, so text shimmered. The new one is a tinted off-white page (`#f7f5ef`), white cards, and one lead color, a deep ledger green (`#1f4d45`). I chose green for a bookkeeping firm because it suits money and trust, and it is a deliberate category cliché. Your brand colors weren't given, so swap in the real lead if Oakline has one.
- **Layout:** The purple "welcome" band is now a plain heading. The content sits in a centered column with a max width, and the cards have a hairline border and rounded corners.
- **Buttons:** Both buttons are now one consistent style in the lead color, with hover and keyboard-focus states.
- **Status:** Each card has a labeled tag, "✓ Ready" or "! Action needed", so status isn't carried by color alone.

**Contrast, measured on the surface each pair sits on**

| Pair | Ratio |
|---|---|
| White on green (header, buttons) | about 9.5:1 |
| Body text `#1d2421` on white | about 15:1 |
| Muted `#55605b` on white | about 6.5:1 |
| Muted `#55605b` on page `#f7f5ef` | about 6:1 |
| "Ready" tag, green on `#e3efe9` | about 8:1 |
| "Action needed" tag, `#8a4b00` on `#fdf0d8` | about 6:1 |

All of these clear the usual 4.5:1 floor for body text. The ratios are hand-computed estimates, so rerun them in a checker before sign-off.

**Assumptions**
- I kept your copy as is and added only the two status labels.
- I only checked the light theme.
- I haven't rendered this in a browser.
