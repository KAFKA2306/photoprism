# Frontend Guidelines

The root `AGENTS.md` defines the product boundary. This file only adds `frontend/` specifics.

## Keep

- Vue 3 + Vuetify 3 and the existing Options API.
- Existing reactive singletons in `src/common/` and `src/app/`; do not add Vuex or Pinia.
- Existing model methods and shared components before raw `$api` calls or new abstractions.
- Web/PWA as the canonical client. Do not add commercial Portal/Plus/Pro overlay behavior to this personal fork.

Do not introduce TypeScript, Composition API, `<script setup>`, or a new dependency unless it replaces existing code and the reduction is measured.

Until translation assets are safely reduced, keep user-visible strings on the existing `$gettext` path rather than creating a second localization mechanism.

## Verify

Use repository-native entry points:

```bash
make fmt-js
make lint-js
make test-js
make build-js
```

Run the narrowest relevant Vitest test first. New or changed behavior needs focused coverage. Treat build/test output as evidence; prose is not a PASS.
