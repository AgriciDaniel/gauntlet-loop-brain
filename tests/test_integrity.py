from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from gauntlet_loop_brain.clock import DATE_OVERRIDE_ENV, reference_date
from gauntlet_loop_brain.integrity import hash_tree


class ClockTests(unittest.TestCase):
    def test_reference_date_uses_valid_override(self) -> None:
        with patch.dict(os.environ, {DATE_OVERRIDE_ENV: "2026-08-17"}):
            self.assertEqual(reference_date(), "2026-08-17")

    def test_reference_date_rejects_invalid_override(self) -> None:
        with patch.dict(os.environ, {DATE_OVERRIDE_ENV: "17-08-2026"}):
            with self.assertRaisesRegex(SystemExit, "must be an ISO date"):
                reference_date()


class TreeHashTests(unittest.TestCase):
    def test_tree_hash_normalizes_json_order_and_line_endings(self) -> None:
        with tempfile.TemporaryDirectory(prefix="gauntlet-tree-hash-") as tmp:
            first = Path(tmp) / "first"
            second = Path(tmp) / "second"
            first.mkdir()
            second.mkdir()
            (first / "data.json").write_text('{"b": 2, "a": 1}\r\n', encoding="utf-8")
            (second / "data.json").write_text('{\n  "a": 1,\n  "b": 2\n}\n', encoding="utf-8")
            (first / "note.md").write_bytes(b"hello\r\n")
            (second / "note.md").write_bytes(b"hello\n")
            self.assertEqual(hash_tree(first), hash_tree(second))

    def test_tree_hash_changes_when_content_changes(self) -> None:
        with tempfile.TemporaryDirectory(prefix="gauntlet-tree-hash-negative-") as tmp:
            root = Path(tmp)
            note = root / "note.md"
            note.write_text("before\n", encoding="utf-8")
            before = hash_tree(root)
            note.write_text("after\n", encoding="utf-8")
            self.assertNotEqual(before, hash_tree(root))

    def test_tree_hash_records_symlink_without_following_it(self) -> None:
        with tempfile.TemporaryDirectory(prefix="gauntlet-tree-hash-symlink-") as tmp:
            root = Path(tmp) / "root"
            root.mkdir()
            external = Path(tmp) / "external.txt"
            external.write_text("before\n", encoding="utf-8")
            (root / "external-link").symlink_to(external)
            before = hash_tree(root)
            external.write_text("after\n", encoding="utf-8")
            self.assertEqual(before, hash_tree(root))


if __name__ == "__main__":
    unittest.main()
