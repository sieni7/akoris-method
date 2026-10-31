# Chapitre 5 — La Qualité et l'Audit

## 1. La Stratégie de Tests : Les 5 Familles
Dans AKORIS, la qualité n'est pas une option négociable, elle est mesurée et tracée. La stratégie de tests repose sur 5 familles distinctes, dont les exigences évoluent selon la maturité du projet (V0, V1, V2) :

| Famille | Description | V0 | V1 | V2 |
|---|---|---|---|---|
| **TNR** | Tests Non Régression (unitaires + intégration). | ✅ Obligatoire | ✅ | ✅ |
| **Sécu** | Checkpoint de sécurité (injections, secrets, CVE). | ✅ Checkpoint | ✅ | ✅ |
| **UAT** | Tests d'acceptation utilisateur. | ⚠️ Implicite | ✅ Formelle | ✅ |
| **E2E** | Tests de bout en bout (parcours critiques). | ⚠️ 1 parcours | ✅ | ✅ |
| **Perf** | Tests de performance et de charge. | ❌ | ❌ | ✅ |

**Règle absolue** : Une tâche sans critère de test associé dans le `current_sprint.md` est invalide. L'Auditor rejettera systématiquement toute livraison ne respectant pas cette règle.

## 2. Les Seuils d'Acceptation (La Grille de Vérité)
L'Auditor s'appuie sur une grille de métriques stricte pour formuler sa recommandation. L'échelle de sévérité canonique est : `critique | eleve | moyen | faible`.

| Métrique | `go` (Clôture propre) | `go with reserve` (Dette) | `no-go` (Rejet) |
|---|---|---|---|
| Couverture TNR | ≥ 80% | 60-79% | < 60% |
| Tests TNR échoués | 0 | 0 (flaky documenté) | ≥ 1 |
| Tests E2E échoués | 0 | 0 (flaky documenté) | ≥ 1 |
| Scénarios UAT | 100% validés | 1 partiel | ≥ 1 échoué |
| Findings sécu critique/élevé | 0 | 0 | ≥ 1 |
| Findings sécu moyen | 0 | 1-3 | > 3 |

## 3. Le Double Mandat de l'Auditor
L'Auditor (Onglet C) possède un double mandat qui exige une séparation stricte des préoccupations dans ses livrables :
1. **QA Permanent (`audit_report.md`)** : Évaluation de la couverture de tests, de la validation des critères d'acceptation, de l'absence de régressions et de la cohérence architecturale.
2. **Checkpoint SecOps (`audit_report-secops.md`)** : Évaluation exclusive de la sécurité (gestion des secrets, injections SQL/XSS, CVE connues, authentification). Ce rapport n'est généré que pour les sprints marqués du symbole 🔒.

**Interdiction formelle** : L'Auditor ne doit **jamais** mélanger les constats QA et SecOps dans un même rapport.

## 4. La Recommandation et la Composition des Verdicts
L'Auditor ne valide pas, il **recommande** le push au Validator en s'appuyant sur ses rapports. Avant de recommander, il lit obligatoirement le fichier `sprint-NN-git.md` pour vérifier la cohérence entre les commits et les tâches planifiées.

**Principe de composition des verdicts :**
- **La sécurité est bloquante** : Un seul finding de sécurité `critique` ou `eleve` entraîne un `no-go` immédiat, quel que soit l'état de la QA.
- **La QA est graduable** : Une couverture TNR de 75% (au lieu des 80% requis) permet à l'Auditor de recommander un `go with reserve`, ce qui ouvrira une dette technique (DT-NNN) à résorber lors d'un sprint ultérieur.
- Le Validator tranche ensuite en émettant le verdict final dans `state.md`.
