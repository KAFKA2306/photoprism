# フロントエンドの日本語

この個人forkでは、UI言語を **日本語 (`ja`) のみに固定**しています。

## 正準ファイル

- `frontend/src/locales.js`: 利用可能なUI言語を日本語1件に固定
- `frontend/src/locales/ja.po`: 日本語翻訳カタログ
- `frontend/src/locales/translations.pot`: gettext の翻訳元テンプレート（生成物のため保持）

日本語以外の `*.po` は個人版では保守しないため削除します。

## 翻訳の更新

新しいUI文言を追加した場合は、まず翻訳元を抽出します。

```bash
make gettext-extract
```

その後 `ja.po` を更新し、必要に応じてフロントエンド用JSONへコンパイルします。

```bash
cd frontend
npm run gettext-compile
```

## 方針

- 言語選択UIに日本語以外を出さない
- ブラウザ言語や `?locale=` で別言語が指定されても `ja` にfallbackする
- 個人版で削除した機能の文言は翻訳カタログからも順次除去する
- `LICENSE` や第三者ライセンスなど、法的に原文保持が必要なファイルは翻訳対象外
