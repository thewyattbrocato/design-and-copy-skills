# Recommended layout for Fernwood notification settings

Group the toggles by what they're about, put the two master switches at the top, and tuck rarely changed settings behind a second level.

## Top level

**1. Delivery channels** (the two masters and quiet hours)
- Push notifications (master)
- Email notifications (master)
- Quiet hours: show as a row that opens a time-range picker, not a toggle. It's a schedule, so a toggle misrepresents it.

Turning a master off should grey out and collapse everything it controls. If both masters are off, show a short "All notifications are off" state instead of 11 dead toggles.

**2. Garden care** (the core value of the app)
- Watering reminders
- Frost alerts
- Harvest windows
- New plant suggestions

**3. Community**
- Friend requests
- Comments on my beds
- Shared bed invites

**4. Updates and marketing**
- Weekly summary email
- Plant-of-the-week
- Product news email
- Sale announcements

## Details that help

- **Per-channel control:** Don't make people hunt through two parallel lists. Give each row a push and an email control, either as two small checkboxes or as a "Push, Email" subtitle that opens a detail view. Weekly summary, product news, and sale announcements are email-only, so they need no channel choice.
- **Defaults:** Keep the garden-care alerts, especially frost, on by default. They're time-sensitive and the reason people use the app. Keep marketing off by default or opt-in.
- **Progressive disclosure:** Make each section a row with a summary ("Watering, Frost, +2 on") that opens its own screen. This works well if you expect more toggles later. With only 14, plain section headers on a single screen are also fine. I'd start with headers and only split into subscreens if the screen still feels long.
- **Section order:** Put channels first because they gate everything else. Then order sections by how much people care, with marketing last.
- **Labels:** Add one line of helper text only where the name is ambiguous. "Harvest windows" and "Plant-of-the-week" would benefit. Skip it for the obvious ones.
- **Move marketing apart:** Sale announcements and product news have a different consent feel from care alerts. Separating them makes the page feel less spammy and may help with compliance.

## What I'd skip

- Collapsing everything into one "all garden alerts" toggle. People often want frost alerts but not plant suggestions.
- Putting quiet hours at the bottom. It's a global rule, so it belongs with the channels.

If you'd like, I can sketch this as a component structure or wireframe in your stack. Tell me what the front end is built in.
