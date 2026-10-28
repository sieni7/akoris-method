# Décision 023 — Git : Builder commit + push, Conventional Commits

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

Le **Builder commit** et **push** (après verdict `go`). Les commits suivent **Conventional Commits** avec footer `Sprint:` et `Tâche:`.

## Règles

- Format : `<type>(<scope>): <desc>` + footer `Sprint: NN`, `Tâche: TN`, `Refs:`.
- Types : `feat`, `fix`, `feat!`/`BREAKING CHANGE:`, `docs`, `test`, `refactor`, `chore`, `sec`.
- `commitlint` en CI rejette les non-conformes.
- Builder commit (fin de tour) + Builder push (après verdict `go`).
- Deux tapes : `go` dans C (verdict) + `go` dans B (push).

## Justification

- **Standard** : Conventional Commits = changelog auto, SemVer auto.
- **Traçabilité** : footer `Sprint:` + `Tâche:`.
- **Un seul acteur git** : le Builder (commit + push).

## Alternatives écartées

- **`<sprint> <type>`** : casse le parsing Conventional Commits.
- **Validator push** : casse le flux.
- **Auditor push** : sort de son rôle.
