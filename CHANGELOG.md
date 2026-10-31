# CHANGELOG — AKORIS

Toutes les évolutions notables de la méthode AKORIS sont documentées ici.
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [SemVer](https://semver.org/lang/fr/).

---

## [Unreleased]

## [0.1.2] - 2026-10-31

### Added
- Standard de Prompt AKORIS (SPA), son template vierge et ses 13 rubriques normatives.
- Réécriture des prompts Orchestrator, Builder et Auditor selon le SPA.
- Instance SPA du Générateur de Contexte, avec brainstorming A1–A4 et phases B/C.
- Chapitres 1 et 2 du livre : [Fondations](docs/01-fondations.md) et [Architecture](docs/02-architecture.md).

### Fixed
- Lot A4 : génération de l’index canonique des dettes lors de l’initialisation d’un projet.
- Lot A5 : suppression de l’index de repli sans PyYAML et avertissement explicite à l’initialisation.
- Bloc 11 : correction du compteur et des faux négatifs du validateur de cohérence.
- Bloc 12 : validation automatisée de la présence et de l’ordre des 13 rubriques SPA.

---
## [0.1.1] — 2026-10-29

### Added
- Kit de référence AKORIS : blocs 1 à 11.
- CI et trois fichiers de tests (`tests/test_build_debt_index.py`, `tests/test_consistency.py`, `tests/test_init_project.py`).
- Texte Apache-2.0 complet et table de couverture des fichiers dans `LICENSE`.
- Statuts V2 explicites pour les décisions concernées.
- Une clarification référencée : décision 049.
- README aligné sur le contenu réel du dépôt.
- Couverture de licence complète, titulaire Oulai Sieni Tarek.

### Changed
- Décompte : **48 décisions figées (001–048) + 1 clarification (049)**.

### Fixed
- Bloc 9 : corrections urgentes du générateur d’index, de l’initialisation, de la clôture, du décompte et des licences.
- Bloc 10 : contradictions de gouvernance, configuration projet, bootstrap et clôture.
- Blocs 1 à 11 : corrections et harmonisations de cohérence.

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
- Découpage 1 tâche = 1+ commits = 1 critère (Formule abandonnée au profit de : 1 tâche → 1 critère → ≥ 1 commit)
- Commande `doctor` (R1+R2+R4 défaut)

---

## Format des versions

- **MAJOR** : refonte de la méthode (breaking change sur les templates)
- **MINOR** : ajout de fonctionnalité / section / décision
- **PATCH** : correction / clarification
