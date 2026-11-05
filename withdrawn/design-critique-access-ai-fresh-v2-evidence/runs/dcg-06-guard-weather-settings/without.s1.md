The structure is solid. Semantic landmarks, a fieldset/legend for the radios, and real `<label>` associations are all there. The biggest problem is the button pair.

**Main issue: the destructive button**
- "Reset app and clear saved places" is irreversible, but it has the same style as "Save changes" and sits right next to it. In a narrow column, a mis-tap is easy.
- Give it a different treatment: a secondary or danger style, separated from Save, or moved to its own "Danger zone" section at the bottom.
- Add a confirmation step (dialog or undo) that says what will be deleted.
- Make "save changes" the clear primary button.
- Set `type="button"` on both, or `type="submit"` on Save, so they behave predictably if the page ever sits inside a `<form>`.

**Accessibility and markup**
- **Wrap in a `<form>`.** Then Enter-to-submit works and the Save button has a real purpose.
- **Add `name` and `value` attributes** to the radios, checkboxes, and select options. Right now nothing can be read back on save, and the radio `name="t"` is cryptic. `name="temperature-unit"` is better.
- **Group the checkboxes.** The two alert checkboxes and the time input could sit in a fieldset with a legend, since they're related.
- **Disable "summary time"** when "daily summary" is off, or hide it. Otherwise it looks active but does nothing.
- **Location checkbox:** add a line of help text explaining what happens when it's off (manual entry? where?). Link it with `aria-describedby`. As written, turning it off leads nowhere.
- **Touch targets:** the labels wrap the inputs, which is good. Make sure each label row has at least about 44px of height and some spacing between rows.
- **Save feedback:** add a status message (`role="status"`) so screen reader users and sighted users both know it saved.

**Smaller things**
- Lowercase headings are fine as a style choice. If it's intentional, do it with CSS (`text-transform`) so the underlying text stays normal-cased for screen readers.
- Unit order: consider defaulting wind and temperature units from the user's locale rather than always starting with Celsius and km/h.
- The wind `<select>` has no `name`, same as above.
- Consider a "last saved" or unsaved-changes indicator if saves aren't instant.

**Suggested button markup**
```html
<div class="actions">
  <button type="submit" class="btn btn-primary">Save changes</button>
</div>

<section class="danger-zone">
  <h2>Reset</h2>
  <p>Clears saved places and restores default settings. This can't be undone.</p>
  <button type="button" class="btn btn-danger">Reset app and clear saved places</button>
</section>
```

If you fix only one thing, fix the destructive button.
