# Model Routing Reference

Use this reference before assigning model overrides to codex-swarm lanes. Omit overrides when the current thread model is already appropriate.

This guidance is based on current official OpenAI model guidance checked on 2026-06-30: `gpt-5.5` is the latest model, is a strong fit for complex coding and tool-heavy agent workflows, and defaults to `medium` reasoning effort. The available Codex thread models in this session are `gpt-5.5`, `gpt-5.4`, `gpt-5.4-mini`, and `gpt-5.3-codex-spark`; do not route to unavailable public API models from inside Codex threads.

## Routing Table

| Lane type | Recommended model | Reasoning | Why |
| --- | --- | --- | --- |
| Mechanical tiny fix, formatting, copy update, obvious test expectation update | `gpt-5.3-codex-spark` | `low` | Fastest reasonable option when the change is local, low-risk, and has an obvious proof. |
| Read-only issue inventory, label clustering, duplicate detection, straightforward GitHub issue summarization | `gpt-5.4-mini` | `low` | Cost-efficient for broad triage where no repo edits happen. |
| Normal app bug, ordinary feature slice, focused test repair, small UI fix | `gpt-5.4` | `medium` | Good everyday coding default when the lane needs repo navigation, implementation, and verification. |
| PR follow-through, review comment fixes, flaky CI classification | `gpt-5.4` | `medium` | Most PR acceptance work is debugging and evidence classification; escalate only when evidence shows architectural risk. |
| Cross-repo workflow, auth/access control, data integrity, migrations, concurrency, security-sensitive work, ambiguous architecture, long-running tool-heavy lane | `gpt-5.5` | `medium` or `high` | Latest and strongest fit for complex coding, tool-heavy agents, and production workflows where wrong assumptions are expensive. |
| Hard incident, multi-service dependency chain, difficult migration, or lane that cheaper models already failed | `gpt-5.5` | `high` or `xhigh` | Use higher effort only when the extra latency/cost is justified by risk or prior failed attempts. |

## Reasoning Effort

- Start at `medium` for `gpt-5.5` unless the lane is clearly simple or latency-sensitive.
- Use `low` for cheap triage, mechanical edits, and fast read-only extraction.
- Use `medium` for normal coding lanes and most PR follow-through.
- Use `high` for ambiguous bugs, cross-repo contracts, migrations, auth, data integrity, security-sensitive work, or long dependency chains.
- Use `xhigh` only for the hardest asynchronous agentic lanes or eval-style investigations where quality matters more than latency/cost.
- Avoid `none` for codex-swarm lanes unless the task is a trivial classification or retrieval step with no planning, tools, or chained decisions.

Higher reasoning effort is not automatically better. If the lane has unclear stopping rules, weak ownership boundaries, or open-ended tool access, increasing effort can waste time. Tighten the lane prompt first; raise effort only when risk or evidence justifies it.

## Prompting For Routed Lanes

For `gpt-5.5` lanes, write outcome-first prompts:

- expected outcome
- success criteria
- allowed side effects
- ownership boundary
- required evidence
- stop conditions
- output shape

Avoid over-prescribing step-by-step implementation unless the exact path matters. For tool-heavy lanes, make tool side effects and retry safety explicit in the worker prompt.

## Escalation And Downgrade Rules

Escalate to `gpt-5.5` when:

- the lane touches auth, permissions, data integrity, migrations, security, or concurrency
- multiple repos or services must agree on a contract
- a cheaper lane returns a plausible but weak plan
- the lane repeatedly fails because it missed architecture or source-evidence constraints

Downgrade to `gpt-5.4-mini` or `gpt-5.3-codex-spark` when:

- the work is read-only triage
- the proof is deterministic and local
- the file ownership is narrow
- failure would be cheap to detect and retry

## Memory Learning

Before routing, search memory for the repo, task type, and prior failure pattern. Use memory to identify:

- models that previously handled the repo well or poorly
- commands and gates that usually prove closure
- known flaky checks or environment blockers
- prior decisions about PR shape, branch policy, or review standards

After the workflow, recommend memory updates when there is durable routing evidence, such as:

- a cheaper model repeatedly closed a class of issue cleanly
- a stronger model was needed because cheaper lanes missed architecture or data constraints
- a repo has a reliable verification command or recurring blocker

Do not write memory unless the user explicitly asks.

## Source Notes

- Official OpenAI `latest-model.md`, fetched 2026-06-30, names `gpt-5.5` as the latest model and says it is a strong fit for complex coding, tool-heavy agents, long-context retrieval, and production workflows.
- The same guide recommends `medium` as the balanced default reasoning effort, `low` for efficient reasoning, and `high`/`xhigh` only when the extra latency and cost are justified.
