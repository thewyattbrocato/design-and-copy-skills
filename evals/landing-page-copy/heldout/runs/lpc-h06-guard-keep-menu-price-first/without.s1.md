The Write tool is disabled in this session, so I couldn't save a file. Here's the page as HTML to paste in. It has the full menu at the top and the price directly under it, before any other content. It uses only your facts.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Puppy Foundations | Corner Post Dog School, Ellis Falls</title>
<style>
  * { box-sizing: border-box; }
  body { margin: 0; font-family: system-ui, -apple-system, "Segoe UI", sans-serif; color: #222; line-height: 1.5; }
  nav { background: #2f3e2f; padding: 0 16px; }
  nav ul { list-style: none; margin: 0 auto; padding: 0; max-width: 760px; display: flex; flex-wrap: wrap; gap: 4px 20px; }
  nav a { display: block; padding: 12px 0; color: #fff; text-decoration: none; font-weight: 600; }
  nav a:hover { text-decoration: underline; }
  .price { background: #f5e6c8; text-align: center; padding: 20px 16px; border-bottom: 1px solid #e0cfa8; }
  .price strong { font-size: 2.2rem; display: block; line-height: 1.1; }
  .price span { font-size: 1.05rem; }
  main { max-width: 760px; margin: 0 auto; padding: 24px 16px 48px; }
  h1 { font-size: 2rem; line-height: 1.2; margin: 0 0 4px; }
  .sub { margin: 0 0 24px; color: #555; }
  h2 { font-size: 1.3rem; margin: 32px 0 8px; }
  ul.list { padding-left: 20px; }
  ul.list li { margin: 4px 0; }
  .cta { background: #2f3e2f; color: #fff; padding: 24px 16px; text-align: center; border-radius: 8px; margin-top: 32px; }
  .cta a.button { display: inline-block; background: #f5c542; color: #222; font-weight: 700; padding: 14px 28px; border-radius: 6px; text-decoration: none; font-size: 1.1rem; margin: 8px 0; }
  .cta a.phone { color: #fff; font-weight: 700; }
</style>
</head>
<body>

<nav aria-label="Main">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/classes">Classes</a></li>
    <li><a href="/blog">Blog</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>

<div class="price">
  <strong>$240</strong>
  <span>for the full 6 weeks</span>
</div>

<main>
  <h1>Puppy Foundations</h1>
  <p class="sub">Corner Post Dog School, Ellis Falls</p>

  <p>A 6-week puppy class that teaches the basics, in a small group of no more than 8 puppies.</p>

  <h2>Class details</h2>
  <ul class="list">
    <li><strong>When:</strong> Tuesdays at 6:30 p.m., for 6 weeks</li>
    <li><strong>Price:</strong> $240 for the full 6 weeks</li>
    <li><strong>Class size:</strong> Max 8 puppies per class</li>
    <li><strong>Where:</strong> Corner Post Dog School, Ellis Falls</li>
  </ul>

  <h2>What your puppy will learn</h2>
  <ul class="list">
    <li>Sit</li>
    <li>Down</li>
    <li>Come</li>
    <li>Walking on a loose leash</li>
    <li>Settling calmly</li>
  </ul>

  <h2>Who can join</h2>
  <ul class="list">
    <li>Puppies must be 8 to 16 weeks old on the first night.</li>
    <li>Proof of first vaccinations is required before the first class.</li>
  </ul>

  <div class="cta">
    <div>Classes are limited to 8 puppies.</div>
    <a class="button" href="https://corner-post.example/puppy">Sign up at corner-post.example/puppy</a>
    <div>or call <a class="phone" href="tel:5550188">555-0188</a></div>
  </div>
</main>

</body>
</html>
```

- **Order at the top:** I put the menu first and the price band directly below it. If your partner wants the price above the menu, move the `<div class="price">` block above the `<nav>`.
- **Menu links:** The links (`/classes`, `/blog` and so on) are placeholders. Swap in your real URLs.
- **Sign-up link:** The sign-up button goes to `https://corner-post.example/puppy`. I added the `https://` to your `corner-post.example/puppy`, so change it if the real address differs.

If you re-enable file writing, I can save this as `puppy-class.html` in the working directory.
