# Décision 010 — Séparation des pouvoirs

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 1-2 (fondations)

---

## Décision

Séparation stricte entre **produire** (Builder), **vérifier** (Auditor), **décider** (Validator).

## Règles

- Le Builder **produit** : code, doc, commits.
- L'Auditor **vérifie** : tests, findings, rapports.
- Le Validator **décide** : verdict, push, dettes.
- Aucun chevauchement.

## Justification

- Principe directeur AKORIS : "L'IA produit ; le contrôle vérifie ; l'autorité humaine décide."
- Évite l'auto-validation (biais).
- Évite l'auto-autorisation (dérive).

## Alternatives écartées

- **Fusion production/vérification** : biais.
- **Fusion vérification/décision** : dérive.
- **Fusion production/décision** : goulot d'étranglement.
