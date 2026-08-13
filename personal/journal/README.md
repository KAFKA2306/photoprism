# 月次写真日記

写真を大量に並べるのではなく、**その月を思い出すのに十分な数枚 + 短い文章**を1ページにする個人用出力。

## 入力

`entries/YYYY-MM.json` を置く。

```json
{
  "month": "2026-08",
  "title": "8月の記録",
  "body": "この月に覚えておきたいこと。",
  "visibility": "private",
  "places": ["京都"],
  "photos": [
    {
      "src": "images/example.webp",
      "alt": "写真の内容を説明する日本語",
      "caption": "短い説明",
      "place": "京都"
    }
  ]
}
```

`visibility` は `private` または `public` のみ。

## 公開出力

```bash
python personal/journal/build.py
```

既定では `public` の月だけ `dist/` に出力する。

ローカル確認に限って非公開月も出す場合:

```bash
python personal/journal/build.py --include-private
```

`--include-private` で生成した `dist/` を公開してはいけない。

## 設計上の役割

このビルダーは最終UIではなく、月次日記のデータ契約と公開境界を先に固定するための最小実装。

PhotoPrism本体との接続では、このJSON契約を基準に次を追加する。

- PhotoPrism photo UID から代表写真を選択
- album UID の関連付け
- AI要約は別フィールドの下書きとして保持
- 公開前に写真、本文、位置情報を再確認
