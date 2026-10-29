# Décision 002 — Verrou state.md

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 1-2 (fondations)

---

## Décision

Un fichier unique `.akoris/state.md` sert de **machine à états** et de **verrou**. Un seul agent peut agir à la fois (`locked_by`).

## Règles

- Un seul `locked_by` à la fois.
- Un agent n'agit que si `next_agent == lui` ET `action == go` ET `GO` humain reçu.
- Lecture de `state.md` au **début** du tour, écriture **en dernier**.
- Si `locked_by != moi` → l'agent répond "pas mon tour" et s'arrête.
- `state.md` commité en clôture de sprint (`chore(state)`).

## Justification

- Élimine les collisions d'écriture entre agents.
- Traçabilité de l'état à chaque instant.
- Pas de coordination directe entre LLM (qui serait chaotique).

## Alternatives écartées

- **Fichier lock** : plus fragile (oubli de suppression).
- **Tour de rôle implicite** : sujet aux dérives.
- **Pas de verrou** : chaos garanti.

> Clarifiée partiellement par ADR-049 (2026-10-28).
