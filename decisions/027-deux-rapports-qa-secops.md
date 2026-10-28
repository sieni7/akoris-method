# Décision 027 — Deux rapports QA/SecOps séparés

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

Les audits QA et SecOps produisent **deux fichiers séparés** : `audit_report.md` et `audit_report-secops.md`.

## Règles

- `audit_report.md` : QA (tous les sprints).
- `audit_report-secops.md` : SecOps (sprints `🔒` uniquement).
- Jamais de mélange dans un même fichier.
- Deux verdicts distincts, composition pour le verdict global.

## Justification

- **Séparation des mandats** : QA et SecOps ne regardent pas les mêmes choses.
- **Traçabilité** : historique QA et historique SecOps séparés.
- **Fichiers courts** : 80 + 60 lignes se lisent mieux que 140 lignes mélangées.

## Alternatives écartées

- **Un seul fichier, deux sections** : historique mélangé, verdict global masque les nuances.
- **Un fichier + sous-dossier** : asymétrie.
- **Pas de rapport séparé** : confusion.
