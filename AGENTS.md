# KAFKA2306 Photo Memories — Agent Guide

**Updated:** 2026-08-16

## Authority

Current user instruction > current official primary sources and upstream > current repository/runtime state > this file > historical prose.

Re-check mutable facts before acting. Subtree `AGENTS.md` files add path-specific detail but must not override this product boundary.

## Product Boundary

This fork is a personal Japanese photo-memory archive built on PhotoPrism. Preserve photo/video indexing, search, albums, people, places, sharing, and monthly memories with `draft / ready / public` states. `personal/journal/memory-month.json` is the user-facing canonical memory boundary; Web/PWA is the canonical client.

Do not re-introduce billing, membership, sponsor, upgrade, donation, sales, team, Portal, or cluster-management product surfaces unless explicitly requested. Android may only be a thin wrapper. Do not duplicate AI, import, or publishing logic outside the canonical boundary.

Preserve licenses, notices, attribution, and upstream-compatible Go/Vue structure unless removal is verified safe.

## Change Discipline

- Before editing a subtree, read its nearest `AGENTS.md`.
- Prefer deletion and reuse over addition.
- One capability gets one canonical implementation and one validation path.
- The existing `Makefile` is the command surface. Do not add Taskfile, extra linters, build orchestrators, or parallel scripts unless they replace an existing owner and reduce measured maintenance.
- Fail fast: do not add broad catches, retries, or fallback defaults that hide unexpected failures. Put retry/restart policy in infrastructure where possible.
- Keep diffs focused. Never commit secrets, private photo paths, face exports, credentials, keystores, or originals.

## Verification

`PASS` requires current execution evidence. Documentation, old runs, or implementation prose alone remain `UNVERIFIED`.

Use the smallest focused check first, then the applicable broader gate before merge.

```bash
python -m unittest discover -s personal/journal/tests -v
```

For the application, use existing Makefile targets such as `make test-short`, `make test-js`, `make build-go`, `make build-js`, and the relevant lint target; `make help` is the command index.

`.github/workflows/codeql-analysis.yml` is the single hosted workflow. It runs on trusted `develop` / `release` pushes, weekly schedule, or manual dispatch; PR synchronization intentionally does not create hosted runs. An `action_required` run with zero jobs is workflow-state evidence, not evidence of a CodeQL vulnerability finding.

If any required gate is unexecuted or failing, keep the PR Draft/UNVERIFIED.

## Tracking

GitHub Issues are the current task ledger. `docs/ja-JP/ROADMAP.md` is direction, not current task state. Keep PR descriptions synchronized with the current repository and evidence.
