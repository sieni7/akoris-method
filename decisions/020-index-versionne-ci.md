# Décision 020 — index.md versionné + vérifié CI

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 6 (scripts)

---

## Décision

`index.md` est **versionné** dans git et **vérifié en CI** (le CI régénère et compare).

## Règles

- `index.md` commité avec les dettes.
- CI : `python build-debt-index.py --check` → exit 1 si divergence.
- Régénéré par l'Orchestrator en clôture de sprint (`chore(debt): regenerate index`).
- Jamais édité à la main.

## Justification

- **Trace historique** de l'évolution des dettes.
- **Consultation sans friction** (GitHub, IDE).
- **Fiabilité** : la CI bloque si désync.

## Alternatives écartées

- **Gitignoré** : pas de trace, friction.
- **Maintenu à la main** : désync garantie.
- **Généré à la volée** : pas de trace.
