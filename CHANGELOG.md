# CHANGELOG — AKORIS

Toutes les évolutions notables de la méthode AKORIS sont documentées ici.
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [SemVer](https://semver.org/lang/fr/).

---

## [0.1.1] — 2026-10-29

### En cours
- Construction du kit de référence (blocs 1 à 10)
- Rédaction du livre (parties 0 à VIII)

### Fixed (Bloc 9 — corrections urgence 1)
- `build-debt-index.py` : bug `split("---")` corrigé (robuste aux `---` dans les valeurs YAML)
- `build-debt-index.py` : tests pytest ajoutés (`tests/test_build_debt_index.py`)
- `init-project.sh` : `git init -b main` (au lieu de `master`)
- `init-project.sh` : création de `debt/index.md`, `sprints/archive/`, `audits/archive/`, `doc/tech/tests.md`, `app/tests/README.md`
- `init-project.sh` : copie de `checklists/` dans le projet
- `cloture.md` : archivage de `state.md` (avec verdict) AVANT le reset
- `CHANGELOG.md` : 62 → 48 décisions (correction du chiffre)
- `LICENSE` : ajout (MIT + CC-BY-4.0 + Apache-2.0)

### Fixed (Bloc 10 — contradictions)
- `contexte.md` §7 : `no-go automatique` → `no-go recommandé` (respecte "l'humain décide")
- `contexte.md` §9 : `locked_by: null` = libre (pas "pas mon tour")
- `contexte.md` : sections projet retirées (renvoi vers `projet.md`)
- `projet.md` : nouveau fichier (sections spécifiques au projet)
- `orchestrator.md` : `doc/produit/` autorisé
- `bootstrap.md` : phase 9 = exception documentée, phase 10 = `go` dans B
- `checklists/bootstrap.md` : phase 10 = `go` dans B
- `checklists/sprint.md` : merge systématique après `go`
- `sprint-NN-git.md` : `1 tâche = 1+ commits`

---

## [0.1.0] — 2026-10-28

### Ajouté
- Identité AKORIS figée :
  - Nom : Adaptive Knowledge & Orchestrated Review for Iterative Systems
  - Finalité : gouvernance du développement logiciel assisté par IA
  - Principe directeur : L'IA produit ; le contrôle vérifie ; l'autorité humaine décide.
  - 3 zéros (boussoles) : zéro hallucination, zéro code spaghetti, zéro dette non maîtrisée
- Structure `akoris-method/` (référentiel générique) et `.akoris/` (instance projet)
- **48 décisions figées** (voir `decisions/`)
- Socle documentaire :
  - `README.md`
  - `METHOD.md`
  - `CHANGELOG.md`
  - `docs/00-introduction-akoris.md`
- Templates complets (contexte, state, agents, bootstrap, dette, roadmap, ADR, sprints, audits, scripts)
- Checklists (phase-0, bootstrap, sprint, verdict, cloture)
- Scripts (build-debt-index.py, init-project.sh)

### Décisions majeures
- Convention GO (`go` en A/B, `go` puis verdict en C)
- Verrou `state.md` (un agent à la fois)
- Roadmap hybride (résumé total + 3 détaillés)
- ADR 4 chiffres, 4 fondateurs
- Registre dettes `debt/` + `index.md` généré
- Conventional Commits + SemVer
- Auditor QA permanent + SecOps checkpoint (`🔒`)
- Stratégie de tests V0 (TNR + sécu + UAT implicite)
- Découpage 1 tâche = 1+ commits = 1 critère
- Commande `doctor` (R1+R2+R4 défaut)

---

## Format des versions

- **MAJOR** : refonte de la méthode (breaking change sur les templates)
- **MINOR** : ajout de fonctionnalité / section / décision
- **PATCH** : correction / clarification
