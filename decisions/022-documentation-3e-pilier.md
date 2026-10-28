# Décision 022 — Documentation : 3e pilier

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

La documentation est un **3e pilier** (`doc/`), à côté de `app/` (exécutable) et `.akoris/` (gouvernance).

## Règles

- `doc/tech/` : README, architecture, API, setup, tests → **Builder**.
- `doc/produit/` : pitch, guide utilisateur, changelog → **Orchestrator**.
- `doc/archive/` : versions obsolètes.
- Validator valide au verdict.
- Un sprint n'est `go` que si la doc impactée est à jour.

## Justification

- **3 natures** : exécutable, documentaire, gouvernance.
- **La doc est un livrable**, pas de la gouvernance.
- **Séparation des propriétaires** : Builder (tech), Orchestrator (produit).

## Alternatives écartées

- **`app/doc/`** : pollue le build.
- **`methode/doc/`** : faux (doc produit ≠ gouvernance).
- **Pas de `doc/`** : doc éparpillée ou absente.
