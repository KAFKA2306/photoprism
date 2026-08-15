# KAFKA2306 Photo Memories — Agent Guide

**Last Updated:** 2026-08-15

## Authority

Use this order when facts conflict:

1. Current user instruction
2. Current official primary sources and upstream PhotoPrism source/docs
3. Current GitHub repository, PR, Issue, and production state
4. This file
5. Historical conversation, old runs, comments, and memory

Historical state is evidence, not ground truth. Re-check it before acting.

## Product Goal

This repository is a personal Japanese photo-memory archive built on PhotoPrism. PhotoPrism remains the indexing / metadata engine; the user-facing canonical boundary is `memory-month.json` under `personal/journal/`.

Keep the product centered on:

- photo and video indexing, search, albums, people, places, and sharing
- monthly memories with `draft / ready / public` publication states
- Japanese-only product UI for this fork
- Google Photos user-selected import boundaries
- Web/PWA as the canonical client; Android is only a thin wrapper when needed

Do not re-introduce billing, membership, sponsor, upgrade, donation, sales, or team/commercial product paths unless explicitly requested.

## Preserve

- `LICENSE`, notices, copyright, and upstream attribution
- PhotoPrism photo/index/search/metadata behavior required by the personal product
- face and place clustering that belongs to photo functionality
- upstream-compatible Go / Vue build structure unless removing it is verified safe

Upstream: https://github.com/photoprism/photoprism
Developer docs: https://docs.photoprism.app/developer-guide/

## Canonical Work Tracking

GitHub Issues are enabled and are the task ledger. `docs/ja-JP/ROADMAP.md` describes product direction; it is not a substitute for current Issue state.

For implementation work, inspect the current PR/Issue and repository state before trusting their older descriptions. Keep PR bodies updated when blockers have already been removed.

## Verification

Prefer the smallest focused check that proves the change, then run the broader gate before merge.

Personal journal:

```bash
python -m unittest discover -s personal/journal/tests -v
```

Go / frontend entry points remain the repository-native commands documented by the Makefile and subtree `AGENTS.md` files. For changes that affect the application, use the relevant focused tests, then the applicable build/lint/test gates before merge.

Hosted workflow policy:

- `.github/workflows/codeql-analysis.yml` is the single hosted quality workflow.
- It runs on trusted `develop` / `release` pushes, weekly schedule, or manual dispatch.
- It verifies the personal journal once and runs CodeQL for Go and JavaScript/TypeScript.
- Pull-request synchronization intentionally does not create hosted runs. Pre-merge verification must therefore be reported from focused/local checks or an explicit manual run.
- Historical `action_required` runs with zero jobs are workflow-state records, not evidence that CodeQL found a vulnerability.

## Change Discipline

- Prefer deletion and reuse over adding parallel systems.
- One capability should have one canonical implementation and one canonical validation path.
- Do not add Ruff, Biome, Oxlint, Nx, Turborepo, prek, or similar tooling merely because it is modern. Add a tool only when it replaces an existing owner or closes a measured gap without duplicating the native PhotoPrism toolchain.
- Do not create Android, AI, import, or publishing logic that duplicates the Web / `memory-month.json` boundary.
- Never commit secrets, private photo paths, face metadata exports, credentials, keystores, or private originals.
- Keep unrelated upstream cleanup out of a functional change unless it directly reduces the maintained surface and is independently verifiable.

## Completion

A change is complete only when the current source, current task state, and verification evidence agree. Do not mark a PR ready or merge solely because an old checklist says the work is done.
