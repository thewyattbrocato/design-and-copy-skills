I couldn't find your token files in this directory, so I used a common convention. If your names differ, swap in your own examples before posting.

```
Team, we're getting one-off colors and spacing values, and it's making the UI hard to maintain. Please use tokens only, never raw hex or px values.

Naming: category-role-variant, lowercase, kebab-case.
• color-text-primary, color-surface-raised, color-border-danger
• space-1 through space-8 (4px steps)

Need something new?
1. Search the tokens file first. The value may already exist.
2. If not, post in #design-system with the use case and where it's needed.
3. A maintainer approves it and adds it to the tokens file.
4. Then use the token in your code.

Don't add a value inline "just this once." That's how the mess started.
```

That's 103 words. I assumed a `category-role-variant` scheme, a 4px spacing scale, and a #design-system channel, so adjust those to match your setup.
