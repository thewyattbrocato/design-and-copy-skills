**What a variable font is**

A normal font family is a bundle of separate files: Regular, Bold, Light, Italic, and so on. Each weight or style is its own file.

A variable font puts all of that into one file with "sliders" built in. Instead of choosing between Light (300) and Bold (700), you can pick any weight in between, like 450 or 612. Some variable fonts also have sliders for width or slant.

**Is it better?**

For a website, usually yes:
- **Fewer files, faster pages.** If your design uses three or four weights, one variable file is often smaller than the separate files combined. That helps load speed.
- **More design flexibility.** Your developer can fine-tune weights without needing more files.
- **Works in all modern browsers.**

It isn't better in every case. If the site only uses one or two weights, a few normal files can be just as small. Very old browsers and some email or design software handle variable fonts poorly, but that rarely matters for a new website.

**One practical note**

A `.ttf` file works, but for the web it's better to convert it to `.woff2`. That's a compressed web format that is much smaller and loads faster. Your developer, or a free tool like Google's `fonttools` or Transfonter, can do this in a minute. Check the license first (see below), because some licenses restrict converting the file.

**Can you put it on your website?**

I can't tell from the file name. Whether you can use it depends on the license your designer got with it, and a font license is separate from owning the file. Things to check:
1. **Ask your designer** where the font came from and whether the license covers web use. Many fonts are licensed for desktop use only (print, logos, documents), and web use needs a separate "webfont" license.
2. **Look for a license file** (often `LICENSE.txt` or `OFL.txt`) in whatever the designer sent.
3. **If it's a free font**, such as from Google Fonts, it's probably under the SIL Open Font License. That license allows web use and doesn't charge for it.
4. **If it's a paid font**, check that the license covers your website's expected traffic. Some licenses are priced by monthly page views.
5. **Confirm the license is in your name** (or your business's). A license bought by the designer for their own use may not cover you.

A short email to your designer should settle it: "Does our license for Marlowe cover web embedding for [your domain], and can it be converted to WOFF2?"

I can look through the files if you tell me where the folder is. I can check for a license and read the font's built-in metadata, which often names the maker and license terms. That would tell us more than the file name does.
