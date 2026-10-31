# Chapitre 6 — Traçabilité et Gestion de Version

## 1. La Convention de Commits (Conventional Commits)
Pour garantir la lisibilité de l'historique et l'automatisation du CHANGELOG, le Builder doit respecter scrupuleusement la norme *Conventional Commits*.

**Structure imposée :**
```text
<type>(<scope>): <description>

[corps optionnel]
```

Types autorisés : feat (nouvelle fonctionnalité), fix (correction), docs (documentation), test (tests), refactor (restructuration), chore (maintenance), sec (sécurité). Les changements cassants (breaking changes) doivent utiliser le suffixe ! (ex: feat!:) ou le footer BREAKING CHANGE:.

Scopes recommandés : auth, api, ui, db, sync, doc, akoris, state, debt.

Un outil de commitlint est configuré en CI pour rejeter automatiquement tout commit non conforme.

## 2. Les Métadonnées de Traçabilité (Footers Obligatoires)
Le lien entre le code source et la gouvernance AKORIS est matérialisé par des footers obligatoires dans le corps de chaque commit.

Format strict :

```text
Sprint: NN
Tâche: TN
Refs: ADR-NNNN, DT-NNN
Signed-off-by: Nom Prénom <email>
```

Sprint & Tâche : Permettent de tracer exactement quelle tâche du current_sprint.md a généré ce commit.

Refs : Lie le commit aux décisions d'architecture (ADR) ou aux dettes techniques (DT) concernées.

DCO (Developer Certificate of Origin) : Le trailer Signed-off-by: est obligatoire. Il certifie que le Builder a le droit de soumettre ce code et qu'il en assume la paternité, garantissant l'intégrité juridique du dépôt.

## 3. Gestion des Branches et Flux de Push
Le modèle de branchement est volontairement simple pour éviter la complexité inutile :

main : Branche stable, protégée, reflétant la production.

sprint-NN : Branche de développement pour le sprint en cours.

Le protocole de push en deux temps :

L'Auditor termine son audit et recommande le push dans son rapport.

Le Validator émet son verdict (go) dans l'Onglet C.

Le Validator donne ensuite un go de déclenchement dans l'Onglet B.

C'est uniquement à ce moment que le Builder exécute le git push, résout d'éventuels conflits (rebase/merge), fusionne sprint-NN dans main, et pose le tag.

## 4. Tags SemVer et CHANGELOG
La gestion des versions suit la norme Semantic Versioning (SemVer) au format vMAJOR.MINOR.PATCH :

MAJOR : Changement cassant (Breaking Change). Nécessite obligatoirement un ADR.

MINOR : Nouvelle fonctionnalité rétrocompatible.

PATCH : Correction de bug rétrocompatible.

Le tag cible est proposé par l'Orchestrator lors de la planification, validé par le Validator lors du verdict, et posé par le Builder après le merge.

Maintenance du CHANGELOG :
Le fichier doc/produit/changelog.md doit être tenu à jour selon le standard Keep a Changelog. Il est structuré par version et généré à partir des commits conventionnels du sprint. Un sprint ne peut être considéré comme go que si la documentation, et particulièrement le changelog, est à jour.
