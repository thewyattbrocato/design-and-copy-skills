Group the 14 toggles by **what they're about**, and show channel (push vs. email) as columns in a grid instead of as separate toggles. That cuts about 14 switches to a few sections and one small grid.

```
Notifications

  Pause all      Push [on]     Email [on]          ← master switches, top of screen

  WHAT TO HEAR ABOUT          Push     Email
  Garden care
    Watering reminders        [✓]      [ ]
    Frost alerts              [✓]      [✓]
    Harvest windows           [ ]      [ ]
  Community
    Friend requests           [✓]      [ ]
    Comments on my beds       [ ]      [ ]
    Shared bed invites        [✓]      [✓]
  Discovery
    New plant suggestions     [ ]      [ ]
    Plant of the week         [ ]      [ ]
    Weekly summary            —        [✓]

  QUIET HOURS                                   ← push only
    [✓] Pause push  10:00 pm – 7:00 am
        [ ] Let frost alerts through

  MARKETING                                     ← separate section
    Product news              email    [ ]
    Sale announcements        email    [ ]
```

Why this works:

- **Masters go at the top, not in the middle.** "Pause all" or the per-channel switches should be the first thing people see. When a master is off, dim the grid below it instead of hiding it, so people can see what they'd get back.
- **The grid replaces toggle sprawl.** Eight topic rows with two channel columns make the choice visible at a glance. Rows the channel doesn't support (weekly summary is email-only, marketing is email-only) show a dash or a single label, not a disabled toggle.
- **Section headers do the explaining.** "Garden care / Community / Discovery" tells people what the switches mean, so the labels can stay short.
- **Quiet hours get their own section.** It's a schedule, not a category, and it only affects push. The "let frost alerts through" exception is worth having, since frost is the one alert that's time-sensitive.
- **Marketing is separate, and its default should be off.** Product news and sales are promotional, not core to garden care, and email marketing carries legal opt-out requirements (CAN-SPAM, GDPR). Keep it visually distinct and make sure the email master switch also stops it. Confirm the exact legal requirements with whoever owns compliance.

Two smaller things:

- **Defaults matter more than layout.** Most people never open this screen, so set sensible defaults: care reminders on, marketing off, comments and suggestions off or in the weekly digest.
- **Consider collapsing the sections.** Show Garden care and Community expanded and Discovery and Marketing collapsed. That reduces the first-glance wall even further.
