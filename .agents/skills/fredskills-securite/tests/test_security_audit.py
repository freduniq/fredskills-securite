"""Tests de non-régression du mini-scanner ; aucune connexion réseau."""
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/security_audit.py'
spec=importlib.util.spec_from_file_location('security_audit',SCRIPT)
module=importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name]=module
spec.loader.exec_module(module)

class AuditScriptTests(unittest.TestCase):
    def test_env_never_read_and_only_path_reported(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'.env').write_text('SUPER_SECRET_VALUE_12345678',encoding='utf-8')
            findings,stats=module.scan(root)
            rendered=module.markdown(findings,stats,root)
            self.assertNotIn('SUPER_SECRET_VALUE_12345678',rendered)
            self.assertTrue(any(x.rule=='R013' for x in findings))

    def test_eval_detection_and_no_source_excerpt(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'app.py').write_text("payload='REDACT_ME_123'\nresult=eval(payload)\n",encoding='utf-8')
            findings,stats=module.scan(root)
            report=module.markdown(findings,stats,root)
            self.assertIn('R001', report)
            self.assertNotIn('REDACT_ME_123', report)

    def test_no_findings_is_not_security_claim(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'index.py').write_text('print("hello")\n',encoding='utf-8')
            findings,stats=module.scan(root)
            self.assertFalse(findings)
            self.assertIn("ne démontre pas",module.markdown(findings,stats,root))

    def test_node_no_lockfile_suspicion(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'package.json').write_text(json.dumps({'name':'test'}),encoding='utf-8')
            findings,_=module.scan(root)
            self.assertIn('R015',{f.rule for f in findings})
            (root/'package-lock.json').write_text('{}',encoding='utf-8')
            findings,_=module.scan(root)
            self.assertNotIn('R015',{f.rule for f in findings})

if __name__=='__main__':
    unittest.main()
