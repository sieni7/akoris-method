# Décision 044 — CLI — State machine

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 8d (process)

---

## Décision

Le CLI valide les transitions d'état via une **state machine** explicite, appliquée en pre-commit et en CI.

## Règles

### Transitions autorisées

```typescript
const TRANSITIONS = {
  'idle → plan': ['orchestrator'],
  'plan → execution': ['builder'],
  'execution → audit': ['auditor'],
  'audit → review': ['validator'],
  'review → closed': ['validator'],
  'review → plan': ['validator'],  // no-go
};
```

### Validation

- Le CLI vérifie que la transition est autorisée **avant** d'écrire `state.md`.
- Si non autorisée, le CLI refuse et affiche un message clair.
- `validate-state` est exécuté en pre-commit et en CI (exit 1 si invalide).

### Champs obligatoires

- `next_agent`, `action`, `locked_by` doivent être cohérents.
- `locked_by` ne peut être non-null que si `action == go`.

## Justification

- **Application** : la gouvernance n'est plus un jeu de rôle (reviewer).
- **Robustesse** : empêche les transitions invalides.
- **Traçabilité** : chaque transition est validée.

## Alternatives écartées

- **Pas de state machine** : les agents peuvent tout écrire.
- **Validation manuelle** : oublis, erreurs.
- **State machine dans les prompts** : appliquée par bonne volonté, pas par l'outil.
