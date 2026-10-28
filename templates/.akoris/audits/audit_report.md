# AUDIT REPORT (QA) — Sprint <NN>

> Rapport d'audit QA. Écrit par l'Auditor (onglet C).
> Ne mélange JAMAIS QA et SecOps (voir `audit_report-secops.md`).

---

## Métadonnées

- **Sprint :** <NN>
- **Date :** <YYYY-MM-DD>
- **Auditeur :** Auditor QA
- **Branche :** sprint-<NN>
- **Commit audité :** <hash>

## Audit par tâche

| Tâche | Critère | Commit | Vérification | Statut |
|-------|---------|--------|--------------|--------|
| T1 | CA1 | <hash> | test passé | ✅ |
| T2 | CA2 | <hash> | test passé | ✅ |
| T3 | CA3 | <hash> | test échoué | ❌ |

## Audit TNR

- **Tests unitaires :** <N>/<N> verts
- **Tests intégration :** <N>/<N> verts
- **Couverture :** <N>%
- **Seuil :** ≥ 80% → ✅ | ⚠️ | ❌

## Audit E2E

- **Tests :** <N>/<N> verts (ou `na`)
- **Flaky :** <N> (documentés)

## Audit UAT

- **Scénarios :** <N>
- **Validés par le Validator :** <N>/<N>

## Findings

| # | Sévérité | Tâche | Description | Suggestion |
|---|----------|-------|-------------|------------|
| F1 | critique | T3 | <desc> | <suggestion> |
| F2 | élevé | T2 | <desc> | <suggestion> |
| F3 | moyen | T1 | <desc> | <suggestion> |
| F4 | mineur | T1 | <desc> | <suggestion> |

## Recommandation de push

- **Verdict QA :** `go` | `go with reserve` | `no-go`
- **Justification :** <raison>
- **Dettes à ouvrir :** DT-NNN, DT-NNN
- **Recommandation push :** `push` | `push avec réserves` | `ne pas push`

## Message pour le Validator

<message synthétique>
