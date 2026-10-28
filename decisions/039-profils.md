# Décision 039 — Profils (Lite / Standard / Strict)

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 8d (process)

---

## Décision

Trois profils de rigueur sont proposés au bootstrap : **Lite**, **Standard**, **Strict**. Le profil est noté dans `.akoris/method-version.md`.

## Règles

### Les 3 profils

| Profil | Usage | Ce qui change |
|--------|-------|---------------|
| **Lite** | Prototype, solo, 1-2 semaines | TNR seul, pas d'ADR fondateurs, audit QA rapide |
| **Standard** | Projet sérieux, solo/duo | TNR + E2E conditionnel + sécu checkpoint + ADR + dettes |
| **Strict** | Prod critique, équipe | TNR + E2E + UAT formelle + sécu + perf + PR + protection branche |

### Choix du profil

- Choisi à la phase 0 (bootstrap).
- Noté dans `.akoris/method-version.md` :
  ```yaml
  method:
    profile: standard
  ```
- Modifiable uniquement par le Validator avec `go` + ADR.

### Adaptation des templates

- Le profil Lite n'a pas `audit_report-secops.md` (pas de SecOps).
- Le profil Strict ajoute `doc/tech/perf.md` (perf obligatoire).

## Justification

- **« Adaptive » devient vrai** : on démarre léger, on monte en rigueur.
- **Réalisme** : un prototype n'a pas besoin de la même rigueur qu'une prod critique.
- **Traçabilité** : le profil est noté, on sait ce qui est attendu.

## Alternatives écartées

- **Un seul profil** : trop lourd pour un prototype, trop léger pour une prod.
- **Profils infinis** : complexité inutile.
- **Profil non noté** : on ne sait pas ce qui est attendu.
