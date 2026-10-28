# Décision 014 — Roadmap figée mais évolutive

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 4 (gouvernance)

---

## Décision

La roadmap est **figée** au bootstrap. Elle est modifiable **uniquement par le Validator** avec `go`, et **ADR obligatoire** si le changement est structurant.

## Règles

- Figée par défaut : l'Orchestrator ne la réécrit pas.
- Modifiable par le Validator avec `go`.
- Changement structurant (capacité majeure, dépendance) → ADR obligatoire.
- Changement non structurant (réordonner, splitter) → `go` suffit.

## Justification

- Évite le scope creep silencieux.
- La roadmap reste un outil humain, pas un dogme.
- Traçabilité des changements structurants (ADR).

## Alternatives écartées

- **Figée totalement** : irréaliste.
- **Évolutive librement** : chaos, dérive.
- **Modifiable sans ADR** : perte de traçabilité.
