# Chapitre 7 — Gestion des Dettes et Décisions d'Architecture

## 1. Le Registre des Dettes (`debt/`)
Dans AKORIS, la dette technique n'est pas un échec, c'est un compromis conscient, tracé et maîtrisé. Le répertoire `.akoris/debt/` centralise cette gouvernance.

- **Structure** : Une dette = un fichier unique nommé `DT-NNN-titre.md` (où `NNN` est un identifiant séquentiel auto-incrémenté).
- **Frontmatter YAML obligatoire** : Chaque fichier doit contenir les métadonnées suivantes pour assurer un suivi rigoureux :
  ```yaml
  ---
  id: DT-NNN
  titre: <titre court et descriptif>
  priorite: P0 | P1 | P2 | P3
  statut: ouverte | en_cours | resorbee | acceptee_definitivement
  sprint_origine: <NN>
  decision_origine: go_with_reserve
  adr_lie: ADR-NNNN
  risque: "<description concise du risque>"
  impact: faible | moyen | eleve | critique
  sprint_resorption_prevu: <NN>
  cree_le: <YYYY-MM-DD>
  ---
  ```
- **Cycle de vie strict** :
  - `ouverte` → `en_cours` : Transition libre lorsque le Builder commence la résorption.
  - `en_cours` → `resorbee` : **UNIQUEMENT** si l'`audit_report.md` contient un finding positif confirmant la résorption. Sinon, le statut reste `en_cours`.
  - `acceptee_definitivement` : Décision exclusive du Validator, accompagnée d'un ADR justifiant pourquoi cette dette ne sera jamais résorbée.

## 2. Seuils Anti-Accumulation et Gouvernance
Pour éviter l'effet "boule de neige" de la dette, AKORIS impose des seuils d'alerte automatiques et des règles de gouvernance strictes :

- **Seuil P0/P1 > 3** : Si plus de 3 dettes de haute priorité (P0 ou P1) sont ouvertes, le prochain sprint **doit** impérativement inclure au moins une tâche de résorption.
- **Seuil Total > 10** : Si le nombre total de dettes ouvertes dépasse 10, l'Auditor a l'obligation de recommander un verdict `no-go`. Le Validator conserve le pouvoir final d'arbitrage et peut passer outre via un `go with reserve`, mais une nouvelle dette de gouvernance sera alors tracée.
- **Automatisation CI** : Le script `build-debt-index.py` est exécuté en fin de sprint par l'Orchestrator pour régénérer l'`index.md` du répertoire `debt/`. Cet index est versionné et sa conformité est vérifiée en CI pour garantir qu'aucune dette n'est "oubliée" ou orpheline.

## 3. Les Architecture Decision Records (ADR)
Les décisions structurantes sont immortalisées via des ADR. Ils garantissent que le "pourquoi" d'une architecture est aussi bien documenté que le "comment".

- **Format immuable** : `.akoris/adr/NNNN-titre-kebab-case.md` (4 chiffres, immuable une fois créé). En cas de remplacement, un nouveau numéro est généré avec la mention "Remplace ADR-NNNN".
- **Les 4 ADR Fondateurs** : Créés obligatoirement lors du bootstrap de tout projet AKORIS :
  1. `0001-stack.md` : Choix technologiques (ex: React, Supabase, Vercel).
  2. `0002-separation.md` : Séparation stricte des répertoires `app/`, `doc/`, `.akoris/`.
  3. `0003-convention-go.md` : Règles de la convention GO et séparation des pouvoirs.
  4. `0004-strategie-tests.md` : Politique de tests et seuils d'acceptation.
- **Lien organique avec les dettes** : Un ADR peut explicitement ouvrir une dette (ex: choix d'une solution rapide en attendant une refactorisation). Cette liaison est tracée via le champ `adr_lie` dans le frontmatter de la dette.
