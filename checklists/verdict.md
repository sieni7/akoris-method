# CHECKLIST — VERDICT (grille de décision)

> **Public :** Validator (humain)
> **Quand :** Après l'audit, avant le push
> **Durée :** 5 minutes
> **Référence :** `.akoris/contexte.md` §6 (verdicts) + §16 (seuils tests)

---

## Lecture des rapports

- [ ] Lire `.akoris/audits/audit_report.md` (QA)
- [ ] **Si sprint 🔒** : lire `.akoris/audits/audit_report-secops.md` (SecOps)
- [ ] Lire la recommandation de l'Auditor (`push` / `push avec réserves` / `ne pas push`)

---

## Grille QA

| Métrique | `go` | `go with reserve` | `no-go` |
|----------|------|-------------------|---------|
| Couverture TNR | ≥ 80% | 60-79% | < 60% |
| Tests TNR échoués | 0 | 0 (flaky doc.) | ≥ 1 |
| Tests E2E échoués | 0 | 0 (flaky doc.) | ≥ 1 |
| Scénarios UAT | 100% validés | 1 partiel | ≥ 1 échoué |
| Findings critiques | 0 | 0 | ≥ 1 |

**Verdict QA :**
- [ ] `go` si toutes les colonnes "go"
- [ ] `go with reserve` si au moins une colonne "reserve"
- [ ] `no-go` si au moins une colonne "no-go"

---

## Grille SecOps (si sprint 🔒)

| Métrique | `go` | `go with reserve` | `no-go` |
|----------|------|-------------------|---------|
| Findings critiques | 0 | 0 | ≥ 1 |
| Findings eleve | 0 | 0 | ≥ 1 |
| Findings moyens | 0 | 1-3 | > 3 |

**Verdict SecOps :**
- [ ] `go` si 0 critique, 0 eleve, 0 moyen
- [ ] `go with reserve` si 0 critique, 0 eleve, 1-3 moyens
- [ ] `no-go` si ≥ 1 critique OU ≥ 1 eleve

**Règle : sécu critique. 1 critique = no-go global, même si QA=go.**

---

## Composition (sprint 🔒)

```
verdict_global = no-go           si QA=no-go OU SecOps=no-go
verdict_global = go_with_reserve si QA=reserve OU SecOps=reserve
verdict_global = go              si QA=go ET SecOps=go
```

- [ ] Calculer `verdict_global`
- [ ] L'écrire dans `state.md` (champ `verdict_global`)

---

## Dettes à ouvrir (si `go with reserve`)

- [ ] Lister les findings "reserve" (QA + SecOps)
- [ ] Pour chaque : créer une dette (via Orchestrator, ID auto)
- [ ] Remplir `state.md` `reserves: [DT-NNN, ...]`

---

## Taper le verdict (onglet C)

- [ ] Si `go` :
  ```
  go
  ```
- [ ] Si `go with reserve` :
  ```
  go with reserve: <détails des réserves, séparés par virgule>
  ```
  Exemple : `go with reserve: auth sans refresh token, tests partiels paiement`
- `go with reserve` sans détail → **refusé : aucun verdict enregistré, le Validator reformule**.
- [ ] Si `no-go` :
  ```
  no-go: <raison>
  ```
  Exemple : `no-go: critères CA2 et CA4 non couverts, tests rouges`

---

## Post-verdict

- [ ] Le `state.md` reflète le verdict
- [ ] Si `go` ou `go with reserve` → passer à la phase PUSH (onglet B)
- [ ] Si `no-go` → retour à l'Orchestrator (onglet A) pour re-planification
- [ ] Si `go with reserve` → vérifier que les dettes sont créées
