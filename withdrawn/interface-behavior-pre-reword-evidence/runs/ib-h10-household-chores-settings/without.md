The biggest problem is that every option starts off or blank. That makes the app do nothing until someone has configured it, and in a household that someone is usually one person who gives up halfway. Make every option ship with a working default, and ask during setup only for things you can't guess: who lives here and which chores exist.

I only have the categories you listed, not all 24 options, so this is by category.

## Sorting rule

For each option, ask three questions in order:
1. **Would a reasonable household ever want it different?** If not, hardcode it.
2. **Can the app infer it?** If so, infer it (timezone, locale, OS dark mode).
3. **Is it personal or household-wide?** Personal options go in each person's profile. Household options are few and live in one place.

You should end up with about 6–8 visible settings.

## Category by category

| Area | Decision | Default |
|---|---|---|
| **Reminder times** | Personal setting, one time per person, not a household matrix. | On, 8:00 on the day a chore is due, plus one evening nudge if it's still undone. |
| **Quiet hours** | Personal setting, a single range. | 10pm–8am. Hold notifications and deliver them in the morning. |
| **Points per chore** | Not a settings screen. Each chore gets a size (Small, Medium, Big) when it's created, and the size sets the points. | Templates come pre-sized, e.g. 1 / 3 / 5. Add one household toggle for "use points", on by default. |
| **Rotation rules** | Cut most of them. Offer one choice per chore: *rotate*, *always the same person*, or *anyone*. | Rotate, in the order people joined, advancing when the chore is done or its due date passes. |
| **Who can edit what** | Collapse the matrix into one household toggle: "only admins can edit chores and points". | Off, so everyone can edit. The creator is admin and is the only one who can remove members or delete the household. |
| **Theme** | Don't build it for v1. | Follow the system. |

## What should just happen

- **Swaps:** anyone can propose one, and the other person accepts or declines. A request expires at the due date, and the chore then stays with the original person. Points go to whoever does the chore.
- **Overdue chores:** remind once the next day, then stop. The chore stays assigned, with no penalty and no repeated nagging.
- **Away or vacation:** add a per-person "I'm away until [date]" toggle. Rotation skips that person automatically, which replaces most of the rotation-rule options.
- **Points and leaderboard:** reset weekly. Use device timezone and locale, including the first day of the week.
- **Notifications:** ask for OS permission once, at the first moment a reminder is useful, not in settings.

## What to cut

Cut anything that exists only to configure an edge case, such as per-chore reminder overrides, custom rotation orders and permissions for individual features. If someone asks for one after launch, add it then.

## A week

1. **Days 1–2:** Write down the defaults above and apply them in code, so the app works with zero configuration. Sort your 24 options into hardcode, infer, personal or household.
2. **Day 3:** Build onboarding: names, then pick chores from templates that already have size and rotation set. The household should have a working schedule in under two minutes.
3. **Day 4:** Build the settings screen with the remaining options, split into "You" (reminder time, quiet hours) and "Household" (points on/off, admin-only editing).
4. **Day 5:** Build swap and away flows, since they replace several settings.
5. **Days 6–7:** Test with one real household from a fresh install and watch where they get stuck. Log which settings anyone changes, and add back only the ones people actually reach for.

If you paste the full list of 24, I'll sort each one into hardcode, infer, personal or household, with a default.
