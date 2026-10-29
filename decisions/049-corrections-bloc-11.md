# Décision 049 — Clarifications des règles de verrou, résorption et clôture

- **Statut :** figée
- **Type :** clarification
- **Date :** 2026-10-28
- **Contexte :** Bloc 11 (revue cycle 2 : règles de verrou (002), de résorption (021) et de clôture (025))

---

## Décision

Cette décision **clarifie et supersède partiellement** les décisions 002, 021 et 025
sur trois points : le verrou `locked_by`, la résorption de dette et la fermeture du sprint.
Elle **ne modifie pas** les décisions elles-mêmes (immuables) ; elle **précise**
ce qui fait foi en cas de divergence.

## Règles

### R1 — Verrou `locked_by` (supersède 002 sur ce point)

- L'agent **écrit** `locked_by: <lui>` au **début** de son tour, après avoir reçu `GO` du Validator ET vérifié `next_agent == lui`.
- L'agent **libère** `locked_by: null` à la **fin** de son tour, avant d'écrire `next_agent`.
- Si `locked_by != moi` ET `locked_by != null` → « pas mon tour ».
- Si `locked_by == null` → verrou libre (l'agent peut prendre si `next_agent == lui`).

### R2 — Résorption de dette (supersède 021 et 025 sur ce point)

- `ouverte` → `en_cours` : **Builder libre** (début de résorption).
- `en_cours` → `resorbee` : **Builder UNIQUEMENT si** `audit_report.md` contient un finding positif confirmant la résorption (commit + test verts). Sinon statut reste `en_cours`.
- `acceptee_definitivement` : **Validator uniquement**, avec ADR justifiant l'acceptation définitive.
- L'Auditor **ne modifie pas** les fichiers `debt/` (scope inchangé). Il **valide dans `audit_report.md`**.

### R3 — Phase: closed

- **Clarification du 2026-10-29 :** Le Builder écrit `phase: closed` en fin de PUSH (opération technique) ; l'Orchestrator vérifie et confirme. Le Validator reste décideur de la transition `review → closed` (décision de gouvernance).

## Justification

- **Cohérence** : la revue cycle 2 a détecté des contradictions entre les décisions 002/021/025 et les templates.
- **Séparation des pouvoirs** : l'Auditor valide, le Builder met à jour le statut, le Validator décide. La résorption est prouvée (audit), pas déclarée.
- **Immutabilité préservée** : 002/021/025 restent « figées » dans l'historique ; 049 précise ce qui fait foi.
- **Responsabilité de clôture** : le Builder écrit `phase: closed` à la fin de PUSH ; l'Orchestrator vérifie et signale toute anomalie.

## Alternatives écartées

- **Modifier 002/021/025 en place** : viole l'immutabilité, contredit décision 015 (esprit ADR).
- **Créer 3 décisions séparées (049-051)** : surcharge, complexité inutile. Une seule décision de synthèse suffit.
- **Ne rien faire** : les contradictions persistent, la méthode reste incohérente.

---

*Remplace partiellement : décisions 002 (verrou), 021 (statut dette), 025 (résorption).*
