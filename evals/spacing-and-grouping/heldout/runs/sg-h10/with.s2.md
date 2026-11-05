I couldn't save the file because the Write tool is disabled in this session. Here is the full page to save as `index.html`. The two other panels are placeholders I made up so you can see the three-panel grid. Swap in your real ones.

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
    --border: #e1e4e8;
    --text: #1f2328;
    --muted: #6b7280;
  }
  body {
    margin: 0;
    padding: var(--space-6);
    font: 15px/1.5 system-ui, sans-serif;
    color: var(--text);
    background: #f6f7f9;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: var(--space-4);
  }
  .panel {
    min-height: 120px;
    padding: var(--space-4);
    background: #fff;
    border: 1px solid var(--border);
    border-radius: 8px;
  }
  .panel h4 {
    margin: 0 0 var(--space-2);
    font-size: 15px;
    font-weight: 600;
  }
  .panel p {
    margin: 0;
    color: var(--muted);
  }
</style>
</head>
<body>
  <div class="grid">
    <div class="panel"><h4>Overview</h4><p>Placeholder panel.</p></div>
    <div class="panel"><h4>Tasks</h4><p>Placeholder panel.</p></div>
    <div class="panel"><h4>Recent activity</h4><p>No activity yet.</p></div>
  </div>
</body>
</html>
```

The styling is deliberately light:
- **Shared surface:** The `.panel` rule is shared by all three cells, so the empty one matches the others: white background, 1px border, 8px radius, no shadow.
- **Padding:** Every panel gets 16px padding, and the gap between panels is also 16px, so they don't blur together.
- **Height:** `min-height: 120px` keeps the empty panel from shrinking to a thin strip next to fuller ones.
- **Heading and text:** The heading sits 8px above the text, closer to its content than to the panel edge. The "No activity yet." text is muted grey and left-aligned like the other panels' content.
- **Layout:** The grid uses `auto-fit` with a 220px minimum column width, so it wraps on narrow screens.

If your real grid uses a different class name or already has its own panel styles, paste the `.panel` and `.panel h4/p` rules into it.
