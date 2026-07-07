---
name: fewest-degrees-of-freedom
description: Problem decomposition framework based on Christopher Alexander's constraint-first solving. The AI decomposes the problem and ranks subproblems by degrees of freedom, then starts with the human on the most constrained one and works through them together. Use when analyzing complex problems, prioritizing decisions, designing systems, planning projects, or any situation requiring sequenced problem-solving. Triggers on requests to break down problems, prioritize decisions, find starting points, or determine what to solve first.
license: MIT
metadata:
  author: quang-design
  version: "1.0.0"
---

# Fewest Degrees of Freedom

Solve the most constrained subproblem first. Unconstrained decisions made early often block the only valid solutions for constrained decisions later.

The AI decomposes the problem and ranks the subproblems by degrees of freedom, then finds the fewest-degrees-of-freedom subproblem to start with the human and works through them together, one at a time.

## Core Algorithm

1. **Decompose** — List all subproblems/decisions in the system
2. **Count degrees of freedom** — For each: how many valid positions/solutions exist?
3. **Rank** — Sort ascending by degrees of freedom (most constrained first)
4. **Solve** — Start with the human on the most constrained subproblem, lock it in, then re-evaluate remaining
5. **Cascade** — Each locked decision reduces degrees of freedom for others

## Degrees of Freedom Indicators

| Low (solve first) | High (solve later) |
|---|---|
| Physical/hard constraints | Aesthetic preferences |
| External dependencies | Internal organization |
| Regulatory/legal requirements | Naming conventions |
| Integration points | Color choices |
| Load-bearing decisions | Decorative elements |
| Things that "must" go somewhere | Things that "could" go anywhere |

## Application Pattern

```
Problem: [state the design/system challenge]

Subproblems identified:
1. [subproblem] — DoF: [1-2 | 3-5 | many] — Why: [constraint source]
2. [subproblem] — DoF: [estimate] — Why: [constraint source]
...

Solve order: [ranked list, most constrained first]

Working through:
1. [most constrained] → Decision: [choice] → New constraints created: [list]
2. [next most constrained, re-evaluated] → ...
```

## Quick Examples

**Kitchen design**: Windows (1-2 spots for good light) → Table (must be in light) → Stove (anywhere with vent access)

**API design**: Auth mechanism (security requirements narrow options) → Data model (business logic constrains) → Endpoint naming (flexible)

**Startup priorities**: Regulatory compliance (binary, external) → Core tech feasibility (physics/math constrain) → Go-to-market (many valid approaches)

**UI layout**: Navigation (users expect patterns) → Primary action placement (Fitts's law) → Secondary elements (flexible)

## Anti-Pattern Recognition

You're doing it wrong when:
- Starting with the "fun" parts
- Optimizing aesthetics before structure
- Making reversible decisions permanent too early
- Spending equal time on all subproblems
- Discovering a constraint invalidates prior work

## When to Use

- System architecture decisions
- Project planning and sequencing
- Design trade-off analysis
- Debugging priority (constrained causes first)
- Resource allocation
- Any "where do I start?" paralysis
