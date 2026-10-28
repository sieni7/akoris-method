# Décision 048 — Mode équipe + validate-method

- **Statut :** V2 / non implémentée
- **Date :** 2026-10-28
- **Contexte :** Bloc 8d (process)

---

## Décision

AKORIS supporte le **mode équipe** (PR + protection de branche) et fournit un script **`validate-method`** qui vérifie la cohérence des règles.

## Règles

### Mode équipe

- Le `go` du Validator **devient** une **approbation GitHub** (review) sur la PR.
- **Protection de branche** : `main` protégée, merge via PR seulement.
- **Nouveau rôle** : `Reviewer` (2e humain) qui peut approuver au lieu du Validator.
- `state.md` est **synchrone** avec la PR (le verdict est un label GitHub).

### validate-method

- **Problème** : les règles sont dupliquées dans `decisions/`, `contexte.md`, `checklists/`, `agents/` → divergent.
- **Solution** : un script `akoris validate-method` qui vérifie la cohérence.
- **Mécanique** :
  - Lit `METHOD.md` (source de vérité).
  - Vérifie que `decisions/`, `contexte.md`, `checklists/`, `agents/` sont **synchrones**.
  - Exit 1 si divergence.

### V1 vs V2

- V1 : mode solo uniquement.
- V2 : mode équipe + validate-method.

## Justification

- **Mode équipe** : AKORIS sort du solo (tech leads, ch. 0.7).
- **validate-method** : le repo respecte son propre principe n°2 (« une seule source de vérité »).
- **Traçabilité** : les règles ne divergent plus.

## Alternatives écartées

- **Mode solo uniquement** : pas adapté aux équipes.
- **Pas de validate-method** : les règles divergent.
- **Règles dans un seul fichier** : `contexte.md` deviendrait énorme.
