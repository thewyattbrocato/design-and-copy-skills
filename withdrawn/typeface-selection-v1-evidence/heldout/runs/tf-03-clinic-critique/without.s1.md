The "messy" look comes mostly from using too many typefaces, and a few of the choices are poor for your audience.

**Main problems**

1. **Six font families on one site.** You have Open Sans, Playfair Display, Montserrat, Lora, Poppins, and Courier New. Most sites do well with two, or three at most. Each one has its own shapes and proportions, so the page feels unplanned.

2. **Four similar sans-serifs.** Open Sans, Montserrat, and Poppins are all sans-serifs, and Poppins and Montserrat are both geometric. They look alike but not identical, which looks like a mistake instead of a deliberate contrast. Playfair Display (a high-contrast serif) and Lora (a softer serif) have the same issue.

3. **Headings change font at every level.** h1, h2, and h3 are each a different family, so the page's hierarchy looks inconsistent instead of clear. Doctor names switch to Lora while the nav and buttons use Poppins, which adds more variation.

4. **Courier New for phone numbers.** A typewriter font looks out of place next to the rest of the page. It also draws attention to a number that should be easy to read and tap.

5. **Playfair Display for h1.** It has very thin hairline strokes that get hard to read at smaller sizes or on low-contrast screens. That matters for older patients.

**Why it matters for your patients**
Older readers tend to have more trouble with thin strokes, tightly spaced letters, and visual clutter. A page full of appointment times, addresses, and phone numbers needs to be predictable and easy to scan.

**A simpler setup**

Use one sans-serif for almost everything, plus an optional serif for headings:

```css
body, nav a, .btn, .phone-number {
  font-family: 'Open Sans', sans-serif;
}
h1, h2, h3, .doctor-name {
  font-family: 'Lora', serif;  /* or just use Open Sans here too */
}
```

If you want the simplest version, use Open Sans everywhere and vary only weight and size.

**Some additions for readability**
- Set body text to at least 18px, with a line-height of about 1.5–1.6.
- Make the phone number bold, not monospace. Wrap it in a `tel:` link so it's tappable on phones.
- Use dark text on a light background with strong contrast, and avoid light gray text.
- Use `font-weight: 600` or `700` for buttons and nav links. Avoid thin weights.

I can only see the CSS you pasted. If you share the HTML or a link to the page, I can check for other issues, such as font sizes, spacing, and color contrast.
