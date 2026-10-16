Partly. Your printer is oversimplifying, but some of the shift is real.

**Why it happens**

- **Gamut:** Screens make light, so they can show very saturated oranges like #ff6a1a (RGB 255, 106, 26). Four-color process ink (CMYK) can't reach that brightness and saturation. The printer has to pull the color toward the nearest value it can make, and the closest match often looks duller.
- **Conversion:** If the file was converted from RGB to CMYK with a generic profile, or the printer's default conversion was used, the orange can drift toward brown. Adding black ink to the orange is a common cause.
- **Paper:** Uncoated stock soaks up ink and dulls color. Coated or silk stock keeps it brighter.

**What to do**

1. **Ask for a specific fix, not a general answer.** Request the press's ICC profile (for example, GRACoL or FOGRA, depending on the press) and the paper stock they plan to use. Ask them to tell you the closest in-gamut CMYK value for your orange.
2. **Consider a spot color for the orange.** A Pantone spot ink, such as a bright orange like PMS 021 C, prints much closer to the screen orange than CMYK does. It costs a little more if you're not already running a spot color, but it's the most reliable way to get a bright orange on paper. Confirm the exact number against a printed Pantone swatch book, not a screen.
3. **Keep black out of the orange.** Make sure the orange areas are only cyan, magenta, and yellow, with no K. Check the file for rich black or grayed-out colors that might be pulling it brown.
4. **Get a color-matched proof on the actual paper.** A printed proof on the same stock is much more useful than a PDF viewed on your screen. Compare it side by side with your website's orange on a calibrated display, and expect some difference.
5. **Reconsider the paper if the orange still looks flat.** A coated or silk stock often makes the difference.

If you send me the printer's answer about the profile, paper, and whether they can do a spot color, I can help you check the numbers and draft the note back to them.
