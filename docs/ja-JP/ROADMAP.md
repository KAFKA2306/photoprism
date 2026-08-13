# 個人版ロードマップ

このファイルが正準の作業台帳。GitHub Issues はこのリポジトリで無効化されているため、Issueの代わりに使用する。

## 完了

- [x] 個人版の目的・保持機能・削除機能を定義
- [x] ルート README を日本語の個人版説明へ置換
- [x] 外部連携の現行公式API境界を記録
- [x] 月次写真日記の公開データ形式を定義
- [x] `visibility: public` の月だけHTMLへ出力する最小ビルダーを追加

## 次に実コードから削除

- [ ] `upgrade` / `connect` のroute・component・文言・テストを削除
- [ ] sponsor / membership / customer / tier / billing 系configを削除
- [ ] 個人単一環境で不要な Portal / Cluster / Instances 導線を削除
- [ ] 日本語以外の言語選択肢を削除
- [ ] 日本語以外の翻訳カタログを削除
- [ ] 英語の利用者向け上流文書を日本語正準文書へ置換または削除
- [ ] 上記削除後、参照残骸を機械監査して0件にする

## 個人機能

- [ ] 月次日記を PhotoPrism の写真選択と接続
- [ ] 月次日記に関連アルバムを紐付ける
- [ ] 月次日記の下書き/確定/公開状態を分離
- [ ] 旅行ビューを Places + Album + 日付でまとめる
- [ ] Markdown/JSON 日記 import/export
- [ ] Google Photos Picker API インポート
- [ ] OpenAI Responses API の任意AI補助
- [ ] Amazon Photos はローカルファイル import/export のみ
- [ ] Android 個人用 PWA/APK
- [ ] 公開用の月次日記出力をプライバシー監査付きで配信

## 最終ゲート

- [ ] 課金・スポンサー・アップグレード導線 0
- [ ] 日本語以外の利用者向けUI 0
- [ ] 個人利用しない Portal / Cluster / team 機能 0
- [ ] 削除済み機能への dead link / dead config / dead test 0
- [ ] 利用者向け文書は日本語のみ
- [ ] build / unit test / frontend test 成功
- [ ] 公開成果物に private 月・秘密情報が含まれない
