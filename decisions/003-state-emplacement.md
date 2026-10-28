# Décision 003 — Emplacement de state.md

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 1-2 (fondations)

---

## Décision

`state.md` vit dans `.akoris/state.md` (gouvernance), pas à la racine du projet.

## Règles

- Emplacement : `.akoris/state.md`.
- Pas de `state.md` à la racine.
- Pas de `state.md` dans `app/` ou `doc/`.

## Justification

- `state.md` est de la **gouvernance**, pas du produit.
- Cohérence avec les 3 piliers (`app/`, `doc/`, `.akoris/`).
- Un seul endroit pour le verrou.

## Alternatives écartées

- **Racine** : mélange gouvernance et produit.
- **Dans app/** : pollue le code.
- **Dans doc/** : mélange documentation et état.
