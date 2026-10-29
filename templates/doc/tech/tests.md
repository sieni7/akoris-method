# Stratégie de tests — <nom-du-projet>

> Référentiel de tests (décision 033). Lu par l'Auditor avant d'auditer,
> par le Validator avant de trancher, par le Builder avant d'écrire.

## Familles actives (V0)

| Famille | V0 | V1 | V2 |
|---------|-----|-----|-----|
| TNR (unit + integration) | ✅ Obligatoire | ✅ | ✅ |
| Sécu (checkpoint 🔒) | ✅ Checkpoint | ✅ | ✅ |
| UAT (acceptation) | ⚠️ Implicite (verdict) | ✅ Formelle | ✅ |
| E2E | ⚠️ 1 si parcours critique | ✅ | ✅ |
| Perf | ❌ | ❌ | ✅ |

## Où

- `app/tests/unit/` — TNR unitaire
- `app/tests/integration/` — TNR intégration
- `app/tests/e2e/` — E2E (placeholder si V0 sans E2E)
- `app/tests/uat/` — UAT (placeholder V1)
- `app/tests/fixtures/` — données partagées

## Comment exécuter

- `pytest` (ou équivalent selon la stack)
- CI : `.github/workflows/ci.yml`

## Seuils

| Métrique | go | go with reserve | no-go |
|----------|-----|-----------------|-------|
| Couverture TNR | ≥ 80% | 60-79% | < 60% |
| Tests TNR échoués | 0 | 0 (flaky doc.) | ≥ 1 |
| Tests E2E échoués | 0 | 0 (flaky doc.) | ≥ 1 |
| Scénarios UAT | 100% validés | 1 partiel | ≥ 1 échoué |
| Findings sécu critiques | 0 | 0 | ≥ 1 |
| Findings sécu élevés | 0 | 0 | ≥ 1 |
| Findings sécu moyens | 0 | 1-3 | > 3 |

## Grille de verdicts

Voir `checklists/verdict.md` (grille par famille).
