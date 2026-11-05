# Tidewater permission redesign

**Assumptions:** Tidewater acts through a service account with real write access. Engineers approve in Slack. Staging and prod are separate clusters or namespaces that Tidewater can tell apart. All numbers below are starting values to test, not findings.

**One-line promise:** While you're away, Tidewater will read, restart and scale within set limits and tell you in a digest. It will never delete, touch secrets, or act cluster-wide without a named person confirming the exact target.

## Core change: ask by consequence, not by command

Today every command gets the same dialog, so the one that matters looks like the 59 that don't. Each command is classified into a tier, and each tier has its own mechanism, look and channel.

The classifier must be **deterministic code outside the model**. It parses the structured call (verb, resource kind, name, namespace, flags, environment). Tidewater should issue typed API calls, not free-form shell strings, so the classifier sees what will actually run.
- **Unknown or unparseable means Tier 2 or higher.** The classifier fails closed.
- **Content Tidewater reads can't change the tier.** Log text or pod annotations may contain injected instructions, so only the parsed call decides.

| Tier | What | Mechanism | Interrupts a human? |
|---|---|---|---|
| **0 Read** | `get`, `describe`, `logs`, `top`, `events` in any environment | Runs. Rate-limited and logged. | No |
| **1 Standing rule** | Reversible, bounded changes that an engineer pre-approved. Examples: restart pods or rollout-restart in staging, scale within a floor and ceiling. | Runs inside the rule's caps. Undo is available. | No. It goes in the digest. |
| **2 Read-it approval** | Any other change, and any prod change outside a standing rule | One approver reads a specific card (below). | Yes |
| **3 Hard gate** | Irreversible or wide-reach actions: deleting namespaces, PVCs, CRDs or nodes, `--all`, wildcards, cluster-scoped changes, scaling to 0, anything touching RBAC | Typed confirmation, a second person, and a hold (below) | Yes, loudly |

**Reads that stay gated:** `get secret`, `logs` on pods labeled sensitive, and `exec` are Tier 2. Auto-running reads is only safe if they can't exfiltrate credentials.

**Why this is at least as safe as today:**
- Everything that can destroy or can't be undone is stricter than today (Tier 3).
- Tier 1 auto-runs only what is reversible, capped and visible.
- Today a bad command gets through if someone taps Approve without reading. In Tier 3 a tap can't approve anything.

## Tier 1: standing rules instead of per-command taps

A rule is written in plain words and restated before it goes live. For example:

> **Rule: Restart stuck pods (staging)**
> Tidewater may restart pods that have been in CrashLoopBackOff or Pending longer than 10 min, in namespaces labeled `env=staging`. Max 5 restarts per workload per hour, then it stops and tells you. It may not touch StatefulSets or anything labeled `critical`.
> **Would act:** `api-7f9` crash-looping 14 min in `staging-payments`.
> **Barely qualifies:** a pod pending 11 min because the node pool is full. Restarting won't help, so it asks instead.
> **Would not act:** `db-0`, a StatefulSet.

**Caps:** every scale rule has a floor and a ceiling (never below 1, at most +N replicas or 2× current, whichever is lower). Every restart rule has a rate limit. Hitting a cap is a problem alert, not a silent stop.

**Dry run:** a new rule runs for a trial period in "would have done" mode. Its proposed actions show up in the digest, and nothing executes until its author turns it live.

**Rules come from approvals.** After the same Tier 2 pattern is approved repeatedly, Tidewater proposes a rule with the cap filled in. This reduces prompts on the safe side, instead of asking engineers to tap faster.

## Tier 2: a card that is worth reading

> **Tidewater wants to change PROD**
> **Do:** scale `checkout-api` from 6 → 10 replicas
> **Where:** cluster `prod-us-east`, namespace `checkout`
> **Why:** p95 latency over threshold for 12 min (link)
> **Affects:** 1 Deployment. Enough node capacity: yes.
> **Undo:** scale back to 6 (one tap in the activity record)
> **Requested by:** @dana (on-call)
> [Approve this exact change] [Deny] [Deny and tell Tidewater why]

Design rules for the card:
- **Computed facts, not model prose.** Blast radius comes from a server-side `--dry-run=server` and a count of affected objects. The model's own explanation is shown but labeled as such.
- **Environment is unmissable:** a colored banner and the word PROD, never only in small text.
- **The button names the action.** There is no bare "Approve".
- **The approval is bound to the exact parsed call.** If the command changes by one character after approval, it needs a new approval.
- **Approvals expire** (starting value: 15 min).
- **Only the on-call or the requesting engineer sees it,** not a channel of 40 people who each assume someone else will read it.

## Tier 3: the namespace-deletion case

> **DESTRUCTIVE: cannot be undone**
> Delete namespace `staging-payments`
> This removes **23 objects**, including **4 PersistentVolumeClaims (212 GiB)**, **2 Secrets**, and a running StatefulSet.
> Last backup of those volumes: *none found*.
> To continue, type the namespace name: `______`
> A second engineer must also approve. Execution happens 5 minutes after both confirm. [Cancel during hold]

- **Typing the target name** forces the approver to read it.
- **A different person** from the requester must also approve.
- **A hold** gives anyone a cancel window.
- **A separate Slack channel or DM thread with a different look,** so it never appears in the same stream as routine prompts.
- **It can't be batched or pre-approved** by a standing rule or a "don't ask again" setting.
- **Optional, and a policy call for your team:** Tidewater doesn't offer namespace deletion at all and sends a ticket to a human. It's rarely a "routine fix."

## Keeping prompts readable

- **Interrupt budget.** Tier 2 and 3 are the only things that ping. If one person gets more than a set number per day (start low, tune), that's a signal to create or fix a rule. Don't make the prompts more frequent or easier to skim.
- **Message kinds, each with its own off control:**
  - **Problem** (a cap was hit, an action failed): immediate.
  - **Approval needed** (Tier 2/3): immediate.
  - **Completion** (Tier 0 and 1 actions): one digest on a schedule the team picks.
  - **Rule suggestion:** rare.
  - **Check-in** (proof of life): adjustable.
- **Digest shows items, not totals.** The odd ones come first (a cap nearly hit, a retry, an action with surprising scope). Each item has its own Undo.

## Mistakes, undo, stop

- **Undo:** every Tier 1 and 2 action has an inverse recorded (previous replica count, previous revision). State what undo can't reach, such as logs already read or data lost with a deleted object.
- **On every digest item:** "Not this one" (skip for a duration or a namespace) and "Never for this kind", which shows the resulting rule before saving.
- **Skipped list:** things Tidewater declined or asked about, lowest confidence first, so missed fixes don't go unnoticed.
- **Status home** (a pinned Slack message or a `/tidewater` command): running or paused, last action and when, active rules against their caps, pending approvals. **Pause all** sits one tap from there, and the paused state shows in the channel topic.
- **Kill switch:** revoking the service account's write permissions cuts Tidewater off at the cluster level, which is stronger than the Slack-side pause.

## Rollout (not guesswork)

1. **Shadow mode.** Run the classifier over your existing command log (you have weeks of approved commands). Look at the tier distribution, and look at which commands land in Tier 2 and 3 that you didn't expect. Adjust before anything changes for users.
2. **Tier 3 first.** Ship the hard gate and the read-it card now. These are pure safety improvements, and they fix the incident that already happened.
3. **Then Tier 0 and 1,** with rules in dry-run first.
4. **Measure reading, not approvals.** Track time-to-approve per tier (a Tier 3 approved in 2 seconds means the design is failing), the denial rate, and how often undo is used. Don't count "prompts reduced" as success by itself.
5. **Widen scope only by proposal.** Tidewater may suggest a new rule after a visible record of clean runs, but it never grants itself wider reach. Nothing that deletes can be widened by a rule.

## Open questions that would change the design

- Does Tidewater's service account have more permissions than its commands need? Narrowing RBAC (no namespace delete at all, unless a break-glass role is used) is the strongest backstop, and it works even if the classifier has a bug.
- Is there a reliable staging vs. prod signal (a label, a cluster name)? Tier assignment depends on it.
- Who is on-call, and is there always a second engineer available for Tier 3?
