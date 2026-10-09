**What's happening**

`flex: 1` is shorthand for `flex: 1 1 0%`, so it lets `.info` grow and shrink. But a flex item can't shrink below its **minimum content size**. For flex items, `min-width` defaults to `auto`, which resolves to the width of the item's longest unbreakable content.

Your email address has no spaces, so the browser sees it as one unbreakable "word." That makes `.info`'s minimum width equal to the full width of the email. The item refuses to shrink past that, so the card overflows its container, and the page scrolls sideways. The avatar and button are pushed along with it.

**The fix**

Override the automatic minimum and tell the browser how to handle the long string:

```css
.volunteer-card { display: flex; align-items: center; gap: 12px; padding: 12px; }
.info { flex: 1; min-width: 0; }
.info span { overflow-wrap: anywhere; }  /* wrap the email onto multiple lines */
```

- `min-width: 0` is the key line. It lets `.info` shrink to the space actually available.
- `overflow-wrap: anywhere` lets the email break across lines. `word-break: break-all` also works, but it's more aggressive.

Two smaller things:

- `.info span` is inline by default. `overflow-wrap` still works on it, but if you want the name and email stacked on separate lines, add `display: block` to it.
- The avatar and button can also get squeezed once `.info` can shrink. Add `flex-shrink: 0` to `.avatar` and `button` so they keep their size.

**Alternative: truncate instead of wrap**

If you'd rather keep the card a single compact row, truncate with an ellipsis:

```css
.info { flex: 1; min-width: 0; }
.info strong,
.info span {
  display: block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

The `min-width: 0` is still required here. Without it, the `overflow: hidden` on the children has nothing to clip against, because the parent has already grown. Truncation hides part of the email, so wrapping is probably better for a volunteer app where people may need to read or copy the full address.
