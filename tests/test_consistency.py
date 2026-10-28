"""Tests de cohérence des règles dans le repo."""

from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_no_singular_task_commit_rule():
    """N2 : aucun document contrôlé ne doit imposer un seul commit par tâche."""
    files_to_check = [
        "templates/.akoris/contexte.md",
        "templates/.akoris/config/agents/builder.md",
        "templates/.akoris/config/bootstrap.md",
        "checklists/sprint.md",
        "templates/.akoris/roadmap/sprint-NN.md",
        "CHANGELOG.md",
    ]
    for f in files_to_check:
        content = read(f)
        # Composer le motif pour que le grep global ne se détecte pas lui-même.
        import re
        singular_rule = "1 tâche = 1 " + "commit"
        matches = re.findall(re.escape(singular_rule) + r"(?!s)", content)
        assert not matches, f"{f} contient encore la règle du commit unique par tâche"


def test_no_context_md_modification_by_orchestrator():
    """N5 : bootstrap.md et phase-0.md ne doivent pas dire 'adapter contexte.md'."""
    files_to_check = [
        "templates/.akoris/config/bootstrap.md",
        "checklists/bootstrap.md",
        "checklists/phase-0.md",
        "README.md",
    ]
    for f in files_to_check:
        content = read(f).lower()
        # Chercher "adapter contexte.md" ou "compléter contexte.md"
        import re
        bad = re.findall(r"(adapter|compléter|modifier)\s+[`.]*contexte\.md", content)
        assert not bad, f"{f} contient encore une instruction d'éditer contexte.md"


def test_decision_049_exists():
    """La décision 049 doit exister (corrections Bloc 11)."""
    assert (REPO_ROOT / "decisions/049-corrections-bloc-11.md").is_file()


def test_decision_049_has_four_sections():
    """Décision 049 : exactement 4 sections ##."""
    content = read("decisions/049-corrections-bloc-11.md")
    import re
    sections = re.findall(r"^## ", content, re.MULTILINE)
    assert len(sections) == 4, f"Attendu 4 sections ##, obtenu {len(sections)}"


def test_locked_by_rules_consistent():
    """N4 : contexte.md §9 nomme qui écrit/lit locked_by."""
    content = read("templates/.akoris/contexte.md")
    assert "écrit" in content.lower() and "locked_by" in content
    assert "libère" in content.lower() and "locked_by" in content
