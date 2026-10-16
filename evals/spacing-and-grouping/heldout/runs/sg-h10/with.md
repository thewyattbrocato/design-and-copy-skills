I couldn't save the file because the Write tool is disabled in this session. Here is the full HTML to paste into a file. I haven't opened it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dashboard</title>
<style>
  :root {
    --space-2: 8px;
    --space-4: 16px;
    --space-6: 24px;
  }
  body {
    margin: 0;
    padding: var(--space-6);
    font: 14px/1.5 system-ui, sans-serif;
    color: #1f2933;
    background: #f5f6f8;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: var(--space-6);
  }
  .panel {
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
    min-height: 140px;
    padding: var(--space-6);
    background: #fff;
    border: 1px solid #e1e4e8;
    border-radius: 8px;
  }
  .panel h4 { margin: 0; font-size: 14px; font-weight: 600; }
  .panel p  { margin: 0; }

  /* Empty state: centered in the leftover space, muted */
  .panel p:not(.value) {
    margin: auto;
    padding-bottom: var(--space-4);
    color: #6b7280;
    text-align: center;
  }
  .value { font-size: 28px; font-weight: 600; line-height: 1.2; }
</style>
</head>
<body>
  <div class="grid">
    <!-- Placeholder siblings so the grid has 3 panels; swap in your real ones -->
    <div class="panel"><h4>Open tasks</h4><p class="value">12</p></div>
    <div class="panel"><h4>Completed</h4><p class="value">48</p></div>
    <div class='panel'><h4>Recent activity</h4><p>No activity yet.</p></div>
  </div>
</body>
</html>
```

What the styling does:
- **Matching the other panels:** all three panels share the same surface, with a 24px padding, a 1px border, an 8px radius and a 140px minimum height. The empty panel is the same size as the others, so it no longer looks lost.
- **Empty state:** "No activity yet." is muted grey and centered in the space below the heading. The heading stays top-left like the other panels' headings.
- **Spacing:** the gap between panels (24px) equals the panel padding, so the panels stay separate. The gap between heading and body is 8px, smaller than the gap between panels. Only three spacing values are used.
- **Layout:** the grid uses `auto-fit`, so it collapses to fewer columns on narrow screens.

The "Open tasks" and "Completed" panels are my stand-ins, because you didn't give me the other two. Replace them with your own. If they use different markup, keep the `.panel` class on them so the sizing carries over.
