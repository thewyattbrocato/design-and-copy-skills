This is solid. Nothing blocks shipping. A few small things:

1. **Add `lining-nums` to the tabular rule.** `tabular-nums` fixes column width but not figure style. If a serif face's default numerals are old-style, digits will bob in the table. `font-variant-numeric: tabular-nums lining-nums;` is a safe default. Check it on the actual font, since Charter and Cambria differ here.

2. **Consider `font-size` and `line-height` on `.tide-table`.** Tables are often set smaller than body text, and tabular figures look best with a little extra leading. You may already handle this elsewhere.

3. **Decide whether `.meta` should always be sans.** If it holds bylines or dates inside article text, it will look different from the surrounding serif. That may be what you want, but it's worth a glance.

4. **Watch the heading weight.** `font-weight: 700` on `system-ui` is fine, but on Linux `system-ui` can resolve to a font with no true bold. Test once there, or drop to 600 if the headings look heavy.

5. **Confirm the fallbacks.** Charter ships with macOS and some Linux distros, Cambria with Windows, and Sitka Text with newer Windows. Everything else falls through to the generic `serif`, which is fine. Since these are all installed system fonts, there's no `@font-face` loading or flash-of-fallback to worry about.

If you can tell me which platforms your readers mostly use, I can point out where the stack will render differently for them.
