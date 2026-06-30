---
name: codex-swarm
description: Standalone workflow for turning GitHub issues, issue searches, bug lists, stakeholder notes, or messy brain dumps into an approved dependency-aware execution plan, then coordinating parallel Codex threads/worktrees through implementation, verification, commit, push, PR creation, monitoring, and final closure. Use when the user says /codex-swarm, asks Codex to swarm all GitHub issues, wants parallel issue execution, wants one brain dump split into multiple PRs, or needs simple issues collapsed and large issues broken into chained work.
license: MIT
metadata:
  author: quang-design
  version: "1.0.0"
---

# Codex Swarm

Use this skill as a standalone coordinator. It turns a messy set of issues into a reviewed execution graph, asks for human approval, then starts and monitors work threads until each lane is closed, blocked, or returned for a decision.

Natural prompts:

- `/codex-swarm all GitHub issues assigned to me in this repo`
- `/codex-swarm this brain dump`
- `/codex-swarm these bugs into parallel PRs`
- `/codex-swarm the open issues, collapse small ones, split large ones`

## Rules

- Keep intake read-only until the human approves the execution plan.
- Inspect primary artifacts before planning: GitHub issues, PRs, comments, logs, docs, Slack, Sentry, repo files, failing checks, or local notes.
- Use memory before planning and again when blocked. Prior repo evidence is useful, but verify drift-prone facts live when cheap.
- Use subagents or Codex threads for bounded subtasks when available.
- Give every spawned thread a concrete `/goal`, ownership boundary, expected output, proof plan, dependency inputs, model choice, and stop condition.
- Do not start implementation for product decisions, missing credentials, destructive operations, unclear repo ownership, or ambiguous priority. Put those in the approval plan.
- Collapse issues when they share files, proofs, risk, or review story.
- Split issues when they have disjoint ownership, different repos, independent proofs, or dependency outputs that should become separate review units.
- Start dependent threads only after prerequisite outputs exist: PR URL, branch, commit, migration, artifact, contract, or explicit blocker.
- Prefer one PR per coherent review story. Use multiple PRs when parallelism, ownership, review risk, or dependency boundaries justify it.
- Do not call the swarm done because threads were spawned. Done means each approved lane is closed, accepted in PR when applicable, or blocked with a concrete reason.

## Intake

1. Identify source scope:
   - explicit brain dump
   - GitHub issue query
   - repo backlog
   - PR comments/check failures
   - stakeholder thread or doc
2. Inspect the real artifacts. If the user says "all GitHub issues", search/read the actual issue list before planning.
3. Normalize each candidate:
   - `id`
   - `title`
   - `source`
   - `repo_or_workspace`
   - `problem`
   - `evidence`
   - `likely_owner_files`
   - `risk`
   - `unknowns`
   - `dependencies`
   - `candidate_proof`
4. Classify each item:
   - `tiny-fix`: obvious, local, low risk
   - `normal`: needs shaping and focused verification
   - `research-first`: needs evidence before implementation
   - `product-or-architecture`: needs durable requirement decisions
   - `blocked`: needs human/external input
5. Read `references/workflow.md` before finalizing a plan with more than three items or any dependency.
6. Read `references/model-routing.md` before assigning model overrides.

## Approval Plan

Produce this before starting implementation threads:

```markdown
## Proposed Codex Swarm

Objective:
Source artifacts inspected:

### Groups

| Group | Items | Why grouped | Repo/worktree | PR shape |
| ----- | ----- | ----------- | ------------- | -------- |

### Parallel Lanes

| Lane | Thread title | Model | Owns | Depends on | Proof plan | Expected output |
| ---- | ------------ | ----- | ---- | ---------- | ---------- | --------------- |

### Blocked / Needs Human

| Item | Question or permission needed | Why it blocks |
| ---- | ----------------------------- | ------------- |

### Execution Policy

- Commit policy:
- Push/PR policy:
- Check cadence:
- Merge/conflict policy:
- Stop conditions:
```

Ask for approval after the plan. Do not spawn execution threads before approval. When the approval plan names a concrete model for a lane, approval of that plan is explicit user approval to pass that model to the thread-creation tool for that lane. If the lane model is listed as `current/default` or the plan omits a concrete model, omit the model field so the host uses its configured default.

## Execution State

After approval, maintain a canonical JSON execution state before spawning threads. Validate it with:

```bash
scripts/validate_plan.py <plan.json>
```

Use this shape:

```json
{
  "objective": "Close the approved issue batch",
  "approved": true,
  "lanes": [
    {
      "id": "lane-auth-guard",
      "title": "Fix server-side admin route protection",
      "model": "gpt-5.5",
      "workflow_path": "normal",
      "owns": ["intake-fe admin route SSR/auth boundary"],
      "depends_on": [],
      "expected_output": "PR URL with verified auth guard fix",
      "proofs": ["focused auth route proof", "repo local gate"]
    }
  ]
}
```

Update the state when dependency edges, ownership, models, expected outputs, proofs, branches, PRs, or blockers change.

## Worker Thread Prompt

For each approved lane, create the thread with the lane model from the approved execution state when it is concrete and supported by the thread tool. Omit the model field only when the approved lane model is `current/default`, omitted, unsupported by the destination host, or the thread tool explicitly rejects it. Then send a prompt shaped like this:

```text
/goal <one-sentence measurable outcome>

Use the standalone codex-swarm lane workflow.

Context:
- Parent objective:
- Lane ID:
- Source artifacts:
- Repo/worktree:
- Ownership boundary:
- Dependencies satisfied:
- Items in scope:
- Items explicitly out of scope:
- Expected PR shape:
- Required proofs:
- Model routing reason:

Workflow:
1. Inspect live repo state, local instructions, branch/worktree, and unrelated changes.
2. Restate the lane's requirement, boundaries, risks, and proof plan.
3. Implement the smallest coherent change for this lane.
4. Verify locally with focused proofs and relevant repo gates.
5. Commit after verification when repo files changed and review is expected.
6. Push and create/update a PR when the lane requires review.
7. Monitor or report PR checks/review state as assigned.
8. Return Closed, Not closed, or Blocked with PR URL, commit, proofs, and residual risk.
```

## Monitoring Loop

Maintain a coordinator worklog:

```text
Parent objective:
Approved plan version:
Plan JSON:
Lane states:
Dependencies:
Threads:
Branches:
PRs:
Proofs:
Blocked decisions:
Next monitor time:
```

At each monitor pass:

1. Read thread status and latest outputs.
2. Update lane state: `planned`, `running`, `blocked`, `needs-review`, `pr-open`, `closed`, or `failed`.
3. If a lane closes, start dependent lanes with the closed lane's concrete outputs.
4. If a lane discovers scope drift, pause implementation and update the approval plan before continuing.
5. If two lanes conflict on files/contracts, pause the later lane and reconcile through a dependency edge.
6. If a lane stalls on missing permission, credentials, destructive action, or product ambiguity, mark it blocked and keep other lanes moving.
7. Continue until every approved lane is closed or blocked with a specific reason.

## Model Routing

Default to the current model unless a lane clearly benefits from a cheaper or stronger model. Use `references/model-routing.md` to pick overrides. Record the concrete model and reason in the approval plan, execution state, and worker prompt. After the user approves the plan, pass the approved concrete model to `create_thread` for that lane when the tool supports it; this avoids silently falling back to the host default after a model-specific plan was approved.

## Final Output

```text
Codex swarm status: Closed / Not closed / Blocked
Plan approved:
Threads:
PRs:
Commits:
Lanes closed:
Lanes blocked:
Verification:
Review/CI state:
Dependency chain:
Human follow-up needed:
Memory notes to consider adding:
```
