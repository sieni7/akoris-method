# Décision 030 — Stratégie de tests V0

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

En V0 : **TNR obligatoire + sécu checkpoint (`🔒`) + UAT implicite (verdict)**. E2E uniquement si parcours critique unique. Perf en V2.

## Règles

- **TNR** (unit + integration) : obligatoire, à chaque sprint.
- **Sécu** : checkpoint aux sprints `🔒`.
- **UAT** : implicite (le verdict du Validator EST l'UAT).
- **E2E** : 1 seul si parcours critique unique, sinon V1.
- **Perf** : V2.

## Justification

- **TNR** = socle non négociable.
- **Sécu checkpoint** = déjà dans la méthode (Auditor SecOps).
- **UAT implicite** = le verdict suffit en V0.
- **E2E** = fragile, lent, coûteux en V0.
- **Perf** = prématuré.

## Alternatives écartées

- **Tout en V0** : paralysie.
- **TNR seul** : sécu non couverte.
- **E2E en V0** : flaky, lent.
