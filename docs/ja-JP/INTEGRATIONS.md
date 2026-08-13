# 外部連携

確認日: 2026-08-13

この文書では、個人版で採用する外部連携を、公式資料で確認できた範囲だけに限定する。

## Google Photos

### 採用: Google Photos Picker API

Google は 2025-03-31 以降、Library API の `photoslibrary.readonly`、`photoslibrary.sharing`、`photoslibrary` スコープを削除し、ユーザーのライブラリ全体から写真を選ばせる用途には Picker API を使うよう案内している。

したがって、本forkでは **Google Photos 全件同期を前提にしない**。ユーザーが Google Photos 側で明示的に選んだ写真・動画を取り込む導線を実装する。

公式資料:

- https://developers.google.com/photos/support/updates?hl=ja
- https://developers.google.com/photos/overview/authorization?hl=ja
- https://developers.google.com/photos/support/release-notes?hl=ja

## OpenAI / ChatGPT

### 採用: 任意のAI補助

OpenAI API の Responses API はテキストと画像入力を扱えるため、次の用途に限定して接続できる。

- 写真の説明
- 月次日記の要約案
- タグ候補
- 代表写真候補を選ぶための補助情報

APIキーはサーバー側の秘密情報として扱い、フロントエンドの公開設定や日記JSONに保存しない。AIが生成した文章は下書きとして扱い、人間の確定操作なしに公開しない。

公式資料:

- https://platform.openai.com/docs/quickstart/make-your-first-api-request
- https://platform.openai.com/docs/api-reference/responses

## Amazon Photos

### 方針: ネイティブ自動同期を作らない

2026-08-13 に Amazon の公式開発者ドキュメントを確認したが、Amazon Photos の個人ライブラリへアクセスする公開開発APIを確認できなかった。検索で見つかる Selling Partner API の画像機能はEC商品画像向けであり、Amazon Photos の個人写真同期用途ではない。

したがって、確認できない非公式API、スクレイピング、ブラウザ自動操作を正準連携にしない。

代わりに次を提供対象とする。

- Amazon Photos から取得したローカルファイルの取り込み
- PhotoPrism 側からの原本エクスポート
- 将来、Amazon が公式APIを公開した場合だけ再評価

公式資料の入口:

- https://developer.amazon.com/ja/docs/
- https://developer.amazon.com/ja/support/

## 連携の共通原則

- 認証情報をGitへ入れない
- 外部サービスに送る対象をユーザーが制御できる
- インポート元と取得日時を provenance として残す
- 外部APIの仕様変更で正準写真を削除・破壊しない
- APIが確認できない機能は実装しない
