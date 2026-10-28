# Décision 047 — Résilience (resume, rollback, hotfix)

- **Statut :** V2 / non implémentée
- **Date :** 2026-10-28
- **Contexte :** Bloc 8d (process)

---

## Décision

AKORIS couvre **3 parcours de résilience** : reprise de session, rollback post-merge, hotfix en production.

## Règles

### 1. Session resume

- **Problème** : un onglet perd son contexte (fermeture, timeout).
- **Solution** : prompt `session-resume.md` qui recharge le contexte en 1 tour.
- **Contenu** : lit `state.md`, `contexte.md`, `current_sprint.md`, `sprint_report.md`.

### 2. Rollback post-merge

- **Problème** : un merge dans `main` casse la prod.
- **Solution** : procédure `rollback.md` (`git revert`, `git tag`, `validate-state`).
- **Contenu** : identifier le commit, revert, tag `vX.Y.Z-rollback`, mise à jour `state.md`.

### 3. Hotfix en production

- **Problème** : bug critique en prod, besoin de corriger hors sprint.
- **Solution** : branche `hotfix-NN`, audit **accéléré**, merge sans sprint.
- **Contenu** : créer `hotfix-NN`, corriger, audit QA rapide, merge, tag `vX.Y.Z+1`.

### Scripts V2

- `akoris resume` : recharge la session.
- `akoris rollback` : rollback guidé.
- `akoris hotfix` : hotfix guidé.

## Justification

- **Couverture complète** : happy path + incidents.
- **Réalisme** : les incidents arrivent, il faut les gérer.
- **Traçabilité** : chaque parcours est documenté.

## Alternatives écartées

- **Happy path seulement** : pas de gestion des incidents.
- **Procédures orales** : oublis, erreurs.
- **Pas de scripts** : friction.
