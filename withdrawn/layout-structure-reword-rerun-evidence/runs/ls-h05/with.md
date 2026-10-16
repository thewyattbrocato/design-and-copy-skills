I couldn't save the file because the Write tool is disabled in this session, so the full single-file template is below. Paste it into something like `docs-template.html`. I haven't opened it in a browser.

**What changed**
- **Measure:** the line length is capped at `70ch`, about 650–700px at 16px. The 1100px content area with no cap was giving you 130+ characters per line.
- **Column widths:** the left nav is `15rem` and the right outline is `13rem`. Both are sized to their contents, and the text column takes the rest.
- **Code blocks and tables:** they share the prose edge and scroll horizontally inside it. They are never wider than the text.
- **Right-hand outline:** the outline stays in its own column at laptop widths and only leaves it below `68rem`. There it becomes an "On this page" disclosure at the top of the article, not a list stranded under the content. Below `48rem` the left nav also becomes a disclosure.
- **Shared edges:** the header and the page body use the same `.container`, so the logo lines up with the nav column.
- **Other:** it uses system fonts and has a dark mode.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Docs article template</title>
<style>
  :root {
    --font: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    --mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;

    --bg: #fff;
    --fg: #1d2025;
    --muted: #5b626d;
    --line: #e3e6ea;
    --accent: #0b5fd6;
    --code-bg: #f5f6f8;

    /* Nav and outline size to what they hold; the text sets the measure. */
    --nav-w: 15rem;
    --toc-w: 13rem;
    --gap: clamp(1.5rem, 3vw, 3rem);
    --measure: 70ch;          /* prose, code and tables share this edge */
    --shell-max: 84rem;
    --header-h: 3.5rem;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #14161a; --fg: #e6e8eb; --muted: #9aa2ad;
      --line: #2a2e35; --accent: #6ea8ff; --code-bg: #1d2026;
    }
  }

  * { box-sizing: border-box; }
  html { scroll-padding-top: calc(var(--header-h) + 1rem); }
  body { margin: 0; font: 1rem/1.65 var(--font); color: var(--fg); background: var(--bg); }
  a { color: var(--accent); }

  /* Header and body share one container, so their edges line up. */
  .container { max-width: var(--shell-max); margin-inline: auto; padding-inline: var(--gap); }

  .site-header {
    position: sticky; top: 0; z-index: 10;
    height: var(--header-h);
    background: var(--bg);
    border-bottom: 1px solid var(--line);
  }
  .site-header .container { height: 100%; display: flex; align-items: center; justify-content: space-between; }
  .brand { font-weight: 650; color: inherit; text-decoration: none; }
  .header-links a { color: var(--muted); text-decoration: none; margin-left: 1.25rem; font-size: .9375rem; }
  .header-links a:hover { color: var(--fg); }

  /* Shell: nav | article | outline */
  .shell {
    display: grid;
    grid-template-columns: var(--nav-w) minmax(0, 1fr) var(--toc-w);
    column-gap: var(--gap);
    align-items: start;
  }

  .sidebar, .toc {
    position: sticky; top: var(--header-h);
    max-height: calc(100vh - var(--header-h));
    overflow-y: auto;
    padding-block: 2rem;
    font-size: .9375rem;
    line-height: 1.4;
  }
  .sidebar h2, .toc h2 {
    margin: 0 0 .5rem;
    font-size: .75rem; letter-spacing: .06em; text-transform: uppercase;
    color: var(--muted); font-weight: 650;
  }
  .sidebar ul, .toc ul { list-style: none; margin: 0 0 1.5rem; padding: 0; }
  .sidebar a, .toc a {
    display: block; padding: .3rem .5rem; margin-left: -.5rem;
    color: var(--muted); text-decoration: none; border-radius: 4px;
  }
  .sidebar a:hover, .toc a:hover { color: var(--fg); }
  .sidebar a[aria-current="page"] { color: var(--accent); font-weight: 600; background: var(--code-bg); }
  .toc ul { border-left: 1px solid var(--line); }
  .toc a { margin-left: 0; padding-left: 1rem; border-radius: 0; }

  /* Article: fills its grid cell; every block is capped at the measure. */
  main { padding-block: 2.5rem 5rem; min-width: 0; }
  .article > * { max-width: var(--measure); }

  .eyebrow { margin: 0 0 .5rem; color: var(--muted); font-size: .875rem; }
  h1 { font-size: clamp(1.875rem, 1.4rem + 1.6vw, 2.5rem); line-height: 1.15; margin: 0 0 1rem; letter-spacing: -.01em; }
  .lede { font-size: 1.1875rem; color: var(--muted); margin: 0 0 2rem; }
  h2 { font-size: 1.5rem; line-height: 1.25; margin: 3rem 0 .75rem; padding-top: 1.5rem; border-top: 1px solid var(--line); }
  h3 { font-size: 1.1875rem; line-height: 1.3; margin: 2rem 0 .5rem; }
  p, ul, ol { margin: 0 0 1rem; }
  li + li { margin-top: .25rem; }

  code { font: .875em var(--mono); background: var(--code-bg); padding: .1em .35em; border-radius: 4px; }
  pre {
    margin: 1.25rem 0;
    padding: 1rem 1.125rem;
    background: var(--code-bg);
    border: 1px solid var(--line);
    border-radius: 8px;
    overflow-x: auto;           /* long lines scroll inside the block */
    font: .875rem/1.55 var(--mono);
    tab-size: 2;
  }
  pre code { background: none; padding: 0; font: inherit; }

  .note {
    margin: 1.5rem 0; padding: .75rem 1rem;
    border-left: 3px solid var(--accent); background: var(--code-bg);
    border-radius: 0 6px 6px 0;
  }
  .note p:last-child { margin: 0; }

  .table-wrap { overflow-x: auto; margin: 1.25rem 0; }
  table { border-collapse: collapse; width: 100%; font-size: .9375rem; }
  th, td { text-align: left; padding: .5rem .75rem; border-bottom: 1px solid var(--line); vertical-align: top; }
  th { font-weight: 650; white-space: nowrap; }

  .pager { display: flex; justify-content: space-between; gap: 1rem; margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--line); }
  .pager a { text-decoration: none; }
  .pager small { display: block; color: var(--muted); }

  /* Collapsed versions of the side navs, shown only when their column is gone. */
  .toc-inline, .nav-inline {
    display: none;
    border: 1px solid var(--line); border-radius: 8px; padding: .5rem 1rem; margin-bottom: 1.5rem;
    max-width: var(--measure); font-size: .9375rem;
  }
  .toc-inline summary, .nav-inline summary { cursor: pointer; font-weight: 600; padding: .25rem 0; }
  .toc-inline ul, .nav-inline ul { list-style: none; padding: 0; margin: .5rem 0; }
  .toc-inline a, .nav-inline a { display: block; padding: .25rem 0; text-decoration: none; }

  /* Small laptops and below: outline becomes a disclosure at the top of the article. */
  @media (max-width: 68rem) {
    .shell { grid-template-columns: var(--nav-w) minmax(0, 1fr); }
    .toc { display: none; }
    .toc-inline { display: block; }
  }

  /* Phones and small tablets: left nav becomes a disclosure too. */
  @media (max-width: 48rem) {
    .shell { grid-template-columns: minmax(0, 1fr); }
    .sidebar { display: none; }
    .nav-inline { display: block; }
    .header-links { display: none; }
    main { padding-block: 1.5rem 3rem; }
  }
</style>
</head>
<body>

<header class="site-header">
  <div class="container">
    <a class="brand" href="#">Acme Docs</a>
    <nav class="header-links" aria-label="Site">
      <a href="#">Guides</a><a href="#">API</a><a href="#">Changelog</a>
    </nav>
  </div>
</header>

<div class="container shell">

  <nav class="sidebar" aria-label="Documentation">
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
      <li><a href="#">Webhooks</a></li>
    </ul>
    <h2>Reference</h2>
    <ul>
      <li><a href="#">REST API</a></li>
      <li><a href="#">CLI</a></li>
      <li><a href="#">Rate limits</a></li>
    </ul>
  </nav>

  <main>
    <details class="nav-inline">
      <summary>Documentation menu</summary>
      <ul>
        <li><a href="#">Introduction</a></li>
        <li><a href="#">Installation</a></li>
        <li><a href="#" aria-current="page">Authentication</a></li>
        <li><a href="#">Making requests</a></li>
        <li><a href="#">Pagination</a></li>
      </ul>
    </details>

    <details class="toc-inline">
      <summary>On this page</summary>
      <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#create-key">Create an API key</a></li>
        <li><a href="#send-key">Send the key</a></li>
        <li><a href="#scopes">Scopes</a></li>
        <li><a href="#rotate">Rotate keys</a></li>
      </ul>
    </details>

    <article class="article">
      <p class="eyebrow">Getting started</p>
      <h1>Authentication</h1>
      <p class="lede">Every request to the Acme API carries an API key. This page shows how to create one, send it, and limit what it can do.</p>

      <h2 id="overview">Overview</h2>
      <p>Keys identify your application and carry a set of scopes. Use a separate key for each environment so you can revoke one without affecting the others. Keys are shown once, at creation; store them in a secrets manager rather than in source control.</p>

      <h2 id="create-key">Create an API key</h2>
      <ol>
        <li>Open <strong>Settings → API keys</strong> in the dashboard.</li>
        <li>Choose <strong>Create key</strong> and name it after the environment, for example <code>staging</code>.</li>
        <li>Select the scopes it needs, then copy the key.</li>
      </ol>

      <h2 id="send-key">Send the key</h2>
      <p>Pass the key as a bearer token in the <code>Authorization</code> header.</p>
<pre><code>curl https://api.acme.example/v1/projects \
  -H "Authorization: Bearer $ACME_API_KEY" \
  -H "Accept: application/json"   # long lines scroll inside the block instead of widening the page</code></pre>

      <div class="note"><p><strong>Note:</strong> Requests without a valid key return <code>401 Unauthorized</code>. Requests with a key that lacks the needed scope return <code>403 Forbidden</code>.</p></div>

      <h3>Using the client library</h3>
<pre><code>import { Acme } from "@acme/client";

const acme = new Acme({ apiKey: process.env.ACME_API_KEY });
const projects = await acme.projects.list({ limit: 20 });</code></pre>

      <h2 id="scopes">Scopes</h2>
      <p>Grant the narrowest scopes that work. A key can hold any combination.</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Scope</th><th>Allows</th></tr></thead>
          <tbody>
            <tr><td><code>projects:read</code></td><td>List and fetch projects.</td></tr>
            <tr><td><code>projects:write</code></td><td>Create, update, and delete projects.</td></tr>
            <tr><td><code>webhooks:manage</code></td><td>Create and remove webhook endpoints.</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="rotate">Rotate keys</h2>
      <p>Create the new key, deploy it, confirm traffic has moved, then revoke the old key. Both keys stay valid until you revoke one, so rotation causes no downtime.</p>

      <nav class="pager" aria-label="Pagination">
        <a href="#"><small>Previous</small>Installation</a>
        <a href="#" style="text-align:right"><small>Next</small>Making requests</a>
      </nav>
    </article>
  </main>

  <aside class="toc" aria-label="On this page">
    <h2>On this page</h2>
    <ul>
      <li><a href="#overview">Overview</a></li>
      <li><a href="#create-key">Create an API key</a></li>
      <li><a href="#send-key">Send the key</a></li>
      <li><a href="#scopes">Scopes</a></li>
      <li><a href="#rotate">Rotate keys</a></li>
    </ul>
  </aside>

</div>
</body>
</html>
```

**Width at 1280px:** the container is 84rem max with 3rem gutters. That leaves about 240px for the nav, 208px for the outline and 48px each for the two gaps, so the text column is roughly 740px. The 70ch cap still applies, so lines stay at 70 characters or fewer.

**Things you might adjust**
- If you want the outline to survive on narrower laptops, lower the `68rem` breakpoint. Don't go much below `64rem`, where the text column gets tight.
- To make the text a little roomier, raise `--measure` to `75ch`. I wouldn't go past that for prose.
- If you want 220px for the nav, set `--nav-w: 13.75rem`.
