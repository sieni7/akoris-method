# CHECKLIST — CLÔTURE DE SPRINT

> **Public :** Orchestrator (IA) + Builder (IA) + Validator (humain)
> **Quand :** Après le verdict `go` ou `go with reserve`, après le push
> **Durée :** 5-10 minutes
> **Référence :** `.akoris/contexte.md` §7 (dettes), §10 (roadmap), §12 (git), §13 (tags)

---

## Prérequis

- [ ] Verdict `go` ou `go with reserve` tapé dans C
- [ ] Push effectué (branche `sprint-NN` → `main`)
- [ ] Merge effectué (si Validator l'a demandé)
- [ ] Tag posé (si applicable)

---

## Étape 1 — Archivage (Orchestrator, onglet A)

- [ ] Taper `go` dans A (déclenche la clôture)
- [ ] L'Orchestrator copie :
  - `.akoris/sprints/current_sprint.md` → `.akoris/sprints/archive/sprint-NN.md`
  - `.akoris/sprints/sprint_report.md` → `.akoris/sprints/archive/sprint-NN-report.md`
  - `.akoris/sprints/sprint-NN-git.md` → `.akoris/sprints/archive/sprint-NN-git.md`
  - `.akoris/audits/audit_report.md` → `.akoris/audits/archive/audit-NN.md`
  - `.akoris/audits/audit_report-secops.md` → `.akoris/audits/archive/audit-NN-secops.md` (si 🔒)
- [ ] Il réinitialise `current_sprint.md` et `sprint_report.md` (vides ou templates)
- [ ] Il supprime `sprint-NN-git.md` de `sprints/`

---

## Étape 2 — Régénération index (Orchestrator)

- [ ] L'Orchestrator exécute `python .akoris/scripts/build-debt-index.py`
- [ ] Il vérifie que `index.md` est à jour
- [ ] Il commit `chore(debt): regenerate index`

---

## Étape 3 — Mise à jour roadmap (Orchestrator)

- [ ] Il met à jour `.akoris/roadmap/ROADMAP.md` :
  - Sprint NN → `Statut: clôturé`
  - Version cible → ✅ (si tag posé)
- [ ] Il détaille le sprint N+3 (maintient 3 d'avance) dans `.akoris/roadmap/sprint-(N+3).md`

---

## Étape 4 — Mise à jour state.md (Orchestrator)

- [ ] Il met `state.md` à :
  - `phase: closed`
  - `next_agent: orchestrator`
  - `action: go`
  - `verdict: null` (réinitialisé)
  - `verdict_qa`, `verdict_secops`, `verdict_global: null`
  - `reserves: []`
  - `message: "Sprint NN clôturé"`

---

## Étape 5 — Commit de clôture (Builder ou Orchestrator)

- [ ] `git add -A`
- [ ] `git commit -m "chore(state): close sprint NN"`
- [ ] `git push origin main`

---

## Étape 6 — Validation finale (Validator)

- [ ] Vérifier que `state.md` est cohérent
- [ ] Vérifier que `ROADMAP.md` est à jour
- [ ] Vérifier que `index.md` est à jour
- [ ] Vérifier que le tag est posé (`git tag -l`)
- [ ] Si tout est bon → le sprint est **clôturé**

---

## Étape 7 — Sprint suivant (si applicable)

- [ ] L'Orchestrator lit la roadmap
- [ ] Il prépare le prochain sprint (phase PLAN de `checklists/sprint.md`)
- [ ] Taper `go` dans A → nouveau sprint

---

## Validation finale

- [ ] Les archives sont créées
- [ ] `index.md` est à jour
- [ ] `ROADMAP.md` est à jour
- [ ] `state.md` est réinitialisé
- [ ] Le tag est posé (si applicable)
- [ ] Le commit de clôture est poussé
- [ ] **Sprint NN est officiellement clôturé.**

**✅ Passer au sprint suivant (ou fin du projet).**
