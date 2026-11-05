# Tidewater permission redesign

**Assumptions:** Tidewater runs `kubectl` against staging and prod clusters. Most of today's 60+ prompts are reads and routine restarts, but I haven't seen your logs. Numbers below are starting values to tune, not findings.

**One-line promise:** While you're away, Tidewater will read freely and do a short list of reversible fixes within caps. It will never delete anything that holds data or structure, and it will never act outside its list without asking.

## 1. Core change: prompts depend on what the command does

A deterministic classifier decides the tier. It parses the verb, resource, namespace, cluster, selectors and flags. It does not use the model's own description of the command. Anything it can't parse, including pipes, `xargs`, `sh -c` and unknown verbs, goes to Tier 2 or higher. Selectors like `-l`, `--all` and `-A` are resolved to the concrete objects before classification, so the tier reflects the real blast radius.

| Tier | Examples | What happens | Interrupts a human? |
|---|---|---|---|
| **0 Read** | `get`, `describe`, `logs`, `top`, `events` | Runs, logged | No |
| **1 Standing rules** | Delete a controller-owned pod, `rollout restart`, scale within bounds | Runs within caps, reported in digest, one-tap undo | No (unless a cap trips) |
| **2 Ask** | Scale to 0 or past the cap, `apply`/`patch`/`edit`, any prod change outside a rule | Individual approval card | Yes |
| **3 Guarded** | Delete namespace, PVC, CRD or node drain, RBAC changes, any `Secret` read or write | Typed confirmation, a second person, a hold | Yes, loudly |

Notes on the tiers:
- **Secret reads** are Tier 3, not Tier 0. `get secret -o yaml` exposes data, so it isn't a harmless read.
- **Tier 1 caps** are written per rule. Example starting values:
  - Restarts: at most 3 per deployment per hour.
  - Scaling: within ±2 replicas of the current count, never to 0, never above a team-set ceiling.
  - Pod deletes: only pods with a controller owner.
- **Circuit breaker:** if Tier 1 actions in a cluster exceed a set rate, or the same fix repeats on the same workload, Tidewater stops auto-running and escalates to a Tier 2 prompt saying "this keeps happening."
- **Rules are owned by the team.** They live in a versioned file changed by reviewed PR, not by Tidewater and not by a Slack button. Tidewater can propose widening a rule, never apply it.

**Why this is at least as safe as today:**
- Unknown means ask, so the default fails closed.
- Every approval is bound to the exact resolved command. A changed command, or an approval older than 15 minutes (assumed), needs a new approval.
- Tier 3 is stricter than today. A tap can no longer delete a namespace.
- Tier 0 and Tier 1 hold only things you could already do with a tap and little risk.

## 2. The prompts that matter

Tier 2 and Tier 3 cards look different from each other and from anything else Tidewater posts. The consequence comes first, and the raw command comes last.

**Tier 2 card:**
```
Approve? Scale checkout-api to 0 replicas in PROD (us-east)
Effect: the service goes fully offline. Currently serving 6 pods.
Why Tidewater wants this: <its stated reason, one line>
Undo: scale back to 6 (one tap after approval)
Requested by: @dana · Expires in 15 min
[Approve]  [Deny]  [Show command]
```

**Tier 3 card:**
```
🛑 DESTRUCTIVE: delete namespace "payments-staging"
This will permanently remove 14 deployments, 9 services, 3 PVCs (210 GiB)
and every Secret in the namespace. This cannot be undone.
Resolved from a server-side dry run, not from the request text.
To proceed:
 1. Type the namespace name: [__________]
 2. A second engineer (not @dana) must also approve
 3. 5-minute hold, cancellable by either of you
[Cancel]
```

The blast-radius figures come from `--dry-run=server` and live object counts. If Tidewater can't compute them, the card says "could not determine scope" and stays at its tier.

In prod, Tier 3 may be better off as "Tidewater can't do this; here's the runbook and who to page." Decide that with the team.

## 3. Keeping attention on the cards that matter

- **Tier 2/3 cards are the only things that interrupt.** Everything else goes to a digest.
- **Daily digest, ordered doubtful first.** It lists every Tier 1 action with its target, reason and an **Undo** button. The first items are the ones near a cap, repeated, or in prod. It never shows a bare total like "31 actions handled."
- **Message kinds:** problems and approval cards interrupt. Concerns ("checkout-api has been restarted 3 times today, cap is 3") are posted once, with what Tidewater is doing, when you'll hear next, and what you can do. Completions are batched. Each kind has its own mute, except Tier 3.
- **Volume watch:** track prompts per engineer per week. If Tier 2 volume climbs, the fix is a reviewed new standing rule, not more taps.
- **Corrections on any digest item:** "Not this one" (optional duration or namespace) and "Never auto-do this kind", which shows the rule it creates and goes to the rules owners as a PR. After the same skip twice, Tidewater proposes the rule.
- **Skipped/denied list:** shows what Tidewater wanted to do and was blocked from, lowest confidence first, so you can spot missed fixes.

## 4. Status, pause, and exit

- `/tidewater status` shows running or paused, the last action and when, the next check, and Tier 1 usage against caps.
- `/tidewater pause` is one step from the status view. While paused, Tier 1 falls back to Tier 2 and the status view says so. Reads stay on.
- Every digest and card has a link to pause, mute or leave, with no reason required. A named on-call human is listed on the status view for when Tidewater is wrong or stuck.

## 5. Rollout, to prove it before it's live

1. **Replay:** run the classifier over 30 days of existing approval logs. Review the tier assignments with the team, especially anything landing in Tier 0 or 1 that you'd want a prompt for. This also gives the real prompt-reduction figure.
2. **Shadow mode:** keep today's approve-everything flow, but show each prompt's would-be tier. Compare for a couple of weeks (assumed). Fix misclassifications.
3. **Go live in stages:** Tier 0 first, then Tier 1 in staging, then Tier 1 in prod. Tier 2/3 cards ship from day one.
4. **Widening:** after a clean run of Tier 1 actions with no undo or complaint, Tidewater may propose raising a cap or adding a rule, as a PR for the owners. It never widens silently.
5. **Incident review:** replay last week's namespace deletion through the classifier. It should land in Tier 3 and be blocked at typed confirmation and the second-person requirement. If it doesn't, the classifier isn't ready.

## 6. Residual risks to decide on

- **Classifier bugs** are now the main risk, replacing "people stop reading." Mitigate with the replay, a test suite of dangerous command shapes, and fail-closed defaults.
- **Auto-run Tier 1 in prod:** if the team isn't comfortable, keep prod Tier 1 as Tier 2 for the first stage and only automate staging.
- **Second approver availability:** off-hours Tier 3 needs an on-call fallback so people don't route around it.

I can turn this into a concrete rules-file schema and classifier test cases, or draft the Slack Block Kit payloads for the two card types. Say which you want.
