I couldn't save the file because the Write tool is disabled in this session. Here is the full file inline. Save it as `docs-template.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Authentication – Docs</title>
<style>
  :root {
    --nav-w: 240px;
    --toc-w: 200px;
    --prose-w: 72ch;          /* ~65–75 characters per line */
    --gap: 48px;
    --header-h: 56px;

    --bg: #fff;
    --fg: #1f2328;
    --muted: #59636e;
    --border: #d1d9e0;
    --accent: #0969da;
    --code-bg: #f6f8fa;

    --font: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    --mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #0d1117; --fg: #e6edf3; --muted: #9198a1;
      --border: #30363d; --accent: #4493f8; --code-bg: #161b22;
    }
  }

  *, *::before, *::after { box-sizing: border-box; }
  html { scroll-padding-top: calc(var(--header-h) + 16px); }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--fg);
    font: 16px/1.65 var(--font);
    -webkit-text-size-adjust: 100%;
  }
  a { color: var(--accent); }

  .site-header {
    position: sticky; top: 0; z-index: 10;
    height: var(--header-h);
    display: flex; align-items: center; padding: 0 24px;
    background: var(--bg);
    border-bottom: 1px solid var(--border);
    font-weight: 600;
  }

  /* Three-column shell: fixed nav | flexible content | fixed TOC */
  .layout {
    display: grid;
    grid-template-columns: var(--nav-w) minmax(0, 1fr) var(--toc-w);
    column-gap: var(--gap);
    max-width: 1320px;
    margin: 0 auto;
    padding: 0 24px;
  }

  .nav, .toc {
    position: sticky; top: var(--header-h);
    align-self: start;
    max-height: calc(100vh - var(--header-h));
    overflow-y: auto;
    padding: 24px 0;
    font-size: 14px; line-height: 1.5;
  }
  .nav h2, .toc h2 {
    margin: 0 0 8px;
    font-size: 12px; letter-spacing: .06em; text-transform: uppercase;
    color: var(--muted);
  }
  .nav ul, .toc ul { list-style: none; margin: 0 0 20px; padding: 0; }
  .nav a, .toc a {
    display: block; padding: 4px 10px;
    color: var(--muted); text-decoration: none;
    border-left: 2px solid transparent;
  }
  .nav a:hover, .toc a:hover { color: var(--fg); }
  .nav a[aria-current="page"] {
    color: var(--accent); font-weight: 600; border-left-color: var(--accent);
  }

  /* min-width:0 lets code scroll instead of stretching the grid track */
  main { min-width: 0; padding: 32px 0 80px; }
  article { max-width: var(--prose-w); }

  article h1 { font-size: 2rem; line-height: 1.2; margin: 0 0 .5em; }
  article h2 {
    font-size: 1.5rem; line-height: 1.3;
    margin: 2.25em 0 .6em; padding-top: 1em;
    border-top: 1px solid var(--border);
  }
  article h3 { font-size: 1.15rem; line-height: 1.35; margin: 1.75em 0 .5em; }
  article p, article ul, article ol { margin: 0 0 1em; }
  article li + li { margin-top: .25em; }
  .lede { font-size: 1.125rem; color: var(--muted); }

  /* Code: never wider than the text; scrolls internally */
  code, pre { font-family: var(--mono); font-size: .875em; }
  :not(pre) > code {
    background: var(--code-bg); border: 1px solid var(--border);
    border-radius: 4px; padding: .1em .35em;
    overflow-wrap: anywhere;
  }
  pre {
    max-width: 100%;
    margin: 0 0 1.25em; padding: 14px 16px;
    overflow-x: auto;
    background: var(--code-bg); border: 1px solid var(--border);
    border-radius: 6px;
    line-height: 1.5; tab-size: 2;
  }

  .table-wrap { max-width: 100%; overflow-x: auto; margin: 0 0 1.25em; }
  table { border-collapse: collapse; font-size: .9375em; width: 100%; }
  th, td { text-align: left; padding: 8px 12px; border-bottom: 1px solid var(--border); vertical-align: top; }
  img, video { max-width: 100%; height: auto; }

  /* Inline "On this page" for screens without the right column */
  .toc-inline { display: none; margin: 0 0 24px; border: 1px solid var(--border); border-radius: 6px; font-size: 14px; }
  .toc-inline summary { cursor: pointer; padding: 10px 14px; font-weight: 600; }
  .toc-inline ul { margin: 0; padding: 0 14px 12px 32px; }

  /* Small laptops/tablets: drop the right column, keep nav + readable content */
  @media (max-width: 1100px) {
    .layout { grid-template-columns: var(--nav-w) minmax(0, 1fr); column-gap: 32px; }
    .toc { display: none; }
    .toc-inline { display: block; }
  }

  /* Phones: single column, nav stacks above content */
  @media (max-width: 760px) {
    .layout { grid-template-columns: minmax(0, 1fr); padding: 0 16px; }
    .nav {
      position: static; max-height: none;
      border-bottom: 1px solid var(--border); padding: 16px 0;
    }
    main { padding-top: 24px; }
    article h1 { font-size: 1.65rem; }
  }
</style>
</head>
<body>

<header class="site-header">Acme Docs</header>

<div class="layout">

  <nav class="nav" aria-label="Documentation">
    <h2>Getting started</h2>
    <ul>
      <li><a href="#">Introduction</a></li>
      <li><a href="#">Installation</a></li>
      <li><a href="#" aria-current="page">Authentication</a></li>
    </ul>
    <h2>Guides</h2>
    <ul>
      <li><a href="#">Making requests</a></li>
      <li><a href="#">Pagination</a></li>
      <li><a href="#">Error handling</a></li>
    </ul>
    <h2>Reference</h2>
    <ul>
      <li><a href="#">REST API</a></li>
      <li><a href="#">Webhooks</a></li>
    </ul>
  </nav>

  <main id="content">
    <article>
      <h1>Authentication</h1>
      <p class="lede">Every request to the API must be authenticated. This page covers API keys, token exchange, and how to rotate credentials safely.</p>

      <details class="toc-inline">
        <summary>On this page</summary>
        <ul>
          <li><a href="#api-keys">API keys</a></li>
          <li><a href="#tokens">Exchanging for a token</a></li>
          <li><a href="#rotation">Rotating credentials</a></li>
          <li><a href="#errors">Error responses</a></li>
        </ul>
      </details>

      <h2 id="api-keys">API keys</h2>
      <p>Create a key in the dashboard under <strong>Settings → API</strong>. Keys are shown once; store them in a secret manager and never commit them to source control. Pass the key in the <code>Authorization</code> header on every request.</p>
      <pre><code>curl https://api.example.com/v1/projects \
  -H "Authorization: Bearer $ACME_API_KEY" \
  -H "Accept: application/json" \
  -H "X-Request-Id: 7f3c1c1e-4a55-4a0b-9d3e-0f5c9b0a1234"</code></pre>

      <h3>Key scopes</h3>
      <p>Each key carries one or more scopes that limit what it can do.</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Scope</th><th>Allows</th></tr></thead>
          <tbody>
            <tr><td><code>read</code></td><td>List and fetch resources.</td></tr>
            <tr><td><code>write</code></td><td>Create, update, and delete resources.</td></tr>
            <tr><td><code>admin</code></td><td>Manage members, billing, and other keys.</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="tokens">Exchanging for a token</h2>
      <p>For browser or mobile clients, exchange a key for a short-lived token from your server and hand only the token to the client.</p>
      <pre><code>const res = await fetch("https://api.example.com/v1/tokens", {
  method: "POST",
  headers: { Authorization: `Bearer ${process.env.ACME_API_KEY}`, "Content-Type": "application/json" },
  body: JSON.stringify({ scopes: ["read"], expires_in: 900 }),
});
const { token } = await res.json();</code></pre>
      <ol>
        <li>Request a token with the minimum scopes needed.</li>
        <li>Return it to the client over HTTPS.</li>
        <li>Request a new one before <code>expires_in</code> elapses.</li>
      </ol>

      <h2 id="rotation">Rotating credentials</h2>
      <p>Rotate keys at least every 90 days, or immediately if one may have leaked. Create the new key first, deploy it, then revoke the old one so there is no downtime.</p>

      <h2 id="errors">Error responses</h2>
      <p>Authentication failures return <code>401</code> with a JSON body describing the problem. Missing scopes return <code>403</code>.</p>
      <pre><code>{ "error": { "code": "invalid_api_key", "message": "The provided API key is not valid." } }</code></pre>
    </article>
  </main>

  <aside class="toc" aria-label="On this page">
    <h2>On this page</h2>
    <ul>
      <li><a href="#api-keys">API keys</a></li>
      <li><a href="#tokens">Exchanging for a token</a></li>
      <li><a href="#rotation">Rotating credentials</a></li>
      <li><a href="#errors">Error responses</a></li>
    </ul>
  </aside>

</div>
</body>
</html>
```

I haven't opened this in a browser, so the layout is untested.

**What I changed**

- **Line length:** the article is capped at `72ch`, which is about 70 characters per line. The 16px text size was fine. The missing max-width was the problem. The content grid track is `minmax(0, 1fr)`, so it fills the space between the side columns, and the prose stays readable inside it.
- **Columns:** the layout is a CSS grid with `240px | flexible | 200px` and a 48px gap. It's capped at 1320px and centered. The right-hand column is narrow enough to fit on a 1280px laptop.
- **"On this page" column:** it used to wrap under the content because it didn't fit. Now, below 1100px, the right column is hidden and replaced by a collapsible "On this page" `<details>` at the top of the article. You never get a stray block under the content.
- **Code blocks:** `pre` has `max-width: 100%` and `overflow-x: auto`. `main` has `min-width: 0`, which stops a long line from stretching the grid track. Code can't be wider than the text and scrolls inside its own box. Tables get the same treatment through `.table-wrap`.
- **Smaller fixes:**
  - Both side columns are sticky and scroll on their own.
  - Headings have `scroll-padding` so anchor links don't land under the sticky header.
  - It supports dark mode.
  - Below 760px it collapses to one column with the nav stacked on top.

If you want the right column to stay visible on narrower laptops, lower `--toc-w` or move the 1100px breakpoint down to about 1000px. The three columns need roughly 240 + 48 + 640 + 48 + 200 plus padding, which is about 1,230px.
