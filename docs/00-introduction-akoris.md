# Chapitre 0 — AKORIS : nom, finalité, principe

> Ce chapitre introduit AKORIS avant d'entrer dans le problème du vibe coding
> (chapitre 1). Il ancre l'identité de la méthode : ce qu'elle est, ce qu'elle
> vise, ce qu'elle n'est pas.

---

## 0.1 Le nom et l'acronyme

**AKORIS** — *Adaptive Knowledge & Orchestrated Review for Iterative Systems*

Chaque mot porte une intention :

| Mot | Sens |
|-----|------|
| **Adaptive** | La méthode s'adapte à la taille du projet, à la nature du sprint, à la maturité de l'équipe. Elle n'est pas rigide. |
| **Knowledge** | La méthode capitalise : contexte, ADR, dettes, roadmap. Rien ne se perd. |
| **Orchestrated** | Les agents (Orchestrator, Builder, Auditor) sont orchestrés, pas laissés libres. Un verrou, un tour, un GO. |
| **Review** | Chaque livraison est revue : QA, SecOps, verdict humain. Pas de "ship and pray". |
| **Iterative** | Le développement est itératif : sprints, roadmap, versions. Pas de big bang. |
| **Systems** | Le produit est un système : code, doc, gouvernance. Pas juste du code. |

Le nom est **court, prononçable, mémorable**. Il évoque l'idée d'un **cœur**
(« cor ») qui bat au rythme des sprints — mais ce n'est qu'une coïncidence.

---

## 0.2 La finalité

AKORIS est une **méthode de gouvernance** du développement logiciel assisté par
intelligence artificielle.

Elle établit un cadre structuré permettant d'**organiser**, de **guider**, de
**contrôler** et d'**évaluer** la contribution des intelligences artificielles
tout au long du processus de développement logiciel.

Son objectif est de faire de l'IA un **moyen de production placé sous une
gouvernance explicite**, plutôt qu'un **substitut à la réflexion, à la décision
et à la responsabilité humaines**.

### Les 3 zéros (boussoles)

AKORIS vise trois zéros :

1. **Zéro hallucination** — les décisions et productions reposent sur des éléments
   vérifiables.
2. **Zéro code spaghetti** — l'architecture est cohérente, l'organisation maîtrisée.
3. **Zéro dette technique non maîtrisée** — les compromis sont identifiés,
   justifiés, documentés et suivis.

Ces zéros sont des **boussoles**, pas des **garanties**. AKORIS **mesure l'écart**
et **trace** les compromis. Un projet AKORIS n'est pas un projet sans dette ;
c'est un projet dont la dette est **connue, tracée et pilotée**.

---

## 0.3 Le principe directeur

> **L'IA produit ; le contrôle vérifie ; l'autorité humaine décide.**

Ce principe est le **cœur** d'AKORIS. Il décompose le développement en trois
rôles, trois responsabilités, **jamais fusionnés**.

### Produire

L'IA (le **Builder**) génère du code, de la documentation, des livrables. Elle
exécute les tâches planifiées. Elle **ne décide pas** de ce qui est bon ; elle
**produit** ce qui est demandé.

### Vérifier

L'IA (l'**Auditor**) contrôle, teste, rapporte. Elle vérifie que ce qui a été
produit respecte les critères d'acceptation, les conventions, les seuils de
qualité. Elle **recommande**, mais elle **ne décide pas**.

### Décider

L'humain (le **Validator**) autorise, tranche, assume la responsabilité. Il tape
`go`, `go with reserve` ou `no-go`. Il ouvre les dettes, valide les ADR, arbitre
les conflits. **Il est le seul à décider.**

### Pourquoi cette séparation

Si l'IA qui produit est aussi celle qui vérifie, elle **s'auto-valide** — et
elle se trompe. Si l'IA qui vérifie est aussi celle qui décide, elle **s'auto-
autorise** — et elle dérive. Si l'humain produit, vérifie et décide, il devient
le **goulot d'étranglement** — et il perd le bénéfice de l'IA.

AKORIS sépare les trois. C'est **la** condition de la gouvernance.

---

## 0.4 Le positionnement

AKORIS **n'est pas** :

- **ni un modèle d'intelligence artificielle** — AKORIS utilise des LLM, mais
  n'en est pas un.
- **ni un éditeur de code** — AKORIS n'est pas Cursor, Copilot ou Windsurf.
  Il peut s'utiliser avec eux, mais ce n'est pas un outil.
- **ni un framework de programmation** — AKORIS n'impose pas de langage, de
  bibliothèque ou d'architecture technique. Il gouverne le **processus**, pas
  le **code**.
- **ni un simple ensemble de prompts** — AKORIS utilise des prompts (identité,
  bootstrap, doctor), mais ce sont des **moyens**, pas la méthode. La méthode
  est le **cadre de gouvernance** qui organise ces prompts.

AKORIS **est** :

- une **méthode de gouvernance** — un cadre structuré, traçable, réplicable.
- **indépendante** des modèles (OpenAI, Anthropic, Google, open-weights), des
  fournisseurs (cloud, local), et des outils (IDE, CLI, chat).
- **transmissible** — elle se documente, se copie, s'adapte.

---

## 0.5 Comment lire ce livre

Le livre est organisé en **9 parties** (0 à VIII) et **34 chapitres**.

### Trois parcours possibles

| Parcours | Public | Chapitres |
|----------|--------|-----------|
| **Découverte** | Curieux, débutant | 0, 1, 2, 3, 9, 10, 13, 24 |
| **Mise en œuvre** | Praticien | 0-8, 9-17, 18-20, 29-31 |
| **Référence** | Utilisateur avancé | 29-33, annexes |

### Structure du livre

- **Partie 0 — AKORIS** (ch. 0) : identité, finalité, principe
- **Partie I — Fondations** (ch. 1-3) : problème, principes, vue d'ensemble
- **Partie II — Architecture** (ch. 4-8) : piliers, agents, GO, state, doctor
- **Partie III — Démarrage** (ch. 9-11) : phase 0, bootstrap, contexte
- **Partie IV — Cycle de sprint** (ch. 12-17) : roadmap, sprint, ADR, dettes, doc, git
- **Partie V — Qualité** (ch. 18-20) : QA, SecOps, verdicts
- **Partie VI — Évolution** (ch. 21-23) : CLI, réplicabilité, futur
- **Partie VII — Pratique** (ch. 24-28) : études de cas, erreurs, anti-patterns
- **Partie VIII — Référence** (ch. 29-33) : templates, checklists, scripts, glossaire
- **Annexes** (A-F) + postface

### Conventions

- **Bloc `>`** : citation, principe, règle à retenir.
- **Tableau** : comparaison, structure, grille.
- **Bloc de code** : exemple, template, commande.
- **⚠️** : point de vigilance, risque, piège.
- **✅** : décision figée, bonne pratique.
- **❓** : question ouverte (rare dans un livre, fréquent dans la construction).

---

## 0.6 Ce que ce livre n'est pas

- **Pas un tutoriel de prompt engineering** — vous n'apprendrez pas à "mieux
  prompter". Vous apprendrez à **gouverner** des agents.
- **Pas un manifeste anti-IA** — AKORIS **utilise** l'IA massivement. Il ne
  s'agit pas de la freiner, mais de la **cadrer**.
- **Pas une baguette magique** — AKORIS demande de la **discipline**. Il y a
  des checklists, des seuils, des verdicts. C'est le prix de la qualité.

---

## 0.7 À qui s'adresse ce livre

- **Vibe coders** qui ont senti que "ça part en vrille" et veulent structurer.
- **Développeurs solo** qui utilisent l'IA et veulent éviter la dette.
- **Tech leads** qui veulent cadrer l'usage de l'IA dans leur équipe.
- **Curieux** qui se demandent comment gouverner des agents IA.

---

> **AKORIS — L'IA produit ; le contrôle vérifie ; l'autorité humaine décide.**

---

*Fin du chapitre 0.*
