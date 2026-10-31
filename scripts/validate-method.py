#!/usr/bin/env python3
"""
validate-method.py — Vérifie la cohérence du référentiel AKORIS.
Usage : python scripts/validate-method.py [--strict] [--repo-root PATH]
"""

import argparse
import re
import sys
from pathlib import Path

CRITICAL_FILES = [
    "README.md", "README.en.md", "METHOD.md", "CHANGELOG.md",
    "CONTACT.md", "LICENSE", ".github/workflows/ci.yml",
    "docs/00-introduction-akoris.md", "scripts/init-project.sh",
    "templates/.akoris/contexte.md", "templates/.akoris/state.md",
    "templates/.akoris/projet.md", "templates/.akoris/config/bootstrap.md",
    "templates/.akoris/config/agents/orchestrator.md",
    "templates/.akoris/config/agents/builder.md",
    "templates/.akoris/config/agents/auditor.md",
    "templates/.akoris/scripts/build-debt-index.py",
    "templates/.akoris/debt/_template.md",
    "templates/.akoris/roadmap/ROADMAP.md",
    "templates/.akoris/roadmap/sprint-NN.md",
    "templates/.akoris/sprints/current_sprint.md",
    "templates/.akoris/sprints/sprint_report.md",
    "templates/.akoris/sprints/sprint-NN-git.md",
    "templates/.akoris/audits/audit_report.md",
    "templates/.akoris/audits/audit_report-secops.md",
    "templates/doc/tech/README.md", "templates/doc/tech/tests.md",
    "templates/doc/produit/README.md", "templates/doc/produit/changelog.md",
]

FOUNDING_ADRS = [
    "templates/.akoris/adr/0001-stack-initiale.md",
    "templates/.akoris/adr/0002-separation-app-doc-akoris.md",
    "templates/.akoris/adr/0003-convention-go.md",
    "templates/.akoris/adr/0004-strategie-tests.md",
]

DECISION_SECTIONS = ["Décision", "Règles", "Justification", "Alternatives"]
CONTEXTE_SECTIONS = [f"§{i}" for i in range(23)]
LINK_REGEX = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
ABSOLUTE_PATH_REGEX = re.compile(r"(?<![\w])/(?:home|tmp|Users|var|etc|opt|root)/")


class Result:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.checks = 0
        self.passed = 0
        self.current_check_has_error = False

    def ok(self, name):
        self.checks += 1
        if not self.current_check_has_error:
            self.passed += 1
        self.current_check_has_error = False

    def error(self, msg):
        self.errors.append(msg)
        self.current_check_has_error = True

    def warning(self, msg):
        self.warnings.append(msg)

    def summary(self):
        return (
            f"Vérifications : {self.passed}/{self.checks} passées\n"
            f"Erreurs : {len(self.errors)}\n"
            f"Warnings : {len(self.warnings)}"
        )


def check_decisions(repo, r):
    d = repo / "decisions"
    if not d.exists():
        r.error("decisions/ absent")
        return
    files = sorted(d.glob("*.md"))
    nums = [int(m.group(1)) for f in files if (m := re.match(r"^(\d{3})-", f.name))]
    missing = [n for n in range(1, 51) if n not in nums]
    if missing:
        r.error(f"Décisions manquantes : {missing}")
    else:
        r.ok("50 décisions numérotées (001-050)")
    for f in files:
        c = f.read_text(encoding="utf-8")
        for s in DECISION_SECTIONS:
            if f"## {s}" not in c:
                r.error(f"{f.name} : section '## {s}' manquante")
    r.ok(f"{len(files)} décisions ont 4 sections")


def check_contexte(repo, r):
    p = repo / "templates/.akoris/contexte.md"
    if not p.exists():
        r.error("contexte.md absent")
        return
    c = p.read_text(encoding="utf-8")
    missing = [
        s for s in CONTEXTE_SECTIONS
        if not re.search(rf"^## {re.escape(s)}(?:\s|—|$)", c, re.M)
    ]
    if missing:
        r.error(f"contexte.md : sections manquantes : {missing}")
    else:
        r.ok("contexte.md a les 23 sections (§0-§22)")


def check_critical_files(repo, r):
    missing = [f for f in CRITICAL_FILES if not (repo / f).exists()]
    if missing:
        r.error(f"Fichiers critiques manquants : {missing}")
    else:
        r.ok(f"{len(CRITICAL_FILES)} fichiers critiques présents")


def check_founding_adrs(repo, r):
    missing = [f for f in FOUNDING_ADRS if not (repo / f).exists()]
    if missing:
        r.error(f"ADR fondateurs manquants : {missing}")
    else:
        r.ok("4 ADR fondateurs présents")


def check_links(repo, r):
    checked = 0
    broken = []
    for md in repo.rglob("*.md"):
        if ".git" in md.parts:
            continue
        c = md.read_text(encoding="utf-8", errors="ignore")
        for m in LINK_REGEX.finditer(c):
            url = m.group(2)
            if url.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if "?" in url:
                url = url.split("?")[0]
            if "#" in url:
                url = url.split("#")[0]
            if not url:
                continue
            if not (md.parent / url).resolve().exists():
                broken.append(f"{md.relative_to(repo)} → {url}")
            checked += 1
    if broken:
        for b in broken[:10]:
            r.error(f"Lien cassé : {b}")
        if len(broken) > 10:
            r.error(f"... et {len(broken)-10} autres")
    else:
        r.ok(f"{checked} liens Markdown valides")
    if checked < 20:
        r.warning("Peu de liens contrôlés")


def check_absolute_paths(repo, r):
    found = []
    templates_dir = repo / "templates"
    if not templates_dir.exists() or not any(p.is_file() for p in templates_dir.rglob("*")):
        r.warning("Dossier templates/ vide")
    for p in templates_dir.rglob("*"):
        if not p.is_file():
            continue
        try:
            c = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if ABSOLUTE_PATH_REGEX.search(c):
            found.append(p.relative_to(repo))
    if found:
        for f in found:
            r.error(f"Chemin absolu dans {f}")
    else:
        r.ok("Aucun chemin absolu dans templates")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--repo-root", type=Path, default=None)
    a = ap.parse_args()
    repo = a.repo_root or Path(__file__).resolve().parent.parent
    if not (repo / "METHOD.md").exists():
        print(f"ERREUR : {repo} n'est pas la racine AKORIS", file=sys.stderr)
        sys.exit(2)
    r = Result()
    print("=== Vérification de cohérence AKORIS ===\n")
    check_decisions(repo, r)
    check_contexte(repo, r)
    check_critical_files(repo, r)
    check_founding_adrs(repo, r)
    check_links(repo, r)
    check_absolute_paths(repo, r)
    print(r.summary())
    print()
    if r.errors:
        print("ERREURS :")
        [print(f"  ❌ {e}") for e in r.errors]
        print()
    if r.warnings:
        print("WARNINGS :")
        [print(f"  ⚠️  {w}") for w in r.warnings]
        print()
    if r.errors:
        sys.exit(1)
    if a.strict and r.warnings:
        sys.exit(1)
    print("✅ Cohérence OK.")
    sys.exit(0)


if __name__ == "__main__":
    main()
