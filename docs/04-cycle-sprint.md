# Chapitre 4 — Le Cycle de Vie d'un Sprint

## 1. La Roadmap : Vision et Planification
La roadmap assure la visibilité à moyen terme et la cohérence des itérations.
- **Vue d'ensemble** : Le fichier `.akoris/roadmap/ROADMAP.md` contient un tableau récapitulatif de tous les sprints (Numéro, Titre, Type, Version cible, Indicateur de sécurité 🔒, Statut).
- **Zoom avant** : Les 3 prochains sprints sont détaillés individuellement dans `.akoris/roadmap/sprint-NN.md`. L'Orchestrator a l'obligation de maintenir ce tampon de 3 sprints d'avance.
- **Règles de gouvernance** : Un sprint est limité à un maximum de **20 tâches**. Au-delà, l'Orchestrator doit découper le périmètre. Tout changement structurant à la roadmap impose la création d'un ADR (Architecture Decision Record).

## 2. Les 5 Étapes du Cycle de Sprint
Un sprint suit un flux de travail rigide, piloté par la convention GO :
1. **Planification (Onglet A)** : L'Orchestrator propose le découpage du sprint, les options techniques et une recommandation. Il s'arrête et attend le `go` du Validator.
2. **Exécution (Onglet B)** : Sur `go`, le Builder exécute les tâches, code, documente les aspects techniques et prépare les commits.
3. **Audit (Onglet C)** : L'Auditor réalise le QA permanent (tests, critères d'acceptation) et, si le sprint est marqué 🔒, le checkpoint SecOps. **L'Auditor recommande le push** au Validator dans son rapport d'audit, mais ne l'exécute pas.
4. **Revue et Verdict (Validator)** : Le Validator examine le rapport d'audit et tranche. Il peut émettre `go` (clôture propre), `go with reserve: <détails>` (clôture avec ouverture de dette), ou `no-go: <raison>` (retour en planification).
5. **Clôture et Push (Onglet B)** : Une fois le verdict `go` obtenu, le Validator donne un second `go` dans l'onglet B. **C'est alors le Builder qui exécute le `git push`**, suivi du merge dans `main` et de l'apposition du tag SemVer.

## 3. Le Moteur de Coordination : `state.md`
Le fichier `.akoris/state.md` orchestre le flux pour éviter les collisions entre agents :
- **Cycle du verrou (`locked_by`)** : Au début de son tour, l'agent vérifie que `next_agent == lui` et que `action == go`. Il acquiert alors le verrou en écrivant `locked_by: <son_nom>`. À la fin de son tour, il libère le verrou (`locked_by: null`) avant de mettre à jour `next_agent`.
- **Lecture/Écriture** : `state.md` est lu uniquement au démarrage du tour. Il est écrit de manière atomique **en dernier**, jamais au milieu d'une opération.

## 4. La Gestion des Tâches et la Traçabilité Git
La traçabilité est la clé de voûte de la méthode AKORIS. Elle repose sur des règles strictes de découpage et de commit :
- **Règle d'atomicité** : 1 tâche = 1 critère d'acceptation = ≥ 1 commit. Le découpage s'arrête au niveau de la tâche ; les sous-tâches sont interdites.
- **Format des commits** : Respect strict des *Conventional Commits* (`<type>(<scope>): <description>`).
- **Footers obligatoires** : Chaque commit doit contenir les métadonnées de traçabilité suivantes :
  ```text
  Sprint: NN
  Tâche: TN
  Refs: ADR-NNNN, DT-NNN
  Signed-off-by: Nom Prénom <email>
  ```
  Le trailer `Signed-off-by:` (DCO - Developer Certificate of Origin) est **obligatoire** pour certifier l'origine et la paternité de chaque ligne de code produite.
- **Journalisation** : Le Builder consigne tous les événements Git (commits, push, merge, tag, conflits) dans `.akoris/sprints/sprint-NN-git.md`.
