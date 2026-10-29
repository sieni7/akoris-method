"""Tests pour scripts/init-project.sh."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCRIPT = REPO_ROOT / "scripts" / "init-project.sh"


def run_init(project_name: str, parent: Path):
    """Exécute init-project.sh et retourne le résultat."""
    env = {
        **os.environ,
        "PATH": f"{Path(sys.executable).parent}:{os.environ['PATH']}",
    }
    return subprocess.run(
        ["bash", str(SCRIPT), project_name, str(parent)],
        capture_output=True, text=True, env=env,
    )


def test_init_creates_main_branch(tmp_path):
    """N1 : git init -b main."""
    result = run_init("test-proj", tmp_path)
    assert result.returncode == 0, f"stderr: {result.stderr}"
    branch = subprocess.check_output(
        ["git", "-C", str(tmp_path / "test-proj"), "branch", "--show-current"],
        text=True,
    ).strip()
    assert branch == "main", f"Branche attendue 'main', obtenue '{branch}'"


def test_init_creates_required_dirs(tmp_path):
    """N1 : debt/, sprints/archive/, audits/archive/."""
    result = run_init("test-proj", tmp_path)
    assert result.returncode == 0, f"stderr: {result.stderr}"
    proj = tmp_path / "test-proj"
    assert (proj / ".akoris" / "debt").is_dir()
    assert (proj / ".akoris" / "sprints" / "archive").is_dir()
    assert (proj / ".akoris" / "audits" / "archive").is_dir()
    assert (proj / "doc" / "tech" / "tests.md").is_file()
    assert (proj / "app" / "tests" / "README.md").is_file()


def test_init_copies_checklists(tmp_path):
    """N1 : checklists/ copié."""
    result = run_init("test-proj", tmp_path)
    assert result.returncode == 0, f"stderr: {result.stderr}"
    proj = tmp_path / "test-proj"
    assert (proj / "checklists").is_dir()
    assert (proj / "checklists" / "phase-0.md").is_file()
    assert (proj / "checklists" / "bootstrap.md").is_file()


def test_init_index_check_passes_on_fresh_project(tmp_path):
    """N1 : le projet frais garde un index valide avec ou sans PyYAML."""
    result = run_init("test-proj", tmp_path)
    assert result.returncode == 0, f"stderr: {result.stderr}"
    proj = tmp_path / "test-proj"
    yaml_check = subprocess.run(
        [sys.executable, "-c", "import yaml"], capture_output=True, text=True,
    )
    if yaml_check.returncode == 0:
        check = subprocess.run(
            [sys.executable, ".akoris/scripts/build-debt-index.py", "--check"],
            cwd=str(proj), capture_output=True, text=True,
        )
        assert check.returncode == 0, (
            f"--check a échoué sur projet frais. stderr: {check.stderr}, stdout: {check.stdout}"
        )
    else:
        assert "PyYAML non détecté" in result.stdout
        assert (proj / ".akoris/debt/index.md").read_text(encoding="utf-8") == (
            (REPO_ROOT / "templates/.akoris/debt/index.md").read_text(encoding="utf-8")
        )
