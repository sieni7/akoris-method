# Décision 019 — Script Python build-debt-index

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 6 (scripts)

---

## Décision

L'index des dettes est généré par un **script Python** (`templates/.akoris/scripts/build-debt-index.py`).

## Règles

- Python 3 + `pyyaml`.
- 3 modes : défaut (régénère), `--check` (compare, CI), `--check-thresholds` (seuils, CI).
- Exit 1 si divergence ou seuil dépassé.
- Seuils : `P0/P1 > 3`, `total > 10`.

## Justification

- **Parsing YAML robuste** (pyyaml).
- **Validation de schéma** (11 champs, valeurs autorisées).
- **Testable** (pytest).
- **Portable** (Python 3 présent partout).

## Alternatives écartées

- **Bash** : parsing fragile, illisible.
- **Node.js** : dépendance Node pas toujours présente.
- **Go** : overkill pour un script de 100 lignes.
