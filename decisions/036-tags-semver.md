# Décision 036 — Tags SemVer

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

Les tags suivent **SemVer** (`vMAJOR.MINOR.PATCH`), proposés par l'Orchestrator, validés par le Validator, posés par le Builder après merge.

## Règles

- Format : `vMAJOR.MINOR.PATCH`.
- MAJOR = breaking change (ADR obligatoire).
- MINOR = feature rétrocompatible.
- PATCH = fix rétrocompatible.
- `v0.1.0` au bootstrap.
- Tag posé après merge dans `main`.
- Changelog dans `doc/produit/changelog.md` (généré).

## Justification

- **Standard** : SemVer est universel.
- **Sémantique claire** : MAJOR/MINOR/PATCH.
- **Changelog auto** : Conventionnel Commits + SemVer.
- **Rollback précis** : on sait ce qui a changé.

## Alternatives écartées

- **Pas de tags** : pas de version, pas de rollback.
- **Tags par sprint** : ne dit rien de la sémantique.
- **Date** : tri fragile.
