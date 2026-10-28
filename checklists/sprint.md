# CHECKLIST — SPRINT (CYCLE COMPLET)

> **Public :** Validator (humain) + Orchestrator + Builder + Auditor
> **Quand :** À chaque sprint
> **Durée :** variable (jours)
> **Référence :** `.akoris/contexte.md` §6 (convention GO)

---

## Phase PLAN (onglet A)

- [ ] L'Orchestrator lit `.akoris/contexte.md` + `state.md` + roadmap
- [ ] Il détaille le sprint N+3 (maintient 3 d'avance)
- [ ] Il écrit `.akoris/sprints/current_sprint.md` avec :
  - Objectif, périmètre IN/OUT
  - Tâches (1 = 1 commit = 1 critère), colonne `Test` remplie
  - Propositions (options + recommandation)
  - Critères d'acceptation du sprint
- [ ] Il met `state.md` à `next_agent: builder, action: go`
- [ ] Lire les propositions
- [ ] Taper `go` dans A

## Phase EXECUTE (onglet B)

- [ ] Taper `go` dans B
- [ ] Le Builder lit `current_sprint.md`
- [ ] Il exécute **tâche par tâche** : 1 tâche = 1+ commits
- [ ] Chaque commit porte : `Sprint: NN`, `Tâche: TN`, `Refs:`
- [ ] Il append au `sprint_report.md` (par tâche)
- [ ] Il met à jour `sprint-NN-git.md` (commits)
- [ ] Il met `state.md` à `next_agent: auditor, action: go`
- [ ] Lire `sprint_report.md`
- [ ] Taper `go` dans C

## Phase AUDIT (onglet C)

- [ ] Taper `go` dans C (déclenche l'audit QA)
- [ ] L'Auditor lit `sprint_report.md` + `sprint-NN-git.md` + `app/`
- [ ] Il exécute les tests, vérifie la couverture
- [ ] Il écrit `audit_report.md` (findings, recommandation push)
- [ ] Il met `state.md` à `next_agent: validator, action: review`
- [ ] **Si sprint 🔒** : deuxième passe SecOps
  - [ ] Taper `go` dans C
  - [ ] L'Auditor écrit `audit_report-secops.md`
  - [ ] Il met `state.md` à `next_agent: validator, action: review`
- [ ] Lire le(s) rapport(s)
- [ ] Passer à `checklists/verdict.md`

## Phase VERDICT (onglet C)

- [ ] Appliquer la grille (`checklists/verdict.md`)
- [ ] Taper le verdict dans C :
  - `go` → clôture
  - `go with reserve: <détails>` → clôture + dette(s)
  - `no-go: <raison>` → re-planification

## Phase PUSH (onglet B) — si `go` ou `go with reserve`

- [ ] L'Orchestrator crée les fichiers de dette (si `go with reserve`)
- [ ] Il met `state.md` à `next_agent: builder, action: push`
- [ ] Taper `go` dans B (déclenche le push)
- [ ] Le Builder :
  - `git push origin sprint-NN`
  - `git checkout main && git merge sprint-NN` (⚠️ merge SYSTÉMATIQUE après `go`)
  - `git tag vX.Y.Z` (si `tag_cible` défini)
  - `git push origin main --tags`
- [ ] Il met à jour `sprint-NN-git.md` (§Push, §Merge, §Tag)
- [ ] Il met `state.md` à `phase: closed, next_agent: orchestrator`
## Phase CLÔTURE (onglet A)

- [ ] Suivre `checklists/cloture.md`

---

## Si `no-go`

- [ ] L'Orchestrator re-planifie
- [ ] Il écrit un nouveau `current_sprint.md`
- [ ] Il met `state.md` à `next_agent: builder, action: go`
- [ ] Taper `go` dans B
- [ ] **Reboucler** (Phase EXECUTE)
