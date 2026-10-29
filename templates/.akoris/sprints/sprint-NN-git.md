---
sprint: <NN>
branche: sprint-<NN>
base: main@<hash>
tag_cible: <vX.Y.Z>
ouvert_le: <YYYY-MM-DDTHH:MM:SSZ>
cloture_le: <YYYY-MM-DDTHH:MM:SSZ>
---

# GIT LOG — Sprint <NN>

> Trace git du sprint. Écrit par le Builder (seul acteur git).
> Archivé avec `sprint-NN.md` et `sprint-NN-report.md` à la clôture.

---

## Commits

> **Règle :** **1 tâche → 1 critère d'acceptation → ≥ 1 commit** (un ou plusieurs commits par tâche, tous référencés par `Tâche: TN`).
> Le commit principal porte `Tâche: TN`. Les commits de test/docs associés
> portent aussi `Tâche: TN`.

| # | Hash | Type | Scope | Message | Tâche | Refs |
|---|------|------|-------|---------|-------|------|
| 1 | <hash> | feat | <scope> | <desc> | T1 | ADR-NNNN |
| 2 | <hash> | test | <scope> | <desc> | T1 | — |
| … | … | … | … | … | … | … |
## Push

| # | Date | Branche | Destination | Hash final | Résultat |
|---|------|---------|-------------|------------|----------|
| 1 | <date> | sprint-<NN> | origin | <hash> | ✅ |

## Merge

| Date | Source | Destination | Hash merge | Résultat |
|------|--------|-------------|------------|----------|
| <date> | sprint-<NN> | main | <hash> | ✅ |

## Tag

| Tag | Hash | Date | ADR |
|-----|------|------|-----|
| vX.Y.Z | <hash> | <date> | ADR-NNNN |

## Événements notables

- <date> : <événement> — <résolution>

## Liens dettes

| Dette | Commits | Statut après sprint |
|-------|---------|---------------------|
| DT-NNN | <hash> | résorbée |

## Liens ADR

| ADR | Commits | Statut |
|-----|---------|--------|
| ADR-NNNN | <hash> | appliqué |
