# Décision 028 — Composition des verdicts

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 5 (qualité)

---

## Décision

Aux sprints `🔒`, le verdict global est **composé** des verdicts QA et SecOps : **sécu bloquante, QA graduable**.

## Règles

```
verdict_global = no-go           si QA=no-go OU SecOps=no-go
verdict_global = go_with_reserve si QA=reserve OU SecOps=reserve
verdict_global = go              si QA=go ET SecOps=go
```

- 1 finding critique sécu = `no-go` global, même si QA=go.
- 1 finding moyen sécu = `go with reserve` global.

## Justification

- La sécurité est **bloquante** (1 critique = refus).
- La QA est **graduable** (couverture, findings mineurs).
- Composition explicite = pas d'ambiguïté.

## Alternatives écartées

- **Verdict unique** : masque les nuances.
- **QA prioritaire** : sécurité négligée.
- **Moyenne des verdicts** : absurde.
