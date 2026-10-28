# Décision 017 — Registre des dettes : debt/ + index généré

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 4 (gouvernance)

---

## Décision

Les dettes vivent dans `.akoris/debt/` : **1 fichier par dette** (`DT-NNN-titre.md`) + un **`index.md` généré**.

## Règles

- 1 fichier/dette : `DT-NNN-titre-kebab.md`.
- `index.md` généré par `scripts/build-debt-index.py`.
- Pas de sous-dossiers dans `debt/`.
- ID séquentiel, jamais renuméroté.
- Une dette résorbée reste (son statut change).

## Justification

- **Symétrie avec `adr/`** : 1 fichier/décision, 1 fichier/dette.
- **Granularité** : une dette riche ne tient pas dans un append.
- **Parallélisation** : 2 agents sur 2 dettes = pas de collision.
- **Scalabilité** : 20+ dettes navigables.

## Alternatives écartées

- **`dette.md` unique** : illisible > 20 dettes, collisions d'écriture.
- **Sans `index.md`** : perte de la vue d'ensemble.
- **`index.md` manuel** : désynchronisation garantie.
