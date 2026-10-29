"""Tests pour scripts/validate-method.py."""

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "validate-method.py"


def test_validate_method_exists():
    assert SCRIPT.exists()


def test_validate_method_runs():
    r = subprocess.run(
        [sys.executable, str(SCRIPT), "--repo-root", str(REPO_ROOT)],
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, f"code {r.returncode}\nstdout:\n{r.stdout}\nstderr:\n{r.stderr}"


def test_validate_method_detects_breakage(tmp_path):
    fake = tmp_path / "fake"
    (fake / "decisions").mkdir(parents=True)
    (fake / "templates" / ".akoris").mkdir(parents=True)
    (fake / "METHOD.md").write_text("# Fake\n", encoding="utf-8")
    (fake / "templates" / ".akoris" / "contexte.md").write_text(
        "## §0\n## §1\n", encoding="utf-8"
    )
    (fake / "decisions" / "001-test.md").write_text(
        "## Décision\n## Règles\n## Justification\n## Alternatives\n",
        encoding="utf-8",
    )
    r = subprocess.run(
        [sys.executable, str(SCRIPT), "--repo-root", str(fake)],
        capture_output=True,
        text=True,
    )
    assert r.returncode == 1


def test_contexte_section_1_is_detected(tmp_path):
    fake = tmp_path / "fake-section"
    (fake / "decisions").mkdir(parents=True)
    (fake / "templates" / ".akoris").mkdir(parents=True)
    (fake / "METHOD.md").write_text("# Fake\n", encoding="utf-8")
    (fake / "templates" / ".akoris" / "contexte.md").write_text(
        "## §10 — Section dix\n", encoding="utf-8"
    )
    r = subprocess.run(
        [sys.executable, str(SCRIPT), "--repo-root", str(fake)],
        capture_output=True,
        text=True,
    )
    assert r.returncode == 1
    assert "contexte.md : sections manquantes" in r.stdout
    assert "'§1'" in r.stdout


def test_compteur_affiche_echec(tmp_path):
    fake = tmp_path / "fake-counter"
    (fake / "decisions").mkdir(parents=True)
    (fake / "METHOD.md").write_text("# Fake\n", encoding="utf-8")
    (fake / "decisions" / "001-test.md").write_text(
        "## Décision\n", encoding="utf-8"
    )
    r = subprocess.run(
        [sys.executable, str(SCRIPT), "--repo-root", str(fake)],
        capture_output=True,
        text=True,
    )
    errors = re.search(r"Erreurs : (\d+)", r.stdout)
    counts = re.search(r"Vérifications : (\d+)/(\d+) passées", r.stdout)
    assert r.returncode == 1
    assert errors and int(errors.group(1)) > 0
    assert counts
    passed, checks = map(int, counts.groups())
    assert passed < checks
