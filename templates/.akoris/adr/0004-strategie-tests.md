# ADR-0004 — Stratégie de tests

- **Date :** <YYYY-MM-DD>
- **Statut :** accepté
- **Décideur :** Validator
- **Sprint d'origine :** 1

---

## Contexte

Le projet doit être testé sans paralyser la vélocité. Il faut choisir
quelles familles de tests activer en V0, V1, V2.

## Options envisagées

1. **Tout en V0** (TNR + E2E + UAT + perf) — paralysie
2. **TNR seul** — sécu non couverte
3. **Socle V0** (TNR + sécu + UAT implicite) + E2E si critique + perf V2

## Décision

- **V0 :** TNR obligatoire + sécu checkpoint (`🔒`) + UAT implicite (verdict)
- **V0 :** E2E uniquement si parcours critique unique
- **V1 :** E2E complet + UAT formelle
- **V2 :** tests de performance

## Conséquences

- ✅ Vélocité préservée
- ✅ Qualité garantie (TNR + sécu)
- ⚠️ E2E absent en V0 (sauf critique)
- 📉 Dette possible : E2E à ajouter en V1

## Alternatives écartées

- **Tout en V0** : paralysie
- **TNR seul** : sécu non couverte

## Références

- Décision 030 (stratégie tests V0)
- Décision 031 (seuils tests)
- doc/tech/tests.md (manuel détaillé)
