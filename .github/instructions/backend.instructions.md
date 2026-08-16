---
applyTo: "internal/**,pkg/**,cmd/**"
---

Follow root `AGENTS.md` and the nearest subtree `AGENTS.md`.

Use existing Go entry points (`make fmt-go`, `make lint-go`, focused `go test`, then the applicable build/test gate). Keep `pkg/*` independent of `internal/*`, keep handlers thin, and reuse existing helpers before adding abstractions. Do not restore commercial product paths.
