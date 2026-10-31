# Chapitre 8 — Diagnostic, Évolution et Réplicabilité

## 1. La Commande `doctor` : L'Auto-Diagnostic Non Intrusif
La commande `doctor` est l'outil d'observation et de santé du système AKORIS. Elle est disponible dans tous les onglets (A, B, C) et obéit à une règle d'or : **elle ne modifie pas `state.md`, ne consomme pas de `GO` et ne déclenche pas de tour d'agent**.

- **Rapports par défaut** :
  - **R1 (État)** : Affiche l'état courant du verrou, de la phase et du prochain agent.
  - **R2 (Statistiques)** : Récapitulatif des tours, commits et dettes résorbées par agent.
  - **R4 (Auto-diagnostic)** : Vérifie la cohérence des règles AKORIS (ex: présence des ADR fondateurs, format des commits).
- **Options avancées** :
  - `--project` : Génère le rapport R5 (santé globale du projet), recommandé dans l'onglet A.
  - `--debug` : Génère le rapport R6 pour le diagnostic d'erreur en cas de blocage.
  - `--report` (V2) : Écrit la sortie dans `.akoris/doctor/` pour archivage et analyse historique.
- **Comportement en cas d'anomalie** : Si une anomalie bloquante est détectée, `doctor` la signale et formule une recommandation, mais n'agit jamais de lui-même. Seul le Validator peut ordonner une correction.

## 2. Roadmap du CLI AKORIS
Pour réduire la friction d'adoption, l'outillage AKORIS évolue selon une roadmap CLI claire :

- **V0 (Scripts de base)** : Automatisation minimale via des scripts bash et Python (`init-project.sh`, `build-debt-index.py`). Suffisant pour appliquer la méthode manuellement avec rigueur.
- **V1 (CLI Interactif)** : Introduction d'un CLI dédié pour gérer le verrouillage de `state.md`, échafauder (scaffold) automatiquement les squelettes de tâches, d'ADR et de dettes, et valider les commits localement avant le push.
- **V2 (Orchestration Native)** : Intégration complète avec les métriques de performance (rapport R3, nécessitant `metrics.md`) et orchestration multi-agents native, réduisant encore la charge cognitive du Validator.

Le script validate-method.py effectue une validation structurelle (présence des fichiers, liens, sections). Il ne remplace pas l'Auditor pour la validation sémantique de la synchronisation documentaire.

## 3. Réplicabilité de la Méthode
La force d'AKORIS réside dans sa capacité à être répliquée à l'identique sur n'importe quel nouveau projet, garantissant une qualité constante dès le premier jour.

- **Le script `init-project.sh`** : Ce script est le point d'entrée unique pour initialiser un nouveau projet. En quelques secondes, il :
  1. Crée l'arborescence racine (`app/`, `doc/`, `.akoris/`).
  2. Copie les templates officiels des agents (Orchestrator, Builder, Auditor) depuis le référentiel `akoris-method/` vers `.akoris/config/`.
  3. Initialise un `contexte.md` vierge mais structuré avec les 22 sections (§0 à §22), prêt à être complété par le Validator.
  4. Configure les hooks Git pour le `commitlint` et le format DCO.
- **Garantie de conformité** : Aucun projet AKORIS ne doit démarrer "à la main". L'utilisation de `init-project.sh` assure que les garde-fous, la séparation des pouvoirs et la traçabilité sont en place avant même que la première ligne de code ne soit écrite.

## 4. Mode Équipe (V2)
Dans sa version actuelle (V1), AKORIS fonctionne avec un seul Validator humain. La décision 048 (V2) prévoit un mode équipe où un second humain (Reviewer) peut approuver les changements. Ce mode n'est pas encore implémenté dans les templates.


## 5. Les Skills Packs (V1.5)
Une compétence (Skill) est un savoir-faire métier (ex: QA-01 Code Reviewer). Un rôle (Builder, Auditor) active cette compétence via une instance SPA. Cette séparation garantit que le code n'est jamais mélangé avec la gouvernance.
