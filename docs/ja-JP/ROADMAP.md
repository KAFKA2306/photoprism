# 個人版ロードマップ

このファイルが正準の作業台帳です。GitHub Issues はこのリポジトリで無効化されているため、Issueの代わりに使用します。

## 完了

- [x] 個人版の目的・保持機能・削除機能を定義
- [x] ルート README を日本語の個人版説明へ置換
- [x] 外部連携の現行公式API境界を記録
- [x] 月次写真日記の公開データ形式を定義
- [x] 月次日記を `draft / ready / public` の3状態へ分離
- [x] AI生成だけでは `public` にしない公開ゲートを定義
- [x] `status: public` の月だけHTMLへ出力
- [x] 公開写真 `src` を成果物内の安全な相対パスへ制限
- [x] 月一覧に代表写真・月・タイトル・場所を表示
- [x] PhotoPrism `photo_uid` / `album_uids` を月次データへ紐付け可能にした
- [x] Google Photos / Amazon Photos / PhotoPrism / local / text の provenance 形式を追加
- [x] Google Photos は Picker API を正準取り込み境界に固定
- [x] Amazon Photos は公式個人ライブラリAPIを確認できるまでローカル import/export のみに固定
- [x] OpenAI / ChatGPT は MCP または明示的テキストI/Oを境界とし、公開判断をAIへ委譲しない方針を固定
- [x] AndroidはWeb/PWA正準 + 必要時のみ薄い個人APKとする方針を日本語文書化
- [x] 月次日記CIを現行Actions majorへ更新

## 実コードから削除するもの

- [x] `upgrade` / `connect` の利用者向けroute・component・文言を削除
- [ ] sponsor / membership / customer / tier / billing 系backend configを削除
- [ ] `ClientConfig` から `Sponsor / Tier / Membership / Customer` と関連するHub参照を削除
- [ ] 個人単一環境で不要な Portal / Cluster / Instances 導線を削除
- [x] 日本語以外の言語選択UIを削除
- [ ] 日本語以外の翻訳カタログを削除
- [ ] 英語などの利用者向け上流文書を日本語正準文書へ置換または削除
- [ ] 上流由来で必要な法的文書・第三者ライセンスを削除対象から明確に分離
- [ ] 上記削除後、参照残骸を機械監査して0件にする

## 個人機能

- [x] 月次日記に PhotoPrism 写真UID・アルバムUIDを保持できる
- [x] 月次日記の下書き/確定/公開状態を分離
- [x] 月次日記の代表写真付き月一覧
- [ ] PhotoPrism UIから月次日記の代表写真を選択する操作
- [ ] 旅行ビューを Places + Album + 日付でまとめる
- [ ] Markdown/JSON 日記 import/export
- [ ] Google Photos Picker API の実インポートadapter
- [ ] OpenAI Responses API / MCP の任意AI補助adapter
- [ ] Amazon Photos由来ローカルファイルのimport provenance自動付与
- [ ] 個人用PWA manifest / installabilityを確認
- [ ] 必要ならAndroid WebView/TWAの最小wrapperを追加
- [ ] 公開用の月次日記出力をプライバシー監査付きで配信

## 最終ゲート

- [ ] 課金・スポンサー・アップグレード導線 0
- [ ] `Sponsor / Membership / Tier / Customer / billing` の実行時config 0
- [ ] 日本語以外の利用者向けUI 0
- [ ] 個人利用しない Portal / Cluster / team 機能 0
- [ ] 削除済み機能への dead link / dead config / dead test 0
- [ ] 利用者向け文書は日本語のみ
- [ ] 法的・第三者ライセンス文書は必要なものを保持
- [ ] build / unit test / frontend test 成功
- [ ] 公開成果物に `draft / ready` の月・秘密情報・外部原本URLが含まれない
