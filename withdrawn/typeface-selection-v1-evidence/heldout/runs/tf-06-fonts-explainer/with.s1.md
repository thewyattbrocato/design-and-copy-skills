## What a variable font is

A normal font family is a separate file for each style: Regular, Bold, Light, Italic and so on. A variable font packs all of those into one file, and you can pick any point along the range. So you can have weight 450 as well as just "Regular" or "Bold".

## Is it better?

Usually, for a website, yes, with one caveat.

- **Fewer files.** One file replaces four to six, which can mean a slightly faster site.
- **More flexibility.** Your designer can fine-tune weights, for example a heading that's a little less heavy than standard bold.
- **Same look.** It doesn't look different from a normal font. It's just packaged more efficiently.

The caveat is that if you only use two or three styles, the size savings are small. It's not a quality difference, just a convenience. All current browsers support variable fonts.

## Are you allowed to use it?

I can't tell from the file name. Having the file doesn't mean you have the rights, and licenses often split these cases:

- **Desktop use** (Word, Canva, printing menus) is licensed separately from **web use** (putting the font on your site).
- Some licenses limit the number of site visitors per month, or require you to buy for each domain.
- Some fonts are free for any use (for example, fonts under the SIL Open Font License). Others are paid or custom.

Ask your designer these questions, and get the answers in writing:

1. Where did Marlowe come from: a foundry, a free library, or is it custom-made for you?
2. Does the license cover **web embedding / self-hosting** for your domain?
3. Is the license in your name or your designer's? Some designers' licenses don't transfer to clients.

If it turns out you only have desktop rights, the foundry can usually sell you a web license.

## Practical notes for your site

- Your developer will probably convert the `.ttf` to **WOFF2**, a smaller web-friendly format. Check that the license allows conversion, since a few don't.
- They should also set a fallback font, so the page still looks fine while the font loads.

I haven't opened the file. If you'd like, I can look at it for embedded license or copyright information. That's often a good clue, but it doesn't replace getting the license from your designer. Just tell me where it's saved.
