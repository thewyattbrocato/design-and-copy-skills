I couldn't save this as a file because the Write tool is disabled in this session, so the full skeleton is below. Copy it into `docs-template.html`. I haven't opened it in a browser, so none of the breakpoints have been checked.

**What I changed**
- **Reading measure:** the text column is capped at `68ch`, about 65–70 characters per line, and 16px text is fine at that width. The 1100px width is gone.
- **Columns:** the nav is 14rem, the content is `minmax(0, 68ch)`, and the outline is 13rem. The total is about 1,200px, so it fits a 1280px laptop.
- **Outline column:** below 1100px it is hidden instead of dropping under the content. Dropping it under the content buried it and pushed the article down.
- **Phones:** below 760px the nav stacks above the article.
- **Code blocks:** they stay inside the text width and scroll horizontally. The wide `pre` in the sample shows this, and tables scroll the same way.
- **Shared edges:** the header and the shell use the same max-width and padding, so the brand lines up with the nav edge.
- **Sticky nav and outline:** both are sticky, and `scroll-padding-top` keeps anchored headings clear of the sticky header.
- **Dark mode:** `prefers-color-scheme` swaps the colors.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Docs article template</title>
<style>
  :root {
    --nav-w: 14rem;
    --toc-w: 13rem;
    --measure: 68ch;          /* reading column: ~65-70 characters per line */
    --gap: 2.5rem;
    --header-h: 3.5rem;
    --fg: #1d2330;
    --muted: #5b6475;
    --line: #e1e5ec;
    --bg: #fff;
    --code-bg: #f5f6f9;
    --accent: #1f5fd1;
    --font: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    --mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root { --fg:#e6e9f0; --muted:#9aa4b6; --line:#2a3140; --bg:#12151c; --code-bg:#1a1f2a; --accent:#7aa7ff; }
  }

  *, *::before, *::after { box-sizing: border-box; }
  html { scroll-padding-top: calc(var(--header-h) + 1rem); }
  body { margin: 0; font: 1rem/1.65 var(--font); color: var(--fg); background: var(--bg); }
  a { color: var(--accent); }

  /* Header and shell share one container, so their edges line up. */
  .header, .shell {
    max-width: calc(var(--nav-w) + var(--measure) + var(--toc-w) + var(--gap) * 2 + 3rem);
    margin-inline: auto;
    padding-inline: 1.5rem;
  }
  .header-wrap { border-bottom: 1px solid var(--line); position: sticky; top: 0; background: var(--bg); z-index: 2; }
  .header { height: var(--header-h); display: flex; align-items: center; gap: 1.5rem; }
  .brand { font-weight: 700; color: inherit; text-decoration: none; }

  /* Three tracks: nav and outline fixed, middle track capped at the measure.
     minmax(0, measure) lets the middle track shrink before anything wraps. */
  .shell {
    display: grid;
    grid-template-columns: var(--nav-w) minmax(0, var(--measure)) var(--toc-w);
    grid-template-areas: "nav main toc";
    column-gap: var(--gap);
    justify-content: center;
    align-items: start;
  }
  .nav  { grid-area: nav; }
  .main { grid-area: main; padding-block: 2rem 4rem; }
  .toc  { grid-area: toc; }

  .nav, .toc {
    position: sticky; top: var(--header-h);
    max-height: calc(100vh - var(--header-h));
    overflow-y: auto;
    padding-block: 2rem;
    font-size: .875rem; line-height: 1.4;
  }
  .nav h2, .toc h2 { font-size: .75rem; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); margin: 0 0 .5rem; padding: 0; border: 0; }
  .nav ul, .toc ul { list-style: none; margin: 0 0 1.5rem; padding: 0; }
  .nav a, .toc a { display: block; padding: .3rem .6rem; color: var(--muted); text-decoration: none; border-radius: 4px; }
  .nav a:hover, .toc a:hover { color: var(--fg); background: var(--code-bg); }
  .nav a[aria-current="page"] { color: var(--fg); font-weight: 600; background: var(--code-bg); }
  .toc { border-left: 1px solid var(--line); padding-left: 1rem; }
  .toc a { padding-left: 0; background: none; }
  .toc .sub a { padding-left: .9rem; }

  /* Article typography */
  .crumbs { font-size: .875rem; color: var(--muted); margin: 0 0 .75rem; }
  h1 { font-size: 2rem; line-height: 1.2; margin: 0 0 .75rem; text-wrap: balance; }
  .lede { font-size: 1.125rem; color: var(--muted); margin: 0 0 2rem; }
  .main h2 { font-size: 1.4rem; line-height: 1.3; margin: 2.5rem 0 .75rem; padding-top: 1.5rem; border-top: 1px solid var(--line); }
  h3 { font-size: 1.1rem; margin: 1.75rem 0 .5rem; }
  p, ul, ol { margin: 0 0 1rem; }
  li + li { margin-top: .25rem; }

  /* Code stays inside the text width and scrolls; it never pokes out of the column. */
  code { font: .875em var(--mono); background: var(--code-bg); padding: .1em .35em; border-radius: 4px; }
  pre { margin: 0 0 1.25rem; padding: 1rem; background: var(--code-bg); border: 1px solid var(--line); border-radius: 6px; overflow-x: auto; font: .875rem/1.55 var(--mono); tab-size: 2; }
  pre code { background: none; padding: 0; font: inherit; }

  table { width: 100%; border-collapse: collapse; font-size: .9375rem; margin-bottom: 1.25rem; display: block; overflow-x: auto; }
  th, td { text-align: left; padding: .5rem .75rem; border-bottom: 1px solid var(--line); vertical-align: top; }
  th { font-size: .8125rem; color: var(--muted); }

  .callout { border-left: 3px solid var(--accent); background: var(--code-bg); padding: .75rem 1rem; border-radius: 0 6px 6px 0; margin: 0 0 1.25rem; }
  .callout p:last-child { margin: 0; }

  .pager { display: flex; justify-content: space-between; gap: 1rem; margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--line); }

  /* Laptop: drop the outline column; the page keeps nav + one readable column. */
  @media (max-width: 1100px) {
    .shell { grid-template-columns: var(--nav-w) minmax(0, var(--measure)); grid-template-areas: "nav main"; }
    .toc { display: none; }
  }

  /* Phone: nav stacks above the article, in source-order reading flow. */
  @media (max-width: 760px) {
    .shell { grid-template-columns: minmax(0, 1fr); grid-template-areas: "nav" "main"; padding-inline: 1rem; }
    .header { padding-inline: 1rem; }
    .nav { position: static; max-height: none; padding-block: 1rem 0; border-bottom: 1px solid var(--line); }
    h1 { font-size: 1.65rem; }
  }
</style>
</head>
<body>

<div class="header-wrap">
  <header class="header">
    <a class="brand" href="#">Acme Docs</a>
    <span style="color:var(--muted)">v2.4</span>
  </header>
</div>

<div class="shell">
  <nav class="nav" aria-label="Documentation">
    <h2>Getting started</h2>
    <ul>
      <li><a href="#">Introduction</a></li>
      <li><a href="#" aria-current="page">Installation</a></li>
      <li><a href="#">Quickstart</a></li>
    </ul>
    <h2>Guides</h2>
    <ul>
      <li><a href="#">Configuration</a></li>
      <li><a href="#">Authentication</a></li>
      <li><a href="#">Deploying</a></li>
    </ul>
    <h2>Reference</h2>
    <ul>
      <li><a href="#">CLI</a></li>
      <li><a href="#">REST API</a></li>
    </ul>
  </nav>

  <main class="main">
    <p class="crumbs">Getting started / Installation</p>
    <h1>Installation</h1>
    <p class="lede">Install the CLI, verify it works, and connect it to your first project in about five minutes.</p>

    <h2 id="requirements">Requirements</h2>
    <p>Acme runs on macOS, Linux, and Windows. You need <code>Node.js</code> 20 or newer and a terminal. Check your version before continuing:</p>
    <pre><code>node --version
# v20.11.1</code></pre>

    <h2 id="install">Install the CLI</h2>
    <p>Install the package globally with your package manager of choice.</p>
    <h3 id="npm">With npm</h3>
    <pre><code>npm install --global @acme/cli</code></pre>
    <h3 id="long">With a very long command</h3>
    <p>Long lines scroll inside the block instead of widening the page:</p>
    <pre><code>curl --fail --silent --show-error --location https://example.com/releases/latest/download/acme-cli-linux-x86_64.tar.gz | tar --extract --gzip --directory /usr/local/bin acme</code></pre>

    <div class="callout"><p><strong>Note:</strong> On Windows, run the terminal as a regular user. Administrator rights are not required.</p></div>

    <h2 id="verify">Verify the install</h2>
    <p>Run the version command. You should see the installed version and your platform.</p>
    <pre><code>acme --version</code></pre>

    <h2 id="options">Install options</h2>
    <table>
      <thead><tr><th>Flag</th><th>Default</th><th>Description</th></tr></thead>
      <tbody>
        <tr><td><code>--channel</code></td><td><code>stable</code></td><td>Release channel to install from.</td></tr>
        <tr><td><code>--prefix</code></td><td><code>/usr/local</code></td><td>Directory the binary is placed in.</td></tr>
        <tr><td><code>--no-telemetry</code></td><td>off</td><td>Disable anonymous usage reporting.</td></tr>
      </tbody>
    </table>

    <h2 id="next">Next steps</h2>
    <ul>
      <li>Follow the <a href="#">Quickstart</a> to create a project.</li>
      <li>Read <a href="#">Configuration</a> to customize defaults.</li>
    </ul>

    <div class="pager">
      <a href="#">← Introduction</a>
      <a href="#">Quickstart →</a>
    </div>
  </main>

  <aside class="toc" aria-label="On this page">
    <h2>On this page</h2>
    <ul>
      <li><a href="#requirements">Requirements</a></li>
      <li><a href="#install">Install the CLI</a></li>
      <li class="sub"><a href="#npm">With npm</a></li>
      <li class="sub"><a href="#long">Long commands</a></li>
      <li><a href="#verify">Verify the install</a></li>
      <li><a href="#options">Install options</a></li>
      <li><a href="#next">Next steps</a></li>
    </ul>
  </aside>
</div>

</body>
</html>
```

**Tuning**
- **Wider article:** raise `--measure`, but keep it at or below about `75ch`. The shell width follows automatically.
- **Keeping the outline on smaller laptops:** lower the `1100px` breakpoint. The middle column shrinks first, down to about 60 characters.
- **Section headings:** the `border-top` rule on each `h2` is a style choice. Remove it if you want a quieter page.
