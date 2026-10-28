# CHANGELOG — AKORIS

Toutes les évolutions notables de la méthode AKORIS sont documentées ici.
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
versionnage [SemVer](https://semver.org/lang/fr/).

---

## [Unreleased]

### En cours
- Construction du kit de référence (blocs 1 à 8)
- Rédaction du livre (parties 0 à VIII)

---

## [0.1.0] — 2026-10-28

### Ajouté
- Identité AKORIS figée :
  - Nom : Adaptive Knowledge & Orchestrated Review for Iterative Systems
  - Finalité : gouvernance du développement logiciel assisté par IA
  - Principe directeur : L'IA produit ; le contrôle vérifie ; l'autorité humaine décide.
  - 3 zéros (boussoles) : zéro hallucination, zéro code spaghetti, zéro dette non maîtrisée
- Structure `akoris-method/` (référentiel générique) et `.akoris/` (instance projet)
- 62 décisions figées (voir `decisions/`)
- Socle documentaire :
  - `README.md`
  - `METHOD.md`
  - `CHANGELOG.md`
  - `docs/00-introduction-akoris.md`

### Décisions majeures
- Convention GO (`go` en A/B, `go` puis verdict en C)
- Verrou `state.md` (un agent à la fois)
- Roadmap hybride (résumé total + 3 détaillés)
- ADR 4 chiffres, 4 fondateurs
- Registre dettes `debt/` + `index.md` généré
- Conventional Commits + SemVer
- Auditor QA permanent + SecOps checkpoint (`🔒`)
- Stratégie de tests V0 (TNR + sécu + UAT implicite)
- Découpage 1 tâche = 1 commit = 1 critère
- Commande `doctor` (R1+R2+R4 défaut)

---

## Format des versions

- **MAJOR** : refonte de la méthode (breaking change sur les templates)
- **MINOR** : ajout de fonctionnalité / section / décision
- **PATCH** : correction / clarification
