# Chapitre 3 — Démarrage et Initialisation

## 1. La Phase 0 : Initialisation des Onglets
Avant tout développement, l'environnement de travail doit être initialisé manuellement pour garantir l'alignement des agents. Cette phase ne nécessite aucun `GO` du Validator, mais une validation séquentielle stricte :
1. **Terminal** : Création des répertoires racines (`mkdir app doc .akoris`) et copie des templates depuis le référentiel de la méthode vers `.akoris/`.
2. **Onglet A (Orchestrator)** : Coller la configuration `orchestrator.md` et répondre "prêt".
3. **Onglet B (Builder)** : Coller la configuration `builder.md` et répondre "prêt".
4. **Onglet C (Auditor)** : Coller la configuration `auditor.md` et répondre "prêt".
5. **Onglet A (Orchestrator)** : Coller le fichier `bootstrap.md` pour lancer la phase 1.

**Règle d'or** : L'ordre A → B → C est immuable. La réponse "prêt" de chaque agent valide son initialisation. La commande `doctor` n'est disponible qu'à partir de la phase 1.

## 2. Le Bootstrap en 10 Phases
Le bootstrap est le processus de fondation du projet. Il est découpé en 10 phases séquentielles, chacune **nécessitant** un `go` explicite du Validator avant de passer à la suivante :

| Phase | Nom | Livrable clé | GO requis |
|---|---|---|---|
| 1 | Vérification | Validation de l'environnement et des prérequis | `go` |
| 2 | Arborescence | Création de la structure de dossiers (`app/`, `doc/`, `.akoris/`) | `go` |
| 3 | Contexte | Rédaction de `.akoris/contexte.md` (§0 à §22) | `go` |
| 4 | Roadmap (Résumé) | Création de `.akoris/roadmap/ROADMAP.md` | `go` |
| 5 | Roadmap (Détail) | Détail des 3 premiers sprints dans `.akoris/roadmap/sprint-NN.md` | `go` |
| 6 | Contexte §10 | Intégration de la roadmap dans le fichier de contexte | `go` |
| 7 | ADR Fondateurs | Création des 4 ADR de base (Stack, Séparation, GO, Tests) | `go` |
| 8 | État Initial | Initialisation de `state.md`, template de dette et script d'index | `go` |
| 9 | Stack Itérative | Configuration de l'outillage (linting, CI, tests) | `go` × N |
| 10 | Clôture Bootstrap | Finalisation et lancement officiel du Sprint 1 | `go` (Onglet B) |

## 3. Le Fichier `contexte.md` : La Constitution du Projet
Le fichier `.akoris/contexte.md` est la source unique de vérité pour la gouvernance du projet.
- **Injection systématique** : Il est injecté en tête de CHAQUE session LLM pour garantir que les agents opèrent avec le même cadre de référence.
- **Immuabilité** : Il est versionné et **modifiable uniquement par le Validator (humain)**. Aucun agent (Orchestrator, Builder, Auditor) n'a le droit de l'écrire ou de le modifier.
- **Structure exhaustive** : Il est strictement calqué sur le template AKORIS et contient exactement **22 sections (§0 à §22)**. Ces sections couvrent l'identité AKORIS, l'identité du projet, les rôles des agents, la séparation des préoccupations, les conventions, les garde-fous, la convention GO, le registre des dettes, le format de `state.md`, les règles du verrou, la roadmap, les ADR, Git, les tags, la documentation, la commande `doctor`, la stratégie de tests, le découpage des tâches, la Phase 0, le Bootstrap, le double mandat de l'Auditor, le glossaire, et enfin la **§22 — Outils compatibles**, qui définit les prérequis techniques pour faire tourner la méthode (3 agents simultanés, dossier partagé, verrou fichier).
