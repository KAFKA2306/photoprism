# 月次写真日記

写真を大量に並べるのではなく、**その月を思い出すのに十分な数枚 + 短い文章**を1ページにする個人用出力です。

## 入力

`entries/YYYY-MM.json` を置きます。

```json
{
  "month": "2026-08",
  "title": "8月の記録",
  "body": "この月に覚えておきたいこと。",
  "status": "draft",
  "places": ["京都"],
  "album_uids": ["as1234567890"],
  "tags": ["旅行", "夏"],
  "provenance": [
    {
      "source": "photoprism",
      "source_id": "as1234567890",
      "note": "旅行アルバムから代表写真を選択"
    }
  ],
  "photos": [
    {
      "src": "images/example.webp",
      "alt": "写真の内容を説明する日本語",
      "caption": "短い説明",
      "place": "京都",
      "photo_uid": "ps1234567890",
      "source": "photoprism"
    }
  ]
}
```

## 状態

`status` は3段階です。

- `draft`: AI生成や編集中を含む下書き。公開不可
- `ready`: 本人確認済み。まだ公開不可
- `public`: 公開してよいと本人が明示的に確定した月だけ

**AI生成だけで `public` へ昇格させません。** 公開は必ず人間の確定操作を経ます。

## 公開出力

```bash
python personal/journal/build.py
```

既定では `status: "public"` の月だけ `dist/` に出力します。公開月の写真 `src` は、外部URL・絶対パス・`..` を含む親ディレクトリ参照を禁止し、公開成果物内の相対パスだけを許可します。

ローカル確認に限って `draft` / `ready` も出す場合:

```bash
python personal/journal/build.py --include-nonpublic
```

このオプションで生成した `dist/` は公開してはいけません。

## PhotoPrismとの接続

月次JSONは独立した正準データです。PhotoPrismの内部DBを直接公開データにせず、必要な写真だけをUIDで参照します。

- `photo_uid`: PhotoPrism写真UID
- `album_uids`: 関連アルバムUID
- `places`: 月の場所
- `tags`: 日記側の検索・振り返り用タグ
- `provenance`: Google Photos / Amazon Photos / PhotoPrism / ローカル / テキスト等の由来

静的公開では、選択した写真だけを公開用 `images/` にコピーする工程を別ゲートにします。原本ライブラリ全体やPhotoPrism内部URLをそのまま公開HTMLへ埋め込みません。

## 月一覧

`index.html` は各月の最初の写真を代表写真として使い、月・タイトル・場所をカード表示します。個人の「写真一覧」ではなく、**思い出を月単位で辿る入口**を正準UIにします。
