# Décision 024 — Branches : main + sprint-NN

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

Une branche par sprint (`sprint-NN`) + `main`. Merge dans `main` après verdict `go`.

## Règles

- `main` = état validé, toujours déployable.
- `sprint-NN` = travail en cours.
- Merge après `go` (Validator) + push (Builder).
- Pas de push après `no-go`.
- Pas de force-push.

## Justification

- **Isolation** par sprint.
- **Rollback** facile (abandonner une branche = annuler un sprint).
- **`main` = état validé** (toujours déployable).

## Alternatives écartées

- **`main` only** : pas d'isolation.
- **`main` + `dev` + `sprint`** : overkill pour un solo.
- **Feature branches** : pas adapté au rythme sprint.
