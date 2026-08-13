#!/usr/bin/env python3
"""個人用の月次写真日記を静的HTMLへ変換する。標準ライブラリのみで動作する。"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlparse

ALLOWED_STATUS = {"draft", "ready", "public"}


class JournalError(ValueError):
    pass


def is_safe_public_src(value: str) -> bool:
    """公開HTMLに埋め込める、リポジトリ内の相対パスだけを許可する。"""
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc or value.startswith(("/", "\\", "//")):
        return False
    path = PurePosixPath(value.replace("\\", "/"))
    return bool(path.parts) and ".." not in path.parts


def load_entry(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise JournalError(f"{path}: JSONを読み込めません: {exc}") from exc

    required = {"month", "title", "body", "photos", "status"}
    missing = sorted(required - data.keys())
    if missing:
        raise JournalError(f"{path}: 必須項目がありません: {', '.join(missing)}")

    month = data["month"]
    if not isinstance(month, str) or len(month) != 7 or month[4] != "-" or not (month[:4].isdigit() and month[5:].isdigit()):
        raise JournalError(f"{path}: month は YYYY-MM 形式にしてください")
    m = int(month[5:])
    if m < 1 or m > 12:
        raise JournalError(f"{path}: month の月が不正です")

    if not isinstance(data["title"], str) or not data["title"].strip():
        raise JournalError(f"{path}: title は空にできません")
    if not isinstance(data["body"], str):
        raise JournalError(f"{path}: body は文字列にしてください")
    if data["status"] not in ALLOWED_STATUS:
        raise JournalError(f"{path}: status は draft / ready / public のいずれかです")
    if not isinstance(data["photos"], list):
        raise JournalError(f"{path}: photos は配列にしてください")

    for i, photo in enumerate(data["photos"]):
        if not isinstance(photo, dict):
            raise JournalError(f"{path}: photos[{i}] はobjectにしてください")
        src = photo.get("src")
        alt = photo.get("alt")
        if not isinstance(src, str) or not src.strip():
            raise JournalError(f"{path}: photos[{i}].src は必須です")
        if not isinstance(alt, str) or not alt.strip():
            raise JournalError(f"{path}: photos[{i}].alt は必須です")
        if data["status"] == "public" and not is_safe_public_src(src):
            raise JournalError(f"{path}: public の写真srcは相対パスだけ使用できます: {src}")

    for key in ("places", "album_uids", "tags"):
        values = data.get(key, [])
        if not isinstance(values, list) or not all(isinstance(v, str) for v in values):
            raise JournalError(f"{path}: {key} は文字列配列にしてください")

    provenance = data.get("provenance", [])
    if not isinstance(provenance, list) or not all(isinstance(v, dict) and isinstance(v.get("source"), str) for v in provenance):
        raise JournalError(f"{path}: provenance は source を持つobject配列にしてください")

    return data


def render_photo(photo: dict[str, Any]) -> str:
    src = html.escape(photo["src"], quote=True)
    alt = html.escape(photo["alt"], quote=True)
    caption = html.escape(str(photo.get("caption", "")))
    place = html.escape(str(photo.get("place", "")))
    meta = " · ".join(v for v in (caption, place) if v)
    figcaption = f"<figcaption>{meta}</figcaption>" if meta else ""
    return f'<figure><img src="{src}" alt="{alt}" loading="lazy">{figcaption}</figure>'


def render_entry(entry: dict[str, Any]) -> str:
    month = html.escape(entry["month"])
    title = html.escape(entry["title"])
    body = "<br>".join(html.escape(entry["body"]).splitlines())
    places = "、".join(html.escape(v) for v in entry.get("places", []))
    tags = " / ".join(html.escape(v) for v in entry.get("tags", []))
    place_html = f'<p class="meta">場所: {places}</p>' if places else ""
    tag_html = f'<p class="meta">タグ: {tags}</p>' if tags else ""
    photos = "".join(render_photo(p) for p in entry["photos"])
    return f"""<article>
<header><p class="month">{month}</p><h1>{title}</h1>{place_html}{tag_html}</header>
<div class="photos">{photos}</div>
<p class="body">{body}</p>
</article>"""


def page(title: str, body: str) -> str:
    safe_title = html.escape(title)
    return f"""<!doctype html>
<html lang="ja-JP">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="index,follow">
<title>{safe_title}</title>
<style>
:root{{color-scheme:light dark;font-family:system-ui,-apple-system,"Noto Sans JP",sans-serif}}
body{{max-width:1040px;margin:0 auto;padding:24px;line-height:1.75}}
a{{color:inherit}}
nav{{margin:0 0 32px}}
article{{margin:0 0 72px}}
.month,.meta{{opacity:.72}}
.photos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin:24px 0}}
figure{{margin:0}}
img{{width:100%;height:auto;display:block;border-radius:12px}}
figcaption{{font-size:.9rem;opacity:.72;margin-top:6px}}
.body{{white-space:normal}}
.month-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px;padding:0;list-style:none}}
.month-card{{border:1px solid currentColor;border-radius:14px;overflow:hidden}}
.month-card a{{display:block;text-decoration:none}}
.month-card img{{aspect-ratio:4/3;object-fit:cover;border-radius:0}}
.month-card .copy{{padding:14px}}
</style>
</head>
<body>
<nav><a href="index.html">月次日記</a></nav>
{body}
</body>
</html>
"""


def render_index_card(entry: dict[str, Any]) -> str:
    filename = f'{entry["month"]}.html'
    cover = ""
    if entry["photos"]:
        photo = entry["photos"][0]
        cover = f'<img src="{html.escape(photo["src"], quote=True)}" alt="{html.escape(photo["alt"], quote=True)}" loading="lazy">'
    places = "、".join(html.escape(v) for v in entry.get("places", []))
    meta = f'<p class="meta">{places}</p>' if places else ""
    return (
        '<li class="month-card"><a href="'
        + html.escape(filename, quote=True)
        + '">'
        + cover
        + '<div class="copy"><p class="month">'
        + html.escape(entry["month"])
        + "</p><strong>"
        + html.escape(entry["title"])
        + "</strong>"
        + meta
        + "</div></a></li>"
    )


def build(entries_dir: Path, out_dir: Path, include_nonpublic: bool = False) -> list[str]:
    entries = [load_entry(p) for p in sorted(entries_dir.glob("*.json"))]
    entries.sort(key=lambda x: x["month"], reverse=True)

    if not include_nonpublic:
        entries = [e for e in entries if e["status"] == "public"]

    out_dir.mkdir(parents=True, exist_ok=True)
    for entry in entries:
        filename = f'{entry["month"]}.html'
        (out_dir / filename).write_text(page(entry["title"], render_entry(entry)), encoding="utf-8")

    index_body = "<h1>月次日記</h1>"
    index_body += "<p>旅行、写真、文章を月ごとに束ねた個人の記憶アーカイブです。</p>"
    index_body += '<ul class="month-grid">' + "".join(render_index_card(entry) for entry in entries) + "</ul>"
    (out_dir / "index.html").write_text(page("月次日記", index_body), encoding="utf-8")
    return [e["month"] for e in entries]


def main() -> int:
    parser = argparse.ArgumentParser(description="月次写真日記を静的HTMLへ変換します")
    parser.add_argument("--entries", type=Path, default=Path(__file__).with_name("entries"))
    parser.add_argument("--out", type=Path, default=Path(__file__).with_name("dist"))
    parser.add_argument(
        "--include-nonpublic",
        action="store_true",
        help="ローカル確認用。公開ビルドには絶対に指定しないこと",
    )
    args = parser.parse_args()
    months = build(args.entries, args.out, args.include_nonpublic)
    print(f"{len(months)}か月分を出力: {', '.join(months) if months else '公開対象なし'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
