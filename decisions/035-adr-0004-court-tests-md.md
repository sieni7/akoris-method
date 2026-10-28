# Décision 035 — ADR-0004 court + tests.md détaillé

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 4 + Bloc 5

---

## Décision

L'ADR-0004 (stratégie de tests) est **court** (décision). Le détail est dans `doc/tech/tests.md` (manuel).

## Règles

- ADR-0004 : 10-15 lignes (décision + conséquences).
- `doc/tech/tests.md` : 50-100 lignes (seuils, structure, exécution).
- Pas de duplication entre les deux.
- ADR = gouvernance (immuable). Doc = documentation (évolutive).

## Justification

- **Séparation des natures** : ADR = décision, doc = manuel.
- **ADR court** : lisible, mémorisable.
- **Doc détaillé** : opérationnel.

## Alternatives écartées

- **ADR long** : perd sa nature de décision.
- **Pas de doc** : ADR trop court pour être opérationnel.
- **Deux ADR** : confusion.
