I couldn't save the flyer as a file because the Write tool is disabled in this session. Here is the full page. Save it as `index.html`, or tell me another way to write it and I'll do that.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Harbor Night Market</title>
<style>
  * { box-sizing: border-box; margin: 0; }
  body {
    min-height: 100vh;
    display: grid;
    place-items: center;
    padding: 2rem 1rem;
    background: #0f2236;
    color: #f4ead5;
    font-family: Georgia, "Times New Roman", serif;
    -webkit-font-smoothing: antialiased;
  }
  .flyer {
    width: 100%;
    max-width: 38rem;
    padding: clamp(2rem, 6vw, 3.5rem) clamp(1.5rem, 6vw, 3.5rem);
    text-align: center;
    border: 1px solid #e8b04a;
    outline: 1px solid #e8b04a;
    outline-offset: 6px;
  }
  h1 {
    font-family: "Avenir Next", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: clamp(2.25rem, 9vw, 3.75rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    text-wrap: balance;
    color: #e8b04a;
  }
  .subtitle {
    margin-top: 1.25rem;
    font-size: clamp(1.05rem, 3.5vw, 1.35rem);
    font-style: italic;
    letter-spacing: 0.02em;
  }
  hr {
    width: 4rem;
    margin: 2rem auto;
    border: 0;
    border-top: 2px solid #e8b04a;
  }
  p {
    font-size: 1.125rem;
    line-height: 1.7;
    max-width: 32em;
    margin-inline: auto;
    text-wrap: pretty;
    hyphens: auto;
  }
  footer {
    margin-top: 2.25rem;
    font-family: "Avenir Next", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #e8b04a;
  }
</style>
</head>
<body>
  <main class="flyer">
    <h1>The Harbor Night Market</h1>
    <p class="subtitle">Fridays, May&ndash;September &mdash; 5pm to 11pm</p>
    <hr>
    <p>Follow the lantern-lit boardwalk to the water&rsquo;s edge, where more than forty food stalls serve everything from smoky grilled oysters to &ldquo;midnight&rdquo; doughnuts. Live bands play on the pier while local makers sell ceramics, candles and prints. Bring friends, bring an appetite, and stay until the very last song fades.</p>
    <footer>Free entry &middot; Pier 9 &middot; Dogs welcome</footer>
  </main>
</body>
</html>
```

**Typography fixes**
- **Date range:** "May-September" now uses an en dash (`&ndash;`), which is the correct mark for a range.
- **Subtitle break:** the double hyphen `--` is now a spaced em dash (`&mdash;`).
- **Footer separators:** I replaced the hyphens with middots (`&middot;`), which is the usual way to separate short items in a flyer footer. If you'd prefer spaced en dashes, swap them in.
- **Quotes and apostrophes:** the paragraph uses curly ones (`&rsquo;`, `&ldquo;`, `&rdquo;`).
- **Fonts:** the page uses only system fonts. Headings and the footer are in a sans-serif stack, and the body is in Georgia.
- **Line breaks:** `text-wrap: balance` on the title and `text-wrap: pretty` on the paragraph keep lines from breaking awkwardly.

The paragraph is exactly 50 words.
