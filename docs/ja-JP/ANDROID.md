# 個人用 Android

確認日: 2026-08-13

## 結論

Android版を独立製品にはしません。**PhotoPrism Web/PWAを正準実装とし、個人端末でアプリアイコンから開きたい場合だけ薄いAPKを持つ**方針です。

写真管理、旅行ビュー、月次日記、Google Photos取り込み、AI連携のロジックをAndroid側へ複製しません。

## 採用順

1. まずWeb/PWAをそのまま使う
2. 個人端末でAPKが必要になった場合だけ薄いAndroidラッパーを作る
3. Android固有機能が本当に必要になった場合だけ最小のネイティブ橋渡しを追加する

## APK方式

第一候補は、本人が管理するPhotoPrismのHTTPS URLだけを表示する最小WebViewラッパーです。

Android公式ドキュメントでは、`WebView` はアプリの一部として管理下のWebアプリやWebページを表示する用途として提供されています。

- https://developer.android.com/develop/ui/views/layout/webapps/webview?hl=ja

PWAの公開URLとAndroidアプリの所有関係を検証できる構成にした場合はTrusted Web Activityも候補にできます。ただし個人用途では、これを必須条件にしません。

- https://developer.chrome.com/docs/android/trusted-web-activity?hl=ja

## 署名

Android公式ドキュメントでは、APKは端末へインストールまたは更新する前に署名が必要です。個人用APKでも署名鍵をGitへ保存しません。

- https://developer.android.com/studio/publish/app-signing?hl=ja

守ること:

- keystoreをGitへcommitしない
- keystore passwordをGitHub Actionsやソースへ平文で置かない
- 本人の署名鍵を継続して保管する
- APKそのものを正準データにしない
- PhotoPrismの原本写真をAPKへ同梱しない

## WebViewで許可する範囲

- 設定したPhotoPrismのHTTPS originだけを通常遷移先として許可
- 外部リンクは明示的に外部ブラウザへ渡す
- 任意URLを入力するブラウザUIは作らない
- 不要なJavaScript bridgeを作らない
- カメラ・位置情報・ファイル選択などの権限は、実際に必要なものだけ個別に許可する

## Google Photos

Google Photos Picker APIはユーザーがGoogle Photos側で写真・動画を選び、アプリへ共有する方式です。Android APK側へGoogle Photosの全件同期ロジックを持たせません。

- https://developers.google.com/photos/picker/guides/get-started-picker?hl=ja

## 完了条件

個人APKを実装するときは次を満たした場合だけ完了とします。

- Web版と機能ロジックが二重化していない
- HTTPS origin allowlistがある
- 署名鍵・認証情報がリポジトリにない
- debug APKとrelease APKを混同しない
- release APKが本人の端末へインストールできる
- 写真表示、共有、月次日記、Google Photos Pickerへの遷移が実機で確認できる
