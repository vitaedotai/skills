import json
from pathlib import Path
import shutil
import tempfile
import unittest
from validate import validate, ROOT

class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)/'package'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','.venv','node_modules','.worktrees','.tmp','__pycache__'))
    def tearDown(self):
        self.temp.cleanup()
    def test_valid_package(self):
        self.assertEqual(validate(self.root),[])
    def test_broken_reference(self):
        (self.root/'README.md').write_text('[missing](does-not-exist.md)')
        self.assertTrue(any('broken' in error for error in validate(self.root)))

    def test_missing_skill(self):
        (self.root/'candidate-outreach/SKILL.md').unlink()
        self.assertTrue(any('paths' in error for error in validate(self.root)))
    def test_individual_install_cannot_require_sibling(self):
        path=self.root/'candidate-outreach/SKILL.md'
        path.write_text(path.read_text()+'\n[other](../job-intake/SKILL.md)\n')
        self.assertTrue(any('individual skill' in error for error in validate(self.root)))
    def test_invalid_metadata(self):
        path=self.root/'candidate-outreach/SKILL.md'
        path.write_text(path.read_text().replace('version: "0.1.0"','version: 12'))
        self.assertTrue(any('strings' in error for error in validate(self.root)))

if __name__=="__main__":
    unittest.main()
