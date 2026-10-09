**Recommendation:** use one designed-together family for all three scripts, and put the Latin face first in every font stack so stop names always render in it.

[...]

- Japanese fonts ship their own Latin glyphs, and they are often clumsy: wide, uneven spacing and a different x-height. Arabic fonts' Latin glyphs are often weak too.
- Put the Latin font first, then the script font: `"Plex Sans", "Plex Sans Arabic", sans-serif`. Latin characters then take the first font and Arabic or Japanese characters fall through to the next.

[...]

**5. Layout**
- Mirror the departures list for RTL with logical properties (`start`/`end`). Keep times and platform numbers in a fixed LTR cell.
- Design for expansion. Arabic strings are often longer, Japanese ones shorter but taller. Avoid fixed heights on the alert card and truncate with care.
- Give each script its own tuned size and line-height tokens (for example, `--lh-ar`, `--lh-ja`) and key them off `lang`.

[...]
