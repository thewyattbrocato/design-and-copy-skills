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
  nav { background: #2b3a2f; padding: 0.75rem 1rem; }
  nav ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 1.25rem; }
  nav a { color: #fff; text-decoration: none; font-weight: 600; }
  main { max-width: 40rem; margin: 0 auto; padding: 1.5rem 1rem 3rem; }
  .price { font-size: 2.5rem; font-weight: 800; margin: 0; }
  .price small { display: block; font-size: 1rem; font-weight: 500; color: #555; }
  h1 { font-size: 1.75rem; margin: 1rem 0 0.25rem; }
  h2 { font-size: 1.25rem; margin-top: 2rem; }
  .btn { display: inline-block; background: #c4561c; color: #fff; padding: 0.9rem 1.5rem; border-radius: 6px; font-weight: 700; text-decoration: none; margin-top: 0.5rem; }
  .call { margin-top: 0.75rem; }
</style>
</head>
<body>

<nav aria-label="Site menu">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/classes">Classes</a></li>
    <li><a href="/blog">Blog</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>

<main>
  <p class="price">$240 <small>for the full 6 weeks</small></p>

  <h1>Puppy Foundations</h1>
  <p>Corner Post Dog School, Ellis Falls</p>

  <a class="btn" href="https://corner-post.example/puppy">Sign up now</a>
  <p class="call">Or call <a href="tel:5550188">555-0188</a></p>

  <h2>Class details</h2>
  <ul>
    <li>6 weeks, Tuesdays at 6:30 p.m.</li>
    <li>Max 8 puppies per class</li>
    <li>Puppies must be 8 to 16 weeks old on the first night</li>
  </ul>

  <h2>What your puppy will learn</h2>
  <ul>
    <li>Sit</li>
    <li>Down</li>
    <li>Come</li>
    <li>Walking on a loose leash</li>
    <li>Settling calmly</li>
  </ul>

  <h2>Before the first class</h2>
  <p>Proof of first vaccinations is required before the first class.</p>

  <h2>Save your puppy's spot</h2>
  <p>Classes are limited to 8 puppies.</p>
  <a class="btn" href="https://corner-post.example/puppy">Sign up at corner-post.example/puppy</a>
  <p class="call">Or call <a href="tel:5550188">555-0188</a></p>
</main>

</body>
</html>
```

- **Menu and price:** The menu is the slim bar at the very top, and the $240 price is the first thing in the page content, above the headline. If your partner means the price should sit above the menu, move the `<p class="price">` block above the `<nav>`.
- **Menu links:** The menu paths (`/classes`, `/blog`, and so on) are placeholders. Swap in your real URLs.
- **Facts:** I used only the facts you gave me. The only added copy is button and heading text like "Sign up now" and "Save your puppy's spot".
- **Sign-up path:** The sign-up button and phone number appear twice, near the top and at the bottom, so people don't have to scroll back up.
