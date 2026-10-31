"""Tests pour templates/.akoris/scripts/build-debt-index.py."""

import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "templates/.akoris/scripts/build-debt-index.py"


def run_script(*args, cwd=None):
    """Exécute le script et retourne (returncode, stdout, stderr)."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True, text=True, cwd=cwd,
    )
    return result.returncode, result.stdout, result.stderr


def write_debt(path: Path, content: str):
    path.write_text(content, encoding="utf-8")


def test_build_debt_index_exit_2_without_yaml():
    """L'absence de PyYAML produit un message explicite et exit 2."""
    code = """
import runpy
import sys
from unittest.mock import patch

script = sys.argv[1]
sys.argv = [script]
with patch.dict("sys.modules", {"yaml": None}):
    runpy.run_path(script, run_name="__main__")
"""
    result = subprocess.run(
        [sys.executable, "-c", code, str(SCRIPT)],
        capture_output=True, text=True,
    )
    assert result.returncode == 2
    assert "ERREUR : PyYAML requis." in result.stderr
    assert "pip install pyyaml" in result.stderr


def test_simple_frontmatter(tmp_path):
    """Cas nominal : un frontmatter simple est parsé."""
    debt_dir = tmp_path / "debt"
    debt_dir.mkdir()
    write_debt(debt_dir / "DT-001-test.md", """---
id: DT-001
titre: Test simple
priorite: P2
statut: ouverte
sprint_origine: 1
decision_origine: go_with_reserve
adr_lie: ADR-0001
risque: "risque simple"
impact: moyen
sprint_resorption_prevu: 2
cree_le: 2026-01-01
---
# DT-001
""")
    code, out, err = run_script("--debt-dir", str(debt_dir))
    assert code == 0, f"stderr: {err}"
    assert (debt_dir / "index.md").exists()


def test_dashes_in_value(tmp_path):
    """Cas du bug : une valeur contient '---'."""
    debt_dir = tmp_path / "debt"
    debt_dir.mkdir()
    write_debt(debt_dir / "DT-002-test.md", """---
id: DT-002
titre: Test avec tirets
priorite: P1
statut: ouverte
sprint_origine: 1
decision_origine: go_with_reserve
adr_lie: ADR-0001
risque: "a --- b --- c"
impact: eleve
sprint_resorption_prevu: 3
cree_le: 2026-01-01
---
# DT-002
""")
    code, out, err = run_script("--debt-dir", str(debt_dir))
    assert code == 0, f"stderr: {err}"
    assert (debt_dir / "index.md").exists()


def test_missing_frontmatter(tmp_path):
    """Cas d'erreur : pas de frontmatter."""
    debt_dir = tmp_path / "debt"
    debt_dir.mkdir()
    write_debt(debt_dir / "DT-003-test.md", "# DT-003\n\nPas de frontmatter.\n")
    code, out, err = run_script("--debt-dir", str(debt_dir))
    assert code == 1
    assert "frontmatter" in err


def test_invalid_priority(tmp_path):
    """Cas d'erreur : priorité invalide."""
    debt_dir = tmp_path / "debt"
    debt_dir.mkdir()
    write_debt(debt_dir / "DT-004-test.md", """---
id: DT-004
titre: Test priorité invalide
priorite: P9
statut: ouverte
sprint_origine: 1
decision_origine: go_with_reserve
adr_lie: ADR-0001
risque: "risque"
impact: moyen
sprint_resorption_prevu: 2
cree_le: 2026-01-01
---
# DT-004
""")
    code, out, err = run_script("--debt-dir", str(debt_dir))
    assert code == 1
    assert "priorite" in err


def test_thresholds_warning(tmp_path):
    """Les seuils dépassés avertissent, mais ne bloquent pas et l'index est généré."""
    debt_dir = tmp_path / "debt"
    debt_dir.mkdir()
    for i in range(1, 5):
        write_debt(debt_dir / f"DT-{i:03d}-test.md", f"""---
id: DT-{i:03d}
titre: Test {i}
priorite: P0
statut: ouverte
sprint_origine: 1
decision_origine: go_with_reserve
adr_lie: ADR-0001
risque: "risque"
impact: eleve
sprint_resorption_prevu: 2
cree_le: 2026-01-01
---
# DT-{i:03d}
""")
    code, out, err = run_script("--debt-dir", str(debt_dir), "--check-thresholds")
    assert code == 0
    assert "SEUIL DÉPASSÉ" in err
    assert (debt_dir / "index.md").exists()
