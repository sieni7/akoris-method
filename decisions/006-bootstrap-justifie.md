# Décision 006 — Bootstrap justifié

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 1-2 (fondations)

---

## Décision

À chaque phase du bootstrap, l'Orchestrator **justifie** sa démarche. Le Validator **réitère `go`** ou **corrige**.

## Règles

- Chaque phase : "Ce que je propose" + "Justification" + "Risques/alternatives" + STOP.
- Le Validator lit, corrige si besoin, tape `go` (ou reformule).
- Pas de passage à la phase suivante sans `go`.

## Justification

- Le bootstrap est **fondationnel** : une erreur ici se propage.
- La justification force la transparence.
- Le Validator peut corriger **avant** que l'erreur ne s'installe.

## Alternatives écartées

- **Bootstrap automatique** : risqué, non contrôlé.
- **Bootstrap sans justification** : boîte noire.
- **Validation a posteriori** : trop tard.
