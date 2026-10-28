# Décision 032 — Structure app/tests/

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

Les tests vivent dans `app/tests/` avec 5 sous-dossiers : `unit/`, `integration/`, `e2e/`, `uat/`, `fixtures/`.

## Règles

- `unit/` : tests unitaires (TNR).
- `integration/` : tests d'intégration (TNR).
- `e2e/` : tests E2E (placeholder si V0 sans E2E).
- `uat/` : scénarios UAT (placeholder V1).
- `fixtures/` : données de test partagées.
- `README.md` : lien vers `doc/tech/tests.md`.

## Justification

- **Standard** : `unit/`, `integration/`, `e2e/` sont universels.
- **Placeholders** : structure prévisible même si vide.
- **Fixtures séparées** : évite la duplication.

## Alternatives écartées

- **Plate** : illisible > 20 tests.
- **Par feature** : mélange les familles.
- **Hybride 4 niveaux** : trop profond.
