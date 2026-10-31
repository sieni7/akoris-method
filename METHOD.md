# AKORIS — Méthode de gouvernance du développement logiciel assisté par IA

> L'IA produit ; le contrôle vérifie ; l'autorité humaine décide.

---

## 1. Identité

- **Nom :** AKORIS
- **Acronyme :** Adaptive Knowledge & Orchestrated Review for Iterative Systems
- **Finalité :** gouvernance du développement logiciel assisté par IA
- **Positionnement :** ni un modèle d'IA, ni un éditeur de code, ni un framework,
  ni un simple ensemble de prompts. Une méthode de gouvernance, indépendante des
  modèles, des fournisseurs et des outils.

---

## 2. Principe directeur

> **L'IA produit ; le contrôle vérifie ; l'autorité humaine décide.**

Trois rôles, trois responsabilités, jamais fusionnés :

- **Produire** : l'IA (Builder) génère du code, de la documentation, des livrables.
- **Vérifier** : l'IA (Auditor) contrôle, teste, rapporte. Elle ne décide pas.
- **Décider** : l'humain (Validator) autorise, tranche, assume la responsabilité.

---

## 3. Les 3 zéros (boussoles)

- **Zéro hallucination** : les décisions et productions reposent sur des éléments
  vérifiables.
- **Zéro code spaghetti** : l'architecture est cohérente, l'organisation maîtrisée.
- **Zéro dette technique non maîtrisée** : les compromis sont identifiés, justifiés,
  documentés et suivis.

Ces zéros sont des **boussoles**, pas des **garanties**. AKORIS **mesure l'écart**
et **trace** les compromis. Un projet AKORIS n'est pas un projet sans dette ; c'est
un projet dont la dette est **connue, tracée et pilotée**.

---

## 4. Les principes fondateurs

1. **Séparation des pouvoirs** — celui qui code n'audite pas, celui qui audite ne
   valide pas, celui qui valide ne code pas.
2. **Une seule source de vérité** — les fichiers du dossier `.akoris/`, pas le chat.
3. **Un agent à la fois** — un verrou (`state.md`) garantit qu'un seul agent agit.
4. **Traçabilité par défaut** — chaque décision, commit, dette, audit est consigné.
5. **Réplicabilité** — la méthode est séparable du projet ; elle se copie, s'adapte,
   se transmet.

---

## 5. Architecture

### Trois piliers (dans le projet)

- **`app/`** — exécutable (le produit livré)
- **`doc/`** — documentaire (doc technique + produit)
- **`.akoris/`** — gouvernance (contexte, state, roadmap, ADR, sprints, audits, dettes)

### Trois onglets + un humain

- **Onglet A** — Orchestrator (planifie, découpe, coordonne)
- **Onglet B** — Builder (exécute, code, commit, push)
- **Onglet C** — Auditor (QA permanent + SecOps checkpoint)
- **Validator** (humain) — autorise, tranche, ouvre les dettes

### Convention GO

- Onglet A : `go` pour autoriser la planification
- Onglet B : `go` pour autoriser l'exécution, puis `go` pour autoriser le push
- Onglet C : `go` pour lancer l'audit, puis verdict (`go` / `go with reserve` / `no-go`)

---

## 6. Outils compatibles

AKORIS est **indépendant des outils**. Il requiert trois capacités :

| Prérequis | Pourquoi |
|-----------|----------|
| **3 agents LLM simultanés** | Onglets A/B/C (Orchestrator, Builder, Auditor) |
| **Un dossier partagé** | `.akoris/` (source de vérité unique) |
| **Un verrou fichier** | `state.md` (un seul agent actif à la fois) |

**Outil de référence :** [OpenCode](https://github.com/opencode-ai/opencode) —
interface multi-onglets, dossier partagé, verrou natif.

**Alternatives :** Manus, Cursor, Windsurf, Claude Projects, ou tout outil
permettant 3 sessions LLM simultanées avec accès fichier partagé.

**Non compatible :** chat unique, outil sans accès fichier, outil sans multi-onglets.

---

## 7. Pour aller plus loin

- **Le livre :** `docs/` (10 chapitres disponibles, ch.0 à ch.9)
- **Les décisions :** `decisions/` (référentiel des décisions et clarifications)
- **Les templates :** `templates/` (à copier dans un projet)
- **Les checklists :** `checklists/` (phase 0, bootstrap, sprint, verdict, clôture)
- **Les scripts :** `scripts/` (init-project, validate-method) ; `templates/.akoris/scripts/` (build-debt-index)
- **Les exemples :** `examples/` (instances SPA et cas d’usage concrets, à venir)
- **Les compétences :** `templates/skills/` (Pilote QA-01 disponible)

---

## 8. Autorité documentaire

En cas de conflit entre les documents :
1. **`METHOD.md`** prime pour les principes fondamentaux (règles de gouvernance, rôles, 3 zéros).
2. **`contexte.md`** prime pour l'application spécifique au projet (stack, règles métier, conventions locales).
Une instance projet ne peut pas contredire `METHOD.md`. Tout conflit doit être tranché par le Validator.
