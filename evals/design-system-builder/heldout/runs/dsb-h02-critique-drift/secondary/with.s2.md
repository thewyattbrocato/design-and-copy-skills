## What's going on

The stylesheet has no shared scale. Each rule picked its own values, and many of them are near-misses of one another, so the app looks almost-consistent, which is harder to diagnose than clearly inconsistent.

- **Near-duplicate colors:** the primary blue is `#2f6fed` on `.btn` and `#2e6dea` on `.btn-big`. The three muted grays (`#8a8f98`, `#8d929b`, `#858a93`) and the two borders (`#e3e5e8`, `#e1e4e8`) are the same story. The green alert and badge are also almost but not quite the same.
- **No radius scale:** 4, 5, 6, 7, 9, 10, 12. Buttons are 5px and the big button is 7px. The select is 4px and the input is 6px.
- **Shadows with no levels:** three different elevations (`0 2px 7px .12`, `0 3px 9px .10`, `0 12px 40px .28`) that are hard to tell apart except at the modal level.
- **Spacing on no grid:** paddings of 9, 11, 13, 17, 18, 22, 26 and margins of 14, 19, 34. Nothing is on a 4px or 8px base.
- **Type sizes on no scale:** 14, 17, 19, 23, 31. The big button and `h4` both use 17px, which is a coincidence rather than a decision.
- **Mismatched control heights:** input is 38px, select is 40px, and buttons have no height, so they will not line up in a form row.
- **Duplicate components:** `.card` and `.panel` are nearly the same thing with different padding and radius. `.btn-big` is a size variant that should be a modifier.
- **Three names for one color:** `.muted`, `.hint` and `.caption` all mean "secondary text" but are slightly different grays.
- **Accessibility:** `#8a8f98` on white is about 3.2:1 and fails WCAG AA for body text. The other two grays are similar. That is probably the one thing users would notice.

Root cause: values were chosen per rule, with no tokens and no reviewed set of allowed values. Each copy-and-tweak added another near-miss.

## What I'd do, in order

1. **Inventory usage first.** Grep the codebase for each hex value and each px value to see how often it is used and where. This tells you which values are load-bearing and which are one-offs. I've only seen this snippet, so I can't tell you which values matter most in the real app.

2. **Collapse near-duplicates into one token each.** Pick one blue, one gray for secondary text, one border, one green, and make them CSS custom properties. This is almost invisible visually and removes the "why does this look different" problem. Don't add new values here, only merge.

3. **Define the scales and map every value onto them.** Something like:
   ```css
   :root {
     --space-1: 4px;  --space-2: 8px;  --space-3: 12px;
     --space-4: 16px; --space-6: 24px; --space-8: 32px;
     --radius-sm: 4px; --radius-md: 8px; --radius-lg: 12px;
     --shadow-sm: 0 2px 6px rgba(0,0,0,.10);
     --shadow-lg: 0 12px 40px rgba(0,0,0,.28);
     --text-secondary: #6b7079;   /* ~5:1 on white */
     --border-default: #e3e5e8;
     --color-primary: #2f6fed;
     --font-sm: 14px; --font-md: 16px; --font-lg: 20px; --font-xl: 24px; --font-2xl: 32px;
     --control-h: 40px;           /* inputs, selects, buttons share this */
   }
   ```
   Map each existing value to the nearest token. Expect small visual shifts; review them on screen rather than trusting the arithmetic.

4. **Refactor components onto the tokens.** Merge `.card` and `.panel` into one surface with a padding modifier if needed. Turn `.btn-big` into `.btn--lg`. Set one height on all controls. Replace `.muted`, `.hint` and `.caption` with a single `.text-secondary`.

5. **Fix contrast while you're there.** Secondary text should be at least 4.5:1. Check the chosen gray in a contrast checker before you ship it.

6. **Keep it from drifting back.** Add a stylelint rule that rejects raw hex and off-scale px values outside the token file. Without this, the same problem returns in a few months.

If you want, I can do steps 2–4 in this file once you tell me where the rest of the stylesheet lives, or I can use the design-system-builder skill to set up the token file properly.
