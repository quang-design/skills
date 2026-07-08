# Workflow Reference

Use this reference when the issue set has more than three items, multiple repos, dependency chains, or likely parallel threads.

## Grouping Heuristics

Collapse items when:

- They touch the same small file set.
- They share one failing proof or one user-visible flow.
- Reviewing them separately would obscure the behavior change.
- One item is only cleanup required by another item.

Split items when:

- They touch disjoint modules or repos.
- They can be verified independently.
- They require different credentials or external systems.
- One item is risky and should not block low-risk fixes.
- A prerequisite produces a contract, migration, API, or artifact another item needs.

Avoid parallelizing:

- Shared migrations without a sequencing plan.
- Broad refactors with overlapping file ownership.
- Product decisions disguised as implementation.
- Work that requires a single test fixture or live resource that cannot tolerate concurrent mutation.

## Dependency Graph

Represent dependencies as concrete outputs, not vague relationships.

Good:

- `B depends on A PR URL and generated API client commit`
- `C depends on migration branch pushed and local schema proof green`

Bad:

- `B depends on backend`
- `C after cleanup`

If dependency outputs are uncertain, make the prerequisite a research or shaping lane before implementation lanes start.

## Approval Threshold

Human approval is required before:

- Spawning new Codex threads for implementation.
- Creating multiple PRs.
- Touching production, billing, secrets, destructive data, or permissions.
- Choosing between product behaviors.
- Changing the parent plan's review shape after approval.

Human approval is not required for:

- Read-only artifact inspection.
- Narrow local verification.
- Starting dependent lanes already approved once prerequisites close exactly as planned.
- Re-routing a lane to `v-change` when the lane discovered scoped drift, as long as no new implementation starts before approval of the changed plan.

## Lane Sizing

Prefer lanes that can close in one focused thread. A lane is too large if its prompt needs multiple unrelated ownership areas, multiple PR stories, or unrelated verification suites. A lane is too small if it creates review overhead for a one-line fix that is naturally verified with a neighboring change.

## Coordinator Duties

The parent coordinator owns:

- Intake normalization.
- Approval plan.
- First-class Codex thread creation in separate worktrees for implementation lanes.
- Thread titles, thread ids, and worktree tracking.
- Dependency scheduling.
- Monitoring and status synthesis.
- Conflict detection across lanes.
- Final summary and memory-learning recommendations.

Lane threads own:

- Verifying they are running in their assigned worker worktree, not the coordinator checkout.
- Repo inspection.
- Slice shaping.
- Implementation.
- Local verification.
- Commit/push/PR work assigned to that lane.
- Honest closure report.

## Failure Handling

If a lane fails, classify it:

- `implementation`: code or tests failed because of branch work.
- `baseline`: existing failure unrelated to branch.
- `environment`: local toolchain, dependency install, network, or service unavailable.
- `permission`: missing auth, credentials, or human approval.
- `scope`: requirements or interfaces changed.
- `conflict`: another lane changed overlapping files/contracts.

Only retry when the classification implies a concrete next action. Do not burn cycles on repeated identical failures.
