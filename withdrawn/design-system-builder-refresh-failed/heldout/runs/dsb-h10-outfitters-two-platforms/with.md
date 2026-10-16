**Do (b): one token file in the repo that generates both the CSS and the Swift.** Don't pick (a) or (c).

- **(c) is the setup you already have.** A shared doc is still typed by hand in two places, and that's how the oranges drifted.
- **(a) fixes only the designer-to-dev link.** Devs still copy values by hand into web and iOS separately, so it can drift again. It's also the most manual option.
- **(b) removes the copying.** A value changes in one place, and both platforms get it from the same build.

The designer can still work in their tool. Make the design tool's variables match the repo file's names once. After that, a value change is a PR that edits the JSON, and the designer approves it. If the tool can export variables as JSON, that export can feed the file instead of someone retyping values. Start without that, though, and add it later if the manual step annoys you.

**How to start**

1. **Inventory the colors.** Search both codebases for hex values and `Color(...)`/`UIColor(...)` literals, and list them with counts (`[count from your repo]`). Expect near-duplicates, such as three grays one step apart. Those are unresolved conflicts, not a palette.
2. **Settle the orange first.** The designer picks one value for the brand orange. That decision is the first entry in the file.
3. **Write a small `tokens.json` organized by role, not by color.** Use names like `color.accent`, `color.text.primary`, `color.text.secondary`, `color.surface`, `color.border.subtle` and `color.danger`. Don't use `orange-500` or `homepage-hero-blue`. Put a short list of raw values underneath. Add spacing as a single scale of 8–10 steps, such as 4, 8, 12, 16, 24, 32, 48, 64.
4. **Generate both outputs with [Style Dictionary](https://styledictionary.com).** It's the standard tool for this. It produces `tokens.css` (custom properties) for the storefront and a `Tokens.swift` file (or an asset catalog) for iOS. Run it in CI and fail the build if the committed output is stale, so nobody edits generated files by hand.
5. **Migrate colors first, then spacing.** Replace literals with tokens as you touch screens, starting with the colors that have drifted. Don't try to convert everything in one pass. Anything that stays a one-off should be marked as an exception.
6. **Write a one-paragraph change rule.** Changing a token means a PR, with the designer approving value changes. Deprecate a token before removing it.

**Later:** dark mode or a second brand fits naturally. Each theme remaps what the roles point to, so the components don't change.

**Assumptions:** the web and iOS code can read a shared file, either in one repo or through a small shared package. I also assumed the design tool supports variables. I couldn't inspect your code from here (this directory is empty). If you point me at the two repos, I can run the color inventory and draft the first `tokens.json` and Style Dictionary config.
