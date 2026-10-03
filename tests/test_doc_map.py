"""The doc catalog in creative-strategy-context/expertise-routing.md.

Parker's chat lists the method docs from this one file (each doc and its
`summary` frontmatter), so a doc added or edited without regenerating the
catalog would be missing or described wrongly there.
"""
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_runtime_hooks import FACTORY

SCRIPT = Path("scripts") / "build-doc-map.py"


def run(root, *args):
    return subprocess.run(
        [sys.executable, str(Path(root) / SCRIPT), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


class DocMapTest(unittest.TestCase):
    def test_the_catalog_is_current(self):
        r = run(FACTORY, "--check")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_a_doc_added_without_regenerating_fails_the_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "scripts").mkdir()
            shutil.copy(Path(FACTORY) / SCRIPT, Path(tmp) / SCRIPT)
            shutil.copytree(Path(FACTORY) / "creative-strategy-context", Path(tmp) / "creative-strategy-context")
            kb = Path(tmp) / "creative-strategy-context"
            catalog = (kb / "expertise-routing.md").read_text(encoding="utf-8")

            (kb / "zz-new-method.md").write_text(
                '---\nsummary: "A new method doc."\n---\n\n# New method\n', encoding="utf-8"
            )
            r = run(tmp, "--check")
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("out of date", r.stdout + r.stderr)
            self.assertEqual((kb / "expertise-routing.md").read_text(encoding="utf-8"), catalog, "--check writes nothing")

            self.assertEqual(run(tmp).returncode, 0)
            self.assertEqual(run(tmp, "--check").returncode, 0)
            self.assertIn("`zz-new-method.md` | A new method doc.", (kb / "expertise-routing.md").read_text(encoding="utf-8"))

    def test_a_top_level_doc_with_no_summary_fails_the_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "scripts").mkdir()
            shutil.copy(Path(FACTORY) / SCRIPT, Path(tmp) / SCRIPT)
            shutil.copytree(Path(FACTORY) / "creative-strategy-context", Path(tmp) / "creative-strategy-context")
            (Path(tmp) / "creative-strategy-context" / "zz-no-summary.md").write_text("# No summary\n", encoding="utf-8")
            r = run(tmp, "--check")
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("zz-no-summary.md", r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
