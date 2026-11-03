"""Meaningful installation checks; no network, credentials or agent API calls."""

import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/install.py"
SPEC = importlib.util.spec_from_file_location("installer", SCRIPT)
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallTest(unittest.TestCase):
    def test_copies_complete_independent_bundle(self):
        with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stdout(io.StringIO()):
            root = Path(directory)
            installer.install(["write-tutorial"], root)
            source = installer.ROOT / "creation/write-tutorial"
            for file in source.rglob("*"):
                if file.is_file():
                    self.assertEqual(file.read_bytes(), (root / "write-tutorial" / file.relative_to(source)).read_bytes())

    def test_conflict_prevents_all_copies(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            conflict = root / "write-reference"
            conflict.mkdir()
            marker = conflict / "SKILL.md"
            marker.write_text("user-owned content")
            with self.assertRaises(ValueError):
                installer.install(["write-tutorial", "write-reference"], root)
            self.assertEqual(marker.read_text(), "user-owned content")
            self.assertFalse((root / "write-tutorial").exists())

    def test_unknown_name_does_not_create_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "not-created"
            with self.assertRaises(ValueError):
                installer.install(["write-tutorial", "../unknown"], root)
            self.assertFalse(root.exists())

    def test_broken_symlink_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "write-tutorial"
            target.symlink_to(root / "missing", target_is_directory=True)
            with self.assertRaises(ValueError):
                installer.install(["write-tutorial"], root)
            self.assertTrue(target.is_symlink())


if __name__ == "__main__":
    unittest.main()
