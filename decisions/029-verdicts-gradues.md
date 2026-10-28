# Décision 029 — Verdicts gradués

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 1-2 (fondations)

---

## Décision

Trois verdicts possibles dans l'onglet C : `go`, `go with reserve`, `no-go`.

## Règles

- `go` : clôture propre.
- `go with reserve: <détails>` : clôture + ouverture de dette(s). Détails **obligatoires**.
- `no-go: <raison>` : retour arrière, re-planification. Raison **obligatoire**.
- `go with reserve` **sans détail** : **refusé explicitement**. Le Validator doit reformuler. **Pas d'approbation silencieuse.**
- `no-go` **sans raison** : **refusé explicitement**. Le Validator doit reformuler.

## Justification

- Un `GO` binaire est trop pauvre.
- Le `go with reserve` permet d'avancer **avec des réserves tracées**.
- Le `no-go` motive le retour arrière.
- Le refus explicite évite les ambiguïtés (reviewer).

## Alternatives écartées

- **GO binaire** : pas de réserves.
- **Score numérique** : subjectif, non standard.
- **Verdict sans détail** : promesse orale qui s'évapore.
- **`go with reserve` = go** : approbation silencieuse, contredit la traçabilité.
