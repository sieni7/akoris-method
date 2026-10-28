# Décision 034 — Grille de verdicts par famille

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

La grille de verdicts est **par famille** (TNR, E2E, UAT, sécu), pas globale.

## Règles

- Chaque famille a ses seuils (voir décision 031).
- L'Auditor rapporte par famille.
- Le Validator tranche par famille.
- Composition aux sprints `🔒` (voir décision 028).

## Justification

- **Granularité** : chaque famille a sa sémantique.
- **Nuances** : TNR ✅ + sécu ⚠️ → `go with reserve`.
- **Traçabilité** : on sait **quelle** famille a échoué.

## Alternatives écartées

- **Globale** : masque les nuances.
- **Par tâche** : trop granulaire.
- **Sans grille** : subjectif.
