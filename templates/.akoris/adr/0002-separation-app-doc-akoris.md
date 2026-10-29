# ADR-0002 — Séparation app/ · doc/ · .akoris/

- **Date :** <YYYY-MM-DD>
- **Statut :** accepté
- **Décideur :** Validator
- **Sprint d'origine :** 1

---

## Contexte

Le projet doit séparer trois natures : le code exécutable, la documentation
et la gouvernance. Sans séparation, ces trois natures se mélangent.

## Options envisagées

1. **Tout dans un seul dossier** — simple, mais mélange les natures
2. **app/ + methode/** — 2 piliers, doc noyée
3. **app/ + doc/ + .akoris/** — 3 piliers, séparation claire

## Décision

Trois piliers : `app/` (exécutable), `doc/` (documentaire), `.akoris/` (gouvernance).

## Conséquences

- ✅ Séparation des natures, propriétaires clairs
- ✅ Chaque pilier a son cycle de vie
- ⚠️ Un dossier de plus à gérer

## Alternatives écartées

- **2 piliers** : doc noyée
- **1 pilier** : chaos

## Références

- Décision 022 (documentation 3e pilier)
