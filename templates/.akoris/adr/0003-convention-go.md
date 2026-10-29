# ADR-0003 — Convention GO

- **Date :** <YYYY-MM-DD>
- **Statut :** accepté
- **Décideur :** Validator
- **Sprint d'origine :** 1

---

## Contexte

Les agents LLM (Orchestrator, Builder, Auditor) ne doivent pas agir sans
autorisation humaine. Il faut un mécanisme simple, mémorisable, traçable.

## Options envisagées

1. **Bouton UI** — dépendant d'un outil, non réplicable
2. **Fichier trigger** — moins lisible
3. **Mot-clé `go`** — simple, mémorisable, réplicable

## Décision

Convention GO : le Validator tape `go` (ou un verdict) dans l'onglet concerné.

- Onglet A : `go` uniquement (planification)
- Onglet B : `go` uniquement (exécution, push)
- Onglet C : `go` (audit), puis verdict (`go` / `go with reserve` / `no-go`)

## Conséquences

- ✅ Contrôle humain à chaque transition
- ✅ Traçable (dans state.md)
- ⚠️ Un tour de plus par transition

## Alternatives écartées

- **Bouton UI** : non réplicable
- **Automatique** : perte de contrôle

## Références

- Décision 001 (convention GO)
- Décision 029 (verdicts gradués)
