**Short answer:** on paper, 16px isn't much smaller for your customers than it is for you. It's marginal in both cases. Your laptop setup just hides that, and the kiosk exposes it.

**Assumptions** (tell me if any are wrong, because they change the numbers):
- The panel is 1920×1080 at 21.5", which is about 102 px/in, or 0.25 mm per pixel.
- Customers stand about 700 mm (28") away.
- You're using a 14" laptop at about 550 mm (22"), roughly 126 CSS px/in.

**Why 16px looks fine to you**

| | Laptop | Kiosk |
|---|---|---|
| Physical cap height of 16px text | 2.2 mm | 2.8 mm |
| Viewing distance | 550 mm | 700 mm |
| Apparent cap height | about 14 arcmin | about 14 arcmin |

- **Same apparent size:** the kiosk text is physically bigger, but the extra distance cancels that out. Both come out around 14 arcminutes.
- **Below the guideline:** ISO 9241 puts the minimum at about 16 arcmin and comfortable reading at 20–22 arcmin. 16px misses the minimum in both setups.
- **Why the laptop hides it:** you can lean in, the retina screen is much sharper, and you're reading a menu you already know. Customers are standing, can't lean in, and are seeing the dishes for the first time on a ~100 ppi panel, probably with glare.
- **Reading in a hurry:** on a kiosk people scan rather than read, so text that's merely readable gets skipped. That's why they ask staff.

**What to change**

Target a cap height of about 4.5 mm (22 arcmin) at 700 mm. That works out to a 6.4 mm em, or about **26px** on this panel. The rule of thumb is `px ≈ distance_mm × 0.0091 ÷ pixel_pitch_mm`.

| Role | Now | New | Notes |
|---|---|---|---|
| Descriptions | 16px | **26px** | weight 500, line height 1.45, dark on white (about 10:1 contrast or better) |
| Dish names | ? | **32px** | weight 600 |
| Prices | ? | **32px** | weight 600, `tabular-nums`, right-aligned |
| Category headings | ? | **40px** | weight 700, more space above than below |
| Allergen/diet tags | ? | **22px minimum** | nothing on screen under 22px |

```css
.dish-desc  { font-size: 1.625rem; line-height: 1.45; font-weight: 500; max-width: 45ch; }
.dish-name  { font-size: 2rem;     line-height: 1.2;  font-weight: 600; }
.dish-price { font-size: 2rem;     font-weight: 600; font-variant-numeric: tabular-nums; }
.category   { font-size: 2.5rem;   line-height: 1.15; margin: 2em 0 0.5em; }
.dish-tag   { font-size: 1.375rem; }
```

- **Layout:** at 26px, a card about 560px wide gives roughly 40 characters per line. Descriptions will wrap to 2–3 lines, so trim them to about 80–100 characters. Put the ingredients customers ask about first.
- **Touch targets:** while you're in there, make buttons at least 16 mm (about 64px) tall. The usual 9–10 mm minimum is for handheld devices.

**Check it:** put up the new text and stand where customers stand. A capital letter should measure at least 4.5 mm on the glass. If the panel is actually 4K (about 205 ppi), multiply every size by about 2, because the same CSS px will be half the physical size.
