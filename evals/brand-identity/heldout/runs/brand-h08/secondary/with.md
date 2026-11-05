**Your designer is partly right, but "just how embroidery works" doesn't excuse the result.** Thread has physical limits: a line that's too thin gets buried by the stitches around it, and text that's too small fills in. Those limits are why embroidery shops ask for a version drawn for stitching. Your logo was never drawn for either the favicon or the thread, so both failures are the same problem: one master file shrunk to a size it wasn't designed for.

**Why it happens**
- **Favicon:** At 32px, a detailed mark, a thin line, or a small tagline has less than a pixel per detail, so antialiasing turns it into gray. The full logo can't be shrunk; it needs a simpler icon.
- **Embroidery:** Fine lines and small letters are the first things to merge. Each thread is roughly 0.5 to 1 mm wide, so anything thinner or closer together fills in. Ask your shop for their minimum line width and minimum letter height. Those numbers decide what can stay.

**What to do (small project, three files)**

1. **Make a small-size icon.** Use a monogram or a single symbol, not the whole lockup. Make it solid, bold, and one color with no hairlines, and check it at 16px and 32px in black on white and white on dark. Export `favicon.svg` and a 32×32 PNG, plus a 180×180 `apple-touch-icon.png`. Link them in your site's `<head>`:
   ```html
   <link rel="icon" href="/favicon.svg" type="image/svg+xml">
   <link rel="icon" href="/favicon-32.png" sizes="32x32">
   <link rel="apple-touch-icon" href="/apple-touch-icon.png">
   ```
2. **Make an embroidery version.** Redraw the logo with heavier strokes, fewer colors (one or two thread colors is ideal), and no fine detail. Either drop the tagline from the polo or make it large enough to meet the shop's minimum letter height, and move it to the back neck or sleeve if it has to stay small-print-free. Ask the shop to digitize from this file, not from the web version.
3. **Test before reordering.** Ask for a sample stitch-out on the same fabric and color you'll buy. Check it at arm's length, the way a client would see it.

**Assumption:** I haven't seen your logo, so I can't say which details to cut. Send the file, and I can suggest specific simplifications. **Trade-off:** the polo will show a simpler mark than the website, so decide whether the tagline belongs on the shirt at all.
