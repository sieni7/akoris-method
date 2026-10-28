# CHECKLIST — BOOTSTRAP (10 PHASES)

> **Public :** Validator (humain) + Orchestrator (IA)
> **Quand :** Après la phase 0, une seule fois par projet
> **Durée :** 30-60 minutes
> **Référence :** `.akoris/config/bootstrap.md`

---

## Règle d'or

**Une phase = un `go`. Jamais deux phases dans le même tour.**
**Chaque phase : lire la proposition → vérifier → taper `go` ou corriger.**

---

## Phase 1 — Vérification

- [ ] L'Orchestrator vérifie l'état du repo
- [ ] Il justifie ce qu'il va créer
- [ ] Lire la justification
- [ ] Taper `go` dans A

## Phase 2 — Arborescence

- [ ] L'Orchestrator propose l'arborescence complète
- [ ] Vérifier : `app/`, `doc/`, `.akoris/` avec sous-dossiers
- [ ] Taper `go` dans A

## Phase 3 — Contexte (§0 + §1-§21)

- [ ] L'Orchestrator vérifie/complète `.akoris/projet.md`
- [ ] Vérifier : §0 AKORIS (contexte) + §1 identité projet et §4 conventions (projet.md)
- [ ] Taper `go` dans A

## Phase 4 — Roadmap (résumé)

- [ ] L'Orchestrator propose `.akoris/roadmap/ROADMAP.md`
- [ ] Vérifier : tableau avec 6 colonnes (`#`, `Titre`, `Type`, `Version cible`, `🔒`, `Statut`)
- [ ] Vérifier : v0.1.0 au bootstrap, v1.0.0 à la prod
- [ ] Taper `go` dans A

## Phase 5 — Roadmap (détail 3 sprints)

- [ ] L'Orchestrator propose `sprint-01.md`, `sprint-02.md`, `sprint-03.md`
- [ ] Vérifier : objectif, périmètre IN/OUT, tâches (1 = 1 commit = 1 critère), tests, budget, risques
- [ ] Taper `go` dans A

## Phase 6 — Roadmap (vérification)

- [ ] L'Orchestrator vérifie que `.akoris/roadmap/ROADMAP.md` est complet
- [ ] Vérifier la cohérence
- [ ] Taper `go` dans A

## Phase 7 — ADR fondateurs (4)

- [ ] L'Orchestrator propose :
  - `0001-stack-initiale.md`
  - `0002-separation-app-doc-akoris.md`
  - `0003-convention-go.md`
  - `0004-strategie-tests.md`
- [ ] Vérifier : contexte, options, décision, conséquences pour chaque
- [ ] Taper `go` dans A

## Phase 8 — État initial

- [ ] L'Orchestrator propose `.akoris/state.md` (phase: setup)
- [ ] Crée `.akoris/debt/_template.md` (déjà là) + `index.md` vide
- [ ] Vérifie `.akoris/scripts/build-debt-index.py` (déjà là)
- [ ] Taper `go` dans A

## Phase 9 — Stack itérative (7 briques)

**Une brique = un `go`.**

- [ ] Brique 1 : Init projet (package.json / pyproject.toml)
- [ ] Brique 2 : Dépendances de base
- [ ] Brique 3 : Linter / formatter
- [ ] Brique 4 : commitlint + husky
- [ ] Brique 5 : CI (build-debt-index + tests)
- [ ] Brique 6 : Premier test (TNR)
- [ ] Brique 7 : Premier commit

## Phase 10 — Clôture bootstrap + Sprint 1

- [ ] L'Orchestrator vérifie la checklist finale
- [ ] Il propose `.akoris/sprints/current_sprint.md` (Sprint 1)
- [ ] Il met `.akoris/state.md` à `next_agent: builder, action: go`
- [ ] Lire la proposition
- [ ] Taper `go` **dans l'onglet B** (le Builder exécute le Sprint 1)
---

## Validation finale

- [ ] Les 10 phases sont passées
- [ ] `.akoris/state.md` indique `next_agent: builder`
- [ ] Le Sprint 1 est prêt dans `current_sprint.md`
- [ ] La stack est posée (build OK, tests OK, CI OK)

**✅ Bootstrap terminé. Passer à l'onglet B pour le Sprint 1.**
