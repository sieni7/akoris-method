# Décision 012 — Phase 0 en 5 étapes

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 1-2 (fondations)

---

## Décision

Avant le bootstrap, une **phase 0** en 5 étapes initialise manuellement les 3 onglets.

## Règles

1. Terminal : mkdir app doc .akoris + copier templates.
2. Onglet A : coller `orchestrator.md` → "prêt".
3. Onglet B : coller `builder.md` → "prêt".
4. Onglet C : coller `auditor.md` → "prêt".
5. Onglet A : coller `bootstrap.md` → Phase 1.

Ordre A → B → C. Aucun `GO` en phase 0.

## Justification

- Les agents connaissent leur rôle **avant** le bootstrap.
- Pas de collision (ordre A → B → C).
- Réplicable (5 étapes, 5-10 min).

## Alternatives écartées

- **Pas de phase 0** : agents sans identité, risque de collision.
- **Bootstrap sans identité** : l'Orchestrator hallucine son rôle.
- **Phase 0 en 3 étapes** : B/C non prêts.
