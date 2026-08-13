import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

BUILD_PATH = Path(__file__).resolve().parents[1] / "build.py"
SPEC = importlib.util.spec_from_file_location("personal_journal_build", BUILD_PATH)
build = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(build)


class BuildJournalTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.entries = self.root / "entries"
        self.out = self.root / "dist"
        self.entries.mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def write_entry(self, name, **overrides):
        entry = {
            "month": "2026-08",
            "title": "8月の記録",
            "body": "本文",
            "visibility": "public",
            "photos": [{"src": "images/a.webp", "alt": "写真"}],
        }
        entry.update(overrides)
        (self.entries / name).write_text(
            json.dumps(entry, ensure_ascii=False),
            encoding="utf-8",
        )

    def test_private_entry_is_not_exported_by_default(self):
        self.write_entry("public.json")
        self.write_entry(
            "private.json",
            month="2026-07",
            title="非公開",
            visibility="private",
        )

        months = build.build(self.entries, self.out)

        self.assertEqual(["2026-08"], months)
        self.assertTrue((self.out / "2026-08.html").exists())
        self.assertFalse((self.out / "2026-07.html").exists())
        self.assertNotIn("非公開", (self.out / "index.html").read_text(encoding="utf-8"))

    def test_private_entry_can_be_rendered_for_local_preview(self):
        self.write_entry("private.json", visibility="private")

        months = build.build(self.entries, self.out, include_private=True)

        self.assertEqual(["2026-08"], months)
        self.assertTrue((self.out / "2026-08.html").exists())

    def test_html_is_escaped(self):
        self.write_entry(
            "escaped.json",
            title="<script>alert(1)</script>",
            body="<b>本文</b>",
            photos=[{"src": "a.webp", "alt": "\"><script>bad()</script>"}],
        )

        build.build(self.entries, self.out)
        output = (self.out / "2026-08.html").read_text(encoding="utf-8")

        self.assertNotIn("<script>", output)
        self.assertIn("&lt;script&gt;", output)

    def test_invalid_month_is_rejected(self):
        self.write_entry("bad.json", month="2026-13")

        with self.assertRaises(build.JournalError):
            build.build(self.entries, self.out)


if __name__ == "__main__":
    unittest.main()
