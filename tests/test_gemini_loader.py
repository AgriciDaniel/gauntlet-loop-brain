from __future__ import annotations

import stat
import tempfile
import unittest
from pathlib import Path

from scripts.gemini_loader import END, START, install_block, remove_block


class GeminiLoaderRaceTests(unittest.TestCase):
    def test_install_race_replaces_swapped_symlink_not_external_target(self) -> None:
        with tempfile.TemporaryDirectory(prefix="gauntlet-gemini-install-race-") as tmp:
            root = Path(tmp)
            loader = root / "GEMINI.md"
            external = root / "external.md"
            loader.write_text("existing loader\n", encoding="utf-8")
            loader.chmod(0o640)
            external.write_text("external must survive\n", encoding="utf-8")

            def swap_to_symlink(path: Path) -> None:
                path.unlink()
                path.symlink_to(external)

            install_block(loader, _before_replace=swap_to_symlink)

            self.assertFalse(loader.is_symlink())
            self.assertEqual(external.read_text(encoding="utf-8"), "external must survive\n")
            installed = loader.read_text(encoding="utf-8")
            self.assertIn("existing loader", installed)
            self.assertIn(START, installed)
            self.assertIn(END, installed)
            self.assertEqual(stat.S_IMODE(loader.stat().st_mode), 0o640)

    def test_uninstall_race_replaces_swapped_symlink_not_external_target(self) -> None:
        with tempfile.TemporaryDirectory(prefix="gauntlet-gemini-remove-race-") as tmp:
            root = Path(tmp)
            loader = root / "GEMINI.md"
            external = root / "external.md"
            loader.write_text(
                f"user content\n\n{START}\n@./gauntlet-loop-brain/GEMINI.md\n{END}\n",
                encoding="utf-8",
            )
            loader.chmod(0o640)
            external.write_text("external must survive\n", encoding="utf-8")

            def swap_to_symlink(path: Path) -> None:
                path.unlink()
                path.symlink_to(external)

            removed = remove_block(loader, _before_replace=swap_to_symlink)

            self.assertTrue(removed)
            self.assertFalse(loader.is_symlink())
            self.assertEqual(loader.read_text(encoding="utf-8"), "user content\n")
            self.assertEqual(external.read_text(encoding="utf-8"), "external must survive\n")
            self.assertEqual(stat.S_IMODE(loader.stat().st_mode), 0o640)

    def test_uninstall_only_block_race_unlinks_swapped_symlink_not_target(self) -> None:
        with tempfile.TemporaryDirectory(prefix="gauntlet-gemini-unlink-race-") as tmp:
            root = Path(tmp)
            loader = root / "GEMINI.md"
            external = root / "external.md"
            loader.write_text(
                f"{START}\n@./gauntlet-loop-brain/GEMINI.md\n{END}\n",
                encoding="utf-8",
            )
            external.write_text("external must survive\n", encoding="utf-8")

            def swap_to_symlink(path: Path) -> None:
                path.unlink()
                path.symlink_to(external)

            removed = remove_block(loader, _before_replace=swap_to_symlink)

            self.assertTrue(removed)
            self.assertFalse(loader.exists())
            self.assertFalse(loader.is_symlink())
            self.assertEqual(external.read_text(encoding="utf-8"), "external must survive\n")


if __name__ == "__main__":
    unittest.main()
