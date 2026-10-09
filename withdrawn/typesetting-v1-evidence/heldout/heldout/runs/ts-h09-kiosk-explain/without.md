**Short answer:** 16px is a different physical size on every screen, and the laptop is a poor stand-in for the kiosk. The kiosk text is probably about as small to your customers as the laptop text is to you. You're just reading under much easier conditions.

## Why 16px looks fine to you

A CSS pixel is not a fixed physical size. What matters is the visual angle the text takes up in the viewer's eye. I'm assuming the kiosk is a 21" 1920×1080 panel, which is about 105 ppi. Check this, because a 4K panel changes the numbers.

| | Laptop (14" Retina) | Kiosk (21" 1080p) |
|---|---|---|
| Pixel density | ~127 CSS px/in | ~105 px/in |
| 16px em height | ~3.2 mm | ~3.9 mm |
| Cap height (~0.7 em) | ~2.2 mm | ~2.7 mm |
| Viewing distance | ~55 cm | ~65 cm |
| Cap height visual angle | ~14 arcmin | ~14 arcmin |

The angular size is the same, about 14 arcminutes. That is readable only in good conditions. Comfortable reading for casual, glanceable text is about 20–24 arcminutes. The laptop works for you because:

- You're seated, close to the screen, and focused.
- The Retina display makes the text much sharper. A 105 ppi panel renders thin strokes coarsely.
- You wrote the menu, so you already know what the words say.
- Your lighting and angle are controlled. A shop has glare, and people stand at an angle to the screen.
- Customers are scanning, often in a queue and under social pressure. They aren't settling in to read.

## What to change

These sizes are for 1080p at about 65 cm. A target of 20–24 arcmin works out to roughly 22–27px, and 24px is the practical choice.

| Element | Now | Change to |
|---|---|---|
| Dish descriptions | 16px | **24px** (never below 22px), weight 400–500, line-height 1.4–1.5 |
| Dish names | ? | **32–36px**, semibold |
| Prices | ? | **28–32px**, semibold |
| Allergen/fine print | ? | **20px minimum** |
| Touch targets (buttons, add/remove) | ? | **at least 64px (about 15 mm)**, with 12–16px gaps |
| Text contrast | ? | **7:1 or better**, for example near-black on white. Avoid gray body text and light font weights. |

Other changes:

- **Shorten the descriptions.** At 24px you'll fit about 40% fewer words per line. Aim for 8–12 words, such as "Pork broth, chashu, soft egg, scallion, nori."
- **Use icons for the questions staff keep getting.** Add small icons for spicy, vegetarian, contains pork, and common allergens. Those are probably the "what's in it?" questions.
- **Put the key info in the card.** Don't hide ingredients behind a tap.
- **Turn the brightness up** and tilt the screen if there's glare.

## Check before you commit

1. Open the kiosk browser console and run `screen.width, screen.height, window.devicePixelRatio`. If the screen is 3840×2160 with a ratio of 1, the text is half the physical size I calculated, and you'd need about 48px. If the ratio is 2, the layout is in CSS pixels and my numbers hold.
2. Put 24px text on the kiosk. Have someone who hasn't seen the menu read it from a standing position at arm's length, and adjust from there.
