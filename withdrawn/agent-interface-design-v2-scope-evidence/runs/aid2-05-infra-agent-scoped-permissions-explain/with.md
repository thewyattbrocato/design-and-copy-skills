# Tidewater permission redesign

**Assumptions** (correct me if any are wrong):
- Tidewater issues kubectl-style commands against staging and prod clusters.
- It can be given its own Kubernetes service account.
- Approvals happen in Slack.

**The promise, shown at setup and on the status home:** "While you're away, Tidewater will read logs and cluster state, restart pods, and scale deployments inside set limits. It will never delete namespaces, volumes, or data, and it will never touch anything outside the limits without a named person approving that exact command."

## The core change

Today, one control (a human tap) guards every command, and fatigue has made that control nominal. The redesign uses three layers, so no single one has to be perfect:

1. **Kubernetes RBAC on Tidewater's service account.** It lacks permission to delete namespaces, PVCs, CRDs or secrets, or to drain nodes. Even a bad approval can't run these. This alone would have prevented last week's incident, and it is stricter than today.
2. **A deterministic policy engine** classifies every command by what it will actually do. It doesn't use the agent's description of the command. The engine parses the verb, resource kind, cluster, namespace and selector. It resolves wildcards, `--all` and label selectors to a concrete object list through a server-side dry run. Anything it can't parse or classify goes to the approval tier.
3. **Human approval, reserved for the commands where judgment matters.** Because it is rare, it can be taken seriously.

## Four tiers

| Tier | Examples | What happens |
|---|---|---|
| **0. Read** | `get`, `describe`, `logs`, `top`, `events` | Runs without a prompt and is logged. Secrets are excluded, and `exec` and `port-forward` are not reads. |
| **1. Bounded and reversible** | Restart a pod. Rolling restart. Scale a deployment within ±limits, in allowlisted namespaces. | Runs without a prompt inside its caps, and shows up in the digest. **Staging only at launch.** Prod stays at tier 2 until a clean record exists (see Trust). |
| **2. Needs a decision** | Anything in prod. Anything over a cap. Scaling to 0. Rollbacks. Edits to configmaps. Anything the engine can't classify. | A short, specific approval prompt (below). |
| **3. Destructive or irreversible** | Deletes of any kind, node drains, anything touching volumes | Tidewater cannot do these. RBAC blocks them. If it needs one, it posts a runbook-style request for a human to run themselves. |

**Starting caps for tier 1 (assumptions to tune, not findings):**
- Scale changes: at most 2× the current replica count, never below 1.
- Restarts: at most 3 per workload per hour.
- Total objects touched: 10 per command.

## The approval prompt (tier 2)

Today's prompts show a command string. The new prompts show consequences, because the command string is what people stopped reading.

> **Tidewater wants to restart `checkout-api` in prod (cluster `use1-prod`)**
> Affects: 1 deployment, 6 pods. Rolling restart, so no downtime expected.
> Why: pods in CrashLoopBackOff for 14 min (link to logs).
> Undo: not needed, because a restart is self-healing.
> Expires in 10 min. **Approve** · **Deny** · **Ask Tidewater why**

Rules for these prompts:
- **Impact first, command second.** Show the resolved object counts. If a selector expands to more than expected, say so in bold.
- **Approval is bound to the exact command.** A hash of the resolved command is stored, and any change forces a new prompt. Approvals expire.
- **Prod prompts go to the on-call or the owning team**, not a broadcast channel. A broadcast lets everyone assume someone else read it.
- **Deny takes one tap with an optional reason.** Tidewater then proposes an alternative instead of retrying the same thing.

## Friction by risk, not uniformly

Tier 3 isn't approvable through Slack at all. For commands in between that could still do damage, add friction in proportion:
- Prod scaling to zero or touching more than the cap: the approver must **type the workload name** to confirm.
- Anything the engine flagged as "resolved scope bigger than the command suggested": a short hold (starting value: 60 s) with the full object list visible.

Tapping approve on a screen that looks like every other screen is what failed last week. These screens look different on purpose.

## What people hear about, and when

| Kind | Example | Delivery |
|---|---|---|
| **Problem** | Approval needed in prod. A command was blocked. A cap was hit. | Immediate DM to the responsible person |
| **Concern** | "Restarted `orders` 3 times in an hour, which is the cap. This looks like a real fault, not a stuck pod." | Immediate, once, with what Tidewater is doing next |
| **Completion** | Tier 0 and tier 1 actions | One digest per shift (the team picks the time) |
| **Check-in** | "Tidewater is running, last action 09:12" | Status home only |

**Digest:** it lists the doubtful items first, such as actions near a cap and restarts of the same workload that keep recurring. Each item has its own **Undo** (scale back to the recorded previous replica count) and the two feedback controls below. Plainly stated: a restart can't be undone, but it is harmless to repeat.

## Slack App Home as the status page

It shows **Running / Paused**, the last action and its time, caps used today against their limits (e.g. "restarts 4 of per-workload 3/h"), and a pending-approvals list. **Pause** is one tap from here, and the paused state is shown as a banner. If a trigger passes while paused, Tidewater says what it skipped and offers "resume now."

## Fixing mistakes

Each digest item has:
- **Not this one:** deny and optionally exempt a namespace or workload for a duration.
- **Never for this kind:** shows the rule it creates in plain words ("Tidewater will no longer restart pods in `payments-*` without approval") plus three example commands it would affect.

A skipped-and-blocked list shows what Tidewater wanted to do and couldn't, because missed fixes otherwise go unnoticed. After the same denial twice, Tidewater proposes the rule.

## Keeping approvals meaningful over time

- **Prompt budget per person.** If someone gets more prompts than a threshold (starting value: 10 a day, to test), Tidewater doesn't send more tap-approve cards. It tells the team the policy needs tuning.
- **Weekly review.** Prompts approved every time are listed with a proposal: "Move this kind to tier 1?" A human accepts it. The policy never loosens itself, and never loosens for anything that deletes or sends.
- **Reflex detection.** If a tier 2 approval comes back faster than the prompt can be read, it's logged and reviewed. Don't punish this. Treat it as a design bug in the prompt.

## Trust, widening scope

Prod tier 1 is a proposal Tidewater makes after a run of clean staging results the team can see in the digests. A human accepts it, and it's reversible with one setting. Nothing widens silently, and nothing in tier 3 ever widens.

## Rollout, to check we're at least as safe

1. **Shadow mode first.** Run the classifier over the last few weeks of approved commands without changing behavior. Review the full list of what would have been auto-allowed. Any command a reviewer wouldn't have wanted auto-allowed is a policy bug to fix before launch.
2. Apply the RBAC restrictions first. They're independent of everything else, take effect immediately, and cost nothing in usability.
3. Launch tier 1 in staging only, and move to prod after the review.

## Safety comparison

| Risk | Today | Redesign |
|---|---|---|
| Destructive command approved by reflex | Possible (it happened) | Blocked by RBAC; no approval path exists |
| Agent misdescribes its command | Approver reads the agent's text | Engine classifies the resolved command |
| Selector expands wider than expected | Invisible | Shown as object counts, with a hold |
| Approval reused for a modified command | Unclear | Bound to the command hash and expires |
| Rubber-stamping | Constant | Rare prompts, budgeted, and reviewed |
| Auto-run commands | None | Staging-only, capped, reversible, and in the digest |

The one place the new design is looser than today is tier 0 and tier 1 running without a tap. That's why tier 1 is capped and staging-only to start, and why shadow mode comes before launch.

**Open question for you:** can the cluster setup give Tidewater a separate service account with scoped RBAC per cluster? The design depends on layer 1, and if it can't, tier 3 would need a hard-deny list in the policy engine instead. That is weaker, because it relies on the engine parsing correctly.
