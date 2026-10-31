# AKORIS

> **Adaptive Knowledge & Orchestrated Review for Iterative Systems**
>
> L'IA produit ; le contrôle vérifie ; l'autorité humaine décide.

[🇫🇷 Français](README.md) · [🇬🇧 English](README.en.md)

[![Version](https://img.shields.io/badge/version-0.1.1-blue)]()
[![Tests](https://img.shields.io/badge/tests-17%20passing-brightgreen)]()
[![Licence](https://img.shields.io/badge/licence-MIT%20%2B%20Apache--2.0%20%2B%20CC--BY--4.0-lightgrey)]()

---

## Sommaire

- [Qu'est-ce qu'AKORIS ?](#quest-ce-quakoris-)
- [Les 3 zéros](#les-3-zéros)
- [Quick start](#quick-start)
- [Architecture](#architecture)
- [Outils compatibles](#outils-compatibles)
- [Structure du dépôt](#structure-du-dépôt)
- [Documentation](#documentation)
- [Contribuer](#contribuer)
- [Auteur](#auteur)
- [Licence](#licence)

---

## Qu'est-ce qu'AKORIS ?

AKORIS est une **méthode de gouvernance** du développement logiciel assisté par
intelligence artificielle. Elle établit un cadre structuré pour organiser,
guider, contrôler et évaluer la contribution des IA tout au long du processus
de développement logiciel.

Son objectif : faire de l'IA un **moyen de production placé sous une gouvernance
explicite**, plutôt qu'un substitut à la réflexion, à la décision et à la
responsabilité humaines.

**Ce qu'AKORIS n'est pas :**

- ❌ ni un modèle d'intelligence artificielle
- ❌ ni un éditeur de code
- ❌ ni un framework de programmation
- ❌ ni un simple ensemble de prompts

C'est une méthode de gouvernance, **indépendante des modèles, des fournisseurs
et des outils**.

---

## Les 3 zéros

| Zéro | Signification |
|------|---------------|
| **Zéro hallucination** | Les décisions reposent sur des éléments vérifiables |
| **Zéro code spaghetti** | L'architecture est cohérente, l'organisation maîtrisée |
| **Zéro dette non maîtrisée** | Les compromis sont identifiés, justifiés, documentés, suivis |

Ces zéros sont des **boussoles**, pas des **garanties**. AKORIS **mesure l'écart**
et **trace** les compromis. Un projet AKORIS n'est pas un projet sans dette ;
c'est un projet dont la dette est **connue, tracée et pilotée**.

---

## Quick start

```bash
# 1. Cloner le référentiel
git clone https://github.com/sieni7/akoris-method.git

# 2. Scaffolder un nouveau projet
./akoris-method/scripts/init-project.sh mon-projet

# 3. Suivre la phase 0
cat akoris-method/checklists/phase-0.md
```

Ensuite :

1. Ouvrir **3 onglets** dans un outil compatible (A, B, C).
2. Coller les prompts d'identité (`templates/.akoris/config/agents/`).
3. Lancer le bootstrap (`templates/.akoris/config/bootstrap.md`).
4. Taper `go` dans l'onglet A pour démarrer la phase 1.

---

## Architecture

### 3 piliers (dans le projet)

```
mon-projet/
├── app/       ← code exécutable (Builder)
├── doc/       ← documentation technique + produit (Builder + Orchestrator)
└── .akoris/   ← gouvernance (contexte, state, roadmap, ADR, dettes)
```

### 3 onglets + 1 humain

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  ONGLET A    │  │  ONGLET B    │  │  ONGLET C    │
│ Orchestrator │  │   Builder    │  │   Auditor    │
│  (planifie)  │  │   (code)     │  │  (audite)    │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
              ┌─────────────────────┐
              │  VALIDATOR (humain) │
              │  (autorise, tranche)│
              └─────────────────────┘
```

### Convention GO

| Onglet | Ce que tape le Validator | Signification |
|--------|--------------------------|---------------|
| A | `go` | Autorise la planification |
| B | `go` | Autorise l'exécution, puis le push |
| C | `go` puis verdict | Lance l'audit, puis tranche |

Verdicts : `go` · `go with reserve: <détails>` · `no-go: <raison>`

---

## Outils compatibles

AKORIS est **indépendant des outils**. Il requiert trois capacités :

| Prérequis | Pourquoi |
|-----------|----------|
| **3 agents LLM simultanés** | Onglets A/B/C (Orchestrator, Builder, Auditor) |
| **Un dossier partagé** | `.akoris/` (source de vérité unique) |
| **Un verrou fichier** | `state.md` (un seul agent actif à la fois) |

### Outil de référence

**[OpenCode](https://github.com/opencode-ai/opencode)** — interface multi-onglets,
dossier partagé, verrou natif. C'est l'outil qui a inspiré et validé AKORIS.

### Alternatives

| Outil | Compatible ? | Note |
|-------|--------------|------|
| **Manus** | ⚠️ Partiel | Agent autonome, pas de multi-onglets natif |
| **Cursor** | ✅ Oui | Multi-fenêtres + accès fichier |
| **Windsurf** | ✅ Oui | Multi-fenêtres + accès fichier |
| **Claude Projects** | ✅ Oui | Multi-projets + fichiers partagés |
| **Chat unique** | ❌ Non | Pas de séparation des rôles |
| **Outil sans accès fichier** | ❌ Non | Pas de `state.md` |

**Critère de compatibilité :** 3 sessions LLM simultanées + accès à un système
de fichiers partagé + un mécanisme de verrou (fichier `state.md`).

---

## Structure du dépôt

```
akoris-method/
├── README.md              ← ce fichier (FR)
├── README.en.md           ← version anglaise
├── METHOD.md              ← les principes fondateurs
├── CHANGELOG.md           ← historique
├── LICENSE                ← MIT + Apache-2.0 + CC-BY-4.0
├── CONTACT.md             ← coordonnées de l'auteur
├── docs/                  ← le livre
├── decisions/             ← 49 décisions figées (001-048, 050) + 1 clarification (049)
├── checklists/            ← phase 0, bootstrap, sprint, verdict, clôture
├── scripts/               ← init-project.sh; scripts/validate-method.py — disponible
├── tests/                 ← 21 tests Python sur 4 fichiers
├── templates/doc/         ← documentation de projet à copier
├── templates/.akoris/     ← templates à copier
└── .github/workflows/     ← CI (pytest + shellcheck + index)
```

---

## Documentation

| Document | Contenu |
|----------|---------|
| [`METHOD.md`](METHOD.md) | Les principes fondateurs |
| [`docs/`](docs/) | Le livre (5 chapitres disponibles, ch.0–4), dont [`ch.3 — Démarrage`](docs/03-demarrage.md) et [`ch.4 — Cycle de Sprint`](docs/04-cycle-sprint.md) |
| [`decisions/`](decisions/) | 49 décisions figées (001-048, 050) + 1 clarification (049) |
| [`checklists/`](checklists/) | Phase 0 → clôture |
| [`templates/.akoris/contexte.md`](templates/.akoris/contexte.md) | La constitution (22 sections) |

---

## Contribuer

Les contributions sont les bienvenues. Avant de proposer une PR :

1. Lire [`METHOD.md`](METHOD.md) et les [`decisions/`](decisions/).
2. Vérifier que la modification respecte les 49 décisions figées (001-048, 050) + 1 clarification (049)
   (ou proposer un ADR pour une nouvelle décision).
3. Lancer `pytest` (21 tests Python sur 4 fichiers).
4. Lancer `shellcheck scripts/*.sh` (0 alerte attendue).
5. Ouvrir une **issue** avant une PR majeure.

---

## Auteur

**Oulai Sieni Tarek**

- 🐙 GitHub : [@sieni7](https://github.com/sieni7)
- 📧 Email : sieni7 [at] gmail [dot] com
- 🌍 Côte d'Ivoire

> Pour les coordonnées complètes (téléphone, WhatsApp), voir [`CONTACT.md`](CONTACT.md).

---

## Licence

| Fichier / Dossier | Licence |
|-------------------|---------|
| `README.md`, `README.en.md`, `CHANGELOG.md`, `CONTACT.md` | Apache-2.0 |
| `METHOD.md`, `decisions/`, `checklists/`, templates de gouvernance, `templates/doc/` | Apache-2.0 |
| `docs/` | CC-BY-4.0 |
| `scripts/*.sh`, `templates/.akoris/scripts/*.py`, `tests/*.py` | MIT |
| `LICENSE` | Apache-2.0 |

Titulaire : **Oulai Sieni Tarek**.

---

## Remerciements

- [OpenCode](https://github.com/opencode-ai/opencode) — outil de référence
- [Keep a Changelog](https://keepachangelog.com/) — format du CHANGELOG
- [SemVer](https://semver.org/) — versionnage
- [Conventional Commits](https://www.conventionalcommits.org/) — convention de commits
- [Michael Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — format ADR

---

> **AKORIS — L'IA produit ; le contrôle vérifie ; l'autorité humaine décide.**
