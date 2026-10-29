# Décision 021 — Création d'une dette

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 4 (gouvernance)

---

## Décision

Le Validator **décide** l'ouverture (verdict `go with reserve`), l'Orchestrator **crée** le fichier (ID auto = dernier + 1).

## Règles

- Validator tranche : `go with reserve: <détails>`.
- Orchestrator crée `DT-NNN-titre.md` avec ID auto, champs remplis.
- Le Validator peut **éditer** ensuite.
- Le Builder **met à jour le statut** (pas l'index).

## Justification

- **ID séquentiel déterministe** (calculé par l'Orchestrator).
- **Séparation** : décision (humain) vs matérialisation (agent).
- **Traçabilité** : le Validator voit la dette créée.

## Alternatives écartées

- **Validator crée tout** : charge manuelle, risque d'oubli.
- **Builder crée** : sort de son rôle (il résorbe, il n'ouvre pas).
- **Auditor crée** : sort de son rôle (il propose, il ne décide pas).

> Clarifiée partiellement par ADR-049 (2026-10-28).
