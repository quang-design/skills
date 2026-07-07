---
name: fewest-degrees-of-freedom
description: Human-and-AI workflow for solving a big problem by attacking its most constrained subproblem first, then locking decisions one atomic step at a time until the whole problem is solved. Based on Christopher Alexander's constraint-first solving. Use when a problem feels too big to start, when analyzing complex systems, prioritizing decisions, planning projects, or facing "where do I start?" paralysis. Triggers on requests to break down a hard problem, decide what to solve first, or work through something step by step with a human.
license: MIT
metadata:
  author: quang-design
  version: "1.0.0"
---

# Fewest Degrees of Freedom

Solve the most constrained subproblem first, together. Lock one atomic decision at a
time, let it cascade, then move to the next-most-constrained. Unconstrained decisions
made early quietly block the only valid solutions for constrained decisions later, so
the big problem is solved from its smallest, tightest piece outward — never all at once.

This is a **shared** workflow between a human and an AI. The AI maps the terrain and
proposes; the human decides and confirms. Neither races ahead of the other.

## Principles (the thought behind this skill)

Keep these as the requirements every run must honor:

- **Fewest degrees of freedom first.** Start where the fewest valid options exist. The
  tightest constraint has the least room to be wrong.
- **Atomic, one at a time.** Solve exactly one subproblem per step. Never batch. Each
  locked piece is small, complete, and verifiable on its own.
- **Smallest to biggest.** Build from the smallest constrained piece outward until the
  full problem is solved. The big picture emerges from settled atoms, not the reverse.
- **Human and AI together.** Every lock is a shared decision. The AI never locks a piece
  the human has not confirmed, and the human is never asked to decide without a clear map.
- **A beautiful working experience.** Calm, legible, unhurried. Always show where we are,
  what is settled, and the single next question. No walls of text, no premature detail,
  no dead ends.

## The Loop

1. **Decompose** — With the human, list every subproblem/decision in the system. Keep it flat and honest; don't solve yet.
2. **Count degrees of freedom** — For each: how many valid solutions genuinely exist? Fewer = more constrained.
3. **Rank** — Sort ascending by degrees of freedom (most constrained first). Show the ranked map to the human.
4. **Focus on one** — Take the single most-constrained open subproblem. This is the only thing in play right now.
5. **Solve together** — AI proposes options + a recommendation with reasoning; human chooses. Confirm before locking.
6. **Lock atomically** — Record the decision. It is now settled and constrains what follows.
7. **Cascade** — Re-evaluate the remaining subproblems: the lock just removed degrees of freedom from some of them. Re-rank.
8. **Repeat** — Return to step 4 with the new most-constrained piece. Continue until every atom is locked and the full problem stands solved.

## Collaboration protocol

The loop only feels beautiful if the handoffs are clean. Each step:

- **Show the map first.** Before asking anything, display the current state so the human
  has full context in one glance (see template). One question at a time.
- **Propose, don't impose.** For the focused subproblem, give the real options, the
  degrees of freedom of each, a recommendation, and the reason. Make the easy "yes" easy.
- **Confirm before locking.** Never treat a proposal as accepted. A lock happens only on
  an explicit human "go".
- **Prefer reversible.** When a decision is genuinely reversible and cheap, say so — it
  lowers the stakes of the step and keeps momentum.
- **Surface cascades out loud.** After each lock, name what it just constrained. This is
  the payoff of the method; make it visible so the human feels the problem shrinking.
- **Stop and flag** if a lock would invalidate an earlier one — reopen that atom instead
  of forcing forward.

## Degrees of Freedom Indicators

| Low DoF — solve first | High DoF — solve later |
|---|---|
| Physical / hard constraints | Aesthetic preferences |
| External dependencies | Internal organization |
| Regulatory / legal requirements | Naming conventions |
| Integration points / contracts | Color choices |
| Load-bearing decisions | Decorative elements |
| Things that *must* go somewhere | Things that *could* go anywhere |

## Working template

Use this shared view. Update it after every lock so the human always sees the whole state.

```
Problem: [the big challenge, one line]

Map (ranked, most constrained first):
  [ ] 1. [subproblem] — DoF: [1-2 | 3-5 | many] — Why constrained: [source]
  [ ] 2. [subproblem] — DoF: [estimate] — Why: [source]
  ...

Locked so far:
  [x] [subproblem] → [decision] → constrained: [what this removed]

--- Focus (one atom) ---
Now solving: [most constrained open subproblem] — DoF: [n]
Options:
  A) [option] — trade-off: [...]
  B) [option] — trade-off: [...]
Recommendation: [A/B] because [reason].

> Awaiting your confirmation to lock.
```

## Quick examples

- **Kitchen design**: Windows (1–2 spots for good light) → Table (must sit in the light) → Stove (anywhere with vent access).
- **API design**: Auth mechanism (security narrows options) → Data model (business logic constrains) → Endpoint naming (flexible).
- **Startup priorities**: Regulatory compliance (binary, external) → Core tech feasibility (physics/math constrain) → Go-to-market (many valid paths).
- **UI layout**: Navigation (users expect patterns) → Primary action placement (Fitts's law) → Secondary elements (flexible).

## Anti-patterns

You're drifting from the method when:

- Starting with the "fun" or high-DoF parts.
- Optimizing aesthetics before structure is settled.
- Locking several subproblems in one step instead of one atom at a time.
- Making a reversible decision permanent too early, or a permanent one casually.
- Proposing and locking in the same breath, without the human's explicit go.
- Discovering a late constraint that invalidates already-locked work.
- Hiding the map — asking the human to decide without showing where we are.

## When to use

- System architecture and design trade-off decisions.
- Project planning and sequencing.
- Debugging priority (most constrained cause first).
- Resource allocation.
- Any "this is too big / where do I even start?" paralysis, solved with a human in the loop.
