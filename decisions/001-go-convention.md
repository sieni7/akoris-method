# Décision 001 — Convention GO

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 1-2 (fondations)

---

## Décision

Le Validator (humain) tape `go` (ou un verdict) **dans l'onglet concerné** pour autoriser un agent à agir. Sans `GO`, l'agent attend.

## Règles

- Onglet A : `go` uniquement (autorise la planification).
- Onglet B : `go` uniquement (autorise l'exécution, puis le push).
- Onglet C : `go` (lance l'audit), puis verdict (`go` / `go with reserve` / `no-go`).
- `no-go` formel **uniquement dans C**.
- En A et B : `go` ou rien.

## Justification

- Un mot-clé simple, mémorisable, sans ambiguïté.
- Le Validator reste aux commandes à chaque transition.
- Séparation nette : autorisation (A/B) vs jugement (C).

## Alternatives écartées

- **Bouton UI** : dépendant d'un outil, non réplicable.
- **Fichier trigger** : moins lisible, plus technique.
- **Automatique** : casse la règle "l'autorité humaine décide".
