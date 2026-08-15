# KAFKA2306 Photo Memories

このリポジトリは、PhotoPrism を基盤にした **KAFKA2306 個人用の写真・旅行・日記・思い出管理システム**です。

一般向けのフォトサービスを作ることは目的にしません。日本で個人利用するために必要な機能だけを残し、課金・スポンサー・商用・チーム運用・多言語など、本forkで使わない機能はコード、UI、設定、文書、テストを含めて削減します。

## 何を残すか

- 日本語 UI（`ja` / `ja-JP`）を唯一の利用言語とする
- 写真・動画の閲覧、検索、整理
- 旅行・場所・時系列での振り返り
- アルバムと、明示的に選んだ写真の共有
- 月次の思い出ページ
  - 数枚の代表写真
  - 月の本文
  - 場所
  - 写真ごとのキャプション
  - `draft / ready / public` の公開状態
- Markdown / JSON など、機械可読なテキストとの連携
- AIによる写真の説明、思い出の要約、検索補助
- Google Photos からユーザーが選択した写真の取り込み
- Android では個人用 PWA / APK を利用できる形にする

## 何を削減するか

- membership / billing / sponsor / donation / upgrade
- 個人単一環境で使わない商用 Portal / team / cluster-management 導線
- 日本語以外のUI言語、翻訳選択肢、不要な翻訳資産
- 本forkで使わない商用・営業・コミュニティ誘導
- 削除済み機能を参照する文書、設定、テスト、画像、リンク

写真機能としての face clustering / People / Places は削除対象ではありません。「画面から隠す」だけでは完了とせず、不要機能の実行時参照が残っていないことを監査します。

## 月次日記

`personal/journal/` に、写真と文章を月単位で静的HTMLへ出力する実装があります。

```bash
python personal/journal/build.py
```

既定では `status: "public"` の月だけが `personal/journal/dist/` に出力されます。`draft` は編集中、`ready` は本人確認済みだが非公開です。AI生成だけで `public` へ昇格させません。

月一覧では各月の最初の写真を代表写真として、月・タイトル・場所をカード表示します。写真を大量に並べるのではなく、**数枚の写真と文章から月を思い出せること**を正準体験にします。

## 外部連携

外部サービスは「現在の公式APIで確認できる範囲」だけを実装対象にします。

- Google Photos: Picker API によるユーザー選択式インポート
- OpenAI / ChatGPT: MCPまたは明示的なテキスト入出力を境界に、写真説明・月次下書き・タグ候補を補助
- Amazon Photos: 2026-08-13 時点で個人ライブラリ向け公開開発APIを公式資料から確認できないため、ネイティブ自動同期は実装せず、ファイルのインポート / エクスポート境界だけを用意する

詳細は [`docs/ja-JP/INTEGRATIONS.md`](docs/ja-JP/INTEGRATIONS.md) を参照してください。

## Android

Android固有の写真管理ロジックは作りません。Web/PWAを正準実装とし、必要な場合だけ個人用の薄いAPKで包みます。方針は [`docs/ja-JP/ANDROID.md`](docs/ja-JP/ANDROID.md) に固定します。

## 作業台帳

GitHub Issues を現在の作業台帳とします。[`docs/ja-JP/ROADMAP.md`](docs/ja-JP/ROADMAP.md) は中長期の方向性を扱い、Issue の現在状態を置き換えません。

## ライセンスと由来

本forkは PhotoPrism のコードを基盤としています。

- upstream: https://github.com/photoprism/photoprism
- upstream developer docs: https://docs.photoprism.app/developer-guide/
- local repository: https://github.com/KAFKA2306/photoprism

リポジトリの `LICENSE` は GNU Affero General Public License v3 であり、課金機能とは無関係な法的条件なので削除しません。上流由来の著作権表示・ライセンス表示・第三者ライセンスは、機能削減の対象とは分離して保持します。
