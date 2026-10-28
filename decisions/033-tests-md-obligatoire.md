# Décision 033 — doc/tech/tests.md obligatoire V0

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

`doc/tech/tests.md` est **obligatoire en V0**. C'est le référentiel de la stratégie de tests.

## Règles

- Contenu : familles actives, où, comment exécuter, seuils, grille de verdicts.
- Écrit par le Builder (phase 9 bootstrap).
- Lu par l'Auditor (avant d'auditer).
- Lu par le Validator (avant de trancher).

## Justification

- **L'Auditor a besoin d'un référentiel** : sans, il audite à l'aveugle.
- **Le Builder a besoin d'un contrat** : sans, il improvise.
- **Le Validator a besoin d'une grille** : sans, il tranche subjectivement.

## Alternatives écartées

- **V1** : l'Auditor sans référentiel en V0.
- **Dans contexte.md** : duplication, mélange gouvernance/doc.
- **Pas de tests.md** : référentiel implicite, dérive.
