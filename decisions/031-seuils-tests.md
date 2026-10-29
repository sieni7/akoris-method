# Décision 031 — Seuils de tests et définition des findings

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

Seuils objectifs : couverture **≥ 80%** (go), **60-79%** (reserve), **< 60%** (no-go). **0 test échoué**, **0 finding critique**.

## Règles

### Seuils

| Métrique | go | go with reserve | no-go |
|----------|-----|-----------------|-------|
| Couverture TNR | ≥ 80% | 60-79% | < 60% |
| Tests TNR échoués | 0 | 0 (flaky doc.) | ≥ 1 |
| Tests E2E échoués | 0 | 0 (flaky doc.) | ≥ 1 |
| Scénarios UAT | 100% | 1 partiel | ≥ 1 échoué |
| Findings critique | 0 | 0 | ≥ 1 |
| Findings eleve | 0 | 0 | ≥ 1 |
| Findings moyen | 0 | 1-3 | > 3 |

### Définition des findings

| Sévérité | Définition | Exemple |
|----------|-----------|---------|
| **critique** | Bloque la livraison, risque sécurité/prod | Secret exposé, injection SQL, CVE critique |
| **eleve** | Impact fort, à corriger avant prod | Auth manquante, CVE eleve, dépendance abandonnée |
| **moyen** | Impact modéré, à tracer | Couverture sous seuil, code dupliqué, TODO non tracé |
| **faible** | Impact faible, informatif | Style, commentaire obsolète, nommage |

## Justification

- **80%** = standard de facto.
- **0 test échoué** = non négociable.
- **0 finding critique** = non négociable.
- **Définition des findings** : sans, les grilles sont inutilisables (reviewer).

## Alternatives écartées

- **Laxiste (60%)** : dette qualité rapide.
- **Strict (90%)** : no-go fréquent, paralyse.
- **Sans définition des findings** : subjectif.
