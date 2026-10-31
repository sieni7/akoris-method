# Standard de Prompt AKORIS (SPA)

**Version :** 0.1
**Portée :** structure et exigences minimales des prompts opératoires réutilisables au sein d’un projet AKORIS.

## Finalité

Le Standard de Prompt AKORIS (SPA) formalise les instructions données à un agent IA afin qu’elles soient lisibles, délimitées et contrôlables. Il vise cinq propriétés complémentaires :

- **Clarté** — chaque instruction précise le rôle, l’objectif et les attentes sans formulation équivoque.
- **Maîtrise** — les responsabilités, autorisations, limites et points de décision humaine sont explicites.
- **Discipline** — le prompt organise le travail et interdit les actions hors mandat.
- **Traçabilité** — les sources, décisions, livrables et changements attendus peuvent être retrouvés.
- **Contrôlabilité** — les résultats peuvent être vérifiés au moyen de critères observables.

Le SPA ne garantit pas à lui seul la qualité d’une réponse. Il rend les instructions et leurs résultats plus faciles à examiner.

## Architecture

Le SPA s’organise en trois niveaux :

1. **Standard** — le présent document définit les rubriques, les principes de conception et les règles de conformité.
2. **Template** — [`templates/spa/SPA-TEMPLATE.md`](../templates/spa/SPA-TEMPLATE.md) fournit un moule vierge à renseigner, sans présumer d’un rôle ou d’un projet.
3. **Instances** — des prompts complets adaptés à un usage, un agent ou un projet. Chaque instance renseigne les rubriques du template et respecte les règles AKORIS applicables.

Une instance peut ajouter des sous-rubriques utiles, mais ne doit ni renommer, omettre ou réordonner les treize rubriques normatives, ni contredire les règles d’autorité applicables.

## Rubriques normatives

Tout prompt conforme comporte les treize rubriques suivantes, dans cet ordre. Les numéros vont de 0 à 12, soit treize rubriques au total.

### 0. Contrat d'exécution

Définit les conditions d’activation, les autorisations préalables, les préconditions et les situations qui imposent de s’arrêter.

### 1. Identité et rôle

Nomme l’agent, sa fonction, ses responsabilités et les pouvoirs qu’il ne possède pas.

### 2. Contexte

Fournit les informations de fond, les références fiables, la hiérarchie des sources et les éléments spécifiques à la mission.

### 3. Objectifs et résultats attendus

Décrit le résultat visé et les effets attendus, sans confondre objectif et moyens.

### 4. Périmètre et exclusions

Délimite les tâches, fichiers, systèmes ou sujets inclus et exclus.

### 5. Entrées et sources de vérité

Identifie les données d’entrée, leur provenance, leur autorité et la conduite à tenir si elles manquent ou se contredisent.

### 6. Processus et phases

Présente les étapes de travail, leur ordre, leurs dépendances et les points de passage entre elles.

### 7. Règles de décision et escalade

Précise qui décide, les choix permis, les conditions d’escalade et les règles d’arrêt en cas de blocage.

### 8. Outils et environnement d'exécution

Décrit les outils, accès, environnements et limites opérationnelles nécessaires à la mission.

### 9. Livrables et format de sortie

Spécifie les résultats à remettre, leur emplacement, leur structure et leur format.

### 10. Qualité et critères d'acceptation

Définit des critères observables permettant de vérifier que le travail est complet, cohérent et acceptable.

### 11. Contraintes, risques et sécurité

Énonce les contraintes obligatoires, les risques pertinents, les données à protéger et les actions interdites.

### 12. Communication et fin de mission

Fixe le protocole de compte rendu, les informations à transmettre, les conditions de clôture et la réponse attendue.

## Principes de conception

- **Universalité** — conserver un socle intelligible pour différents rôles et domaines, sans imposer d’outil particulier.
- **Adaptabilité** — adapter les consignes au contexte de l’instance sans altérer l’ordre et le sens des rubriques.
- **Proportionnalité** — ajuster le niveau de détail et les contrôles à l’impact et à la complexité de la mission.
- **Non-redondance** — éviter les répétitions et désigner explicitement une source de vérité lorsqu’une règle est partagée.
- **Traçabilité** — relier les instructions importantes à leurs sources, décisions, livrables ou critères de vérification.
- **Indépendance technologique** — décrire les capacités et résultats requis avant de nommer une technologie, sauf nécessité propre au contexte.

## Règles de conformité

Un prompt est conforme au SPA lorsque les six règles suivantes sont respectées :

1. **Structure** — les treize rubriques normatives apparaissent dans l’ordre prescrit, avec leurs numéros et titres inchangés.
2. **Complétude** — chaque rubrique contient une instruction utile ou indique explicitement qu’elle n’est pas applicable avec une justification.
3. **Cohérence** — les rôles, autorisations, sources, étapes et livrables ne se contredisent pas entre eux ni avec les règles gouvernantes.
4. **Délimitation** — le périmètre, les exclusions et les limites d’autorité sont explicites; une demande hors périmètre conduit à l’arrêt ou à une escalade.
5. **Validation** — les décisions qui relèvent d’une autorité humaine ne sont pas prises implicitement par l’agent; les seuils d’approbation sont nommés.
6. **Vérifiabilité** — les livrables et critères d’acceptation sont observables, et les affirmations importantes peuvent être reliées à des éléments vérifiables.

## Relation entre AKORIS et le SPA

**AKORIS gouverne; le SPA formalise.** AKORIS définit la gouvernance du travail assisté par IA : séparation des pouvoirs, autorité humaine, source de vérité, contrôle et traçabilité. Le SPA fournit une forme normalisée pour exprimer les instructions d’un prompt.

Le SPA n’est ni un remplacement d’AKORIS ni une autorité concurrente. Une instance SPA utilisée dans un projet AKORIS doit respecter `METHOD.md`, le contexte spécifique du projet et les décisions applicables. En cas de conflit, l’agent s’arrête et demande l’arbitrage de l’autorité humaine plutôt que d’inventer une priorité.
