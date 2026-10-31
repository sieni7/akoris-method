# Roadmap du CLI AKORIS (V1)

> Ce document définit la vision, l'architecture et les commandes du futur outil en ligne de commande (CLI) d'AKORIS.
> **Statut** : Planifié (V1). Aucun code n'est encore écrit.
> **Volume** : 5 commandes racines, 22 sous-commandes.

## 1. Vision et Principes

Le CLI AKORIS (nom de code : `akoris-cli`) vise à réduire la friction d'adoption de la méthode et à automatiser les tâches répétitives, sans jamais violer le principe directeur : **"L'IA produit ; le contrôle vérifie ; l'autorité humaine décide."**

**Principes de conception :**
- **Sécurité** : Aucune gestion de secrets dans le CLI.
- **Contrôle humain** : Le CLI propose, mais ne force jamais une action.
- **Guidage interactif** : À chaque fin de tour, le CLI affiche une invite claire indiquant qui doit agir et quelles sont les options.

## 2. L'Expérience Utilisateur (L'Invite Interactive)

C'est le cœur de l'UX du CLI. À chaque exécution d'une commande, le CLI doit afficher une invite formatée.

**Exemple d'invite :**
```text
🔴 Agent Builder prêt !

Validator, action requise :
1. Valider le code et passer à l'Audit (go)
2. Demander des corrections (go with reserve)
3. Rejeter et re-planifier (no-go)

Recommandation : Action 1 (go).
Pourquoi : Les 24 tests passent et la couverture est à 85%.
Conséquence : Passage de la phase d'exécution à la phase d'audit.

Tapez `1`, `2` ou `3` pour choisir.
```

## 3. Les Commandes (V1 - Priorité P0)

### A. Amorçage (`akoris init`)
- **`init <nom>`** : Scaffolde un nouveau projet (crée `app/`, `doc/`, `.akoris/`, copie les agents, initialise Git et DCO). Se termine en positionnant le focus sur l'agent Orchestrator (Onglet A) pour le bootstrap.

### B. Gouvernance (`akoris govern`)
*Rôle : Coordonner les agents et lire/écrire `state.md`.*
- **`govern status`** : Affiche un tableau récapitulatif (Sprint, Phase, Agent actif, Tâches restantes, Dettes ouvertes, Statut du verrou).
- **`govern focus`** : Affiche l'agent actif et l'onglet correspondant, avec l'invite interactive (options 1/N, recommandation).
- **`govern go`** : Prépare le `go`. Affiche le mot en évidence pour copie manuelle (ou l'envoie via API en V2).
- **`govern state show [--raw]`** : Affiche l'état. Par défaut, un résumé lisible. Avec `--raw`, le YAML brut.
- **`govern task list`** : Affiche un tableau formaté des tâches du sprint (ID | Statut | Description).
- **`govern debt list`** : Liste les dettes (lit `debt/index.md`).

### C. Contrôle (`akoris audit`)
*Rôle : Exécuter les règles de qualité et de sécurité.*
- **`audit doctor`** : Lance l'auto-diagnostic (R1, R2, R4). Options `--project` et `--debug`.
- **`audit method`** : Vérifie la cohérence du dépôt AKORIS (8/8 checks).
- **`audit logs`** : Affiche les derniers événements de `sprint_report.md` ou `sprint-NN-git.md`.

### D. Configuration (`akoris config`)
*Rôle : Gérer l'expérience utilisateur du CLI.*
- **`config completion`** : Génère le script d'autocomplétion (bash, zsh, fish, powershell).

## 4. Les Commandes (V1.5 - Priorité P1)

- **`govern switch <agent>`** : Force manuellement le changement d'agent dans `state.md`.
- **`govern context`** : Génère le prompt de contexte AKORIS à coller dans l'onglet actif.
- **`govern state watch`** : Affiche en temps réel les modifications de `state.md`.
- **`govern debt add`** : Ouvre une nouvelle dette (crée le fichier `DT-NNN.md`).
- **`audit check`** : Vérifie que les derniers commits respectent le format Conventionnel et le DCO.
- **`prompt list`** : Liste les templates SPA disponibles.
- **`prompt create`** : Génère un squelette de prompt avec les 13 rubriques.
- **`config alias set/get/rm/ls`** : Gère les raccourcis de commandes.

## 5. Les Commandes (V2 - Priorité P2)

- **`govern state graph`** : Affiche le chemin de transition (ex: Plan -> Code -> Audit) en ASCII.
- **`prompt resolve`** : Injecte automatiquement le Gist et le contexte dans une instance SPA.
- **`prompt evaluate`** : Vérifie qu'un prompt respecte les 13 rubriques du standard.
- **Orchestration native** : Intégration avec les API des LLM pour envoyer le `GO` sans copier-coller.

## 6. Anti-patterns (Ce qui est écarté)

| Commande rejetée | Raison de l'exclusion |
| :--- | :--- |
| **`secrets`** | Risque de sécurité majeur. Les secrets doivent rester dans l'environnement. |
| **`dashboard`** | Redondant avec `govern status`. Le CLI reste dans le terminal. |
| **`registry`** | Collision avec le vocabulaire AKORIS (ADR, Dettes). |
| **`doctor --fix`** | Violation du principe "L'autorité humaine décide". Le CLI propose, ne corrige pas. |
