# KAFKA2306 Photo Memories — Code Map

**Updated:** 2026-08-18

このファイルは、このforkで現在使う構造だけを示します。上流PhotoPrismの全edition、配布、商用運用を網羅する文書ではありません。

## 正準入口

- `README.md` — 個人用プロダクト境界と利用方法
- `AGENTS.md` — 変更規則と検証規則
- `Makefile` — build / test / lint / journal / local environment のコマンド入口
- `compose.yaml` — ローカルDocker環境の唯一のCompose設定
- `.env.example` — ローカル環境で設定する値
- `LICENSE`, `NOTICE` — 上流由来の法的表示

## 個人用の成果物

- `personal/journal/build.py` — 月次日記の静的HTML生成
- `personal/journal/schema.json` — 月次データのschema
- `personal/journal/tests/` — 月次日記の検証
- `personal/journal/README.md` — 月次データと公開状態の説明

月次日記は `draft / ready / public` を区別し、公開成果物は `public` だけを対象にします。

## Backend

- `cmd/photoprism/` — CLI entry point
- `internal/commands/` — CLI command orchestration
- `internal/server/` — HTTP serverとroutes
- `internal/api/` — HTTP API handlers
- `internal/config/` — configurationとdatabase initialization
- `internal/entity/` — GORM models、queries、migrations
- `internal/photoprism/` — indexing、import、faces、media処理の中心
- `internal/ai/` — computer vision / AI integration
- `internal/workers/` — background workers
- `internal/auth/` — sessions、ACL、認証実装
- `internal/service/` — 外部サービス連携。Placesもここに含まれるため、directory単位では削除しない
- `internal/ffmpeg/`, `internal/thumb/`, `internal/meta/` — media処理
- `pkg/` — `internal/` に依存しない共通utility

### 削除時の注意

`internal/service/` には個人利用で不要な上流サービス連携と、残すPlaces系処理が混在しています。商用・Portal・cluster関連を削るときは参照元とfocused testを確認し、directoryごとの一括削除をしません。

## Frontend

- `frontend/src/` — Vue frontend
- `frontend/src/page/` — pages
- `frontend/src/component/` — reusable components
- `frontend/src/css/` — styles
- `assets/templates/` — initial HTML templates

利用者向け言語は日本語を正準とします。不要な言語資産は、runtime参照とbuild参照を確認してから削除します。

## Local environment

正準Composeは `compose.yaml` だけです。通常起動するserviceは次の2つです。

- `photoprism`
- `mariadb`

Keycloak、dummy OIDC、dummy LDAP、Traefik、Prometheus、PostgreSQL、preview環境、multi-arch配布用Composeは正準ローカル環境に含めません。

```bash
cp .env.example .env
make up
make terminal
make dep
make build-all
make start
```

## 検証

変更に応じて最小のfocused checkから実行し、必要なbroader gateへ進みます。

```bash
make journal-test
make test-short
make test-js
make build-go
make build-js
make lint
```

実行していないcheckをPASSとして扱いません。

## 残す機能

- 写真・動画のindexing、検索、整理
- albums
- People / face clustering
- Places
- 明示的に選択した写真のsharing
- 月次日記
- 日本語UI
- AIによる説明・要約・検索補助
- Google Photos Picker APIを境界にしたユーザー選択式import
- Web / PWA

## 削減対象

次はrepository-wideの参照を確認してから削減します。

- billing / membership / sponsor / donation / upgrade
- commercial Portal / team / cluster-management
- commercial専用route、API client、config、UI、test
- 日本語以外の不要な利用者向けtranslation catalog
- 上流配布・demo・releaseだけに必要なdocker / setup / script
- `.ldap.cfg`, `.qdrant.yaml` など、残存参照の確認が必要なfixture / config
- 削除済み機能を説明するstale documentation

## 削らないもの

- `LICENSE`, `NOTICE`
- 上流由来の著作権表示・第三者ライセンス
- People / Places / face clustering
- originalsや個人写真を守るためのsecurity / permission処理

不要かどうか不明なものは、参照と実行証拠を確認するまで残します。
