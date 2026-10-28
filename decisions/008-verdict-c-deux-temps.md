# Décision 008 — Verdict en C en deux temps

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 1-2 (fondations)

---

## Décision

Dans l'onglet C, le Validator tape **deux fois** : `go` (lance l'audit), puis **verdict** (tranche).

## Règles

- 1er `go` : autorise l'Auditor à auditer.
- 2e tape : verdict (`go` / `go with reserve` / `no-go`).
- Les deux tapes sont distincts, séparés par la lecture du rapport.

## Justification

- L'Auditor ne se lance **jamais** sans autorisation explicite.
- Le Validator lit l'audit **avant** de trancher.
- Traçabilité : deux moments, deux décisions.

## Alternatives écartées

- **Un seul tape** : l'audit se lance sans contrôle, ou le verdict est donné sans lecture.
- **Audit automatique** : perte de contrôle.
- **Verdict sans audit** : subjectif.
