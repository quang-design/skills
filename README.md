# Skills

[![skills.sh](https://skills.sh/b/quang-design/skills)](https://skills.sh/quang-design/skills)

A small collection of agent skills I use for planning and coordinating engineering work.

The goal is simple: give agents a clearer process before they touch code.

Each skill should be easy to read, easy to change, and useful in real repositories.

## Install

```bash
npx skills@latest add quang-design/skills
```

Then choose the skills you want to install for your agent.

## Available skills

### codex-swarm

[`codex-swarm`](./skills/codex-swarm/SKILL.md) helps turn a messy set of work into an approved execution plan.

It can take GitHub issues, bug lists, notes, or a brain dump and turn them into:

- grouped work
- parallel lanes
- clear ownership
- dependency order
- proof plans
- PR follow-up
- blocker tracking

It does not start implementation first. It reads the work, proposes a plan, asks for approval, then coordinates the threads.

Use it when you want to split a larger batch of work across multiple Codex threads or worktrees without losing track of what each thread owns.

Example prompts:

```text
/codex-swarm all GitHub issues assigned to me in this repo
/codex-swarm this brain dump
/codex-swarm these bugs into parallel PRs
/codex-swarm the open issues, collapse small ones, split large ones
```

## Repo structure

```text
skills/
  codex-swarm/
    SKILL.md
    agents/
      openai.yaml
    references/
      model-routing.md
      workflow.md
    scripts/
      validate_plan.py
```

## Skill structure

Each skill lives in `skills/<skill-name>/`.

The main file is `SKILL.md`:

```md
---
name: codex-swarm
description: Standalone workflow for turning issue dumps into approved parallel execution plans.
license: MIT
metadata:
  author: quang-design
  version: "1.0.0"
---
```

Supporting files can sit next to it:

- `references/` for longer guides
- `scripts/` for validation helpers
- `agents/` for agent-specific metadata

## Publishing

This repo is meant to work with skills.sh.

After the GitHub repo is public, check the install with:

```bash
npx skills@latest add quang-design/skills
```

Repo page:

```text
https://skills.sh/quang-design/skills
```

## License

MIT. See [`LICENSE`](./LICENSE).
