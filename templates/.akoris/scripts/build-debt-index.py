#!/usr/bin/env python3
"""
build-debt-index.py — Génère .akoris/debt/index.md depuis les fichiers DT-NNN.md.

Usage :
    python build-debt-index.py [--check] [--check-thresholds] [--debt-dir DIR]

Modes :
    (défaut)            : régénère index.md
    --check             : régénère en mémoire et compare avec index.md existant.
                          Exit 1 si divergence (CI).
    --check-thresholds  : vérifie les seuils anti-accumulation.
                          Avertit si P0/P1 > 3 ou total > 10, sans bloquer.
    --debt-dir DIR      : chemin vers .akoris/debt/ (défaut: .akoris/debt)

Dépendances : pyyaml (pip install pyyaml)
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERREUR : PyYAML requis. Installe-le : pip install pyyaml", file=sys.stderr)
    sys.exit(2)

REQUIRED_FIELDS = [
    "id", "titre", "priorite", "statut", "sprint_origine",
    "decision_origine", "adr_lie", "risque", "impact",
    "sprint_resorption_prevu", "cree_le",
]

VALID_PRIORITES = {"P0", "P1", "P2", "P3"}
VALID_STATUTS = {"ouverte", "en_cours", "resorbee", "acceptee_definitivement"}
VALID_IMPACTS = {"faible", "moyen", "eleve", "critique"}

THRESHOLD_P0_P1 = 3
THRESHOLD_TOTAL = 10


def parse_frontmatter(path: Path) -> dict:
    """Extrait le YAML frontmatter d'un fichier Markdown.

    Format attendu : le fichier commence par `---\n`, se termine par `\n---\n`.
    Robuste aux `---` dans les valeurs YAML (ex. `risque: "a --- b"`).
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path.name} : pas de frontmatter YAML (doit commencer par '---\\n')")
    # Chercher le prochain '\n---' APRÈS le début (index 4)
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"{path.name} : frontmatter YAML incomplet (manque le '---' de fermeture)")
    frontmatter = text[4:end]
    data = yaml.safe_load(frontmatter)
    if not isinstance(data, dict):
        raise ValueError(f"{path.name} : frontmatter YAML n'est pas un dict")
    return data


def validate(data: dict, path: Path) -> list[str]:
    """Valide les champs obligatoires et les valeurs autorisées. Retourne une liste d'erreurs."""
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"{path.name} : champ manquant '{field}'")
    if data.get("priorite") not in VALID_PRIORITES:
        errors.append(f"{path.name} : priorite '{data.get('priorite')}' invalide (attendu: {VALID_PRIORITES})")
    if data.get("statut") not in VALID_STATUTS:
        errors.append(f"{path.name} : statut '{data.get('statut')}' invalide (attendu: {VALID_STATUTS})")
    if data.get("impact") not in VALID_IMPACTS:
        errors.append(f"{path.name} : impact '{data.get('impact')}' invalide (attendu: {VALID_IMPACTS})")
    return errors


def scan_debts(debt_dir: Path) -> list[dict]:
    """Scanne tous les DT-NNN-*.md et retourne leurs données validées."""
    if not debt_dir.exists():
        raise FileNotFoundError(f"Dossier introuvable : {debt_dir}")

    debts = []
    errors = []
    for path in sorted(debt_dir.glob("DT-*.md")):
        try:
            data = parse_frontmatter(path)
            errs = validate(data, path)
            if errs:
                errors.extend(errs)
                continue
            debts.append(data)
        except (ValueError, yaml.YAMLError) as e:
            errors.append(str(e))

    if errors:
        print("ERREURS DE VALIDATION :", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    return debts


def generate_index(debts: list[dict]) -> str:
    """Génère le contenu de index.md."""
    lines = [
        "# INDEX DES DETTES — généré automatiquement",
        "> Ne pas éditer à la main. Régénérer via `scripts/build-debt-index.py`.",
        "",
        "| ID | Titre | Priorité | Statut | Sprint origine | Sprint résorption | ADR |",
        "|----|-------|----------|--------|----------------|-------------------|-----|",
    ]
    for d in sorted(debts, key=lambda x: x["id"]):
        lines.append(
            f"| {d['id']} | {d['titre']} | {d['priorite']} | {d['statut']} | "
            f"{d['sprint_origine']} | {d['sprint_resorption_prevu']} | {d['adr_lie']} |"
        )

    total = len(debts)
    open_debts = [d for d in debts if d["statut"] in ("ouverte", "en_cours")]
    p0_p1_open = [d for d in open_debts if d["priorite"] in ("P0", "P1")]

    lines.extend([
        "",
        "---",
        "",
        "## Résumé",
        "",
        f"- **Total dettes :** {total}",
        f"- **Ouvertes / en cours :** {len(open_debts)}",
        f"- **P0/P1 ouvertes :** {len(p0_p1_open)} (seuil : {THRESHOLD_P0_P1})",
        f"- **Total ouvertes :** {len(open_debts)} (seuil : {THRESHOLD_TOTAL})",
        "",
    ])
    return "\n".join(lines)


def check_thresholds(debts: list[dict]) -> bool:
    """Retourne True si les seuils sont respectés, False sinon."""
    open_debts = [d for d in debts if d["statut"] in ("ouverte", "en_cours")]
    p0_p1_open = [d for d in open_debts if d["priorite"] in ("P0", "P1")]

    ok = True
    if len(p0_p1_open) > THRESHOLD_P0_P1:
        print(f"SEUIL DÉPASSÉ : {len(p0_p1_open)} dettes P0/P1 ouvertes > {THRESHOLD_P0_P1}", file=sys.stderr)
        ok = False
    if len(open_debts) > THRESHOLD_TOTAL:
        print(f"SEUIL DÉPASSÉ : {len(open_debts)} dettes ouvertes > {THRESHOLD_TOTAL}", file=sys.stderr)
        ok = False
    return ok


def main():
    parser = argparse.ArgumentParser(description="Génère l'index des dettes AKORIS.")
    parser.add_argument("--check", action="store_true",
                        help="Vérifie que index.md est à jour (exit 1 si divergence).")
    parser.add_argument("--check-thresholds", action="store_true",
                        help="Avertit si les seuils anti-accumulation sont dépassés (ne bloque pas).")
    parser.add_argument("--debt-dir", type=Path, default=Path(".akoris/debt"),
                        help="Chemin vers .akoris/debt/ (défaut: .akoris/debt)")
    args = parser.parse_args()

    debts = scan_debts(args.debt_dir)
    index_content = generate_index(debts)
    index_path = args.debt_dir / "index.md"

    if args.check_thresholds:
        check_thresholds(debts)  # Affiche les warnings mais ne bloque plus
        index_path.write_text(index_content, encoding="utf-8")
        print(f"index.md régénéré ({len(debts)} dettes).")
        sys.exit(0)

    if args.check:
        if not index_path.exists():
            print(f"ERREUR : {index_path} n'existe pas.", file=sys.stderr)
            sys.exit(1)
        existing = index_path.read_text(encoding="utf-8")
        if existing.strip() != index_content.strip():
            print("ERREUR : index.md n'est pas à jour. Régénère-le.", file=sys.stderr)
            sys.exit(1)
        print("index.md est à jour.")
        sys.exit(0)

    index_path.write_text(index_content, encoding="utf-8")
    print(f"index.md régénéré ({len(debts)} dettes).")


if __name__ == "__main__":
    main()
