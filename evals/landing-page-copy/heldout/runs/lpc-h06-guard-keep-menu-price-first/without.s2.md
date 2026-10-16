I couldn't save the page as a file because the Write tool is disabled in this session. Here is the full HTML to paste into `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Puppy Foundations | Corner Post Dog School, Ellis Falls</title>
<style>
  body { margin: 0; font-family: system-ui, sans-serif; color: #222; line-height: 1.5; }
  nav { background: #fff; border-bottom: 1px solid #ddd; padding: 12px 20px; }
  nav ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 8px 24px; }
  nav a { color: #222; text-decoration: none; font-weight: 600; }
  .price { background: #1f4d3a; color: #fff; text-align: center; padding: 20px; }
  .price strong { font-size: 2.2rem; display: block; }
  main { max-width: 640px; margin: 0 auto; padding: 24px 20px 48px; }
  h1 { margin-top: 0; }
  ul.details li { margin-bottom: 6px; }
  .cta { display: inline-block; background: #c8501e; color: #fff; padding: 14px 28px; border-radius: 6px; font-weight: 700; text-decoration: none; margin: 8px 0; }
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
  for the full 6 weeks
</div>

<main>
  <h1>Puppy Foundations</h1>
  <p>Corner Post Dog School, Ellis Falls</p>

  <a class="cta" href="https://corner-post.example/puppy">Sign up for Puppy Foundations</a>
  <p>Or call <a href="tel:5550188">555-0188</a>.</p>

  <h2>What your puppy learns</h2>
  <ul>
    <li>Sit</li>
    <li>Down</li>
    <li>Come</li>
    <li>Walking on a loose leash</li>
    <li>Settling calmly</li>
  </ul>

  <h2>Class details</h2>
  <ul class="details">
    <li><strong>Length:</strong> 6 weeks</li>
    <li><strong>When:</strong> Tuesdays at 6:30 p.m.</li>
    <li><strong>Class size:</strong> Max 8 puppies per class</li>
    <li><strong>Price:</strong> $240 for the full 6 weeks</li>
  </ul>

  <h2>Who can join</h2>
  <ul>
    <li>Puppies must be 8 to 16 weeks old on the first night.</li>
    <li>Proof of first vaccinations is required before the first class.</li>
  </ul>

  <h2>Save your puppy's spot</h2>
  <p>Classes are limited to 8 puppies.</p>
  <a class="cta" href="https://corner-post.example/puppy">Sign up at corner-post.example/puppy</a>
  <p>Or call <a href="tel:5550188">555-0188</a>.</p>
</main>

</body>
</html>
```

- **Order:** The menu is the first element, with the price banner directly under it. That keeps the price ahead of all page content. If your partner wants the price above the menu, move the `<div class="price">` block above the `<nav>`.
- **Menu links:** The menu URLs (`/`, `/classes`, `/blog`, `/about`, `/contact`) are placeholders, so swap in your real paths.
- **Copy:** I used only the facts you gave, with no added claims or testimonials.
