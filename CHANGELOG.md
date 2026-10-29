# CHANGELOG — AKORIS

Toutes les évolutions notables de la méthode AKORIS sont documentées ici.
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [SemVer](https://semver.org/lang/fr/).

---

## [Unreleased]

### Added
- Rédaction du livre (parties 0 à VIII) en cours.

---

## [0.1.1] — 2026-10-29

### Added
- Kit de référence AKORIS : blocs 1 à 11.
- CI et trois fichiers de tests (`tests/test_build_debt_index.py`, `tests/test_consistency.py`, `tests/test_init_project.py`).
- Texte Apache-2.0 complet et table de couverture des fichiers dans `LICENSE`.
- Statuts V2 explicites pour les décisions concernées.
- Une clarification référencée : décision 049.
- README aligné sur le contenu réel du dépôt.
- Couverture de licence complète, titulaire Sieni.

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
- Découpage 1 tâche = 1+ commits = 1 critère
- Commande `doctor` (R1+R2+R4 défaut)

---

## Format des versions

- **MAJOR** : refonte de la méthode (breaking change sur les templates)
- **MINOR** : ajout de fonctionnalité / section / décision
- **PATCH** : correction / clarification
