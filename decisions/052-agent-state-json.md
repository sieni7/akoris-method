# Décision 052 — État opérationnel structuré des agents

**Statut :** décision de cadrage validée pour étude et conception ; implémentation non engagée.  
**Portée :** architecture de contexte, état et reprise des agents AKORIS.

## 1. Principe

Le fichier documentaire `state.md` doit être renforcé par un fichier d'état structuré au format JSON. Le nom cible reste à arbitrer entre `state.json` et `agent_state.json`.

Les deux représentations sont complémentaires :
- `state.md` expose un état lisible par les humains : contexte utile, explications, décisions, points d'attention et historique synthétique.
- Le fichier JSON expose un état explicite, typé et exploitable par les agents et les outils : identifiants, statuts, affectations, étapes, dépendances, références et métadonnées nécessaires à l'exécution.

## 2. Conséquences structurelles et opérationnelles

La conception devra traiter au minimum :
- la reprise fiable d'une mission après interruption ;
- le chargement sélectif et non ambigu du contexte ;
- la transmission contrôlée de l'état entre A, B et C, dans l'ordre obligatoire A → B → C ;
- le suivi des missions, activations de spécialisations, livrables, vérifications, blocages et décisions ;
- la traçabilité des sources et des preuves ;
- l'interopérabilité avec les outils et les automatisations ;
- la validation du format et la gestion de son évolution.

## 3. Cohérence et autorité des données

Les deux fichiers ne doivent pas devenir des sources concurrentes ni diverger silencieusement. La conception devra préciser :
- quelle représentation fait autorité pour chaque catégorie de données ;
- si le JSON est la source structurée de référence et le Markdown sa vue explicative dérivée, ou si une autre répartition est justifiée ;
- comment sont générés, synchronisés ou contrôlés les deux fichiers ;
- comment les conflits, données absentes et états périmés sont détectés ;
- comment sont versionnés le schéma JSON et les migrations.

Aucune règle de synchronisation ou de priorité n'est réputée définitivement décidée par la présente note.

## 4. Garanties AKORIS

Le dispositif ne modifie pas les rôles constitutionnels :
- A reste l'orchestrateur et le point de coordination ;
- B exécute les missions qui lui sont confiées ;
- C intervient après B pour la vérification indépendante ;
- l'ordre A → B → C demeure obligatoire.

Un état JSON ne confère aucune autorité supplémentaire à un agent et ne vaut ni approbation humaine, ni validation d'audit, ni autorisation de fusion ou de déploiement.

## 5. Travaux à conduire

Avant toute implémentation :
1. inventorier le contenu et les usages actuels de `state.md` ;
2. définir les cas d'usage et le modèle de données minimal ;
3. arbitrer le nom du fichier ;
4. proposer un schéma JSON versionné et documenté ;
5. définir les règles d'autorité, de synchronisation et de validation ;
6. définir les règles de mise à jour par rôle et les protections contre les écritures concurrentes ;
7. prévoir des tests de cohérence, de migration et de reprise de mission.

## 6. Positionnement dans la feuille de route

Ce chantier est transversal. Il doit être conçu en cohérence avec le contrat opérationnel commun v0.1 et les fiches de spécialisation, puis intégré à la conception de l'architecture opérationnelle AKORIS. Il ne doit pas être réduit à une simple tâche de documentation ni implémenté prématurément avant clarification du modèle.
