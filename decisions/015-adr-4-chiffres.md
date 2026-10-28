# Décision 015 — Numérotation ADR à 4 chiffres

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 4 (gouvernance)

---

## Décision

Les ADR sont numérotés sur **4 chiffres** : `NNNN-titre-kebab-case.md` (ex. `0001-stack-initiale.md`).

## Règles

- Format : `NNNN-titre-kebab-case.md`.
- Numérotation séquentielle : 0001, 0002, …
- Jamais renuméroté. Remplacement = nouveau numéro + `remplace ADR-NNNN`.

## Justification

- **Standard Nygard** (le format ADR le plus répandu).
- Tri alphabétique = tri chronologique.
- Référence stable (`ADR-0004` est cité sans ambiguïté).
- Marge : 9999 ADR = largement suffisant.

## Alternatives écartées

- **3 chiffres** : casse au-delà de 999.
- **Date** : tri fragile.
- **Sans préfixe** : pas d'ordre, collisions.
