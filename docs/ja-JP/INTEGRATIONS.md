# 外部連携

確認日: 2026-08-13

この文書では、個人版で採用する外部連携を、公式資料で確認できた範囲だけに限定します。

## Google Photos

### 採用: Google Photos Picker API

Google は 2025-03-31 以降、Library API の `photoslibrary.readonly`、`photoslibrary.sharing`、`photoslibrary` スコープを削除しました。既存ライブラリ全体から写真を選ぶ用途は Picker API が正準です。

したがって、本forkでは **Google Photos 全件同期を作りません**。ユーザーが Google Photos 側で明示的に選択した写真・動画だけを取り込みます。

取り込み時に月次日記へ残す provenance:

- `source: "google_photos"`
- Picker session / 選択結果を識別できる値
- 取り込み日時
- PhotoPrismへ登録後の `photo_uid`

Google Photosを正準ストレージにはせず、取り込み済み原本はPhotoPrism側の通常のバックアップ対象として扱います。

公式資料:

- https://developers.google.com/photos/support/updates?hl=ja
- https://developers.google.com/photos/overview/authorization?hl=ja
- https://developers.google.com/photos/picker/reference/rest
- https://developers.google.com/photos/support/release-notes?hl=ja

## ChatGPT / OpenAI

### 採用: MCPを第一境界、生成AIは任意補助

PhotoPrism本体にはMCP APIを無効化する設定が存在するため、この個人版では **MCPを写真・日記をAIから読むための正準境界**として残します。写真DBへ直接SQL接続させません。

OpenAIの公式資料では、Responses APIからremote MCP serverをtoolとして利用できます。またChatGPTのカスタムMCPアプリは、2026-08-13時点では主にBusiness / Enterprise / Edu向けの開発者機能として案内されています。したがって個人版は、ChatGPT UI固有機能を必須依存にせず、次の2経路を分離します。

1. **無料で維持できる境界**: Markdown / JSON exportをChatGPT等へ手動で渡せる
2. **任意のAPI連携**: OpenAI Responses APIからPhotoPrism MCPを読み、写真説明・月次要約・タグ候補を作る

AIができること:

- 選択写真の説明候補
- 月次日記の本文下書き
- タグ候補
- 旅行単位の振り返り候補
- 代表写真候補の理由付け

AIがしてはいけないこと:

- 月次日記を自動で `public` にする
- 原本を削除する
- private / draft / ready の内容を公開成果物へ混ぜる
- APIキーや認証情報を日記JSONへ保存する

公式資料:

- https://help.openai.com/ja-jp/articles/12584461
- https://help.openai.com/en/articles/11487775-connectors-in
- https://platform.openai.com/docs/quickstart/make-your-first-api-request

## Amazon Photos

### 方針: ネイティブ自動同期を作らない

2026-08-13 に Amazon の公式開発者ドキュメントを確認しましたが、Amazon Photos の個人ライブラリへアクセスする公開開発APIを確認できませんでした。Selling Partner APIなどの商品画像向けAPIを個人写真同期へ流用しません。

したがって、確認できない非公式API、スクレイピング、ブラウザ自動操作を正準連携にしません。

代わりに次だけを提供対象とします。

- Amazon Photosからダウンロードしたローカルファイルの取り込み
- PhotoPrism側からの原本エクスポート
- provenanceへ `source: "amazon_photos"` を記録
- 将来Amazonが公式APIを公開した場合だけ再評価

公式資料の入口:

- https://developer.amazon.com/ja/docs/
- https://developer.amazon.com/ja/support/

## テキスト・日記連携

写真と文章は同じDBへ無理に押し込まず、月次JSONを結合点にします。

- 写真: PhotoPrism `photo_uid`
- アルバム: `album_uids`
- 文章: `body`
- 場所: `places`
- 出典: `provenance`
- 公開状態: `status`

これにより、Git管理したMarkdown、既存の日記、ChatGPTとの会話から人間が採用した文章などを、写真原本とは独立して入出力できます。

## 連携の共通原則

- 認証情報をGitへ入れない
- 外部サービスに送る対象をユーザーが制御できる
- インポート元と取得日時をprovenanceとして残す
- 外部APIの仕様変更で正準写真を削除・破壊しない
- APIが確認できない機能は実装しない
- 有料サービスは必須依存にしない
