I found a few real problems and fixed them below.

```css
:root {
  --font-body: Georgia, Cambria, 'Times New Roman', Times, serif;
  --font-ui: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  --font-mono: ui-monospace, 'SF Mono', Menlo, Consolas, 'Courier New', monospace;
}
body { font-family: var(--font-body); font-size: 1.125rem; line-height: 1.6; }
nav, button, label, input, select, textarea, .meta { font-family: var(--font-ui); }
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-ui);
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -0.01em;
}
code, pre { font-family: var(--font-mono); }
code { font-size: 0.9em; }
pre code { font-size: inherit; }
pre { font-size: 0.9em; }
```

**What I changed**
- **Nested code shrank twice.** `code, pre { font-size: 0.9em }` applies to both elements, so `<pre><code>` rendered at about 0.81em. Code blocks would have looked too small. Now the size is set once.
- **`font-weight: 650` is unreliable.** It only works with variable fonts. System UI fonts don't have a 650 weight, so browsers and OSes would round it differently (600 on some, 700 on others). I used 600 so it's consistent.
- **Headings had no line-height.** They inherited the body's 1.6, which looks loose on multi-line headings. I set 1.2.
- **`h4`–`h6` were missing.** They would have fallen back to the serif body font. If you never use them, that's harmless, but it breaks as soon as someone does.
- **`select` and `textarea` were missing.** Form controls don't inherit fonts by default, so these would have used the browser's default font.
- **Font stacks were missing some fallbacks.** I added `Times` to the serif stack and `SF Mono` to the mono stack.

**Not changed, but worth checking before it goes out**
- **Line length.** For long-form essays, the setup doesn't cap the measure. Something like `max-width: 65ch` on the article container keeps lines readable. I left it alone because I can't see your layout CSS.
- **Sans headings over serif body.** This is a legitimate choice, but it reads more "app" than "essay". If you want a more literary feel for Slow Harbour Notes, using `--font-body` for headings would do it. That's a design call, so I left it.
