# Chapitre 2 — L'Architecture du Système

## 1. Les 3 Piliers Structurels (Séparation des répertoires)

L'intégrité du projet repose sur une séparation stricte des préoccupations au niveau du système de fichiers :

- **`app/`** : Le produit exécutable (ce qui est livré). **Seul le Builder écrit ici.** C'est le code source de l'application.
- **`doc/`** : Le documentaire. Il est divisé en `doc/tech/` (rédigé par le Builder : architecture, API, tests) et `doc/produit/` (rédigé par l'Orchestrator : guide utilisateur, pitch, changelog).
- **`.akoris/`** : La gouvernance. Le répertoire contient le contexte, l'état (`state.md`), la roadmap, les ADR, les sprints, les audits et les dettes. Chaque agent a un scope d'écriture défini. Aucun agent ne modifie `app/` et `.akoris/state.md` de façon contradictoire dans le même tour.

## 2. Les 3 Onglets de Travail (Le flux SPA)

Le développement est orchestré via trois sessions LLM simultanées (ou onglets), chacune incarnant un agent avec un rôle et un scope d'écriture stricts :

- **Onglet A — Orchestrator** : Planifie, découpe les tâches, propose des options, coordonne et régénère l'index des dettes. Il ne code pas, n'audite pas et ne valide pas.
- **Onglet B — Builder** : Exécute, code, documente (aspect technique), commit, push, merge et tag selon les autorisations AKORIS. Il ne planifie pas, n'audite pas et ne valide pas.
- **Onglet C — Auditor** : Effectue le QA permanent et les checkpoints SecOps (`🔒`). Il rapporte les anomalies et recommande le push au Validator. Il ne code pas, ne corrige pas et ne valide pas.
- **Le Validator (humain)** : Opère en dehors des agents automatisés. Il autorise, tranche les débats et ouvre les dettes. Il est le seul à pouvoir modifier `.akoris/contexte.md`.

## 3. La Convention GO (Le moteur du flux)

Le système ne progresse que sur injonction humaine. Il existe deux types de signaux `GO` qu'il ne faut pas confondre :

- **GO de déclenchement** : Donné en début de tour (onglets A, B ou C). Il autorise l'agent à travailler sur la tâche en cours.
- **Verdict** : Donné exclusivement en fin de cycle (onglet C, après audit). Il tranche sur la livraison.

**Les 3 verdicts possibles :**

1. `go` : Clôture propre. La tâche est acceptée par le Validator.
2. `go with reserve: <détails>` : Clôture avec ouverture ou suivi de dettes. Les détails des réserves sont obligatoires (ex. `go with reserve: DT-001 manque de tests E2E`). Un verdict sans détail est refusé.
3. `no-go: <raison>` : Refus de la livraison. La raison est obligatoire. Le travail retourne à l'Orchestrator pour re-planification.

*Règle d'or* : Sans `GO` humain, l'agent reste en attente. Un agent ne lit `state.md` qu'au démarrage de son tour.

## 4. Le Cœur du Contrôle : `state.md`

Le fichier `.akoris/state.md` est l'unique source de vérité concernant l'état courant du système. Il assure la coordination entre les agents via un mécanisme de verrouillage strict :

- **Rôle** : Définir quel agent doit agir (`next_agent`), l'action attendue (`action`) et l'état des verdicts.
- **Mécanisme de verrouillage (`locked_by`)** : Un seul agent peut être verrouillé à la fois.
  - L'agent écrit `locked_by: <lui>` au **début** de son tour (après vérification du GO et de `next_agent`).
  - L'agent libère `locked_by: null` à la **fin** de son tour, avant de passer la main.
- **Cycle de vie d'un tour** :
  1. Lecture de `contexte.md` et `state.md` (début de tour uniquement).
  2. Acquisition du verrou (`locked_by`).
  3. Exécution de la tâche dans son scope autorisé.
  4. Libération du verrou et mise à jour atomique de `state.md` (en dernier, jamais au milieu).

Toute anomalie de verrou (ex. verrou orphelin de plus de 30 minutes) ne peut être résolue que par une intervention manuelle du Validator (`go force-unlock`).

---

*Fin du chapitre 2.*
