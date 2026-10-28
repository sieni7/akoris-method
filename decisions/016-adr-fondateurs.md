# Décision 016 — 4 ADR fondateurs

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 4 (gouvernance)

---

## Décision

Au bootstrap, **4 ADR fondateurs** sont créés :
- `0001-stack-initiale.md`
- `0002-separation-app-doc-akoris.md`
- `0003-convention-go.md`
- `0004-strategie-tests.md`

## Règles

- 4 ADR au bootstrap, pas plus.
- Les ADR supplémentaires naissent d'une décision structurante **rencontrée en cours de route**.
- Chaque ADR : contexte, options, décision, conséquences.

## Justification

- Couvre les 4 décisions les plus impactantes.
- Évite la sur-documentation au bootstrap.
- Les autres décisions sont dans `contexte.md` (pas besoin d'ADR).

## Alternatives écartées

- **2 ADR** : sous-documente (GO et tests sont structurants).
- **6-7 ADR** : sur-documentation, décisions prématurées.
- **0 ADR** : perte de traçabilité fondatrice.
