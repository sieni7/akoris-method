# Décision 025 — Auditor QA permanent

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

L'Auditor exerce un mandat **QA permanent** à chaque sprint : tests, critères d'acceptation, régressions, cohérence.

## Règles

- À chaque sprint, l'Auditor vérifie : tests exécutés, critères couverts, régressions absentes.
- Il écrit `audit_report.md` (QA).
- Il recommande le push (`push` / `push avec réserves` / `ne pas push`).
- Il ne mélange JAMAIS QA et SecOps.
- **Preuve attendue (V1)** : le rapport cite les commandes exécutées et leurs résultats (texte).
- **Preuve attendue (V2)** : le rapport attache les logs, runs CI et sorties scanners (machine).
- **Résorption d'une dette** : l'Auditor valide la résorption (commit + test). Le Builder ne peut PAS passer une dette en `resorbee` seul.

## Justification

- Sans QA, le Validator valide à l'aveugle.
- La QA est le socle de la qualité.
- Le rapport QA est le référentiel du verdict.
- La preuve (V1 texte, V2 machine) est la condition de « zéro hallucination ».

## Alternatives écartées

- **QA optionnelle** : dette qualité rapide.
- **QA par le Builder** : auto-validation.
- **QA par le Validator** : goulot d'étranglement.
- **Résorption auto-déclarée par le Builder** : biais, contredit la séparation des pouvoirs.
